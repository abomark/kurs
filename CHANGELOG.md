# CHANGELOG

Referert av [DESIGN_GUIDE.md](DESIGN_GUIDE.md) — oppdateres ved hver design- eller modul-endring.

For detaljerte krav-endringer, se PRD.md §8.

---

## 2026-05-25 — Tre nye moduler (UTKAST): Evolusjon, Prompt engineering, Kostnader

Tre nye presentasjonsmoduler (FR-3.11) lagt til som UTKAST. Strukturen er på plass — innholdet (`.md`-filer) er placeholders med `_Andre skriver: ..._`-markører.

**Hvorfor:**
- **Evolusjon** (m01): rammer hele kurset med historisk perspektiv (Google → AI-assistanse → spesifikasjon). Motiverende intro, ikke teknisk.
- **Prompt engineering** (m18): broen fra konsept-modulene (AGENTS/skills/memory) til praktisk dagligbruk. Anatomi, SQL-mønstre, anti-patterns, før/etter-sammenligning.
- **Kostnader** (m25): operasjonell forberedelse før Avslutning. Kostnadsmodell, intern sporing, resource monitors, best practices.

**Ny modul-rekkefølge (26 moduler, 9 seksjoner):**
1. **Introduksjon** (m01–m07): Evolusjon (NY) → Cortex Code → CLI → Snowsight → Arkitektur → Demo → Individuell 1
2. **AGENTS.md** (m08–m10)
3. **Modellvalg** (m11–m12)
4. **skills.md** (m13–m14)
5. **memory.md** (m15–m17)
6. **Prompt engineering** (m18) — NY seksjon
7. **Anvendt praksis** (m19–m20)
8. **Dybde** (m21–m24)
9. **Avslutning** (m25–m26): Kostnader (NY) → Avslutning

**Pedagogisk reorder er bevart:** konsept→gruppeoppgave-blokker (AGENTS, skills, memory) ligger fortsatt umiddelbart etter hverandre. Prompt engineering plassert etter hele memory.md-blokken — bygger på konseptene og leder inn i anvendt praksis.

**Endringer:**
- Tre nye mapper: `modules/{evolusjon,prompt_engineering,kostnader}/` med `__init__.py`, `app_logic.py` og placeholder-content-filer (5/7/6 stk respektivt).
- Tre nye wrappers: `pages_content/modules/m01_evolusjon.py`, `m18_prompt_engineering.py`, `m25_kostnader.py`.
- 23 eksisterende wrappers renamet med ny `m{NN}_<slug>`-prefiks (cascade via tmp-suffix).
- 23 eksisterende `modules/<slug>/app_logic.py`-filer: docstring header, `crumb()` og `st.caption("Modul N · ...")` oppdatert til nye nummer.
- `data/moduler.py`: `MODULER` utvidet 23→26, `SECTIONS` utvidet 8→9 (ny `prompt_engineering`-seksjon, `kostnader` lagt til Avslutning-seksjon).
- `modules/shared/ui.py`: ny `load_split_markdown(module_file, name, splitter="## ")`-helper som returnerer dict over `##`-seksjoner. Brukes av Prompt engineering for to-kolonners Før/Etter-eksempel.
- 2 `next_module_cta_for(...)`-kall oppdatert for å ikke hoppe over de nye modulene:
  - `gruppeoppgave_3_resultater` → `prompt_engineering` (var: `individuell_oppgave_2`)
  - `individuell_oppgave_5` → `kostnader` (var: `avslutning`)

**Kostnader-modulen har en placeholder-URL:** `KOSTNADS_DASHBOARD_URL` øverst i `modules/kostnader/app_logic.py` peker på `https://placeholder.intern.bank/cortex-code-kostnader`. Andre erstatter med faktisk URL til internt Streamlit-dashboard.

**URL-endringer:** bokmerker til alle 23 eksisterende moduler fungerer ikke lenger — `?page=mXX_<slug>` har nytt XX. Slugs uendret, så DB-tabeller uberørt.

**Innhold Andre må fylle ut:**
- `modules/evolusjon/content/{intro,era_1_googling,era_2_assistanse,era_3_spesifikasjon,hvor_er_du}.md`
- `modules/prompt_engineering/content/{intro,anatomi,sql_spesifikt,anti_patterns,iterativ,agents_vs_inline,eksempel_sammenligning}.md` (sistnevnte med `## Før` og `## Etter`)
- `modules/kostnader/content/{intro,kostnadsmodell,kostnadsdrivere,spore_forbruk,resource_monitors,best_practices}.md` + sett faktisk `KOSTNADS_DASHBOARD_URL`.

---

## 2026-05-25 — Modellvalg-seksjon mellom AGENTS.md og skills.md

Ny seksjon "Modellvalg" lagt inn mellom AGENTS.md-blokken og skills.md-blokken. Seksjonen inneholder to moduler: `tilgjengelige_modeller` (flyttet fra Avslutning) og en ny `individuell_oppgave_modellvalg`.

**Hvorfor:** modellvalg er sentralt for bank-analytikere (kostnad/kvalitet/regulatorisk avveining) og fortjente egen plass i konseptrekka, ikke som referanse-modul på slutten. Plassert etter AGENTS.md fordi modellvalg ofte styres _via_ AGENTS.md-konfigurasjonen.

**Endringer:**
- Ny mappe `modules/individuell_oppgave_modellvalg/` med `app_logic.py` + tre placeholder-content-filer (`oppgave`, `steg`, `forventet`). Andre fyller inn innhold.
- `tilgjengelige_modeller` flyttet fra m21 (Avslutning) til m10 (Modellvalg-seksjon).
- Ny `individuell_oppgave_modellvalg` ved m11.
- Moduler m10–m20 skjøvet ned 2 plasser til m12–m22. Avslutning flyttet fra m22 til m23.
- `data/moduler.py`: ny `Modellvalg`-seksjon i `SECTIONS`. `Avslutning`-seksjonen står nå alene med kun `m23_avslutning`.
- 13 wrapper-filer renamet, 12 `app_logic.py`-filer fikk captions/crumbs/docstrings oppdatert.
- 5 `next_module_cta_for`-kall justert:
  - `gruppeoppgave_1_resultater` → `tilgjengelige_modeller` (var: `skills_md`)
  - `tilgjengelige_modeller` → `individuell_oppgave_modellvalg` (var: `avslutning` — gammel pages/-format)
  - `individuell_oppgave_modellvalg` → `skills_md` (ny modul, ny CTA)
  - `autonomous_loop` → `individuell_oppgave_5` (var: `tilgjengelige_modeller` — brutt etter flyttingen)
  - `individuell_oppgave_5` → `avslutning` (var: `agents_md` — sløyfe-CTA tilbake til start, ikke ønskelig her)

**URL-endringer:** bokmerker til 13 flyttede moduler fungerer ikke lenger — `?page=mXX_<slug>` har nytt XX. Slugs uendret, så DB-tabeller uberørt.

---

## 2026-05-25 — Pedagogisk reorder: konsept → øvelse-blokker

`MODULER` flyttet om så hver konsept-modul får sin tilhørende gruppeoppgave umiddelbart etterpå. `SECTIONS` utvidet fra 5 til 7 seksjoner basert på pedagogiske blokker — ikke modul-type.

**Hvorfor:** Tidligere lå AGENTS.md (m07) men Gruppeoppgave 1 (m14), skills.md (m08) men Gruppeoppgave 2 (m12). Deltakeren måtte lære tre konsepter etter hverandre og «huske bakover» når øvelsene kom. Bryter prinsippet om at øvelse skal følge ferskt lært stoff.

**Ny modul-rekkefølge:**
1. **Introduksjon** (01–06): Cortex Code → CLI → Snowsight → Arkitektur → Demo → Individuell 1
2. **AGENTS.md** (07–09): AGENTS.md → Gruppeoppgave 1 → Resultater 1
3. **skills.md** (10–11): skills.md → Gruppeoppgave 2
4. **memory.md** (12–14): memory.md → Gruppeoppgave 3 → Resultater 3
5. **Anvendt praksis** (15–16): Individuell 2 → Individuell 3
6. **Dybde** (17–20): Demo 2 → Individuell 4 → Autonomous loop → Individuell 5
7. **Avslutning** (21–22): Tilgjengelige modeller → Avslutning

**Hva som flyttet:**
- Gruppeoppgave 1 + Resultater: m14, m15 → m08, m09
- skills.md: m08 → m10
- Gruppeoppgave 2: m12 → m11
- memory.md: m09 → m12
- Gruppeoppgave 3 + Resultater: m10, m11 → m13, m14
- Individuell oppgave 2: m13 → m15

Alle andre moduler beholdt nummer. Slugs uendret — DB-tabeller (`kurs.<slug>_responses`) uberørt.

**Endringer:**
- `data/moduler.py`: `MODULER` rerangert. `SECTIONS` skrevet om til 7 pedagogiske blokker.
- `pages_content/modules/`: 8 wrapper-filer renamet (`m{NN}_<slug>.py`-prefiks oppdatert).
- 8 `modules/<slug>/app_logic.py`-filer: `crumb()` + `st.caption("Modul N · ...")` oppdatert til nye nummer.
- 3 `next_module_cta_for(...)`-kall oppdatert for ny pedagogisk sekvens:
  - `skills_md` → `gruppeoppgave_2` (var: `gruppeoppgave_1`)
  - `gruppeoppgave_1_resultater` → `skills_md` (var: `demo_2`)
  - `gruppeoppgave_3_resultater` → `individuell_oppgave_2` (var: `gruppeoppgave_2`)

**URL-endringer:** bokmerker til de 8 flyttede modulene fungerer ikke lenger (`?page=mXX_<slug>` har nytt XX). Sluggen er uendret, så lenker som bare bruker slug-formen ville fungert — men hele appen bruker `m{nr:02d}_<slug>`-formen.

**Åpne avveininger flagget til Andre:**
- Gruppeoppgave 2 (skills.md-blokken) mangler resultatside. Hvis det skal være konsistent med de to andre blokkene, må ny `gruppeoppgave_2_resultater`-modul opprettes (separat oppgave).
- «Anvendt praksis»-seksjonen (m15–m16) er to placeholder-oppgaver uten innhold ennå. Kan ende opp i en av konsept-blokkene når innholdet kommer.

---

## 2026-05-25 — Individuell oppgave 1 flyttet inn i Innføring

Bytter plass på `m06_agents_md` ↔ `m07_individuell_oppgave_1`. Individuell oppgave 1 hører nå hjemme i Innføring-seksjonen (etter Første demo), ikke i Konfigurasjon.

**Hvorfor:** pedagogisk flyt — etter live-demoen (modul 5) er det naturlig at deltakerne får prøve selv før de går videre til de konseptuelle konfigurasjons-modulene. Plassering i Innføring matcher også tematisk: hands-on intro til verktøyet, ikke "konfigurasjon".

**Endringer:**
- `data/moduler.py`: `individuell_oppgave_1` til nr=6 (kategori P), `agents_md` til nr=7. `SECTIONS.innforing` får nytt medlem `m06_individuell_oppgave_1`; `SECTIONS.konfigurasjon` mister det og starter nå med `m07_agents_md`.
- Wrapper-filer renamet: `m06_agents_md.py` → `m07_agents_md.py`, `m07_individuell_oppgave_1.py` → `m06_individuell_oppgave_1.py`.
- Captions/crumbs oppdatert i begge `app_logic.py`-filene.
- `next_module_cta_for` i individuell_oppgave_1 endret fra `individuell_oppgave_2` (langt unna i Gruppearbeid) til `agents_md` (neste i sekvens).

---

## 2026-05-25 — Sidebar: seksjonsgruppering med "Du er her"-badge

Kursmodulene grupperes nå visuelt i fem seksjoner i sidemenyen (Innføring, Konfigurasjon, Gruppearbeid, Dybde, Avslutning). Den aktive seksjonen får 3px Vann-stripe til venstre og en kompakt "Du er her"-badge ved siden av seksjonsetiketten. De andre seksjonene har tynn dempet stripe.

**Hvorfor:** med 22 moduler i én flat liste mistet brukeren raskt oversikt over hvor i kursforløpet de var. Seksjoner gir temporal gruppering uten å bryte den sekvensielle 01–22-nummereringen eller endre kategori-prikkenes betydning (modul-*type*, ikke seksjon).

**Endringer:**
- `data/moduler.py`: ny `SECTIONS`-konstant + `section_for_page()`-helper. Seksjoner refererer `page_id`-strenger (ikke nr), så stabil over om-nummerering.
- `components/sidebar.py`: `render_sidebar` itererer nå over `SECTIONS` i stedet for flat modul-løkke. Hver seksjon rendres som én HTML-blob (kan ikke splittes — Streamlit lukker åpne div mellom markdown-kall). Aktiv modul-styling endret fra venstrekant til mykt bakgrunnsfyll så seksjons-stripen får være "den med kantlinjen".
- Forside, "Bli kjent" og "Resultater" uberørt — seksjonsgruppering gjelder kun under "Kursmoduler".

PRD uendret. Inndelingen avtalt med Andre (m04 Arkitekturoversikt i Innføring, m21 Tilgjengelige modeller i Avslutning som referanse-modul selv om kategori-kode er K).

---

## 2026-05-25 — Arkitekturoversikt (modul 4)

Ny konsept-modul som forklarer Cortex Codes interne arkitektur som én tool-augmented LLM-agent. Plassert rett før Første demo (modul 5) i Innføring-kategorien.

**Hvorfor:** Bank-analytikere får mer ut av demoen hvis de først forstår at "agenten" er én LLM med fem integrerte lag — ikke et flermodulsystem med separat planner/executor/validator. Demystifiserer hva som faktisk skjer under panseret før de ser den i bruk.

**Endringer:**
- Ny mappe `modules/arkitektur/` med `app_logic.py` + syv content-filer (`intro`, `system_prompt`, `tool_interface`, `skills_system`, `oppgavestyring`, `kontekstbevissthet`, `forbehold`).
- Layout: intro-tekst + fem `st.expander`-blokker hvor brukeren klikker for å se detaljer. Hver ekspander dekker ett lag (System Prompt, Tool Interface, Skills-system, Oppgavestyring, Kontekstbevissthet) — innhold beskriver hva det er, hvordan det fungerer, og konkrete eksempler fra Cortex Code.
- Ny wrapper `pages_content/modules/m04_arkitektur.py`.
- Moduler 4–21 skjøvet ned til 5–22 i `data/moduler.py`. 18 wrapper-filer renamet tilsvarende.
- Captions/crumbs oppdatert i 18 `modules/<slug>/app_logic.py`-filer.
- `DESIGN_GUIDE.md` §11: "21 moduler" → "22 moduler".
- PRD changelog: v0.27.

**Innhold:** Drafted basert på det agenten selv kan observere av sin egen arkitektur (system-prompt, tilgjengelige verktøy, skills-mekanisme, TODO-listing, kontekst-verktøy). Forbehold-callout gjør det tydelig at det _ikke_ dekker Snowflakes backend-orkestrering rundt agenten.

---

## 2026-05-24 (sent) — memory.md (modul 8) + Gruppeoppgave 3 (9–10)

Tre nye moduler om Cortex Codes persistent-memory-mekanisme, plassert rett etter skills.md (modul 7). Speiler etablerte mønstre: konsept-modul (som agents_md/skills_md) + interaktiv gruppeoppgave med par-diskusjon (som gruppeoppgave_1) + offentlig resultater-side (som gruppeoppgave_1_resultater).

**Hvorfor:** Cortex Code har et opt-in Memory-tool (`CORTEX_ENABLE_MEMORY=1`) som persisterer på tvers av sesjoner i `~/.snowflake/cortex/memory/`. Det er et viktig kompetanse-gap for bank-analytikere: memory er bruker-scope (ikke prosjekt-scope som AGENTS.md), og GDPR-/compliance-vinklingen rundt hva som bør lagres lokalt fortjener egen modul.

**Endringer:**
- Ny mappe `modules/memory_md/` (konsept, kategori K) med `app_logic.py` + åtte content-filer (`what_is_it`, `how_it_works`, `where_to_place`, `vs_agents_md`, `why_not_skill`, `what_to_store`, `example`, `transition`). Innhold er drafted basert på research mot Snowflake-docs; Andre redigerer.
- Ny mappe `modules/gruppeoppgave_3/` (interaktiv, kategori G) med `app_logic.py`, `admin_logic.py`, `db.py`, `config.py`, `views.py`, `reducer.py`, `supabase_schema.sql`, `content/intro.md`. Fire spørsmål: Q1/Q2/Q4 fritekst, Q3 valg (bank-risiko). Ny tabell `kurs.gruppeoppgave_3_responses` (per DM-5.2).
- Ny mappe `modules/gruppeoppgave_3_resultater/` (read-only, kategori G) med `app_logic.py` som gjenbruker `render_results` fra `gruppeoppgave_3.views`.
- Wrappers: `m08_memory_md.py`, `m09_gruppeoppgave_3.py`, `m10_gruppeoppgave_3_resultater.py`.
- Moduler 8–18 skjøvet ned til 11–21 i `data/moduler.py`. Wrapper-filer i `pages_content/modules/` renamet tilsvarende.
- Captions/crumbs oppdatert i 11 `modules/<slug>/app_logic.py`-filer.
- `DESIGN_GUIDE.md` §11: "18 moduler" → "21 moduler".
- PRD changelog: v0.26.

**Manuelt steg:** Kjør `modules/gruppeoppgave_3/supabase_schema.sql` i Supabase SQL Editor for å opprette tabellen.

**`viz`-gjenbruk:** `gruppeoppgave_3/views.py` importerer `render_wordcloud`/`render_barchart` direkte fra `modules.gruppeoppgave_1.viz` — ingen duplisering av Plotly-/wordcloud-koden. Hvis Gruppeoppgave 1 senere flytter eller forandrer signatur, må Gruppeoppgave 3 oppdateres.

---

## 2026-05-24 — Gruppeoppgave 2 lagt til som modul 8

Ny modul innsatt rett etter skills.md (modul 7) — praktisk oppfølger der gruppene selv skriver en `SKILL.md`-fil. Skill-temaet er datakvalitets-sjekk: input er en tabell, output en rapport om duplikater, NULL-rater, kardinalitet og outliers. Universell, testbar, og direkte anvendelig på bank-tabeller.

**Hvorfor:** PRD §FR-3.11. Etter skills.md (konseptuell) er det pedagogisk naturlig å la deltakerne lage sin egen skill umiddelbart. Alle gruppene jobber med samme spec slik at plenums-runden blir lettere å gjennomføre.

**Endringer:**
- Ny mappe `modules/gruppeoppgave_2/` med `app_logic.py` + tre placeholder-content-filer (`oppgave.md`, `steg.md`, `forventet.md`). Layout speiler `individuell_oppgave_2`-mønsteret (callout + to subheaders).
- `pages_content/modules/m08_gruppeoppgave_2.py` — wrapper.
- Moduler 8–17 skjøvet ned til 9–18 i `data/moduler.py`. Wrapper-filer i `pages_content/modules/` renamet tilsvarende (`m08_individuell_oppgave_2` → `m09_individuell_oppgave_2`, …, `m17_avslutning` → `m18_avslutning`).
- `crumb()`- og `st.caption()`-tekster i 10 `modules/<slug>/app_logic.py`-filer + `gruppeoppgave_1_resultater/app_logic.py` oppdatert til nye modul-numre.
- `DESIGN_GUIDE.md` §11: "17 moduler" → "18 moduler".
- PRD changelog: v0.25.

**Ren presentasjon — ingen datainnsamling.** Refleksjon skjer muntlig i plenum, ingen Supabase-tabell, ingen resultatside.

---

## 2026-05-24 — Bli kjent: segmentert Likert-kontroll

Ren UX-redesign av Modul 0 (`modules/oppvarming/app_logic.py`). Backend, datalagring og state-håndtering uendret.

**Hvorfor:** dagens layout ga spørsmålene for lite plass (uunødvendig wrap), Likert-knappene fløt løst uten visuell sammenheng, og skalaretningen var kun synlig i toppbanneret.

**Endringer:**
- Kolonneforhold flippet fra `[3, 5]` til `[3, 2]` — spørsmålsteksten får mest plass.
- Spørsmålsnummer som mono-badge (`Q1`, `Q2`, …) i stedet for `1.`-prefix.
- `st.radio(horizontal=True)` restylet via scoped CSS (`stylable_container`) som én sammenhengende segmentert bar: 36×30px segmenter, Vann-fyll på valgt segment, hvit tekst.
- Endepunkt-labels (`uenig` / `enig`) duplisert på hver rad — ikke kun i toppbanneret.
- Skala-hint krympet fra fullt `callout()` til kompakt inline pille med Frost venstrekant.
- `st.divider()` mellom rader erstattet av subtil 1px border-bottom; padding strammet til `14px 16px`.
- Besvarte rader får svak Vann-tint via CSS `:has(input:checked)` (ingen rerun).

PRD uendret — FR-3.14 spesifiserer ikke UI-detaljer for radio-layout.

---

## 2026-05-23 (sent) — Kategori-prikker i sidemenyen

Stor refactoring av navigasjon: `st.navigation()` erstattet med custom sidebar som viser kategori-prikker per modul (DESIGN_GUIDE §11).

**Hvorfor:** Med 17 moduler hvor individuelle oppgaver er flettet inn mellom konseptmoduler, gir tematisk gruppering motstrid med sekvensiell nummerering. Løsning: én sekvensiell liste 01–17 + farget prikk per modul.

**Fem kategorier:**
- **I** Innføring (Frost `#7EB5D2`) — Cortex Code, Snowsight vs CLI, Cortex i Snowsight, Første demo
- **K** Konfigurasjon (Lavendel `#B197FC`) — AGENTS.md, skills.md, Tilgjengelige modeller
- **P** Praksis (Mynt `#66D9A8`) — Individuelle oppgaver 1–5
- **G** Gruppe (Korall `#FFAD80`) — Gruppeoppgave 1, Resultater
- **F** Fordypning (Sky `#94A3B8`) — Demo 2, Autonomous loop, Avslutning

**Nye filer:**
- `app.py` — entry. Leser `?page=...` fra URL og dispatcher.
- `data/moduler.py` — KANONISK modul-liste (17 moduler) + kategori-mapping.
- `components/sidebar.py` — custom sidebar med prikker + scoped CSS.
- `pages_content/` — 17 modul-wrappers (`mNN_<slug>.py`) + `forside.py`, `bli_kjent.py`, `resultater.py`, `admin.py`. Hver fil er en pass-through til eksisterende `modules.<slug>.app_logic.main`.

**Slettet:**
- `hub.py`, `home.py`, `pages/*.py` (19 filer). Erstattet av app.py + pages_content/.

**URL-endringer:**
- Tidligere `/cortex_code` → nå `?page=m01_cortex_code`
- Tidligere `/agents_md` → nå `?page=m05_agents_md` (modul-nummer endret fra 10 → 5 i ny spec-rekkefølge)
- Bokmerker fra tidligere kjøringer fungerer ikke lenger.

**Modul-rekkefølge endret** til spec-orden (interleaved):
1. Cortex Code, 2. Snowsight vs CLI, 3. Cortex i Snowsight, 4. Første demo,
5. AGENTS.md (K), 6. Individuell 1 (P), 7. skills.md (K), 8. Individuell 2 (P),
9. Gruppeoppgave 1 (G), 10. Resultater (G), 11. Individuell 3 (P), 12. Demo 2 (F),
13. Individuell 4 (P), 14. Autonomous loop (F), 15. Individuell 5 (P),
16. Tilgjengelige modeller (K), 17. Avslutning (F)

**Endre i fremtiden:** kun `data/moduler.py`. Sidebaren og forsiden følger automatisk.

**Kjør:** `streamlit run app.py` (ikke `hub.py` lenger).

---

## 2026-05-23 — Bli kjent: 5 → 10 Likert-påstander

Oppvarmings-modulen ("Bli kjent") utvidet med fem nye Cortex Code-spesifikke påstander (ID 6–10). Totalt 10 påstander i Likert-griden, fortsatt én form med én submit.

Q1–5 (uendret): generell teknisk bakgrunn — Snowflake-bruk, AI-verktøy, CLI-komfort, kodebakgrunn, holdning til AI-agenter.

Q6–10 (nye): Cortex Code-modenhet:
- 6: Jeg bruker Cortex Code regelmessig
- 7: Jeg kjenner anbefalt praksis for bruk av Cortex Code
- 8: Jeg forstår sentrale begreper som agent, modell og prompt
- 9: Jeg forstår hva som driver kostnader ved bruk av Cortex Code
- 10: Jeg vet hvordan jeg optimaliserer bruken av Cortex Code

Pedagogisk: kursleder kan se "generell teknisk modenhet" (Q1–5) mot "Cortex Code-modenhet" (Q6–10) side ved side på resultatsiden.

Endringer:
- `modules/oppvarming/config.py` — `STATEMENTS` utvidet til 10 oppføringer
- `modules/oppvarming/supabase_schema.sql` — CHECK-constraint `question_id between 1 and 10`
- `PRD.md` §FR-3.14 oppdatert til 10 påstander, changelog v0.24

**Manuelt steg:** kjør oppdatert `supabase_schema.sql` i Supabase SQL Editor. Det dropper og gjenoppretter `kurs.oppvarming_responses`-tabellen (eksisterende data slettes — var test).

Ingen kode-endringer nødvendige i `app_logic.py`, `views.py`, `db.py` — alle itererer over `STATEMENTS` og håndterer variabel størrelse automatisk.

---

## 2026-05-23 — Modul 16: Tilgjengelige modeller

Ny modul lagt til som UTKAST (FR-3.11, FR-3.12) — Andre skriver innholdet selv.

- Ny mappe: `modules/tilgjengelige_modeller/` med `__init__.py`, `app_logic.py` og 4 tomme placeholder-content (intro, oversikt, valg, eksempel)
- Ny wrapper: `pages/tilgjengelige_modeller.py` (URL: `/tilgjengelige_modeller`)
- `hub.py`: ny `st.Page` mellom Autonomous loop og Avslutning
- `home.py`: ny `MODULES`-entry med eksplisitt placeholder-beskrivelse
- Modul-rekkefølge: Avslutning flyttet fra 16 → 17 (tittel, caption, crumb, page_title oppdatert)
- `modules/autonomous_loop/app_logic.py`: CTA-kort peker nå til Tilgjengelige modeller (var Avslutning)

URL-er uendret for alle eksisterende moduler.

---

## 2026-05-23 — DESIGN_GUIDE v2: hierarki og container-system

Stor revisjon: skifter fra brand-disiplin (v1) til produkt-design (v2).
Bakgrunn er ikke lenger Fjell heldekkende, men nær-svart canvas med
elevation-trinn. Brand-farger reserveres for aksenter og containere.

### Tema og farger
- `.streamlit/config.toml`: `backgroundColor #002776 → #0A0F1F`, `secondaryBackgroundColor #0A3494 → #0F1729`, `textColor #F8E9DD → #F4F6FB`, `codeBackgroundColor #001A52 → #131C33`
- Font: `Arial → Inter, Arial, sans-serif` (Inter primær, Arial fallback). `[[theme.fontFaces]]` blokk for å laste Inter fra Google Fonts.
- Sidebar-tekst: Syrin → Text-secondary `#A8B3C7`.
- Border: solid Frost → semi-transparent `rgba(126, 181, 210, 0.10)`.

### Shared UI (`modules/shared/ui.py`)
- Eksporterer fargekonstanter (`COLOR_*`, `TEXT_*`, `BORDER*`) som single source of truth.
- `callout()` — nye kvadratiske ikoner (i / ! / ✓ / ·) i stedet for emojis. Bakgrunn-opacity senket fra 0.20 → 0.12 (info), 0.15 → 0.12 (warning). Bakoverkompatibel: `kind="highlight"` mappes til `"success"`, `kind="warning"` til `"warn"`.
- `metric_card(label, value, sub)` — NY: KPI-kort med uppercase-label, 32px tabular verdi, Frost-farget sub-tekst.
- `metric_row(metrics)` — NY: rad med flere metric-kort i `st.columns`.
- `card(key, padding)` — NY: context manager som pakker innhold i kort med surface-1, border, radius.
- `crumb(parts)` — NY: breadcrumb øverst på modul-side.
- `next_module_cta(title, description, page)` — NY: erstatter "---" + tekstlinje med interaktivt CTA-kort.

### Diagrammer (`modules/gruppeoppgave_1/viz.py`)
- `render_barchart` migrert fra `plotly.express` til `plotly.graph_objects` for full akse-kontroll.
- Y-akse: `dtick=1`, kun heltallsticks. Tidligere 0.2/0.4/0.6/0.8-ticks når N=2 var visuell støy.
- Tomme kategorier: text-labels skjules ("0" rendres som tom streng), så hierarkiet 1–5 er klart men ikke dominerende.
- Snitt-linje: nytt `mean` argument tegner stiplet vertikal Syrin-linje med annotasjon.
- Likert-mode: nytt `likert=True` argument legger "uenig"/"nøytral"/"enig"-undertekster på tick 1/3/5.
- Diagrammer wraps automatisk i `card()` — ingen flytende grafer på canvas lenger.

### Sidebar (`hub.py`)
- Modul-titler: to-sifret mono-prefix (`01 · Cortex Code` i stedet for `1. Cortex Code` + emoji-ikon).
- Sidebar-ikoner fjernet fra `st.Page(...)`-kall (emojis renders inkonsistent på tvers av OS).
- Seksjons-headers: `"👋 Oppvarming"`, `"📚 Kursmoduler"`, `"🔒 Administrasjon"` → `"Oversikt"`, `"Kursmoduler"`, `"Administrasjon"`.

### Resultater Oppvarming
- `oppvarming/views.py`: viktige tall (totalt antall svar, snitt-score, antall spørsmål) løftet til metric-kort på toppen.
- Diagrammer bruker nå snitt-linje og Likert-ankere på x-aksen.
- `oppvarming_resultater/app_logic.py`: crumb øverst, ny H1 "Resultater fra Oppvarming", refresh-kontroller i kompakt høyre-kolonne.

### Hva er IKKE endret
- 16 modulsider rører innholdet ikke (Andre eier innholdet — se CLAUDE.md).
- Eksisterende `callout()`-kall i moduler fungerer som før via alias-mapping.
- `gruppeoppgave_1/views.py` og `admin_logic.py` urørt — bruker fortsatt `render_barchart`/`render_wordcloud` med kompatibel API.

---

## 2026-05-23

### Design system etablert
- [DESIGN_GUIDE.md](DESIGN_GUIDE.md) opprettet som autoritativ kilde for visuell stil
- Palett: Vann/Fjell/Sand/Frost/Syrin (se DESIGN_GUIDE §2)
- Font: Arial gjennomgående
- `.streamlit/config.toml` justert til kanonisk versjon fra guide
- Emojis restaurert i H1/H2-overskrifter og callout-titler per guide §5
- Sidebar-ikoner i `hub.py` restaurert
- Tidligere "ingen ikoner"-regel overstyrt — emojis er nå en del av designet (kun i headers og callout-prefikser, ikke som tekst-dekorasjon)
- `callout()`-helper i `modules/shared/ui.py` matcher guide §5.2–5.4
- CLAUDE.md oppdatert: peker til DESIGN_GUIDE.md som single source of truth for stil

### Modul-tillegg (separat fra design)
- Modul 1 (Cortex Code) har lydklipp `Snowflake RBAC.mp3` via `st.audio`
- Modul 6 (skills.md) — separat oppføring (utenfor scope for denne endringen)

### Full migrasjon til callout() (siste runde)
Alle gjenværende `st.info`/`st.warning`/`st.success`/`st.error` erstattet med `callout()` per DESIGN_GUIDE §6.

Mapping:
- `st.info` → `callout(kind="info")` (Vann)
- `st.success` → `callout(kind="highlight")` (Frost)
- `st.warning` → `callout(kind="warning")` (Syrin)
- `st.error` → `callout(kind="warning")` (Syrin — guide §8 forbyr rødt)
- Empty-state ("Venter på flere svar…") → `callout(kind="subtle")` (Sand-dempet)

Migrerte filer: cortex_code, skills_md, alle individuell_oppgave_{1–5}, cortex_interaction, oppvarming, demo_1, demo_2, gruppeoppgave_1 (app_logic + admin_logic + views + viz).

Form-toast (`st.toast`) er ikke migrert — guide nevner ikke toasts, og de er per natur transiente.

### Modul-rekkefølge: hands-on før konsept

Individuelle oppgaver 1–5 flyttet til posisjon 5–9 i Kursmoduler-seksjonen, rett etter Første demo. Konseptuelle og workshop-moduler skyves ned tilsvarende.

Ny rekkefølge:

| Posisjon | Modul |
|---|---|
| 1 | Cortex Code |
| 2 | Snowsight vs CLI |
| 3 | Cortex Code i Snowsight |
| 4 | Første demo |
| 5–9 | Individuelle oppgaver 1–5 |
| 10 | AGENTS.md |
| 11 | skills.md |
| 12 | Gruppeoppgave 1 |
| 13 | Resultater Gruppeoppgave 1 |
| 14 | Demo 2 |
| 15 | Autonomous loop i dybden |
| 16 | Avslutning |

Endringer:
- `hub.py` — st.Page-blokker omordnet, title-prefikser renummerert
- `home.py` — `MODULES`-lista omordnet og `number`-feltene oppdatert
- Alle berørte `app_logic.py` — `st.caption("Modul N · …")` oppdatert + docstring-modul-numre
- Alle berørte `pages/*.py` wrappers — `page_title` oppdatert
- `PRD.md` §FR-3.10 sidemeny-eksempel oppdatert, changelog v0.22

URL-er er uendret (slugs er beholdt).
