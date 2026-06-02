# CLAUDE.md

## Målgruppe

Kurset er rettet mot **analytikere og data scientists i norske banker**. Det former hvordan innhold og eksempler skal vinkles:

- **Regulatorisk kontekst:** Finanstilsynet, GDPR, IFRS. Risk-, IT- og Compliance-godkjenning er ofte gate-keeperen for nye verktøy — ikke personlig preferanse alene.
- **Risikoaverse kultur:** Agent-/autonomi-tilnærminger må holdes opp mot eksisterende kontrollrammeverk. Antageligen mer skepsis enn entusiasme rundt "agenten gjør det selv".
- **Variert teknisk bakgrunn:** Fra SQL+Excel via notebooks til Python/ML-pipelines. SAS og R fortsatt i bruk hos noen. Snowflake-adopsjon er relativt fersk.
- **Datasensitivitet:** Eksempler skal være **generiske eller fiktive** — aldri konkrete kundeegenskaper, transaksjoner eller andre PII-fragmenter. Bruk "kundeID 123" og syntetiske kolonner.
- **AI-verktøy i hverdagen:** Forvent at deltakere har testet Copilot/Claude/ChatGPT privat, men sjelden hatt full produksjonsbruk på jobben. Mange er nysgjerrige, men ikke nødvendigvis erfarne i agentisk flyt.

**Konsekvenser for innhold:**
- Unngå tech-bro-tonalitet ("AI eats the world"). Bank-publikummet vil se konkret nytte mot deres faktiske oppgaver.
- Konkrete eksempler bør være anonymiserte og bank-aktuelle: kredittscoring, kundefrafall, regulatorisk rapportering, dataplattform-pipelines.
- Snakke om risiko + nytte parallelt — ikke skjule begrensningene.

## Visuell stil: følg DESIGN_GUIDE.md

[`DESIGN_GUIDE.md`](DESIGN_GUIDE.md) er **single source of truth** for all visuell stil i appen — farger, fonter, layout, callouts, emoji-bruk og forbudte mønstre. Den overstyrer dine generelle preferanser om "moderne" eller "kreativ" UI.

**Kort sammendrag:**
- Palett (lyst «Bankbrief», jf. DESIGN_GUIDE §2): Vann/Marine (`#0A2C72`), Fjell (`#071E50`), Frost/Azur (`#1F6FC4`), Sand/Fersken (`#F8E6D5`), Syrin/Amber (`#C9821B`)
- Font: Arial gjennomgående (ikke Inter, ikke Roboto)
- Tema: [`.streamlit/config.toml`](.streamlit/config.toml) — kanonisk versjon i DESIGN_GUIDE §6
- Callouts: `callout()`-helper i `modules/shared/ui.py` matcher guide §5.2–5.4
- **Ingen emojis; SVG-linjeikoner er ikon-språket** (DESIGN_GUIDE §1.7, eier-beslutning 2026-05-31): overskrifter, `st.subheader`, `st.expander`-labels, callout-titler, crumbs og brødtekst skal aldri ha emoji-dekorasjon. Sanksjonert ikon-form er SVG-linjeikoner via `svg_icon()` i `modules/shared/ui.py` (callout-badger, funksjonskort-disker, knapper). Typografiske piler (`→`/`←`) i prosa er ok. Ett emoji-unntak: nettleserfanens favicon `page_icon="❄"` i `app.py` (fane-metadata, ikke side-innhold).
- **Aldri en-dash (`–`) eller em-dash (`—`)** noe sted (DESIGN_GUIDE §1.8, eier-beslutning 2026-05-31): bruk vanlig bindestrek `-`, komma eller kolon - også i docstrings og kommentarer.
- **Aldri `é`/`É`** (DESIGN_GUIDE §1.10, eier-beslutning 2026-05-31): bruk alltid `e`/`E`; det vanligste tilfellet er ordet for tallet 1 (skriv «en», uten aksent).

**Når du legger til/endrer en modul:** gå gjennom sjekklista i DESIGN_GUIDE §10 før du sier "ferdig".

**Endringslogg:** oppdater også [`CHANGELOG.md`](CHANGELOG.md) ved hver design- eller modul-endring.

## Innhold på modulsider — Andre skriver selv

**Du genererer ikke innhold på modulsider uten eksplisitt forespørsel.**

Når Andre ber om en ny modul eller side, bygger du KUN strukturen:
- Mappestruktur (`modules/<navn>/`, `pages_content/modules/m{nr:02d}_{slug}.py`)
- Navigasjon (oppføring i `data/moduler.py`: `MODULER` + `SECTIONS`)
- Seksjons-headere og layout (`st.subheader`, `st.container`, `st.columns`, ...)
- Tomme/eksplisitt merkede placeholder-felt der innhold skal inn

Snakkepunkter, beskrivelser, eksempler, taleformuleringer, demo-steg og lignende — det fyller Andre ut selv manuelt.

**Unntak:** Hvis Andre eksplisitt ber om innhold ("draft snakkepunktene", "skriv beskrivelsen", "foreslå eksempler", "fyll ut basert på <kilde>"), så drafter du. Hvis i tvil — spør først.

**Hvorfor:** Innholdet skal være Andres egne ord og produktspesifikke kunnskap. AI-fabrikerte påstander om Snowflake/Cortex Code/produktdetaljer er en risiko (kan være feil) og en forurensning (Andre må verifisere alt jeg har funnet på).

## Single source of truth: PRD.md

[`PRD.md`](PRD.md) er **single source of truth** for dette prosjektet. Kode og PRD skal til enhver tid være i sync.

- Før du endrer kode: les relevant PRD-seksjon. Hvis koden divergerer fra PRD-en, avgjør hvilken som er riktig — så oppdater den andre.
- Før du endrer atferd: oppdater PRD-en *først*, så koden. Aldri silent drift.
- Hvis PRD er tvetydig: avklar med eier (Andre) i samtale, så oppdater PRD-en med avklaringen, så koden.
- Nye krav får ny ID (f.eks. neste ledige `FR-3.10`). Aldri renummerer eksisterende ID-er.

## Kodekommentarer skal referere PRD

Når koden implementerer en bestemt PRD-paragraf og koblingen ikke er åpenbar fra koden alene, **legg ved en referanse** i en kort kommentar:

```python
# PRD §FR-3.4: skjul resultater til minst 3 svar er inne
MIN_RESPONSES_BEFORE_REVEAL = 3
```

```python
# PRD §NFR-4.2: anon må ikke kunne SELECT — bruk returning=minimal
.insert({...}, returning="minimal")
```

**Når referere:** WHY-en kommer fra PRD, eller magisk verdi/policy som vil virke vilkårlig uten kontekst.

**Når IKKE referere:** trivielle ting (variabelnavn, små helpers, opplagt UI-tekst). PRD-referanse er signalbærende — overbruk gjør den verdiløs.

## Sjekk før commit / før du sier "ferdig"

1. **Diverger koden fra PRD?** Hvis ja: hvilken er riktig? Oppdater den andre.
2. **Er det en ny `FR-` eller `NFR-`?** Legg den til i PRD med ny ID, og referer fra koden.
3. **Endret du en eksisterende paragraf vesentlig?** Oppdater endringsloggen i PRD §8.
4. **Slettet du kode som realiserte et PRD-krav?** Slett kravet eller marker det som ut-av-scope.

## Repo-orientering

Entry point: `streamlit run app.py` fra repo-rot.

Appen er **ikke** Streamlit-multipage. `app.py` leser `?page=<slug>` fra URL-en
og dispatcher til riktig side. Navigasjon styres av en custom sidebar
(`components/sidebar.py`) med kategori-prikker og seksjoner. `data/moduler.py`
er den kanoniske modul-lista som både sidebaren og forsiden leser fra.

```
kurs/
├── PRD.md # ← single source of truth
├── CLAUDE.md # ← denne fila
├── DESIGN_GUIDE.md # ← visuell stil-autoritet
├── CHANGELOG.md
├── app.py # Entry point: leser ?page=… og dispatcher til side
├── components/
│ └── sidebar.py # Custom sidebar (kategori-prikker + seksjoner)
├── data/
│ └── moduler.py # ← kanonisk modul-liste: MODULER, SECTIONS, page_id()
├── pages_content/ # Sideinnhold (IKKE Streamlit-multipage)
│ ├── forside.py # Forside (?page=forside)
│ ├── bli_kjent.py # Oppvarming/Bli kjent (?page=bli_kjent)
│ ├── resultater.py # Samle-resultatside
│ ├── admin.py # Admin
│ └── modules/ # Tynne wrappers, en per modul, navngitt m{nr:02d}_{slug}
│   ├── m01_evolusjon.py # → modules.evolusjon.app_logic.main as render
│   ├── m12_gruppeoppgave_1.py
│   ├── m13_gruppeoppgave_1_resultater.py
│   └── … # 29 wrappers totalt
├── modules/
│ ├── <slug>/ # En mappe per modul (slug matcher data/moduler.py)
│ │ ├── app_logic.py # main() – KUN layout (FR-3.12)
│ │ └── content/ # Markdown-blokker (FR-3.12)
│ ├── gruppeoppgave_1/ # Interaktiv workshop (eksempel på full modul)
│ │ ├── app_logic.py # main() for deltaker
│ │ ├── admin_logic.py # main() for admin
│ │ ├── views.py # Delt resultatvisning (PRD §FR-3.13)
│ │ ├── db.py # Supabase-klient (schema=kurs)
│ │ ├── reducer.py # PRD §FR-3.5
│ │ ├── viz.py # PRD §FR-3.4 (ordsky + barchart)
│ │ ├── config.py # QUESTIONS, STOPWORDS
│ │ ├── claude_answers.py # PRD §FR-3.6
│ │ └── supabase_schema.sql # PRD §DM-5.1
│ └── shared/
│ └── ui.py # Felles helpers: load_markdown, callout, card …
├── .streamlit/secrets.toml # IKKE commit (gitignored)
├── requirements.txt # PRD §7
└── README.md # Praktisk oppsett
```

## Konvensjoner

- **Imports:** filer inne i `modules/<navn>/` bruker relative imports (`from .config import …`). Wrappers i `pages_content/modules/` bruker absolutt og eksponerer `render` (ikke `main`): `from modules.<slug>.app_logic import main as render`.
- **Set page config:** kalles en gang sentralt i `app.py` (layout velges via `WIDE_LAYOUT_PAGES`), *ikke* i wrapperne, `app_logic.py` eller `admin_logic.py`.
- **Navigasjon:** `app.py` leser `?page=<slug>`. Faste sider (`forside`, `bli_kjent`, `resultater`, `admin`) ligger i `pages_content/`. Modul-sider rutes via `page_id()` → `pages_content/modules/m{nr:02d}_{slug}.py`. Ikke endre wrapper-filnavn uten å oppdatere `nr`/`slug` i `data/moduler.py` tilsvarende (og PRD §FR-3.8).
- **Secrets:** alltid via `st.secrets[...]`. Aldri hardkod, aldri legg i config.py.
- **Språk:** UI og kommentarer i koden på norsk (matcher målgruppen). PRD og denne fila også på norsk.

## Vanlige kommandoer

```bash
# Sett opp lokalt
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

# Kjør
streamlit run app.py
```

## Når du legger til en ny modul

Sjekk PRD §FR-3.8 og §FR-3.12 først. Deretter:

1. Opprett `modules/<navn>/` med:
   - `__init__.py`
   - `app_logic.py` (KUN layout, ingen prosa-strenger – jf. §FR-3.12)
   - `content/` (mappe med `.md`-filer for all prosa)
   - Evt. `admin_logic.py`, `db.py`, `config.py` for interaktive moduler
2. Lag `pages_content/modules/m{nr:02d}_{slug}.py` som tynn wrapper: `from modules.<slug>.app_logic import main as render`.
3. Bruk `load_markdown(__file__, name)` og `load_titled_markdown(__file__, name)` fra `modules/shared/ui.py` for å hente innhold inn i layout.
4. Registrer modulen i `data/moduler.py`: ny dict i `MODULER` (`nr`, `slug`, `tittel`, `kategori`) og legg `page_id()` i riktig seksjon i `SECTIONS`. Både sidebaren og forsiden leser herfra.
5. Hvis ny DB-tabell: lag `kurs.<navn>_responses` i det felles `kurs`-schemaet (PRD §DM-5.2). Definer `SCHEMA = "kurs"` og `TABLE = "<navn>_ responses"` som konstanter i `db.py`. Ingen Supabase dashboard-endring nødvendig — `kurs` er allerede i "Exposed schemas".
6. Oppdater PRD §8 endringslogg.

**Andre skriver innholdet selv** — ikke generer prosa i `.md`-filene uten eksplisitt forespørsel. Lag tomme `<!-- placeholder -->`-filer.

## Hvis du er Claude (eller annen AI-agent)

- Les PRD.md før du foreslår strukturelle endringer.
- Foreslå PRD-oppdateringer eksplisitt i samtale — ikke gjør dem "i forbifarten" sammen med kode.
- Hvis du ser drift (kode != PRD), si fra heller enn å stille-rette en av sidene.
