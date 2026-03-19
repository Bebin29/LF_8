"""Unit-Tests für das Alarm-Modul."""

from unittest.mock import MagicMock, patch

from src.alarm import AlarmManager


class TestAlarmManagerCheckValue:
    """Tests für die check_value Methode (Zwei-Stufen-Logik)."""

    def setup_method(self) -> None:
        """Erstellt eine AlarmManager-Instanz mit temporärer Logdatei."""
        self.alarm = AlarmManager(log_path="test_alarm.log")

    def test_value_below_soft_limit_returns_ok(self) -> None:
        """Wert unter Softlimit gibt OK zurück."""
        result = self.alarm.check_value("Disk", 50.0, 80.0, 95.0)
        assert result == "OK"

    def test_value_at_soft_limit_returns_warning(self) -> None:
        """Wert auf Softlimit gibt WARNING zurück."""
        result = self.alarm.check_value("RAM", 80.0, 80.0, 95.0)
        assert result == "WARNING"

    def test_value_above_soft_below_hard_returns_warning(self) -> None:
        """Wert zwischen Soft- und Hardlimit gibt WARNING zurück."""
        result = self.alarm.check_value("Disk", 90.0, 80.0, 95.0)
        assert result == "WARNING"

    def test_value_at_hard_limit_returns_critical(self) -> None:
        """Wert auf Hardlimit gibt CRITICAL zurück."""
        result = self.alarm.check_value("Processes", 200.0, 150.0, 200.0)
        assert result == "CRITICAL"

    def test_value_above_hard_limit_returns_critical(self) -> None:
        """Wert über Hardlimit gibt CRITICAL zurück."""
        result = self.alarm.check_value("RAM", 99.0, 80.0, 95.0)
        assert result == "CRITICAL"


class TestAlarmManagerLogging:
    """Tests für die Logdatei-Funktionalität."""

    def test_softlimit_writes_warning_to_log(self, tmp_path) -> None:
        """Softlimit-Überschreitung schreibt WARNING in die Logdatei."""
        log_file = tmp_path / "test.log"
        alarm = AlarmManager(log_path=str(log_file))

        alarm.check_value("Disk", 85.0, 80.0, 95.0)

        log_content = log_file.read_text(encoding="utf-8")
        assert "WARNING" in log_content
        assert "SOFTLIMIT Disk" in log_content
        assert "85.0" in log_content

    def test_hardlimit_writes_critical_to_log(self, tmp_path) -> None:
        """Hardlimit-Überschreitung schreibt CRITICAL in die Logdatei."""
        log_file = tmp_path / "test.log"
        alarm = AlarmManager(log_path=str(log_file))

        alarm.check_value("RAM", 96.0, 80.0, 95.0)

        log_content = log_file.read_text(encoding="utf-8")
        assert "CRITICAL" in log_content
        assert "HARDLIMIT RAM" in log_content

    def test_log_contains_hostname(self, tmp_path) -> None:
        """Log-Eintrag enthält den Hostnamen."""
        log_file = tmp_path / "test.log"
        alarm = AlarmManager(log_path=str(log_file))

        alarm.check_value("Disk", 85.0, 80.0, 95.0)

        log_content = log_file.read_text(encoding="utf-8")
        assert alarm.hostname in log_content


class TestAlarmManagerEmail:
    """Tests für den E-Mail-Versand."""

    @patch("src.alarm.smtplib.SMTP")
    def test_hardlimit_triggers_email(self, mock_smtp) -> None:
        """Hardlimit-Überschreitung löst E-Mail-Versand aus."""
        mock_server = MagicMock()
        mock_smtp.return_value.__enter__ = MagicMock(return_value=mock_server)
        mock_smtp.return_value.__exit__ = MagicMock(return_value=False)

        alarm = AlarmManager(
            log_path="test_email.log",
            smtp_host="smtp.test.com",
            smtp_port=587,
            smtp_sender="test@test.com",
            smtp_receiver="admin@test.com",
        )

        alarm.check_value("Disk", 96.0, 80.0, 95.0)

        mock_smtp.assert_called_once_with("smtp.test.com", 587)
        mock_server.sendmail.assert_called_once()

    def test_no_smtp_config_skips_email(self, tmp_path) -> None:
        """Ohne SMTP-Konfiguration wird keine E-Mail versendet."""
        log_file = tmp_path / "test.log"
        alarm = AlarmManager(log_path=str(log_file))

        result = alarm.check_value("Disk", 96.0, 80.0, 95.0)

        assert result == "CRITICAL"
