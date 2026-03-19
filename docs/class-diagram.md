# Klassendiagramm: LF8 Monitoring System

## Übersicht

Das folgende Diagramm zeigt die Architektur der Software mit allen Klassen,
ihren Attributen, Methoden und Beziehungen.

## Diagramm

```mermaid
classDiagram
    class SystemMonitor {
        +get_disk_usage(path: str) Dict~str, float~
        +get_ram_usage() Dict~str, float~
        +get_process_count() int
        +get_logged_users() List~Dict~str, str~~
        +get_all_metrics(disk_path: str) Dict
        +format_output(metrics: Dict)$ str
    }

    class AlarmManager {
        -log_path: Path
        -smtp_host: Optional~str~
        -smtp_port: int
        -smtp_sender: Optional~str~
        -smtp_receiver: Optional~str~
        -smtp_username: Optional~str~
        -smtp_password: Optional~str~
        -hostname: str
        -_logger: Logger
        -_setup_logging() None
        -_log(level: int, message: str, value: float) str
        -_send_email(message: str, value: float) bool
        +check_value(metric_name: str, current_value: float, soft_limit: float, hard_limit: float) str
    }

    class ConfigLoader {
        -config_path: Path
        -_config: ConfigParser
        -_parse_thresholds(section: str) Dict~str, float~
        +get_interval() int
        +get_soft_limits() Dict~str, float~
        +get_hard_limits() Dict~str, float~
        +get_smtp_config() Dict~str, Any~
    }

    class main {
        <<module>>
        +parse_args(args: list) Namespace
        +run_checks(monitor, alarm, soft_limits, hard_limits, ...) None
        +main(args: list) None
    }

    main --> ConfigLoader : lädt Konfiguration
    main --> SystemMonitor : erfasst Metriken
    main --> AlarmManager : prüft Schwellenwerte

    SystemMonitor ..> AlarmManager : Messdaten übergeben
    ConfigLoader ..> AlarmManager : SMTP-Config + Schwellenwerte
```

## Beziehungen

| Beziehung | Beschreibung |
|-----------|-------------|
| `main` → `ConfigLoader` | Lädt Schwellenwerte und SMTP-Konfiguration aus config.ini |
| `main` → `SystemMonitor` | Erfasst Systemmetriken (Disk, RAM, Prozesse, User) |
| `main` → `AlarmManager` | Prüft Messwerte gegen Soft-/Hardlimits |
| `SystemMonitor` ⇢ `AlarmManager` | Messdaten werden an check_value() übergeben |
| `ConfigLoader` ⇢ `AlarmManager` | SMTP-Credentials und Schwellenwerte konfigurieren den AlarmManager |
