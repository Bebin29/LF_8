"""Modul für Schwellenwert-Überwachung und Alarmierung.

Stellt ein zweistufiges Alarmsystem bereit:
- Softlimit: Warnung + Eintrag in Logdatei
- Hardlimit: Warnung + Logdatei + E-Mail via SMTP
"""

import logging
import smtplib
import socket
from datetime import datetime
from email.mime.text import MIMEText
from pathlib import Path
from typing import Optional


class AlarmManager:
    """Zweistufiges Alarmsystem mit Soft- und Hardlimit.

    Bei Softlimit-Überschreitung: Warnung + Logdatei-Eintrag.
    Bei Hardlimit-Überschreitung: Warnung + Logdatei + E-Mail.
    """

    def __init__(
        self,
        log_path: str = "monitor.log",
        smtp_host: Optional[str] = None,
        smtp_port: int = 587,
        smtp_sender: Optional[str] = None,
        smtp_receiver: Optional[str] = None,
        smtp_username: Optional[str] = None,
        smtp_password: Optional[str] = None,
    ) -> None:
        """Initialisiert den AlarmManager.

        Args:
            log_path: Pfad zur Logdatei.
            smtp_host: SMTP-Server Hostname.
            smtp_port: SMTP-Server Port.
            smtp_sender: Absender E-Mail-Adresse.
            smtp_receiver: Empfänger E-Mail-Adresse.
            smtp_username: SMTP-Benutzername.
            smtp_password: SMTP-Passwort.
        """
        self.log_path = Path(log_path)
        self.smtp_host = smtp_host
        self.smtp_port = smtp_port
        self.smtp_sender = smtp_sender
        self.smtp_receiver = smtp_receiver
        self.smtp_username = smtp_username
        self.smtp_password = smtp_password
        self.hostname = socket.gethostname()

        self._logger = logging.getLogger(f"alarm.{id(self)}")
        self._setup_logging()

    def _setup_logging(self) -> None:
        """Konfiguriert das Logging in die Logdatei."""
        handler = logging.FileHandler(self.log_path, encoding="utf-8")
        formatter = logging.Formatter(
            "%(asctime)s | %(hostname)s | %(levelname)s | %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )
        handler.setFormatter(formatter)
        self._logger.addHandler(handler)
        self._logger.setLevel(logging.DEBUG)

    def _log(self, level: int, message: str, value: float) -> str:
        """Schreibt einen Eintrag in die Logdatei.

        Args:
            level: Logging-Level (WARNING oder CRITICAL).
            message: Beschreibender Text.
            value: Aktueller Messwert.

        Returns:
            Die formatierte Log-Nachricht.
        """
        log_message = f"{message} | Aktueller Wert: {value}"
        self._logger.log(
            level, log_message, extra={"hostname": self.hostname}
        )
        return log_message

    def check_value(
        self,
        metric_name: str,
        current_value: float,
        soft_limit: float,
        hard_limit: float,
    ) -> str:
        """Prüft einen Messwert gegen Soft- und Hardlimit.

        Args:
            metric_name: Name der Metrik (z.B. 'Disk', 'RAM').
            current_value: Aktueller Messwert.
            soft_limit: Schwellenwert für Warnung.
            hard_limit: Schwellenwert für kritischen Alarm.

        Returns:
            Status-String: 'OK', 'WARNING' oder 'CRITICAL'.
        """
        if current_value >= hard_limit:
            message = (
                f"HARDLIMIT {metric_name}: "
                f"{current_value} >= {hard_limit}"
            )
            self._log(logging.CRITICAL, message, current_value)
            self._send_email(message, current_value)
            return "CRITICAL"

        if current_value >= soft_limit:
            message = (
                f"SOFTLIMIT {metric_name}: "
                f"{current_value} >= {soft_limit}"
            )
            self._log(logging.WARNING, message, current_value)
            return "WARNING"

        return "OK"

    def _send_email(self, message: str, value: float) -> bool:
        """Versendet eine Alarm-E-Mail via SMTP.

        Args:
            message: Alarm-Nachricht.
            value: Aktueller Messwert.

        Returns:
            True bei Erfolg, False bei Fehler.
        """
        if not all([self.smtp_host, self.smtp_sender, self.smtp_receiver]):
            self._logger.warning(
                "SMTP nicht konfiguriert, E-Mail wird nicht versendet.",
                extra={"hostname": self.hostname},
            )
            return False

        # Nach dem all()-Check sind diese Werte garantiert gesetzt
        smtp_host: str = self.smtp_host  # type: ignore[assignment]
        smtp_sender: str = self.smtp_sender  # type: ignore[assignment]
        smtp_receiver: str = self.smtp_receiver  # type: ignore[assignment]

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        body = (
            f"Alarm-Meldung vom Monitoring-System\n"
            f"{'=' * 40}\n"
            f"Zeitpunkt:  {timestamp}\n"
            f"Host:       {self.hostname}\n"
            f"Meldung:    {message}\n"
            f"Wert:       {value}\n"
        )

        msg = MIMEText(body, "plain", "utf-8")
        msg["Subject"] = f"[ALARM] {self.hostname}: {message}"
        msg["From"] = smtp_sender
        msg["To"] = smtp_receiver

        try:
            with smtplib.SMTP(smtp_host, self.smtp_port) as server:
                server.starttls()
                if self.smtp_username and self.smtp_password:
                    server.login(self.smtp_username, self.smtp_password)
                server.sendmail(
                    smtp_sender, smtp_receiver, msg.as_string()
                )
            return True
        except smtplib.SMTPException as e:
            self._logger.error(
                f"E-Mail-Versand fehlgeschlagen: {e}",
                extra={"hostname": self.hostname},
            )
            return False
