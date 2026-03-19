# LF8 Monitoring System

![CI Pipeline](https://github.com/Bebin29/LF_8/actions/workflows/ci.yml/badge.svg?branch=develop)
![Python](https://img.shields.io/badge/python-3.10%20|%203.12-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Platform](https://img.shields.io/badge/platform-Windows%20|%20Linux-lightgrey)

Ein plattformunabhängiges System-Monitoring-Tool mit zweistufigem Alarmsystem, entwickelt im Rahmen des Lernfeld 8 (ITECH).

## Features

- **System-Monitoring** — Festplatte, RAM, Prozesse und eingeloggte Nutzer via psutil
- **Zweistufiges Alarmsystem** — Softlimit (Warning + Log) und Hardlimit (Critical + Log + E-Mail)
- **SMTP-Alarmierung** — Automatischer E-Mail-Versand bei kritischen Schwellenwerten
- **Konfigurierbar** — Schwellenwerte und SMTP-Settings via `config.ini` und Umgebungsvariablen
- **CLI-Steuerung** — Flexible Parametrisierung via `argparse`
- **CI/CD Pipeline** — Automatisierte Tests, Linting, Type Checking, Security Scanning und Releases
- **Docker-Support** — Containerisiertes Deployment

## Quickstart

```bash
# Repository klonen
git clone https://github.com/Bebin29/LF_8.git
cd LF_8

# Dependencies installieren
pip install -r requirements.txt

# Alle Checks ausführen
python -m src.main --all
```

## Usage

```bash
# Einzelne Metriken
python -m src.main --disk
python -m src.main --ram
python -m src.main --processes

# Alle Metriken
python -m src.main --all

# Eigene Config-Datei
python -m src.main --all --config my_config.ini

# Intervall-Modus (alle 10 Sekunden)
python -m src.main --all --interval 10

# Hilfe
python -m src.main -h
```

### Docker

```bash
# Einmalig
docker compose up

# Intervall-Modus
docker compose run monitor --all --interval 10
```

## Architektur

```
src/
├── main.py              # CLI-Einstiegspunkt (argparse)
├── monitoring.py         # SystemMonitor: Metriken erfassen (psutil)
├── alarm.py             # AlarmManager: Zwei-Stufen-Alarm + SMTP
└── utils/
    └── config_loader.py  # ConfigLoader: config.ini + .env
```

```
main.py
  ├── ConfigLoader  → lädt config.ini + Umgebungsvariablen
  ├── SystemMonitor → erfasst Disk, RAM, Prozesse, User
  └── AlarmManager  → prüft Soft-/Hardlimits, loggt, sendet E-Mails
```

## Konfiguration

**config.ini** — Schwellenwerte und SMTP-Server:

```ini
[monitoring]
interval = 5

[thresholds_soft]
disk = 80.0
ram = 80.0
processes = 150

[thresholds_hard]
disk = 95.0
ram = 95.0
processes = 200

[smtp]
host = smtp.example.com
port = 587
sender = monitor@example.com
receiver = admin@example.com
```

**.env** — SMTP-Credentials (nicht im Repository):

```
SMTP_USERNAME=monitor@example.com
SMTP_PASSWORD=dein_passwort
```

## CI/CD Pipeline

Jeder Push und PR durchläuft automatisch:

| Check | Tool | Zweck |
|-------|------|-------|
| Tests | pytest + Coverage | Funktionale Korrektheit (22 Tests) |
| Linting | flake8 | Code-Stil (PEP 8) |
| Type Check | mypy | Statische Typprüfung |
| Security | bandit | Sicherheitsanalyse |

Bei Merge auf `main` wird automatisch ein GitHub Release erstellt.

## Dokumentation

- [CI/CD Sequenzdiagramm](docs/pipeline-sequence.md)
- [Klassendiagramm](docs/class-diagram.md)
- [Verteildiagramm](docs/deployment-diagram.md)
- [Open-Source Analyse](docs/opensource-analyse.md)
- [Scrum-Rollen](docs/agile/scrum-rollen.md)
- [Sprint-Planung](docs/agile/sprint-planung.md)
- [Retrospektiven](docs/agile/retrospektiven.md)
- [Planungsmethoden](docs/agile/planungsmethoden.md)
- [Prozessvergleich](docs/agile/prozessvergleich.md)

## Projektboard

[Kanban Board](https://github.com/users/Bebin29/projects/6)

## Contributing

Siehe [CONTRIBUTING.md](CONTRIBUTING.md) für Entwicklungsrichtlinien.

## Lizenz

MIT
