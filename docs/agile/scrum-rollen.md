# Scrum-Rollen und Teamstruktur

## Teamübersicht

| Rolle | Name | Verantwortlichkeiten |
|-------|------|---------------------|
| Product Owner | Jonas | Anforderungen priorisieren, Backlog pflegen, Abnahme der Ergebnisse |
| Scrum Master | Marlon | Prozess moderieren, Hindernisse beseitigen, Retrospektiven leiten |
| Developer | Ben | Implementierung, Code Reviews, Unit Tests |
| Developer | Justin | Implementierung, Dokumentation, Integrationstests |

## Rollenbeschreibungen

### Product Owner

Der Product Owner vertritt die Interessen der Stakeholder (in unserem Fall: die Anforderungen
der Berufsschule) und ist verantwortlich für die Maximierung des Produktwerts.

**Aufgaben im Projekt:**
- Pflege und Priorisierung des Product Backlogs (GitHub Issues)
- Definition der Akzeptanzkriterien für jedes Issue
- Abnahme der fertigen Features nach dem Review
- Entscheidung über die Reihenfolge der Implementierung (MoSCoW-Priorisierung)

### Scrum Master

Der Scrum Master sorgt dafür, dass das Team die Scrum-Praktiken einhält und
unterstützt bei der Beseitigung von Hindernissen.

**Aufgaben im Projekt:**
- Moderation der Sprint-Planung und Retrospektiven
- Überwachung des Kanban-Boards (GitHub Projects)
- Sicherstellung, dass der Workflow eingehalten wird (Feature-Branch → PR → Review → Merge)
- Eskalation von Blockern (z.B. technische Probleme, fehlende Zugänge)

### Developer

Die Developer sind für die technische Umsetzung verantwortlich. In unserem 4er-Team
teilen sich zwei Entwickler die Implementierungsarbeit.

**Aufgaben im Projekt:**
- Implementierung der Features gemäß Akzeptanzkriterien
- Schreiben von Unit- und Integrationstests
- Code Reviews bei Pull Requests
- Technische Dokumentation (Klassendiagramm, Sequenzdiagramm)

## Erweiterte Rollen in komplexeren Projekten

In größeren, realen Projekten kommen weitere Rollen hinzu, die in unserem
Berufsschulprojekt nicht erforderlich, aber in der Praxis relevant sind:

### Stakeholder

Stakeholder sind Personen oder Gruppen, die ein Interesse am Projektergebnis haben,
aber nicht direkt am Entwicklungsprozess beteiligt sind.

**Beispiele:** Auftraggeber, Endnutzer, Management, Lehrerteam (in unserem Kontext).

**Relevanz:** In unserem Projekt nimmt das Lehrerteam die Rolle der Stakeholder ein —
sie definieren die Anforderungen (Aufgabenstellung) und bewerten das Ergebnis.

### Release Manager

Der Release Manager koordiniert die Auslieferung der Software in die
Produktivumgebung und stellt sicher, dass alle Qualitätskriterien erfüllt sind.

**Aufgaben:**
- Koordination des Release-Prozesses (develop → main)
- Sicherstellung, dass alle CI/CD-Checks bestanden sind
- Erstellung von Release Notes
- Rollback-Planung bei Problemen

**Relevanz:** In unserem Projekt wird diese Rolle durch die CD-Pipeline und die
Branch Protection Rules automatisiert. Bei größeren Projekten mit mehreren Teams
ist eine dedizierte Person dafür notwendig.

### QA Engineer / Tester

Ein dedizierter QA Engineer fokussiert sich ausschließlich auf die Qualitätssicherung
und entwickelt Teststrategien unabhängig vom Entwicklungsteam.

**Aufgaben:**
- Erstellung von Testplänen und Testfällen
- Explorative Tests (manuell)
- Performance- und Lasttests
- Pflege der Testautomatisierung

**Relevanz:** In unserem Projekt übernehmen die Developer diese Rolle mit.
Bei größeren Projekten sorgt ein separater QA Engineer für eine unabhängige
Qualitätsperspektive.

### DevOps Engineer

Der DevOps Engineer ist verantwortlich für die Infrastruktur, CI/CD-Pipelines
und den Betrieb der Software in der Produktivumgebung.

**Aufgaben:**
- Aufbau und Pflege der CI/CD-Pipeline
- Infrastruktur-Management (Server, Container, Cloud)
- Monitoring und Alerting in der Produktivumgebung
- Incident Response bei Ausfällen

**Relevanz:** In unserem Projekt haben wir die CI/CD-Pipeline mit GitHub Actions
aufgebaut. In realen Projekten ist dies eine Vollzeit-Rolle, besonders wenn
Kubernetes, Cloud-Infrastruktur oder komplexe Deployment-Strategien im Spiel sind.
