"""Unit-Tests für das Monitoring-Modul."""

from src.monitoring import SystemMonitor


def test_system_monitor_exists():
    """Prüft, dass die SystemMonitor-Klasse instanziiert werden kann."""
    monitor = SystemMonitor()
    assert monitor is not None
