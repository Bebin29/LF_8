# Contributing

Vielen Dank für dein Interesse an diesem Projekt! Hier findest du alles, was du brauchst, um beizutragen.

## Entwicklungsumgebung einrichten

```bash
# Repository klonen
git clone https://github.com/Bebin29/LF_8.git
cd LF_8

# Virtual Environment erstellen und aktivieren
python -m venv venv
source venv/bin/activate    # Linux/macOS
venv\Scripts\activate       # Windows

# Abhängigkeiten installieren
pip install -r requirements.txt

# SMTP-Credentials konfigurieren (optional)
cp .env.example .env
# .env mit echten Werten befüllen
```

## Branching-Strategie

Wir arbeiten mit Git Flow:

- **main** — Produktionsbranch, nur über PRs von develop
- **develop** — Integrationsbranch, nur über PRs von Feature-Branches
- **feature/*** — Feature-Branches für einzelne Issues

Neues Feature starten:

```bash
git checkout develop
git pull
git checkout -b feature/mein-feature
```

## Pull Request Workflow

1. Feature-Branch erstellen (siehe oben)
2. Änderungen committen (atomare Commits)
3. Branch pushen: `git push -u origin feature/mein-feature`
4. PR gegen `develop` erstellen
5. CI muss grün sein (alle 5 Checks)
6. Nach Review: PR mergen

## Code-Standards

Alle Checks laufen automatisch in der CI-Pipeline. Lokal prüfen:

```bash
# Tests
pytest tests/ -v --cov=src

# Linting
flake8 src/ tests/ --max-line-length=120

# Type Checking
mypy src/ --ignore-missing-imports

# Security
bandit -r src/
```

Bitte stelle sicher, dass alle vier Checks lokal grün sind, bevor du einen PR erstellst.

## Commit-Konventionen

Wir nutzen Conventional Commits:

- `feat:` — Neues Feature
- `fix:` — Bugfix
- `docs:` — Dokumentation
- `test:` — Tests
- `ci:` — CI/CD-Änderungen
- `security:` — Sicherheitsrelevante Änderungen

Beispiel: `feat: add CPU monitoring to SystemMonitor`

## Projekt lokal ausführen

```bash
# Alle Checks
python -m src.main --all

# Einzelne Metriken
python -m src.main --disk --ram

# Mit eigenem Config-File
python -m src.main --all --config my_config.ini

# Intervall-Modus (alle 10 Sekunden)
python -m src.main --all --interval 10

# Hilfe
python -m src.main -h
```
