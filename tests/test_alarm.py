"""Unit-Tests für das Alarm-Modul."""

from src.alarm import AlarmManager


def test_alarm_manager_exists():
    """Prüft, dass die AlarmManager-Klasse instanziiert werden kann."""
    manager = AlarmManager()
    assert manager is not None
