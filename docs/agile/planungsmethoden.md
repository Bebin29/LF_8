# Planungs- und Schätzungsmethoden

## Verwendete Methode: MoSCoW-Priorisierung

### Beschreibung

MoSCoW ist eine Priorisierungstechnik, die Anforderungen in vier Kategorien einteilt:

| Kategorie | Bedeutung | Beispiel aus dem Projekt |
|-----------|-----------|------------------------|
| **Must have** | Unverzichtbar für den Erfolg | CI-Pipeline, Unit Tests, Schwellenwertprüfung |
| **Should have** | Wichtig, aber nicht kritisch | Zwei Module, E-Mail-Versand, 3+ QA-Maßnahmen |
| **Could have** | Wünschenswert bei ausreichend Zeit | config.ini, 5+ Tests, Plattformunabhängigkeit |
| **Won't have** | Bewusst ausgeschlossen (diesmal) | GUI, Datenbank-Anbindung, Docker-Deployment |

### Anwendung im Projekt

Die MoSCoW-Priorisierung war durch die Aufgabenstellung vorgegeben und wurde
direkt in die Sprint-Planung übernommen:

1. **Sprint 0 + 1:** Alle Must-Haves implementiert
2. **Sprint 1 + 2:** Alle Should-Haves implementiert
3. **Sprint 2:** Alle Could-Haves implementiert

### Bewertung

**War MoSCoW ein Zugewinn für unser Team?** Ja.

**Vorteile:**
- Klare Priorisierung von Anfang an — das Team wusste immer, was als Nächstes kommt
- Verhindert "Feature Creep" — Could-Haves werden erst angegangen, wenn Must/Should stehen
- Einfach verständlich, auch für Teammitglieder ohne Agile-Erfahrung
- Gut kombinierbar mit dem Kanban-Board (Labels für Prioritätsstufen)

**Nachteile:**
- Keine Aufwandsschätzung enthalten — MoSCoW sagt nichts darüber aus, wie lange
  ein Feature dauert
- Die Grenzen zwischen Should und Could sind manchmal subjektiv
- Bei kleinen Teams (wie unserem 4er-Team) ist die Methode fast zu simpel —
  komplexere Projekte profitieren zusätzlich von Story Points oder T-Shirt-Sizing

## Weitere betrachtete Methode: Planning Poker

### Beschreibung

Planning Poker ist eine konsensbasierte Schätzungsmethode, bei der jedes Teammitglied
verdeckt eine Karte mit einem Aufwandswert (Fibonacci: 1, 2, 3, 5, 8, 13, 21) zeigt.
Bei großen Abweichungen wird diskutiert, bis ein Konsens erreicht wird.

### Warum wir es nicht verwendet haben

- Bei einem 4er-Team mit klarer Aufgabenstellung war der Overhead nicht gerechtfertigt
- Die MoSCoW-Kategorien waren bereits durch die Aufgabenstellung vorgegeben
- Planning Poker entfaltet seinen Wert vor allem bei unklaren Anforderungen und
  größeren Teams, wo unterschiedliche Einschätzungen aufgedeckt werden müssen

### Wann Planning Poker sinnvoll wäre

- Teams ab 5+ Personen mit unterschiedlichen Erfahrungsstufen
- Projekte mit unklaren oder komplexen Anforderungen
- Wenn Aufwandsschätzungen für Stakeholder oder Projektplanung benötigt werden
