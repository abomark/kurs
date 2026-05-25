# PRD – Kurs

**Status:** Aktiv
**Eier:** Andre
**Single source of truth.** All kode skal være konsistent med denne fila. Se [CLAUDE.md](CLAUDE.md) for hvordan kode og PRD holdes synkronisert.

Stabile seksjons-ID-er (f.eks. `FR-3.2`, `NFR-4.1`) er ment å brukes i kodekommentarer der koplingen ikke er åpenbar. Ikke endre ID-er — legg til nye.

---

## 1. Bakgrunn og mål

Interaktive kursmoduler for opplæring i AI-verktøy (AGENTS.md, prompt caching, tool use osv.). Hver modul har en deltakerflate hvor kursdeltakere kan svare på spørsmål live, og en presentatørflate hvor svarene visualiseres for hele rommet.

**Mål:**
- Aktivisere deltakere i stedet for passiv slide-konsumering.
- Gi presentatøren stemningsmåler i sanntid.
- Bygge en plattform som tåler 3–10 moduler over tid.

**Ikke-mål:** Læringsplattform (LMS), poengsystem, sertifisering, asynkron deltakelse.

---

## 2. Brukere

### 2.1 Deltaker
Kursdeltaker som svarer fra mobil eller laptop i kursrommet. Helt anonym. Forventes å bruke <5 min per modul.

### 2.2 Presentatør
Kursleder (eier). Har eget passord. Ser live-resultater, kan moderere, eksportere og nullstille.

---

## 3. Funksjonelle krav (FR)

### FR-3.1 Spørsmål per modul
Hver modul har et fast sett spørsmål, definert i `modules/<navn>/config.py` som `QUESTIONS`-dict.

Hvert spørsmål har:
- `type`: enten `"text"` (fritekst) eller `"choice"` (radioknapp).
- `text`: spørsmålsteksten på norsk.
- For `choice`: `options`-liste med 2–4 alternativer.
- For `text`: valgfri `placeholder`.

**Gruppeoppgave 1 har akkurat fire spørsmål** (Q1, Q2 fritekst; Q3, Q4 valg med tre alternativer hver).

### FR-3.2 Innsending
- Deltakere kan sende inn flere svar på samme spørsmål i samme sesjon (ingen klient-side rate limit utover at form tømmes etter submit).
- Etter innsending: toast-bekreftelse ("Takk! Svar lagret på spørsmål N") + tom form klar for nytt svar.
- En per-spørsmål-teller i `st.session_state` vises som caption.

### FR-3.3 Lagring
- Alle svar lagres i Supabase-tabellen `kurs.responses`.
- Anonymt: kun `question_id`, `answer_text` eller `answer_choice`, og `created_at`.
- Ingen IP, session-ID, brukernavn eller cookie utover Streamlits default.

### FR-3.4 Visualisering (presentatør-side)
- **Fritekst-spørsmål (Q1, Q2):** ordsky med kun de **10 hyppigste ordene**. Render i 1600×900 (16:9, slide-klar). Under ordskyen: tekst-liste over topp 10 med frekvens.
- **Valg-spørsmål (Q3, Q4):** barchart (`st.bar_chart`) som viser absolutt antall per alternativ.
- **Skjul resultater** til minst `MIN_RESPONSES_BEFORE_REVEAL = 3` svar er kommet inn for det aktuelle spørsmålet (privacy-by-timing).

### FR-3.5 Ordreduksjon (MVP)
Fritekst reduseres til tokens via `reducer.py`:
1. Lowercase + strip.
2. Filtrer bort `NON_ANSWERS` (vet ikke, n/a, etc.) og tomt.
3. Fjern tegnsetting (behold `æøåÆØÅ`).
4. Splitt på whitespace, komma, semikolon, skråstrek.
5. Filtrer bort stopwords (`STOPWORDS` – norsk + engelsk) og tokens kortere enn 3 tegn.
6. Returner liste med duplikater (frekvens styrer størrelse i ordskyen).

**Senere:** byttes til AI-versjon med samme signatur (`reduce_answers(list[str]) -> list[str]`). Se `claude_answers.py`-prompten i kursnotatene.

### FR-3.6 "Hva glemte vi?"-diff
Egen tab på presentatør-siden. Viser ordsky over tokens som finnes i `CLAUDE_ANSWERS_QN` men ikke i deltakersvar (set difference, duplikater fra Claude beholdes). Brukes som diskusjonsfôr, ikke fasit.

### FR-3.7 Admin-funksjoner
Presentatør-siden har fem tabs:
1. **Resultater** – live ordskyer + barcharts, auto-refresh 10 sek.
2. **Hva glemte vi?** – diff-ordskyer.
3. **Moderering** – liste over alle svar med sletteknapp per rad.
4. **Eksport** – last ned alle svar som CSV.
5. **Nullstill** – slett alle svar (krever å skrive "SLETT" i bekreftelsesfelt).

Tilgang: passord lagret i `st.secrets["ADMIN_PASSWORD"]`, sjekket med `hmac.compare_digest`.

### FR-3.8 Multimodul-arkitektur
- Hver modul lever under `modules/<navn>/` som en Python-pakke.
- Felles entry: `streamlit run hub.py` på repo-rot.
- URL-mønster: `/<modulnavn>` for deltaker, `/admin_<modulnavn>` for presentatør.
- Hub-siden ([`hub.py`](hub.py)) lister alle moduler fra `MODULES`-konstanten med kort, status og lenker.
- Felles deploy, felles Supabase-prosjekt, ett schema per modul.

### FR-3.9 Soft-gate for deltakere (valgfri)
Hvis `st.secrets["PARTICIPANT_CODE"]` er satt og ikke tom: deltakere må skrive inn koden før de ser spørsmålene. Presentatør oppgir koden muntlig i kursrommet. Skrus av ved tom verdi.

### FR-3.10 Sidemeny-struktur
Sidemenyen styres via `st.navigation` i [`hub.py`](hub.py) med fire seksjoner i fast rekkefølge:

1. **Forside** (uten seksjons-header)
2. **Oppvarming** — pre-kurs (Bli kjent + Resultater). Ingen tallprefix.
3. **Kursmoduler** — nummerert linært. Aktuelle rekkefølge: `01. Cortex Code`, `02. Snowsight vs CLI`, `03. Cortex Code i Snowsight`, `04. Arkitekturoversikt`, `05. Første demo`, `06. AGENTS.md`, `07. Individuell oppgave 1`, `08. skills.md`, `09. memory.md`, `10. Gruppeoppgave 3`, `11. Resultater Gruppeoppgave 3`, `12. Gruppeoppgave 2`, `13. Individuell oppgave 2`, `14. Gruppeoppgave 1`, `15. Resultater Gruppeoppgave 1`, `16. Individuell oppgave 3`, `17. Demo 2`, `18. Individuell oppgave 4`, `19. Autonomous loop i dybden`, `20. Individuell oppgave 5`, `21. Tilgjengelige modeller`, `22. Avslutning`. Rekkefølge i `data/moduler.py` (`MODULER`-listen) styrer visningsrekkefølge.
4. **Administrasjon** — sist, slik at admin-sidene havner nederst i sidemenyen.

Hver kursmodul kan ha både en deltakerside (i seksjon 3) og en tilsvarende admin-side (i seksjon 4), men admin er ikke obligatorisk (jf. FR-3.11).

**Begrensning:** Streamlit støtter to visuelle nivåer (seksjons-header + sider). Tre-strukturert hierarki med 3+ nivåer eller sammenklappbare grupper krever custom sidebar/CSS og er ikke i scope.

### FR-3.11 Presentasjons-moduler (uten database)
Noen moduler er **ren les/forstå** — presentatøren bruker dem som "slides med interaktivitet". Disse:

- Trenger ikke Supabase, eget schema eller `db.py`.
- Har kun en `app_logic.py` med `main()` i `modules/<navn>/`, og en wrapper i `pages/<navn>.py`.
- Krever ikke admin-side (`pages/admin_<navn>.py` ikke nødvendig).
- Pedagogisk grep typisk: `st.expander` per begrep + `st.toggle("Vis alle")` for slide-/live-modus.

**Eksempel:** Cortex Code-modulen (modul 1) — dekoder marketing-tekst til klartekst.

### FR-3.12 Innhold i markdown-filer (separat fra Python)
Modul-innhold (prosa, snakkepunkter, beskrivelser, demo-steg, eksempler) lagres i `.md`-filer under `modules/<navn>/content/`. Python-fila (`app_logic.py`) styrer KUN layout (når kommer en `st.expander`, hvilke kolonner, hvilken `st.toggle`) — den skal ikke inneholde prosa-strenger.

**Loader-helpers** i [`modules/shared/ui.py`](modules/shared/ui.py):

- `load_markdown(__file__, name)` → returnerer rå markdown fra `content/<name>.md`. Bruk for blokker som rendres med `st.markdown`, `st.info`, `st.success` osv. Returnerer en synlig placeholder-melding hvis fila mangler.
- `load_titled_markdown(__file__, name)` → returnerer `(title, body)` der `title` leses fra første `# `-linje. Bruk for expandere/kort der tittel må passes som separat argument til Streamlit.

**Hvorfor:**
- [[feedback-module-content]] — Andre eier innholdet, ikke Claude. Markdown er prosa-vennlig (preview, syntax-highlight, ingen escape-helvete).
- Klar arbeidsdeling: Python ↔ Claude (layout), markdown ↔ Andre (innhold).
- Diff-bart og versjonerbart per innholdsendring uten å røre Python.

**Unntak:** Interaktive datadrevne moduler (f.eks. Gruppeoppgave 1 med `QUESTIONS`-config) trenger ikke følge dette mønsteret når innholdet primært er strukturert data, ikke prosa.

### FR-3.14 Oppvarming (Bli kjent)
Egen seksjon i sidemenyen (" Oppvarming") som kjøres **før** modul 1, for å la kursleder kalibrere undervisningen etter deltakergruppen.

**Innhold:**
- "Bli kjent" — ti **påstander** vurdert på 1–5 Likert-skala (1 = uenig, 5 = enig). Alle besvares samtidig i én form med én submit-knapp. Hver innsending lagrer 10 rader (én per påstand). Påstandene defineres i `modules/oppvarming/config.py` som `STATEMENTS`-dict. **Q1–5** dekker generell teknisk bakgrunn (Snowflake-erfaring, AI-verktøy, CLI-komfort, kodebakgrunn, holdning til AI-agenter). **Q6–10** dekker Cortex Code-modenhet spesifikt (bruksfrekvens, beste praksis, terminologi, kostnadsmodell, optimalisering).
- "Resultater" — offentlig read-only side med 10 barcharts (én per påstand, x-akse 1–5) + beregnet snittsvar. Samme prinsipp som FR-3.13.

**Tabell:** `kurs.oppvarming_responses` (jf. DM-5.2 — felles schema, prefix per modul). Kolonner: `id`, `question_id` (1–10), `answer_value` (smallint 1–5), `created_at`. SQL-definisjonen ligger i [`modules/oppvarming/supabase_schema.sql`](modules/oppvarming/supabase_schema.sql) og må kjøres MANUELT i Supabase SQL Editor. Siden `kurs` allerede er i Exposed schemas, trengs ingen dashboard-endring.

**Pedagogisk grep:** undertittel "Modul 0" brukes muntlig, men sidemenyen viser bare "Bli kjent" / "Resultater" uten tallprefix — seksjonsheaderen (" Oppvarming") signaliserer kontekst.

**Avvik fra NFR-4.1 reveal-terskel:** Oppvarming setter `MIN_RESPONSES_BEFORE_REVEAL = 1` (default er 3). Begrunnelse: Likert-tall (1–5) er mindre identifiserende enn fritekstsvar, og kursleder ønsker å se trender umiddelbart fra første deltaker. Implementert via `min_responses`-argument til `render_barchart`.

### FR-3.13 Offentlig resultatvisning
For interaktive moduler kan det finnes en **offentlig, read-only resultatside** som viser aggregerte grafer uten passord-gate. Eksempel: Resultater Gruppeoppgave 1 (modul 8).

**Hva som vises:** kun hovedresultatene (ordskyer for fritekst-spørsmål, barcharts for valg-spørsmål) — samme som "Resultater"-tab på admin-siden.

**Hva som IKKE vises:** moderering, sletting, CSV-eksport, "Hva glemte vi?"-diff og andre admin-funksjoner. Disse blir værende på den passordbeskyttede admin-siden.

**Sikkerhet:** Streamlit-serveren bruker `service_role`-key server-side til å hente aggregerte data. Service-keyen lekker ALDRI til nettleseren — brukere ser kun ferdig-renderte grafer. Anon-rollen i Supabase trenger derfor IKKE SELECT-rettighet (jf. NFR-4.2).

**Personvern:** samme `MIN_RESPONSES_BEFORE_REVEAL`-guard (FR-3.4) gjelder — grafene viser ikke noe før minst N svar er kommet inn.

**Implementasjon:** Renderings-funksjoner (`render_results`, cache-helpers) ekstrahert til `modules/<modul>/views.py` slik at både admin-siden og offentlig resultatside deler én kilde til sannhet.

### FR-3.15 Designsystem (tema + helpers)
**[`DESIGN_GUIDE.md`](DESIGN_GUIDE.md) (v2) er autoritativ kilde for visuell stil.** Den dekker fargesystem, typografi, container-system, callouts, sidebar-mønster, diagram-regler og en sjekkliste. [`CHANGELOG.md`](CHANGELOG.md) oppdateres parallelt ved hver design-/modul-endring.

**Kort sammendrag** (detaljer i guide v2):

- **Canvas:** nær-svart `#0A0F1F`, ikke Fjell heldekkende. Brand-fargene er aksenter på containere/komponenter.
- **Surfaces:** surface-1 `#0F1729` (kort, sidebar), surface-2 `#131C33` (nestede elementer), surface-3 `#1A2542` (code-headers).
- **Brand-palett:** Vann (`#005AA4`), Fjell (`#002776`), Sand (`#F8E9DD`), Frost (`#7EB5D2`), Syrin (`#D3D3EA`).
- **Tekst:** primær `#F4F6FB`, sekundær `#A8B3C7`, tertiær `#6B7691`. Sand er ikke lenger hovedtekst.
- **Font:** Inter primær, Arial fallback. `[[theme.fontFaces]]`-blokk i `.streamlit/config.toml` laster Inter fra Google Fonts.
- **Helpers i [`modules/shared/ui.py`](modules/shared/ui.py):**
  - `callout(body, kind=..., title=..., key=...)` — kinds `"info"` (Vann), `"success"` (Frost), `"warn"` (Syrin), `"subtle"` (dempet). v1-aliaser `"highlight"`→`"success"` og `"warning"`→`"warn"` støttes.
  - `metric_card(label, value, sub)` og `metric_row([...])` — KPI-kort for viktige tall øverst på resultat-/dashboard-sider.
  - `card(key, padding)` — context manager for å pakke innhold (typisk diagrammer) i et standard kort.
  - `crumb(parts)` — breadcrumb øverst på modul-side.
  - `next_module_cta(title, description, page)` — CTA-kort til neste modul.
- **Sidebar:** seksjons-headers ("Oversikt"/"Kursmoduler"/"Administrasjon"), to-sifret mono-prefix på modul-titler (`01 · …`), ingen emojis i sidebar-items.
- **Diagrammer:** Plotly via `render_barchart` (i `modules/gruppeoppgave_1/viz.py`). Heltallsticks på Y-akse, snitt visualisert som stiplet vertikal linje (`mean=`), Likert-mode med "uenig"/"enig"-ankere (`likert=True`). Diagrammet ligger inni et kort.
- **Emojis:** tillatt i H1/H2 på modul-sider og som accent i callout-titler. **Ikke** i sidebar-items, ikke som dekorasjon midt i brødtekst. Maks 2 per overskrift.

**Migrering:** Eksisterende moduler beholder sine `callout()`-kall (bakoverkompatibilitet). Nye/oppgraderte moduler bruker også `card()`, `metric_row()`, `crumb()` og `next_module_cta()` der det gir mening. Modul 5 (AGENTS.md) er referanse-implementasjon for callouts.

---

## 4. Ikke-funksjonelle krav (NFR)

### NFR-4.1 Personvern
- Ingen PII lagres. Deltakerflate har caption: "Vennligst ikke skriv navn, bedriftshemmeligheter…".
- Resultatvisning gated på `MIN_RESPONSES_BEFORE_REVEAL` (se FR-3.4) for å hindre at enkeltsvar kan spores via timing.
- Presentatør kan slette enkeltsvar (FR-3.7 tab 3).

### NFR-4.2 Sikkerhet
- **RLS påkrevd:** `kurs.responses` har RLS aktivert. Anon-rollen har KUN `INSERT`-tilgang (ingen SELECT, UPDATE, DELETE).
- Inserts bruker `returning="minimal"` (PostgREST `Prefer: return=minimal`) slik at anon ikke trenger SELECT-rettighet.
- `service_role`-key brukes kun av admin-siden. Lagret i `st.secrets["SUPABASE_SERVICE_KEY"]`, aldri commit.
- `ADMIN_PASSWORD` sammenliknes med `hmac.compare_digest` (konstant tid).
- `.streamlit/secrets.toml` er i `.gitignore`.

### NFR-4.3 Ytelse / oppdatering
- DB-spørringer på presentatør-siden caches med `@st.cache_data(ttl=5)`.
- Auto-refresh-intervall: `REFRESH_INTERVAL_MS = 10_000` (10 sek). Konfigurert i `config.py`.
- "Refresh nå"-knapp på hver tab nuller cachen.

### NFR-4.4 Språk og tilgjengelighet
- UI på norsk gjennomgående.
- Wordcloud-fonten må støtte `æøå`.
- Layout sentrert på deltakerside (mobile-vennlig), wide på presentatør-side.

### NFR-4.5 Skalérbarhet
- 1 Supabase-prosjekt skal håndtere alle moduler. Hver modul har eget schema.
- 10–30 samtidige deltakere per kursrunde (forventet last). Skal også fungere ved 100 uten endringer.

---

## 5. Datamodell

### DM-5.1 Tabell `kurs.responses`

Definisjon i [`modules/gruppeoppgave_1/supabase_schema.sql`](modules/gruppeoppgave_1/supabase_schema.sql).

| Kolonne | Type | Beskrivelse |
|---|---|---|
| `id` | `bigserial` PK | Auto-inkrement |
| `question_id` | `smallint` NOT NULL, CHECK 1–4 | Refererer til `QUESTIONS`-dict |
| `answer_text` | `text` NULL | Fritekst (FR-3.1 type=text) |
| `answer_choice` | `text` NULL | Valg (FR-3.1 type=choice) |
| `created_at` | `timestamptz` NOT NULL DEFAULT `now()` | Innsendingstidspunkt |

CHECK-constraint: nøyaktig ett av `answer_text` og `answer_choice` skal være satt.

Indeks: `(question_id, created_at desc)`.

### DM-5.2 Felles schema, tabell-prefix per modul
**Alle moduler bruker det felles Postgres-schemaet `kurs`.** Tabeller navngis med modulnavn som prefix for å unngå kollisjon, f.eks. `kurs.oppvarming_responses`, `kurs.<framtidig_modul>_responses`.

**Unntak:** Gruppeoppgave 1 bruker tabellnavnet `kurs.responses` (uten prefix). Det er historisk — etablert da modulen ennå het AGENTS.md og var den eneste i prosjektet. Beholdes for å unngå migrasjon av eksisterende data.

**Konvensjon i `db.py`:** modulen definerer `SCHEMA = "kurs"` og `TABLE = "<modul>_responses"`-konstanter, og bruker dem i alle `.table(TABLE)`-kall. `ClientOptions(schema=SCHEMA)` setter default i klienten.

**Supabase-oppsett:** `kurs` er allerede lagt til i "Exposed schemas". Nye moduler trenger derfor INGEN dashboard-konfigurasjon — bare kjør tabell-SQL-en og koden virker.

**Hvorfor felles schema:** holder Supabase-konfigurasjonen enkel, gjør cross-modul-spørringer mulig hvis det skulle bli relevant, unngår at vi må huske å eksponere et nytt schema hver gang vi legger til en modul.

---

## 6. Ut av scope

- Brukerregistrering eller autentisering for deltakere.
- Persistent identitet på tvers av kursrunder.
- Sammenligning mellom kohorter (kun innenfor én kjøring).
- AI-reduksjon i MVP (planlagt v2 – se FR-3.5).
- Internasjonalisering (kun norsk).
- Mobil-app eller PWA (ren web-app holder).
- Egen LMS-funksjonalitet.

---

## 7. Avhengigheter og verktøyvalg

Definert i [`requirements.txt`](requirements.txt):

- `streamlit>=1.40` – web-rammeverk, multipage via `pages/`
- `supabase>=2.9` – database-klient, RLS
- `wordcloud>=1.9` + `matplotlib>=3.8` – ordsky-rendering
- `streamlit-autorefresh>=1.0` – periodisk re-rendring av admin-side

Endringer her må også oppdatere [NFR-4.5](#nfr-45-skalérbarhet) hvis det påvirker last-håndtering.

---

## 8. Endringslogg

Større beslutninger noteres her. Små refaktoreringer trenger ikke føres.

- **v0.27** – Modul 4 (Arkitekturoversikt) lagt til som UTKAST (FR-3.11, FR-3.12). Kategori I (Innføring), plassert rett før Første demo. Layout: introtekst + fem klikkbare `st.expander`-blokker (System Prompt, Tool Interface, Skills-system, Oppgavestyring, Kontekstbevissthet) + forbehold-callout. Innhold drafted basert på agent-arkitekturen som Cortex Code selv beskriver. Moduler 4–21 skjøvet ned til 5–22; URL-slugs uendret men `m{nr:02d}_<slug>`-filnavn under `pages_content/modules/` oppdatert.
- **v0.26** – Modul 8 (memory.md) + Gruppeoppgave 3 (modul 9) + Resultater Gruppeoppgave 3 (modul 10) lagt til. memory.md er konsept-modul (FR-3.11, FR-3.12) med åtte content-seksjoner og drafted innhold om Cortex Codes Memory-tool (`~/.snowflake/cortex/memory/`, `CORTEX_ENABLE_MEMORY`-opt-in). Gruppeoppgave 3 er interaktiv (par-diskusjon) med fire spørsmål (hva bør / ikke bør lagres + bank-spesifikk risiko) — speiler gruppeoppgave_1-mønsteret med ny `kurs.gruppeoppgave_3_responses`-tabell (DM-5.2). Resultater-modulen deler `render_results` med admin-tab. Moduler 8–18 skjøvet ned til 11–21; URL-slugs uendret men `m{nr:02d}_<slug>`-filnavn under `pages_content/modules/` oppdatert.
- **v0.25** – Modul 8 (Gruppeoppgave 2) lagt til som UTKAST (FR-3.11, FR-3.12). Praktisk oppfølger til skills.md: alle grupper lager samme skill (datakvalitets-sjekk). Ren presentasjons-modul uten datainnsamling — refleksjon foregår muntlig i plenum. Skjelett-mappe `modules/gruppeoppgave_2/` med tre placeholder-content-filer (oppgave, steg, forventet). Moduler 8–17 skjøvet ned til 9–18; URL-slugs uendret, men `m{nr:02d}_<slug>`-prefiks for filene under `pages_content/modules/` oppdatert tilsvarende.
- **v0.24** – Modul 16 (Tilgjengelige modeller) lagt til som UTKAST (FR-3.11, FR-3.12). Skjelett-mappe `modules/tilgjengelige_modeller/` med fire tomme placeholder-content-filer (intro, oversikt, valg, eksempel). Avslutning flyttet fra 16 → 17. `autonomous_loop` CTA-kort peker nå til ny modul (var Avslutning). URL-er for eksisterende moduler er uendret.
- **v0.24** – Bli kjent (FR-3.14) utvidet fra 5 til 10 Likert-påstander. Q6–10 er Cortex Code-spesifikke (bruksfrekvens, beste praksis, terminologi, kostnader, optimalisering). SQL CHECK-constraint `question_id between 1 and 10`. Eksisterende `kurs.oppvarming_responses`-data slettes (drop+recreate via SQL).
- **v0.23** – `DESIGN_GUIDE.md` v2: produkt-design over brand-disiplin. Canvas byttet fra Fjell heldekkende til nær-svart `#0A0F1F`; brand-fargene reserveres for aksenter/containere. Inter primær font med Arial fallback (Inter lastet via `[[theme.fontFaces]]`). Nye helpers i `modules/shared/ui.py`: `metric_card`/`metric_row`, `card` (context manager), `crumb`, `next_module_cta`. `callout()` får kvadratiske ikoner i stedet for emojis; kinds renavn `"highlight"`→`"success"` og `"warning"`→`"warn"` (aliaser beholdt). Sidebar-titler tosifret mono-prefix uten emojis (`"01 · Cortex Code"`). Plotly-diagrammer i `render_barchart` har heltallsticks, snitt-linje (`mean=`) og Likert-ankere (`likert=True`); wraps i `card()`. `oppvarming/views.py` viser metric-kort på toppen (totalt antall svar, snitt-score, antall spørsmål). FR-3.15 fullstendig omskrevet for v2-helpers. Innhold på modul-sider urørt.
- **v0.22** – Individuelle oppgaver 1–5 flyttet til posisjon 5–9 (rett etter Første demo). AGENTS.md → 10, skills.md → 11, Gruppeoppgave 1 → 12, Resultater → 13. Pedagogisk: hands-on før konseptuell utdyping.
- **v0.21** – Full migrasjon til `callout()` per DESIGN_GUIDE §6: alle `st.info`/`st.warning`/`st.success`/`st.error` byttet ut i 13 moduler. Empty-state-meldinger bruker `kind="subtle"`. Form-toast beholdt (transient).
- **v0.20** – `DESIGN_GUIDE.md` etablert som autoritativ kilde for visuell stil. `CHANGELOG.md` opprettet. Tidligere "ingen ikoner"-regel overstyrt: emojis nå påkrevd i H1/H2 og callout-titler. `.streamlit/config.toml` justert til kanonisk versjon fra guide. Sidebar-ikoner og subheader-emojis restaurert i alle 17 modulene.
- **v0.19** – Modul 6 lagt til som UTKAST: skills.md (konseptuell presentasjons-modul, FR-3.11/FR-3.12, parallell til AGENTS.md). Tomme placeholder-filer i `content/` — Andre skriver innholdet selv. Modul 6–15 renummerert til 7–16 (Gruppeoppgave 1 → 7, …, Avslutning → 16). URL-er uendret.
- **v0.18** – Designsystem lagt til (FR-3.15): `.streamlit/config.toml` med Vann/Fjell/Sand/Frost/Syrin-palett, `callout()`-helper via `streamlit-extras.stylable_container`. Modul 5 (AGENTS.md) migrert som demo. Ikke-ikoner-regelen beholdt.
- **v0.17** – Oppvarming senker reveal-terskel til 1 svar (FR-3.14, avvik fra NFR-4.1). `render_barchart` aksepterer nå `min_responses`-parameter; gruppeoppgave_1 beholder default 3.
- **v0.16** – Oppvarming bygget om til Likert (FR-3.14): fem påstander på 1–5-skala (1 = uenig, 5 = enig), grid-layout med én submit. Schema-migrasjon: `answer_choice text` → `answer_value smallint`. Snittsvar vises på resultatsiden.
- **v0.15** – Sju nye moduler lagt til som UTKAST: Individuelle oppgaver 2–5 (utforske, datakvalitet, optimaliser, refleksjon), Demo 2 (realistisk bank-use-case), Autonomous loop i dybden, og Avslutning. Andre skriver innholdet i `.md`-filene per FR-3.12.
- **v0.14** – Schema-strategi forenklet (DM-5.2): alle moduler bruker felles `kurs`-schema med tabell-prefix per modul. Oppvarming-tabellen flyttet fra `oppvarming.responses` til `kurs.oppvarming_responses`. Ingen nye Supabase-schemas trenger eksponering for fremtidige moduler.
- **v0.13** – Oppvarmings-seksjon lagt til (FR-3.14): "Bli kjent" (5 choice-spørsmål) og "Resultater Bli kjent" som kjøres før modul 1.
- **v0.12** – Modul 8 lagt til: Individuell oppgave 1 (hands-on instruksjon for å legge til Analyse GIT repo i Snowflake). Presentasjons-modul med markdown-innhold.
- **v0.11** – Modul 7 lagt til: Resultater Gruppeoppgave 1 (offentlig read-only). Ny FR-3.13. Rendering-logikk ekstrahert til `modules/gruppeoppgave_1/views.py` slik at admin og offentlig side deler kode. Barcharts viser nå absolutte tall over hver bar (Plotly).
- **v0.10** – Modul 5 lagt til: AGENTS.md (konseptuell presentasjons-modul). Eksisterende AGENTS.md interaktive workshop renames til Gruppeoppgave 1 (modul 6) — mappe (`modules/gruppeoppgave_1/`), URL (`/gruppeoppgave_1`) og titler oppdatert. Schema (`kurs`) beholdes uendret.
- **v0.9** – Innhold separert fra layout (FR-3.12): markdown-filer under `modules/<navn>/content/`, loader-helpers i `shared/ui.py`. Refaktorert: cortex_code, cortex_interaction, cortex_in_snowsight, demo_1. AGENTS.md uendret (datadrevet).
- **v0.8** – Modul 4 lagt til som UTKAST: Første demo (presentatør-runbook med tre demo-segmenter). AGENTS.md renummerert til modul 5.
- **v0.7** – Modul 3 lagt til som UTKAST: Cortex Code i Snowsight (presentasjons-modul, trenger faktisk innhold). AGENTS.md renummerert til modul 4. Home.py viser nå også "Utkast"-moduler med link.
- **v0.6** – Modul 2 lagt til: Snowsight vs CLI (presentasjons-modul). AGENTS.md renummerert til modul 3.
- **v0.5** – Modul 1 lagt til: Cortex Code (presentasjons-modul, FR-3.11). AGENTS.md renummerert til modul 2.
- **v0.4** – Sidemeny via `st.navigation`: seksjoner ("Kursmoduler", "Administrasjon"), nummererte modul-titler, admin sist (FR-3.10). `hub.py` splittet i entry + `home.py`.
- **v0.3** – Multimodul-arkitektur: introdusert `hub.py`, `pages/<modul>.py` wrappers, `modules/<navn>/app_logic.py`-mønster.
- **v0.2** – Schema-isolasjon: tabeller flyttet fra `public` til `kurs`. Diff-ordsky lagt til. Topp 10-filter i ordsky.
- **v0.1** – MVP: én Streamlit-app med fire spørsmål, ordsky for fritekst, barchart for valg, passordbeskyttet admin.
