"""Einstiegspunkt für das LF8 Monitoring System.

Steuert das Monitoring über CLI-Parameter oder config.ini.
Verbindet SystemMonitor und AlarmManager.
"""

import argparse
import sys

from src.alarm import AlarmManager
from src.monitoring import SystemMonitor
from src.utils.config_loader import ConfigLoader


def parse_args(args: list[str] | None = None) -> argparse.Namespace:
    """Parst die Kommandozeilenargumente.

    Args:
        args: Argumentliste (None für sys.argv).

    Returns:
        Namespace mit den geparsten Argumenten.
    """
    parser = argparse.ArgumentParser(
        prog="lf8-monitor",
        description=(
            "LF8 Monitoring System - Überwacht Systemressourcen "
            "und löst bei Schwellenwertüberschreitung Alarme aus."
        ),
        epilog=(
            "Beispiele:\n"
            "  python -m src.main --disk --ram\n"
            "  python -m src.main --all --config my_config.ini\n"
            "  python -m src.main --processes --interval 10"
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )

    parser.add_argument(
        "--disk",
        action="store_true",
        help="Festplattenauslastung prüfen",
    )
    parser.add_argument(
        "--ram",
        action="store_true",
        help="Arbeitsspeicher-Auslastung prüfen",
    )
    parser.add_argument(
        "--processes",
        action="store_true",
        help="Anzahl der laufenden Prozesse prüfen",
    )
    parser.add_argument(
        "--all",
        action="store_true",
        help="Alle Metriken prüfen",
    )
    parser.add_argument(
        "--config",
        type=str,
        default="config.ini",
        help="Pfad zur Konfigurationsdatei (Standard: config.ini)",
    )
    parser.add_argument(
        "--interval",
        type=int,
        default=None,
        help="Intervall in Sekunden für wiederholte Prüfung",
    )
    parser.add_argument(
        "--log",
        type=str,
        default="monitor.log",
        help="Pfad zur Logdatei (Standard: monitor.log)",
    )

    return parser.parse_args(args)


def run_checks(
    monitor: SystemMonitor,
    alarm: AlarmManager,
    soft_limits: dict,
    hard_limits: dict,
    check_disk: bool = False,
    check_ram: bool = False,
    check_processes: bool = False,
) -> None:
    """Führt die ausgewählten Checks durch.

    Args:
        monitor: SystemMonitor-Instanz.
        alarm: AlarmManager-Instanz.
        soft_limits: Dict mit Softlimit-Schwellenwerten.
        hard_limits: Dict mit Hardlimit-Schwellenwerten.
        check_disk: Festplatte prüfen.
        check_ram: RAM prüfen.
        check_processes: Prozesse prüfen.
    """
    metrics = monitor.get_all_metrics()
    print(SystemMonitor.format_output(metrics))

    if check_disk:
        alarm.check_value(
            "Disk",
            metrics["disk"]["percent"],
            soft_limits.get("disk", 80.0),
            hard_limits.get("disk", 95.0),
        )

    if check_ram:
        alarm.check_value(
            "RAM",
            metrics["ram"]["percent"],
            soft_limits.get("ram", 80.0),
            hard_limits.get("ram", 95.0),
        )

    if check_processes:
        alarm.check_value(
            "Processes",
            float(metrics["processes"]),
            soft_limits.get("processes", 150.0),
            hard_limits.get("processes", 200.0),
        )


def main(args: list[str] | None = None) -> None:
    """Hauptfunktion des Monitoring-Systems."""
    parsed = parse_args(args)

    try:
        config = ConfigLoader(parsed.config)
    except FileNotFoundError as e:
        print(f"Fehler: {e}", file=sys.stderr)
        sys.exit(1)

    soft_limits = config.get_soft_limits()
    hard_limits = config.get_hard_limits()
    smtp_config = config.get_smtp_config()

    monitor = SystemMonitor()
    alarm = AlarmManager(log_path=parsed.log, **smtp_config)

    check_disk = parsed.all or parsed.disk
    check_ram = parsed.all or parsed.ram
    check_processes = parsed.all or parsed.processes

    if not any([check_disk, check_ram, check_processes]):
        check_disk = True
        check_ram = True
        check_processes = True

    if parsed.interval:
        import time

        try:
            while True:
                run_checks(
                    monitor, alarm, soft_limits, hard_limits,
                    check_disk, check_ram, check_processes,
                )
                print(f"\nNächste Prüfung in {parsed.interval} Sekunden...\n")
                time.sleep(parsed.interval)
        except KeyboardInterrupt:
            print("\nMonitoring beendet.")
    else:
        run_checks(
            monitor, alarm, soft_limits, hard_limits,
            check_disk, check_ram, check_processes,
        )


if __name__ == "__main__":
    main()
