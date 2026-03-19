# Sequenzdiagramm: CI/CD Pipeline

## Übersicht

Das folgende Diagramm zeigt den vollständigen Software Development Life Cycle (SDLC)
von der lokalen Entwicklung bis zum Deployment in die Produktivumgebung.

## Diagramm

```mermaid
sequenceDiagram
    actor Dev as Developer
    participant Local as Lokale Umgebung
    participant GH as GitHub (Remote)
    participant CI as CI Pipeline<br/>(GitHub Actions)
    participant CD as CD Pipeline<br/>(GitHub Actions)
    participant Prod as Produktion<br/>(GitHub Release)

    Note over Dev, Prod: Phase 1: Entwicklung (Feature Branch)

    Dev->>Local: Code schreiben & lokal testen
    Dev->>Local: git checkout -b feature/xyz
    Dev->>Local: git commit (atomare Commits)
    Local->>GH: git push origin feature/xyz (HTTPS)

    Note over Dev, Prod: Phase 2: Code Review & CI (develop)

    Dev->>GH: Pull Request → develop erstellen
    GH->>CI: PR Event triggert CI Pipeline (Webhook)

    par Qualitätssicherung (parallel)
        CI->>CI: pytest (Unit Tests + Coverage)
        CI->>CI: flake8 (Linting)
        CI->>CI: mypy (Static Type Checking)
        CI->>CI: bandit (Security Scanning)
    end

    alt Alle Checks bestanden
        CI-->>GH: Status: success (GitHub API)
        GH-->>Dev: ✓ Ready to merge
        Dev->>GH: PR mergen → develop
    else Check fehlgeschlagen
        CI-->>GH: Status: failure (GitHub API)
        GH-->>Dev: ✗ Fixes erforderlich
        Dev->>Local: Fehler beheben
        Local->>GH: Fix pushen (HTTPS)
        GH->>CI: CI erneut getriggert
    end

    Note over Dev, Prod: Phase 3: Release & CD (main)

    Dev->>GH: Pull Request: develop → main
    GH->>CI: PR Event triggert CI Pipeline (Webhook)
    CI-->>GH: Status: success (GitHub API)
    Dev->>GH: PR mergen → main

    GH->>CD: Push auf main triggert CD Pipeline (Webhook)
    CD->>CD: Build Artefakt erzeugen
    CD->>CD: Version-Tag generieren
    CD->>Prod: GitHub Release erstellen (GitHub API)
    CD->>Prod: Artefakt hochladen

    Prod-->>Dev: Release verfügbar (Notification)
```

## Verwendete Protokolle

| Protokoll | Verwendung |
|-----------|------------|
| **HTTPS** | Git Push/Pull zwischen lokaler Umgebung und GitHub |
| **GitHub API (REST)** | Status Checks, Release-Erstellung, Artefakt-Upload |
| **Webhooks (HTTPS)** | GitHub triggert Actions-Workflows bei Push/PR Events |
| **SMTP** | Benachrichtigungen bei Release (GitHub Notifications) |

## QA-Maßnahmen im Detail

| Maßnahme | Tool | Zweck |
|----------|------|-------|
| Unit Tests | pytest + pytest-cov | Funktionale Korrektheit, Testabdeckung |
| Linting | flake8 | Code-Stil, PEP 8 Konformität |
| Type Checking | mypy | Statische Typprüfung, Fehler vor Laufzeit erkennen |
| Security Scan | bandit | Sicherheitslücken im Python-Code erkennen |
| Code Review | Pull Requests | Manuelle Prüfung durch Entwickler |
| Branch Protection | GitHub Rules | Erzwingt CI-Checks und PR-Reviews vor Merge |
