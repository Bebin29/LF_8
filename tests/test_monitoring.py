"""Unit-Tests für das Monitoring-Modul."""

from unittest.mock import patch

from src.monitoring import SystemMonitor


class TestDiskUsage:
    """Tests für die Festplatten-Überwachung."""

    def test_disk_usage_returns_required_keys(self) -> None:
        """Disk-Usage enthält alle erwarteten Schlüssel."""
        result = SystemMonitor.get_disk_usage()
        assert "total_gb" in result
        assert "used_gb" in result
        assert "free_gb" in result
        assert "percent" in result

    def test_disk_usage_percent_in_range(self) -> None:
        """Disk-Percent liegt zwischen 0 und 100."""
        result = SystemMonitor.get_disk_usage()
        assert 0.0 <= result["percent"] <= 100.0

    def test_disk_usage_invalid_path_returns_zeros(self) -> None:
        """Ungültiger Pfad gibt Nullwerte zurück."""
        result = SystemMonitor.get_disk_usage("/nonexistent/path")
        assert result["percent"] == 0.0


class TestRamUsage:
    """Tests für die Arbeitsspeicher-Überwachung."""

    def test_ram_usage_returns_required_keys(self) -> None:
        """RAM-Usage enthält alle erwarteten Schlüssel."""
        result = SystemMonitor.get_ram_usage()
        assert "total_gb" in result
        assert "used_gb" in result
        assert "available_gb" in result
        assert "percent" in result

    def test_ram_usage_percent_in_range(self) -> None:
        """RAM-Percent liegt zwischen 0 und 100."""
        result = SystemMonitor.get_ram_usage()
        assert 0.0 <= result["percent"] <= 100.0


class TestProcessCount:
    """Tests für die Prozess-Überwachung."""

    def test_process_count_is_positive(self) -> None:
        """Prozessanzahl ist größer als 0."""
        count = SystemMonitor.get_process_count()
        assert count > 0


class TestLoggedUsers:
    """Tests für die Nutzer-Überwachung."""

    def test_logged_users_returns_list(self) -> None:
        """Logged Users gibt eine Liste zurück."""
        users = SystemMonitor.get_logged_users()
        assert isinstance(users, list)


class TestFormatOutput:
    """Tests für die Konsolenausgabe."""

    def test_format_output_contains_headers(self) -> None:
        """Formatierte Ausgabe enthält alle Sektionsüberschriften."""
        monitor = SystemMonitor()
        metrics = monitor.get_all_metrics()
        output = SystemMonitor.format_output(metrics)

        assert "SYSTEM MONITORING REPORT" in output
        assert "Festplatte" in output
        assert "Arbeitsspeicher" in output
        assert "Prozesse" in output
        assert "Eingeloggte Nutzer" in output
