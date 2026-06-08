# modules.md — Nye moduler eller sider

**Lesing:** Før du lager en ny modul, side, eller endrer navigasjonen.

---

**Single source of truth:** [PRD.md](../PRD.md) §FR-3.8 og §FR-3.12

## Oversikt

Moduler ligger i `modules/<slug>/` og eksponeres via en wrapper i `pages_content/modules/m{nr:02d}_{slug}.py`.

Navigasjon styres av `data/moduler.py` — `MODULER`-listen (modul-metadata) og `SECTIONS`-listen (kategorier).

## Når du lager en ny modul

1. Les PRD §FR-3.8 og §FR-3.12 først
2. Opprett `modules/<slug>/` med:
   - `__init__.py`
   - `app_logic.py` (KUN layout, ingen prosa)
   - `content/` (mappe med `.md`-filer for all tekst)
   - Evt. `admin_logic.py`, `db.py`, `config.py` for interaktive moduler
3. Lag `pages_content/modules/m{nr:02d}_{slug}.py` som wrapper
4. Registrer i `data/moduler.py`:
   - Legg til dict i `MODULER` (nr, slug, tittel, kategori)
   - Legg til `page_id()` i riktig seksjon i `SECTIONS`
5. Hvis ny DB-tabell: lag `kurs.<slug>_responses` i Supabase (jf. PRD §DM-5.2)
6. Oppdater PRD §8 (endringslogg)

## Layout struktur

Les `modules/shared/ui.py` for hjelpere:
- `module_header(title, subtitle="...")` — modul-hero (azur eyebrow, marine H1)
- `crumb()` — brødsmulesti (for navigasjon)
- `callout(text, kind="info"|"tip"|"warn"|"subtle")` — fargede informasjonsbokser
- `card(key="...")` — hvite kort
- `load_markdown(__file__, "name")` — hent `.md`-filer fra `content/` mappen

## Innhold

**Viktig:** Du genererer **ikke** innholdet på moduler uten eksplisitt forespørsel. Lag tomme `<!-- placeholder -->`-filer.

Eier skriver snakkepunkter, eksempler, og beskrivelser selv.
