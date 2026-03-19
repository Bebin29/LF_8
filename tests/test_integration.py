"""Integrationstests: Zusammenspiel von Monitoring und Alarm."""

from src.alarm import AlarmManager
from src.monitoring import SystemMonitor


class TestMonitoringAlarmIntegration:
    """Testet das Zusammenspiel von SystemMonitor und AlarmManager."""

    def test_disk_check_triggers_alarm(self, tmp_path) -> None:
        """Disk-Messdaten werden korrekt an AlarmManager übergeben."""
        log_file = tmp_path / "integration.log"
        monitor = SystemMonitor()
        alarm = AlarmManager(log_path=str(log_file))

        disk = monitor.get_disk_usage()
        # Softlimit auf 0 setzen, damit garantiert WARNING kommt
        result = alarm.check_value("Disk", disk["percent"], 0.0, 101.0)

        assert result == "WARNING"
        assert log_file.exists()

    def test_ram_check_triggers_alarm(self, tmp_path) -> None:
        """RAM-Messdaten werden korrekt an AlarmManager übergeben."""
        log_file = tmp_path / "integration.log"
        monitor = SystemMonitor()
        alarm = AlarmManager(log_path=str(log_file))

        ram = monitor.get_ram_usage()
        result = alarm.check_value("RAM", ram["percent"], 0.0, 101.0)

        assert result == "WARNING"

    def test_process_check_with_realistic_limits(self, tmp_path) -> None:
        """Prozessanzahl wird korrekt gegen Limits geprüft."""
        log_file = tmp_path / "integration.log"
        monitor = SystemMonitor()
        alarm = AlarmManager(log_path=str(log_file))

        count = monitor.get_process_count()
        # Hardlimit auf 1 setzen, damit garantiert CRITICAL kommt
        result = alarm.check_value("Processes", float(count), 0.0, 1.0)

        assert result == "CRITICAL"

    def test_full_monitoring_cycle(self, tmp_path) -> None:
        """Kompletter Durchlauf: Alle Metriken erfassen und prüfen."""
        log_file = tmp_path / "integration.log"
        monitor = SystemMonitor()
        alarm = AlarmManager(log_path=str(log_file))

        metrics = monitor.get_all_metrics()

        assert "disk" in metrics
        assert "ram" in metrics
        assert "processes" in metrics
        assert "users" in metrics

        # Alle Checks durchführen (mit hohen Limits → OK)
        disk_status = alarm.check_value(
            "Disk", metrics["disk"]["percent"], 99.0, 100.0
        )
        ram_status = alarm.check_value(
            "RAM", metrics["ram"]["percent"], 99.0, 100.0
        )

        assert disk_status == "OK"
        assert ram_status == "OK"
