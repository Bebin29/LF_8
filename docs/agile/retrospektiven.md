# Sprint-Retrospektiven

## Sprint 0: Setup & Architektur

### Was lief gut?
- Die Projektstruktur war von Anfang an sauber definiert (Separation of Concerns)
- CI-Pipeline war sofort einsatzbereit und hat direkt Fehler in den Branch Protection
  Rules aufgedeckt (Job-Namen stimmten nicht mit der Matrix überein)
- Git-Flow-Branching-Strategie (main/develop/feature) wurde früh etabliert

### Was lief nicht gut?
- Branch Protection Rules mussten nachträglich angepasst werden, da die CI-Job-Namen
  durch die Python-Versionsmatrix anders benannt wurden als erwartet
- Der initiale Push auf `main` wurde vergessen, sodass der Branch auf dem Remote
  nicht existierte

### Was nehmen wir mit?
- CI-Pipeline immer sofort testen, nicht nur konfigurieren
- Bei Matrix-Builds die tatsächlichen Check-Namen verifizieren
- Branch Protection erst setzen, wenn die Pipeline mindestens einmal erfolgreich lief

---

## Sprint 1: Core Monitoring

### Was lief gut?
- Feature-Branch-Workflow hat sich bewährt — jedes Feature isoliert entwickelt und getestet
- Die Trennung in Alarm- und Monitoring-Modul war sauber und hat die Testbarkeit erleichtert
- mypy hat direkt Type-Fehler im AlarmManager aufgedeckt (`Optional[str]` in SMTP-Methode)
- CD-Pipeline mit automatischen GitHub Releases funktionierte auf Anhieb

### Was lief nicht gut?
- mypy-Fehler im AlarmManager hätten durch konsistentere Typisierung vermieden werden können
  (der `all()`-Check wurde von mypy nicht als Type Guard erkannt)
- Die config.ini musste nachträglich um Soft-/Hardlimits erweitert werden, da die
  ursprüngliche Struktur nur einfache Schwellenwerte vorsah

### Was nehmen wir mit?
- Type Hints von Anfang an strikt schreiben, nicht erst durch mypy-Fehler korrigieren
- Konfigurationsstruktur vor der Implementierung vollständig durchdenken
- Separate Commit für Fixes (z.B. mypy-Korrekturen) statt alles in einen großen Commit zu packen

---

## Sprint 2: CLI, Config & Tests

### Was lief gut?
- ConfigLoader und CLI konnten in einem Feature-Branch zusammengefasst werden,
  da sie eng zusammenhängen
- 22 Tests wurden implementiert (weit über die geforderten 5 für Could-Have)
- Logger-Isolationsproblem wurde schnell identifiziert und behoben
- flake8 hat unbenutzte Imports sofort aufgedeckt

### Was lief nicht gut?
- Logger-Caching in Python hat zu Test-Failures geführt — mehrere AlarmManager-Instanzen
  teilten sich denselben Logger und damit denselben FileHandler
- Zwei Python-Versionen auf dem System (3.11 + 3.14) führten zu Verwirrung bei
  der lokalen Testausführung (psutil war nur für eine Version installiert)

### Was nehmen wir mit?
- Bei Logging in Python immer eindeutige Logger-Namen verwenden (z.B. mit `id(self)`)
- Lokale Entwicklungsumgebung mit virtualenv isolieren, um Versionskonflikte zu vermeiden
- Tests immer lokal ausführen, bevor sie gepusht werden

---

## Sprint 3: Agile Dokumentation

### Was lief gut?
- Scrum-Rollen konnten klar auf das 4er-Team verteilt werden
- Die Retrospektiven basieren auf echten Erfahrungen aus den vorherigen Sprints
- GitHub Projects Board war von Anfang an gepflegt und aktuell

### Was könnte verbessert werden?
- Retrospektiven sollten idealerweise direkt nach jedem Sprint stattfinden,
  nicht gesammelt am Ende
- Das Board hätte aktiver für die Kommunikation im Team genutzt werden können
  (z.B. Kommentare in Issues für Diskussionen)

### Was nehmen wir mit?
- Retrospektiven sind am wertvollsten, wenn sie zeitnah stattfinden
- Ein gepflegtes Board ist die Grundlage für transparente Zusammenarbeit
