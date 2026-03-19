# Verteildiagramm: LF8 Monitoring System

## Übersicht

Das folgende Diagramm zeigt die Verteilung der Software-Komponenten
auf die verschiedenen Umgebungen und deren Kommunikation.

## Diagramm

```mermaid
graph TB
    subgraph local["Lokale Entwicklungsumgebung"]
        dev["Developer Workstation"]
        py["Python 3.10+"]
        venv["Virtual Environment<br/>(psutil, pytest, flake8, mypy, bandit)"]
        src["src/<br/>main.py | monitoring.py | alarm.py"]
        config["config.ini"]
        env[".env<br/>(SMTP Credentials)"]
        docker["Docker Engine<br/>(optional)"]

        dev --> py --> venv --> src
        src --> config
        src --> env
        docker -.-> src
    end

    subgraph github["GitHub (Cloud)"]
        repo["Repository<br/>Bebin29/LF_8"]
        issues["GitHub Issues<br/>& Projects"]
        actions["GitHub Actions<br/>(Runner: ubuntu-latest)"]

        subgraph ci["CI Pipeline"]
            test["pytest<br/>(Python 3.10 + 3.12)"]
            lint["flake8"]
            typecheck["mypy"]
            security["bandit"]
        end

        subgraph cd["CD Pipeline"]
            build["Build Artifact"]
            release["GitHub Release<br/>(Versioniert)"]
        end

        repo --> actions
        actions --> ci
        actions --> cd
        cd --> release
    end

    subgraph prod["Produktivumgebung"]
        container["Docker Container<br/>(python:3.12-slim)"]
        monitor_app["Monitoring App<br/>(--all --interval 5)"]
        logfile["Logdatei<br/>(monitor.log)"]
        container --> monitor_app --> logfile
    end

    subgraph external["Externe Dienste"]
        smtp["SMTP Server<br/>(E-Mail Versand)"]
    end

    dev -- "git push (HTTPS)" --> repo
    release -- "Docker Pull / Download" --> container
    monitor_app -- "SMTP (Port 587, TLS)" --> smtp
    dev -- "gh CLI (HTTPS)" --> issues

    style local fill:#e1f5fe,stroke:#0288d1
    style github fill:#fff3e0,stroke:#f57c00
    style prod fill:#e8f5e9,stroke:#388e3c
    style external fill:#fce4ec,stroke:#c62828
    style ci fill:#fff8e1,stroke:#f9a825
    style cd fill:#f3e5f5,stroke:#7b1fa2
```

## Komponenten und Kommunikation

### Lokale Entwicklungsumgebung
Die Entwicklung findet auf lokalen Workstations statt. Python 3.10+ mit einem
Virtual Environment stellt alle Abhängigkeiten bereit. Der Quellcode liegt in
`src/`, die Konfiguration in `config.ini` und sensible SMTP-Credentials in `.env`.
Optional kann die Anwendung lokal auch als Docker-Container gestartet werden.

### GitHub (Cloud)
Das Repository auf GitHub dient als zentraler Punkt für Versionsverwaltung,
Issue-Tracking und automatisierte Pipelines. Bei jedem Push oder Pull Request
werden die CI-Jobs (pytest, flake8, mypy, bandit) auf GitHub Actions Runnern
(ubuntu-latest) ausgeführt. Bei einem Merge auf `main` erstellt die CD-Pipeline
automatisch ein versioniertes GitHub Release mit Build-Artefakt.

### Produktivumgebung
Die Software wird als Docker-Container (basierend auf python:3.12-slim)
bereitgestellt. Der Container führt das Monitoring im Intervall-Modus aus
und schreibt Alarme in eine Logdatei.

### Externe Dienste
Bei Hardlimit-Überschreitungen wird eine E-Mail über einen externen SMTP-Server
versendet. Die Kommunikation erfolgt über Port 587 mit TLS-Verschlüsselung.

## Protokolle

| Verbindung | Protokoll | Port |
|------------|-----------|------|
| Developer → GitHub | HTTPS (Git + API) | 443 |
| GitHub Actions → Runner | HTTPS | 443 |
| Monitoring → SMTP Server | SMTP + TLS | 587 |
| Developer → Docker Hub | HTTPS | 443 |
