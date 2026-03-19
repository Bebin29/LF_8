# Vergleich: Scrum vs. traditionelle Softwareentwicklungsmodelle

## Übersicht

In der Softwareentwicklung gibt es verschiedene Vorgehensmodelle. Grob lassen sie sich
in **iterative** (z.B. Scrum) und **sequenzielle** (z.B. Wasserfall, V-Modell) Ansätze
unterteilen. Im Folgenden werden die Modelle verglichen und Vor- sowie Nachteile benannt.

## Die Modelle im Überblick

### Scrum (iterativ/agil)

Scrum ist ein agiles Framework, das Software in kurzen Iterationen (Sprints, 1-4 Wochen)
entwickelt. Nach jedem Sprint liegt ein potenziell auslieferbares Produktinkrement vor.

```
Sprint 1 → Sprint 2 → Sprint 3 → Sprint 4
[Plan→Do→Review→Retro] → [Plan→Do→Review→Retro] → ...
```

**Kernprinzipien:**
- Kurze Feedback-Zyklen
- Selbstorganisierte Teams
- Anpassung an sich ändernde Anforderungen
- Kontinuierliche Verbesserung (Retrospektiven)

### Wasserfallmodell (sequenziell)

Das Wasserfallmodell durchläuft feste Phasen streng nacheinander.
Jede Phase muss abgeschlossen sein, bevor die nächste beginnt.

```
Anforderungen → Entwurf → Implementierung → Test → Betrieb
      ↓            ↓            ↓             ↓        ↓
   (fertig)     (fertig)     (fertig)      (fertig)  (fertig)
```

**Kernprinzipien:**
- Vollständige Planung vor Projektbeginn
- Klare Phasengrenzen und Meilensteine
- Umfangreiche Dokumentation pro Phase
- Änderungen sind teuer und schwierig

### V-Modell (sequenziell mit Verifikation)

Das V-Modell erweitert das Wasserfallmodell um eine Testphase, die jeder
Entwicklungsphase gegenübersteht. Die linke Seite des "V" ist die Entwicklung,
die rechte Seite die zugehörige Verifikation.

```
Anforderungen ────────────────── Abnahmetest
     \                              /
      Entwurf ──────────── Integrationstest
           \                    /
            Implementierung ── Unit Test
```

**Kernprinzipien:**
- Jede Entwicklungsphase hat eine korrespondierende Testphase
- Tests werden parallel zur Entwicklung geplant
- Stärkerer Fokus auf Qualitätssicherung als beim Wasserfall
- Ebenfalls sequenziell — Rücksprünge sind nicht vorgesehen

## Vergleich

| Kriterium | Scrum | Wasserfall | V-Modell |
|-----------|-------|------------|----------|
| **Flexibilität** | Hoch — Änderungen in jedem Sprint möglich | Niedrig — Änderungen nur mit hohem Aufwand | Niedrig — Änderungen erfordern Rücksprünge |
| **Kundenfeedback** | Kontinuierlich (nach jedem Sprint) | Erst am Ende (Abnahme) | Erst in der Testphase |
| **Planbarkeit** | Mittel — Sprint-Planung, aber Gesamtumfang kann sich ändern | Hoch — alles ist vorab geplant | Hoch — Phasen und Tests vorab definiert |
| **Dokumentation** | Minimal — "Working Software over Documentation" | Umfangreich — pro Phase | Umfangreich — pro Phase + Testdoku |
| **Qualitätssicherung** | Integriert (CI/CD, Reviews, Tests pro Sprint) | Am Ende (Testphase) | Parallel zur Entwicklung geplant |
| **Teamgröße** | Kleine Teams (3-9 Personen) | Beliebig, oft große Teams | Beliebig, oft in regulierten Branchen |
| **Risikomanagement** | Früh — Probleme werden in Sprints sichtbar | Spät — Probleme erst in der Testphase | Mittel — Tests sind geplant, aber spät ausgeführt |
| **Time-to-Market** | Schnell — erstes Inkrement nach Sprint 1 | Langsam — erst nach allen Phasen | Langsam — erst nach allen Phasen |

## Vor- und Nachteile

### Scrum

| Vorteile | Nachteile |
|----------|-----------|
| Schnelle Anpassung an neue Anforderungen | Schwer planbar für Festpreisprojekte |
| Regelmäßiges Kundenfeedback | Erfordert erfahrene, selbstorganisierte Teams |
| Frühe Fehlererkennung durch kurze Zyklen | Kann bei schlechter Umsetzung chaotisch wirken |
| Hohe Motivation durch sichtbare Fortschritte | Scope Creep möglich, wenn PO nicht konsequent priorisiert |
| Kontinuierliche Verbesserung durch Retrospektiven | Overhead durch Meetings (Daily, Planning, Review, Retro) |

### Wasserfallmodell

| Vorteile | Nachteile |
|----------|-----------|
| Klare Struktur und Meilensteine | Keine Flexibilität bei Änderungen |
| Einfach zu verstehen und zu managen | Fehler werden erst spät entdeckt |
| Gut planbar (Zeit, Budget, Umfang) | Kein Kundenfeedback bis zum Ende |
| Umfangreiche Dokumentation | Hoher Dokumentationsaufwand |
| Geeignet für stabile Anforderungen | Hohe Kosten bei nachträglichen Änderungen |

### V-Modell

| Vorteile | Nachteile |
|----------|-----------|
| Bessere QA als Wasserfall durch parallele Testplanung | Genauso unflexibel wie Wasserfall |
| Klare Zuordnung: Entwicklungsphase ↔ Testphase | Hoher Dokumentations- und Planungsaufwand |
| Bewährt in regulierten Branchen (Medizin, Automobil) | Tests werden erst spät ausgeführt |
| Fehler werden systematischer gefunden | Kein Kundenfeedback während der Entwicklung |

## Fazit: Warum Scrum für unser Projekt?

Für unser Berufsschulprojekt war Scrum die richtige Wahl, weil:

1. **Kurze Projektlaufzeit** — In wenigen Wochen mussten wir ein funktionierendes System liefern. Scrum ermöglichte es, nach jedem Sprint ein funktionierendes Inkrement zu haben.
2. **Kleines Team** — Mit 4 Personen ist Scrum ideal. Wasserfall oder V-Modell hätten einen unverhältnismäßigen Planungsoverhead erzeugt.
3. **Lerneffekt** — Durch die Retrospektiven konnten wir aus Fehlern lernen (z.B. Branch Protection, mypy-Typisierung) und den Prozess verbessern.
4. **CI/CD-Integration** — Scrum und CI/CD ergänzen sich perfekt: Jeder Sprint liefert getesteten, deployten Code.

In regulierten Branchen (z.B. Medizintechnik) oder bei Projekten mit fixen Anforderungen
und Festpreisverträgen wäre hingegen das V-Modell besser geeignet, da es eine
nachvollziehbare Dokumentation und systematische Testplanung garantiert.
