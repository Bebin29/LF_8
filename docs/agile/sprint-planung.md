# Sprint-Planung und Aufgabenverteilung

## Übersicht

Das Projekt wurde in 4 Sprints aufgeteilt (jeweils ca. 1 Woche).
Die Aufgaben wurden mit MoSCoW priorisiert und über GitHub Issues + Projects verwaltet.

**Kanban-Board:** https://github.com/users/Bebin29/projects/6

## Sprint 0: Setup & Architektur (KW 12)

| Aufgabe | Priorität | Verantwortlich | Status |
|---------|-----------|---------------|--------|
| Projektstruktur & Environment-Setup | Must | Ben | Done |
| CI/CD Pipeline (pytest + flake8) | Must | Ben | Done |
| GitHub Project Board einrichten | Must | Ben | Done |
| Branch-Strategie (main/develop/feature) | Must | Ben | Done |

**Ziel:** Fundament schaffen — Repository, Pipeline und agiler Prozess stehen.

## Sprint 1: Core Monitoring (KW 13)

| Aufgabe | Priorität | Verantwortlich | Status |
|---------|-----------|---------------|--------|
| AlarmManager implementieren | Must | Ben | Done |
| SystemMonitor implementieren | Must | Ben | Done |
| QA-Maßnahmen erweitern (mypy, bandit) | Should | Ben | Done |
| CD Pipeline mit GitHub Releases | Could | Ben | Done |
| Sequenzdiagramm der Pipeline | Must | Ben | Done |

**Ziel:** Kernmodule stehen und die Pipeline ist vollständig (CI + CD).

## Sprint 2: CLI, Config & Tests (KW 13)

| Aufgabe | Priorität | Verantwortlich | Status |
|---------|-----------|---------------|--------|
| ConfigLoader (configparser) | Could | Ben | Done |
| CLI mit argparse | Should | Ben | Done |
| 22 automatisierte Tests | Could | Ben | Done |
| Klassendiagramm | Must | Ben | Done |

**Ziel:** Software ist konfigurierbar, steuerbar und vollständig getestet.

## Sprint 3: Agile Dokumentation (KW 13)

| Aufgabe | Priorität | Verantwortlich | Status |
|---------|-----------|---------------|--------|
| Scrum-Rollen dokumentieren | Must | Ben | Done |
| Sprint-Planung & Retrospektiven | Must/Should | Ben | In Progress |
| Vergleich Scrum vs. traditionelle Modelle | Could | Ben | Todo |

**Ziel:** Agiler Prozess ist vollständig dokumentiert.

## Priorisierungsmethode

Die Priorisierung erfolgte nach **MoSCoW** (Must/Should/Could/Won't), wie in der
Aufgabenstellung vorgegeben. Innerhalb der Prioritätsstufen wurde nach technischen
Abhängigkeiten sortiert (z.B. Alarm vor Monitoring, weil Monitoring den Alarm nutzt).
