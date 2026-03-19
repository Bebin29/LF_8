"""Hilfsmodul zum Laden der Konfiguration.

Liest Schwellenwerte, SMTP-Credentials und Monitoring-Parameter
aus einer INI-Datei mittels configparser.
"""

import configparser
from pathlib import Path
from typing import Any, Dict


class ConfigLoader:
    """Lädt und validiert die Konfiguration aus config.ini."""

    def __init__(self, config_path: str = "config.ini") -> None:
        """Initialisiert den ConfigLoader.

        Args:
            config_path: Pfad zur Konfigurationsdatei.

        Raises:
            FileNotFoundError: Wenn die Datei nicht existiert.
        """
        self.config_path = Path(config_path)
        if not self.config_path.exists():
            raise FileNotFoundError(
                f"Konfigurationsdatei nicht gefunden: {self.config_path}"
            )

        self._config = configparser.ConfigParser()
        self._config.read(self.config_path, encoding="utf-8")

    def get_interval(self) -> int:
        """Gibt das Monitoring-Intervall in Sekunden zurück."""
        return self._config.getint("monitoring", "interval", fallback=5)

    def get_soft_limits(self) -> Dict[str, float]:
        """Gibt die Softlimit-Schwellenwerte zurück.

        Returns:
            Dict mit Metrik-Name und Schwellenwert.
        """
        return self._parse_thresholds("thresholds_soft")

    def get_hard_limits(self) -> Dict[str, float]:
        """Gibt die Hardlimit-Schwellenwerte zurück.

        Returns:
            Dict mit Metrik-Name und Schwellenwert.
        """
        return self._parse_thresholds("thresholds_hard")

    def _parse_thresholds(self, section: str) -> Dict[str, float]:
        """Parst eine Threshold-Sektion aus der Config.

        Args:
            section: Name der Sektion.

        Returns:
            Dict mit Metrik-Name und Schwellenwert.
        """
        thresholds: Dict[str, float] = {}
        if self._config.has_section(section):
            for key, value in self._config.items(section):
                thresholds[key] = float(value)
        return thresholds

    def get_smtp_config(self) -> Dict[str, Any]:
        """Gibt die SMTP-Konfiguration zurück.

        Returns:
            Dict mit SMTP-Parametern.
        """
        if not self._config.has_section("smtp"):
            return {}

        return {
            "smtp_host": self._config.get("smtp", "host", fallback=None),
            "smtp_port": self._config.getint("smtp", "port", fallback=587),
            "smtp_sender": self._config.get("smtp", "sender", fallback=None),
            "smtp_receiver": self._config.get(
                "smtp", "receiver", fallback=None
            ),
            "smtp_username": self._config.get(
                "smtp", "username", fallback=None
            ),
            "smtp_password": self._config.get(
                "smtp", "password", fallback=None
            ),
        }
