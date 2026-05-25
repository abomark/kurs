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
- Palett: Vann (`#005AA4`), Fjell (`#002776`), Sand (`#F8E9DD`), Frost (`#7EB5D2`), Syrin (`#D3D3EA`)
- Font: Arial gjennomgående (ikke Inter, ikke Roboto)
- Tema: [`.streamlit/config.toml`](.streamlit/config.toml) — kanonisk versjon i DESIGN_GUIDE §6
- Callouts: `callout()`-helper i `modules/shared/ui.py` matcher guide §5.2–5.4
- Emojis: påkrevd i H1/H2-overskrifter og callout-titler. IKKE som dekorasjon i brødtekst. Maks 2 emojis per overskrift.

**Tidligere "ingen ikoner"-regel er overstyrt.** Emojis er nå en del av designet — i headers og callouts, ikke som tekst-dekorasjon.

**Når du legger til/endrer en modul:** gå gjennom sjekklista i DESIGN_GUIDE §10 før du sier "ferdig".

**Endringslogg:** oppdater også [`CHANGELOG.md`](CHANGELOG.md) ved hver design- eller modul-endring.

## Innhold på modulsider — Andre skriver selv

**Du genererer ikke innhold på modulsider uten eksplisitt forespørsel.**

Når Andre ber om en ny modul eller side, bygger du KUN strukturen:
- Mappestruktur (`modules/<navn>/`, `pages/<navn>.py`)
- Navigasjon (oppføring i `hub.py` og `home.py`)
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
- Nye krav får ny ID (f.eks. neste ledige `FR-3.10`). Aldri renummerér eksisterende ID-er.

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

Entry point: `streamlit run hub.py` fra repo-rot.

```
kurs/
├── PRD.md # ← single source of truth
├── CLAUDE.md # ← denne fila
├── hub.py # Forside (URL: /)
├── pages/ # Streamlit multipage – URL per fil
│ ├── cortex_code.py # Modul 1
│ ├── cortex_interaction.py # Modul 2
│ ├── cortex_in_snowsight.py # Modul 3
│ ├── demo_1.py # Modul 4
│ ├── agents_md.py # Modul 5 (presentasjon)
│ ├── skills_md.py # Modul 6 (presentasjon)
│ ├── gruppeoppgave_1.py # Modul 7 (interaktiv workshop)
│ └── admin_gruppeoppgave_1.py # Admin for gruppeoppgave_1
├── modules/
│ ├── agents_md/ # Modul 5 – konseptuell presentasjon
│ │ ├── app_logic.py
│ │ └── content/ # Markdown-blokker (FR-3.12)
│ ├── skills_md/ # Modul 6 – konseptuell presentasjon
│ │ ├── app_logic.py
│ │ └── content/ # Markdown-blokker (FR-3.12)
│ ├── gruppeoppgave_1/ # Modul 7 – interaktiv workshop
│ │ ├── app_logic.py # main() for deltaker
│ │ ├── admin_logic.py # main() for admin
│ │ ├── db.py # Supabase-klient (schema=kurs)
│ │ ├── reducer.py # PRD §FR-3.5
│ │ ├── viz.py # PRD §FR-3.4
│ │ ├── config.py # QUESTIONS, STOPWORDS
│ │ ├── claude_answers.py # PRD §FR-3.6
│ │ └── supabase_schema.sql # PRD §DM-5.1
│ └── shared/
│ └── ui.py # Felles loader-helpers (FR-3.12)
├── .streamlit/secrets.toml # IKKE commit (gitignored)
├── requirements.txt # PRD §7
└── README.md # Praktisk oppsett
```

## Konvensjoner

- **Imports:** filer inne i `modules/<navn>/` bruker relative imports (`from .config import …`). Wrappers i `pages/` og `hub.py` bruker absolutt (`from modules.gruppeoppgave_1.app_logic import main`).
- **Set page config:** kalles én gang i hver `pages/*.py` wrapper, *ikke* i `app_logic.py` eller `admin_logic.py`.
- **Streamlit multipage:** filnavn i `pages/` blir URL-en automatisk. Ikke endre filnavn uten å oppdatere PRD §FR-3.8 og lenker i `hub.py`.
- **Secrets:** alltid via `st.secrets[...]`. Aldri hardkod, aldri legg i config.py.
- **Språk:** UI og kommentarer i koden på norsk (matcher målgruppen). PRD og denne fila også på norsk.

## Vanlige kommandoer

```bash
# Sett opp lokalt
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

# Kjør
streamlit run hub.py
```

## Når du legger til en ny modul

Sjekk PRD §FR-3.8 og §FR-3.12 først. Deretter:

1. Opprett `modules/<navn>/` med:
   - `__init__.py`
   - `app_logic.py` (KUN layout, ingen prosa-strenger – jf. §FR-3.12)
   - `content/` (mappe med `.md`-filer for all prosa)
   - Evt. `admin_logic.py`, `db.py`, `config.py` for interaktive moduler
2. Lag `pages/<navn>.py` (og evt. `pages/admin_<navn>.py`) som tynne wrappers.
3. Bruk `load_markdown(__file__, name)` og `load_titled_markdown(__file__, name)` fra `modules/shared/ui.py` for å hente innhold inn i layout.
4. Legg modul til som `st.Page` i `hub.py` og til `MODULES` i `home.py`.
5. Hvis ny DB-tabell: lag `kurs.<navn>_responses` i det felles `kurs`-schemaet (PRD §DM-5.2). Definer `SCHEMA = "kurs"` og `TABLE = "<navn>_ responses"` som konstanter i `db.py`. Ingen Supabase dashboard-endring nødvendig — `kurs` er allerede i "Exposed schemas".
6. Oppdater PRD §8 endringslogg.

**Andre skriver innholdet selv** — ikke generér prosa i `.md`-filene uten eksplisitt forespørsel. Lag tomme `<!-- placeholder -->`-filer.

## Hvis du er Claude (eller annen AI-agent)

- Les PRD.md før du foreslår strukturelle endringer.
- Foreslå PRD-oppdateringer eksplisitt i samtale — ikke gjør dem "i forbifarten" sammen med kode.
- Hvis du ser drift (kode != PRD), si fra heller enn å stille-rette én av sidene.
