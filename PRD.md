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
- "Bli kjent" — femten **påstander** vurdert på 1–5 Likert-skala (1 = uenig, 5 = enig). Alle besvares samtidig i én form med én submit-knapp. Hver innsending lagrer 15 rader (én per påstand). Påstandene defineres i `modules/oppvarming/config.py` som `STATEMENTS`-dict. **Q1–5** dekker generell teknisk bakgrunn (Snowflake-erfaring, AI-verktøy, CLI-komfort, kodebakgrunn, holdning til AI-agenter). **Q6–11** dekker Cortex Code-modenhet spesifikt (bruksfrekvens, beste praksis, terminologi, kostnadsmodell, optimalisering, modellvalg). **Q12–15** dekker agent-konfigurasjon (verktøy agenten har tilgjengelig, skills, hvordan lage personlige skills, system prompt).
- "Resultater" — offentlig read-only side med 15 barcharts (én per påstand, x-akse 1–5) + beregnet snittsvar. Samme prinsipp som FR-3.13.

**Tabell:** `kurs.oppvarming_responses` (jf. DM-5.2 — felles schema, prefix per modul). Kolonner: `id`, `question_id` (1–15), `answer_value` (smallint 1–5), `created_at`. SQL-definisjonen ligger i [`modules/oppvarming/supabase_schema.sql`](modules/oppvarming/supabase_schema.sql) og må kjøres MANUELT i Supabase SQL Editor. Siden `kurs` allerede er i Exposed schemas, trengs ingen dashboard-endring.

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
- **Font:** Arial gjennomgående (`Arial, Helvetica, sans-serif`). Ingen webfonter / `[[theme.fontFaces]]` — Arial er forhåndsinstallert og samsvarer med bankenes skrifttype-policy. Mono/kode: JetBrains Mono via CSS.
- **Helpers i [`modules/shared/ui.py`](modules/shared/ui.py):**
  - `callout(body, kind=..., title=..., key=...)` — kanoniske kinds matcher Designsystemet (INFO/TIPS/ADVARSEL): `"info"` (marine — fakta), `"tip"` (grønn — råd/anbefaling), `"warn"` (amber — risiko), `"subtle"` (dempet grå — empty-states). Deprecated aliaser: `"success"`/`"highlight"`→`"tip"`, `"warning"`→`"warn"`. SVG-linjeikon settes automatisk ut fra kind.
  - `metric_card(label, value, sub)` og `metric_row([...])` — KPI-kort for viktige tall øverst på resultat-/dashboard-sider.
  - `card(key, padding)` — context manager for å pakke innhold (typisk diagrammer) i et standard kort.
  - `crumb(parts)` — breadcrumb øverst på modul-side.
  - `next_module_cta(title, description, page)` — CTA-kort til neste modul.
- **Sidebar:** seksjons-headers ("Oversikt"/"Kursmoduler"/"Administrasjon"), to-sifret mono-prefix på modul-titler (`01 · …`), ingen emojis i sidebar-items.
- **Diagrammer:** Plotly via `render_barchart` (i `modules/gruppeoppgave_1/viz.py`). Heltallsticks på Y-akse, snitt visualisert som stiplet vertikal linje (`mean=`), Likert-mode med "uenig"/"enig"-ankere (`likert=True`). Diagrammet ligger inni et kort.
- **Emojis/ikoner:** ingen emojis noe sted (DESIGN_GUIDE §1.7) — overskrifter, callout-titler, crumbs og brødtekst er ren tekst. Ikon-språket er SVG-linjeikoner via `svg_icon()` (callout-badger, kort-disker, knapper). Typografiske piler (`→`/`←`) i prosa er ok.

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

- **v0.61** – Fjernet **Forside** og **Test: Skills (HTML)** (var modul 28). Forside: `pages_content/forside.py` slettet, «Forside»-lenke + dispatch fjernet; ny standard-side er første kursmodul (Evolusjon) via `_DEFAULT_PAGE = page_id(MODULER[0])` i `app.py`; ukjente sider (inkl. gammel `?page=forside`) gir grasiøs feilside. Test-skills: MODULER-entry + «Test»-SECTIONS + wrapper + `modules/test_skills_html/` + `_WIDE_LAYOUT_SLUGS`-oppføring fjernet (var siste modul, ingen renummerering; 27 moduler igjen). FR-3.10s nav-spec var fra før utdatert (ikke patchet). Ingen ny FR/NFR. Verifisert: py_compile + AppTest, 0 feil.
- **v0.60** – skills.md (modul 17): flettet inn eier-levert utkast additivt (etter sammenligning «mister vi mye?» -> nei, behold dagens rike side + hekt på utkastets tillegg). Tre grep: (1) ny seksjon «Hvorfor bruke skills?» (`content/hvorfor.md`, etter «Hva er en skill?»); (2) tommelfingerregel-callout (`content/naar_regel.md`, kind=tip, etter «Når bør du lage en custom skill?»-stegene); (3) custom-kortet beriket med «typiske bruksområder» (utvidet `content/typer.md`). Dagens layout + skill-development-eksempelet (`lage_prompt`, broen til Gruppeoppgave 2) + anatomi-kort/to-kolonne/badge-steg/callouts er urørt - ingen substans eller visuell design mistet. Ingen wholesale omskriving. Ingen ny FR/NFR. Verifisert: py_compile + AppTest (m17), 0 feil, 0 emoji/dash/`é`.
- **v0.59** – Context engineering (modul 24): full restrukturering rundt eier-levert innhold (innholds-unntaket i CLAUDE.md). Ny seksjonsflyt i `app_logic.py`: intro «hva er det» -> god prompt -> prompt-mal -> daarlig vs bedre prompt (2 kolonner) -> vanlige feil (warn) -> hvor legges konteksten (tabell) -> hovedregel (tip) -> CTA. Prompt-kodeblokker via `render_markdown_wrapped_code`. 8 nye content-filer; 6 gamle prompt-engineering-filer slettet (og `load_split_markdown`-bruk fjernet). Subtitle -> «Riktig kontekst, på riktig sted, til riktig tid». Ingen ny FR/NFR. Verifisert: py_compile + AppTest (m24), 0 feil.
- **v0.58** – Individuell oppgave: Bundled skill (modul 19): fjernet «Forventet resultat»-seksjonen (subheader + `forventet`-markdown + divider) fra `app_logic.py`; siden er nå Oppgave -> Steg -> CTA. `content/forventet.md` beholdt men ubrukt. Ingen ny FR/NFR. Verifisert: py_compile + AppTest (m19), 0 feil.
- **v0.57** – Individuell oppgave: Modellvalg (modul 16): de to prompt-tekstene (oppgave 1 og 2) bryter nå ord og vokser vertikalt i stedet for å lage horisontal scroll. Ny helper `render_markdown_wrapped_code(markdown_text)` i `modules/shared/ui.py` som splitter markdown på ```-kodeblokker og rendrer dem som `st.code(..., wrap_lines=True)` (prosaen rundt som vanlig markdown). `app_logic.py` bruker den for `oppgave_1`/`oppgave_2`; content-filene er urørt (kun rendering endret, jf. §FR-3.12). Ingen ny FR/NFR. Verifisert: AppTest (m16) - 2 `st.code` med `wrap_lines=True`, prosa beholdt, 0 feil.
- **v0.56** – Sidebar-bredde endret 280px -> 320px og samlet i én konstant `SIDEBAR_WIDTH` i `components/sidebar.py` (de tre hardkodede 280px-verdiene fjernet, ny `_SIDEBAR_WIDTH_CSS` injisert i `render_sidebar`). Bakgrunn: Streamlit 1.50 har ingen native dra-resize av sidebaren (kun collapse), så fri «dra linja»-justering ville krevd en skjør JS-hack mot Streamlit-interne DOM; eier valgte en annen fast bredde. DESIGN_GUIDE pinner ikke bredden i prosa. Ingen ny FR/NFR. Verifisert: py_compile + AppTest (render_sidebar), 0 feil.
- **v0.55** – «Kostnader» flyttet til **egen seksjon** mellom **Plan Mode** og **AGENTS.md** (var nr 7 i «Komme i gang»). Ny `SECTIONS`-gruppe `kostnader` (label «Kostnader», kun `m11_kostnader`) plassert etter `plan_mode`- og før `agents_md`-seksjonen. Sekvensiell renummerering: kostnader 7->11; @-mentions + Plan Mode-modulene skjøvet ned ett hakk (at_mentions 8->7, oppg 9->8, plan_mode 10->9, oppg 11->10); AGENTS.md (12) og alt etter uendret. Berørt: 5 wrapper-filer renamet, 5 crumb-nr, `data/moduler.py` (MODULER + SECTIONS), 3 CTA-er rekoblet (`individuell_oppgave_1`->`at_mentions`, `individuell_oppgave_plan_mode`->`kostnader`, `kostnader`->`agents_md`). `kostnader/content/*.md` fortsatt ubrukt. Ingen ny FR/NFR. Verifisert: AppTest 34 sider 0 feil, crumb-nr==MODULER-nr, 1..31 uten hull. **Merk:** `scripts/lag_kursoversikt_xlsx.py` er fra før ute av sync med 31-moduls-tilstanden (lister slettet «Cortex Code i Snowsight», gamle titler/seksjoner, nr opp til 36 med hull) - ikke patchet her; bør rebygges separat fra `data/moduler.py`.
- **v0.54** – Første demo (modul 5): redusert til kun «Agenda for demoen»-callouten; de tre detalj-segmentene (Workspace/rolle/metadata, Cortex Code/«Vis meg de 5 første radene»/kontekst-panelet, Kostnadsdashbord) fjernet fra `demo_1/app_logic.py` (selve demoen kjøres live). `DEMO_FILES`-loopen + ubrukt `load_titled_markdown`-import fjernet; content-filene beholdt men ubrukt. Ingen ny FR/NFR (layout-reduksjon av §FR-3.11-modul). Verifisert: py_compile + AppTest (m05), 0 feil.
- **v0.53** – Under panseret (modul 4, slug `arkitektur`): fjernet «Forbehold»-callouten nederst, og flyttet «Demo: spør agenten om seg selv»-callouten fra toppen til sist (der Forbehold lå, rett før CTA). Ny rekkefølge: intro -> de fem lagene (expandere) -> demo -> CTA. Kun `modules/arkitektur/app_logic.py`; `content/forbehold.md` er nå ubrukt (beholdt, ikke slettet). Ingen ny FR/NFR. Verifisert: py_compile + AppTest (m04), 0 feil.
- **v0.52** – Evolusjon (modul 1): epoke-tittelen (Før/Nå/Snart) flyttet opp på samme rad som nummer-badgen, til høyre for «1/2/3» (tidligere under badgen). `signature_card` fikk et nytt valgfritt `title`-argument som rendrer badge + tittel i en flex-rad (18px marine, som `feature_card`-tittel); `evolusjon/app_logic.py` sender nå `title=era_title` og dropper den separate `#### {tittel}`-linja. Bakoverkompatibelt (title=None gir badge alene). DESIGN_GUIDE §8 oppdatert. Ingen ny FR/NFR (visuell helper-justering). Verifisert: py_compile + AppTest (m01): badge + tittel i samme rad i alle tre kort, 0 feil.
- **v0.51** – Navigasjons-omlegging i front av kurset. **«Arkitekturoversikt» (slug `arkitektur`) flyttet fra «Komme i gang» til «Introduksjon»** og er nå **nr 4** (etter «Snowsight vs CLI»). Fanen omdøpt til **«Under panseret»** (kun visningsnavn: MODULER-tittel, `module_header` og crumb; slug uendret). **«Cortex Code i Snowsight» (slug `cortex_in_snowsight`) slettet** (var tom placeholder) - modul-mappe, wrapper, MODULER- og SECTIONS-oppføring fjernet; `cortex_interaction`-CTA peker nå til `arkitektur`. **Full sekvensiell renummerering 1..31** (lukket også pre-eksisterende hull i halen): 28 wrapper-filer renamet + crumb-nr oppdatert i hver berørte `app_logic.py`. CTA-kjeden er slug-basert og uberørt utover `cortex_interaction`. Verifisert: py_compile, konsistens (1..31 uten hull, alle wrappers finnes), 0 `cortex_in_snowsight`-referanser, AppTest 0 feil.
- **v0.50** – Cortex Code (modul 2) fikk tre nye oversiktsseksjoner øverst (eier-innhold, additivt): **Hva er Cortex Code?** (AI-kodeagent, integrert i Snowflake, forstår roller/schemaer/beste praksis, aktivt workspace som kontekst), **Hvorfor bruke Cortex Code?** (resultater = prompts pluss data, kontekst fra miljø og data, derfor ikke et eksternt verktøy), **Hvordan kan vi bruke det?** (Streamlit-dashbord, SQL, ML utenfor scope, notebook-analyse). Lagt rett etter modul-headeren, over den eksisterende «decode dokumentasjonssitatet»-delen (sitat/begrep-expandere/oppsummering/eksempel beholdt). «Hva er»-bullets oversatt fra eierens engelske kladd til norsk. Tre nye `content/`-filer (`hva_er`/`hvorfor`/`hvordan`) + tre `st.subheader`-seksjoner i `app_logic.py`. Ingen ny FR/NFR. Ingen emoji/em-dash/en-dash/`é`. Verifisert: py_compile + AppTest (m02), 0 feil.
- **v0.50** – Evolusjon (modul 1): xkcd-tegneserie «Vibe coding vs Agentic SDLC» lagt inn under epoke-kortene (erstatter den gamle «Bilde fra Snowflake»-placeholderen). Ny `_image_or_placeholder`-helper i `app_logic.py` + bildefil `content/vibe_vs_agentic_sdlc.png`. Ny `content/bilde_ramme.md` (UTKAST) vist som `st.caption` rammer bildet for analytiker-/bank-publikum og demper tech-bro-tonen (bildet er SE-/hype-rammet; jf. CLAUDE.md). Epoke-titler endret «Nå» -> «I dag» og «Snart» -> «Fremover». Ingen ny FR/NFR (content/layout i §FR-3.11/§FR-3.12). Verifisert: py_compile + AppTest (m01), 0 feil.
- **v0.49** – Snowsight vs CLI (modul 3): de to skjermbildene lagt inn. `content/snowsight.png` (Snowsight web-UI med Cortex Code-panel) og `content/cli.png` (Cortex Code v1.0.35 i terminal) erstatter de stiplete placeholderne (`_image_or_placeholder` viser dem automatisk via `st.image(..., width="stretch")`). Ingen kodeendring (helperen fantes fra v0.46); kun to bildefiler lagt til. Verifisert: AppTest (m03) viser 2 bilder, ingen placeholder, 0 feil.
- **v0.48** – Cortex Code (modul 2) layout-justeringer etter eier-tilbakemelding: (1) fjernet `st.caption("La oss pakke ut hva som faktisk står her.")` under dokumentasjons-callouten; (2) fjernet `st.toggle("Vis alle forklaringer")` (`show_all`) - begrep-expanderne er nå alltid `expanded=False`, brukeren klikker frem ett og ett; (3) flyttet «Lytteklipp: Snowflake RBAC»-seksjonen opp til rett under dokumentasjons-callouten (over «Begrep for begrep»). Kun `modules/cortex_code/app_logic.py`; content urørt. FR-3.11s «typisk … `st.toggle('Vis alle')`»-mønster står fortsatt som generell mulighet (denne modulen velger det bort). Ingen ny FR/NFR. Verifisert: py_compile + AppTest (m02): caption + toggle borte, lytteklipp før «Begrep for begrep», 7 expandere kollapset, 0 feil.
- **v0.48** – "Bli kjent" (oppvarming, §FR-3.14) utvidet fra 11 til 15 Likert-påstander. Nye Q12-15 dekker agent-konfigurasjon: verktøy agenten har tilgjengelig, skills, hvordan lage personlige skills, og system prompt. Endret `STATEMENTS` i `modules/oppvarming/config.py` og CHECK-constraint i `modules/oppvarming/supabase_schema.sql` (`question_id between 1 and 15`); SQL re-kjøres manuelt i Supabase (drop+recreate, nullstiller tabellen - pre-kurs, jf. v0.24). All Python er generisk (looper over `STATEMENTS`, `len(STATEMENTS)`), så app_logic/db/views/resultater plukker opp de nye automatisk. Samtidig rettet eksisterende §FR-3.14-drift (teksten sa fortsatt "ti påstander / question_id 1-10 / 10 barcharts" mens config hadde 11). Ingen ny FR/NFR. Verifisert: py_compile + struktur (15 nøkler 1-15) + smoke-import.
- **v0.47** – Oppgave-opprydding. Slettet tre individuelle oppgaver (`individuell_oppgave_3`/`_4`/`_5`, gamle nr 27/29/31) og `individuell_oppgave_kurs_kunde` (nr 33, dupliserte lineage-temaet som dekkes tidligere). Konkurrent-oppgaven (`individuell_oppgave_konkurrent`, nr 34) gjort om til **gruppeoppgave**: `kategori` P->G + tittel «Individuell oppgave: Konkurrent-signaler» -> «Gruppeoppgave: Konkurrent-signaler» (slug/mappe/wrapper uendret; Andre skriver selv gruppe-innrammingen i content). Numrene 27/29/31/33 er bevisst latt stå som hull - ingen renummerering: `find_by_page_id` matcher eksakt nr, så navigasjon/sidebar/forside er upåvirket. Tre CTA-er rekoblet forbi de slettede: `individuell_oppgave_2` -> `demo_2`, `autonomous_loop` -> `individuell_oppgave_kohort`, `individuell_oppgave_kohort` -> `individuell_oppgave_konkurrent`. SECTIONS trimmet (anvendt_praksis = kun oppgave_2; dybde = demo_2 + autonomous_loop; kurs_data = kohort + konkurrent). Oppdatert README, CONTENT_REVIEW, `scripts/lag_kursoversikt_xlsx.py`. Ingen FR/NFR slettet (oppgavene dekkes av generiske §FR-3.11/§FR-3.12, ingen egne ID-er). Kurset har nå 32 moduler (mNN-numre opp til 36, med hull). Verifisert: py_compile + wrapper-integritet (32 wrappere, 0 orphans), 0 døde referanser i kode.
- **v0.46** – Snowsight vs CLI (modul 3): fjernet fordeler/ulemper/«når passer den best» for begge flater + «velg»-takeaway etter eier-tilbakemelding (ikke korrekt info); slettet `snowsight_card.md`/`cli_card.md`/`closing.md`. To kolonner viser nå skjermbilde via `st.image` (ny `_image_or_placeholder`-helper med stiplet placeholder til bildene legges i `content/` som `snowsight.png`/`cli.png`). Ny `content/cli_docs.md` lenker til offisiell Snowflake-doc for Cortex Code CLI (`.../user-guide/cortex-code/cortex-code-cli`). Ingen ny FR/NFR (content/layout i eksisterende §FR-3.11/§FR-3.12). Verifisert: py_compile + AppTest (m03), 0 feil.
- **v0.45** – Evolusjon (modul 1) reframet (eier-innhold). Undertittel «Tre epoker i hvordan vi skriver kode» -> «... kode og gjør analyser». De tre epoke-kortene gikk fra «Era 1/2/3» (Google / AI-assistent / spesifikasjon) til **Før / Nå / Snart** med ny brødtekst fra Andre; content-filene `era_1_googling`/`era_2_assistanse`/`era_3_spesifikasjon` omdøpt til `epoke_1_for`/`epoke_2_naa`/`epoke_3_snart` (ERA_FILES oppdatert). Lagt til en Snowflake-illustrasjon etter kortene (foreløpig en merket placeholder-boks; Andre bytter inn `st.image`). Ny refleksjons-callout «Tenk igjennom: Hva krever dette av løsninger rundt oss?» (`content/losninger_rundt_oss.md`) erstatter «Hvor er du i dag?»-callouten; «Spørsmål til deg» (rolle) beholdt. `hvor_er_du.md` nå ubrukt (beholdt, ikke slettet). Ingen ny FR/NFR (content + layout i eksisterende §FR-3.11/§FR-3.12-modul). Ingen emoji/em-dash/en-dash/`é`. Verifisert: py_compile + AppTest (m01), 0 feil.
- **v0.44** – «Kostnader» flyttet fra slutten (gammel nr 34) til seksjonen **«Komme i gang»** rett etter Individuell oppgave 1, og siden er redusert til en ren peker: den sier nå kun «Gjennomgang i PowerPoint» (resten av kostnads-temaet tas i plenum). Full renummerering: kostnader ble nr 08, og modulene som var 08-33 ble skjøvet +1 (til 09-34); Avslutning/Test beholdt 35/36. Berørt: 27 wrapper-filer i `pages_content/modules/` (mNN_*) flyttet, 26 crumb-numre i `app_logic.py` justert, `data/moduler.py` (MODULER-nr + SECTIONS: `m08_kostnader` inn i `komme_i_gang`, ut av `avslutning`), tre CTA-er rekoblet (`individuell_oppgave_1` -> `kostnader`, `kostnader` -> `at_mentions`, `individuell_oppgave_konkurrent` -> `avslutning`), `scripts/lag_kursoversikt_xlsx.py` reordnet. URL-ene `?page=mNN_...` for de skjøvne modulene endret; ingen DB-tabeller berørt. `kostnader/content/*.md` er nå ubrukt (beholdt, ikke slettet). Ingen ny FR/NFR (flytting + content-reduksjon av eksisterende §FR-3.11-modul). FR-3.10s opplistede rekkefølge er fortsatt utdatert fra før og ble ikke oppdatert her. Verifisert: py_compile + AppTest alle 36 sider, crumb-nr == MODULER-nr, 0 feil.
- **v0.43** – Ny typografiregel **DESIGN_GUIDE §1.10**: bokstaven `é`/`É` (U+00E9/U+00C9) skal aldri brukes; bruk alltid `e`/`E` (vanligst: «en» for tallet 1, uten aksent). Parallell til §1.7 (emoji) og §1.8 (em-/en-dash). Eier-beslutning. Lagt til i DESIGN_GUIDE §1 + CLAUDE.md «Kort sammendrag»; authority-filenes egne forekomster ryddet (DESIGN_GUIDE 5, CLAUDE.md 6). Retroaktiv sweep av app-/innholds-/kodefiler utført (eier-godkjent, `perl -CSD` over working-tree `.py`/`.md`); working tree er `é`-fri bortsett fra regel-definisjonstegnene i DESIGN_GUIDE/CLAUDE og historiske CHANGELOG/PRD-entries. Verifisert: 142 py_compile + AppTest, 0 feil. Ingen ny FR/NFR (designregel).
- **v0.42** – Varmere epoke-kort på Evolusjon (modul 1). De tre epoke-kortene leste som «kalde» (hvit `card()`, tynn grå kant, ingen aksent). Ny helper `signature_card(number=None)` i `modules/shared/ui.py` (context manager): designsystemets varme signaturflate (fersken `#F8E6D5` + azur venstrekant `#1F6FC4`) + valgfritt marine nummer-badge, men innhold rendret via `st.markdown` i `with`-blokken så markdown (kursiv) bevares - i motsetning til `feature_card` (ferdig HTML-streng). `evolusjon/app_logic.py` bruker den nå med `number=1/2/3`; innhold urørt. DESIGN_GUIDE §8 oppdatert (funksjonskort-liste + «velg flate bevisst»-note). Ingen ny FR/NFR (rent visuelt, design-helper). Ingen emojis (§1.7) / em-dash/en-dash (§1.8). Verifisert: py_compile + AppTest (m01), 0 feil.
- **v0.41** – Modul 24 omdøpt fra «Prompt engineering» til «Context engineering» (slug `prompt_engineering`→`context_engineering`, mappe + wrapper `m24_*` flyttet via `git mv`, `MODULER`/`SECTIONS` id/label/page_id + CTA fra `gruppeoppgave_3_resultater` + `scripts/lag_kursoversikt_xlsx.py` rad 24 oppdatert). Bakgrunn (B1 fra pedagogisk gjennomgang): modulens tema er context engineering - hvordan gi agenten riktig kontekst - og de tidlige øvelsene er bevisst uavhengige av denne ferdigheten, så det er ikke et rekkefølge-avvik. URL `?page=m24_*` endret; ingen DB-tabeller berørt; `theme-light/` (untracked) urørt. Ingen ny FR/NFR (identitets-omdøping av eksisterende §FR-3.11/§FR-3.12-modul); innholdsreframing (subtitle/expander-labels/.md fortsatt prompt-rammet) gjenstår for eier. Samme runde: korte begrepsglosser (token/kontekstvindu i m15, kohort/Streamlit i m31, lineage i m08, `@`-bro i m17, dbt i m05) + to framoverpekere (AGENTS.md-teaser i m06, skills i m10). Verifisert: py_compile + AppTest, 0 feil.
- **v0.40** – Modul 15 (`tilgjengelige_modeller`) utvidet med en grunnlagsseksjon **«Hva er en LLM»** øverst (etter intro, før Oversikt-tabellen). Forklarer LLM = Large Language Model, next-token-prediksjon, parametere/datamengde, multimodalitet, at Opus/Sonnet/Haiku er LLM-er fra Anthropic, og distinksjonen modell-som-tenker vs. agent (modell + verktøy + loop) - et begrep som tidligere kun var antydet i `arkitektur` (modul 5), aldri sagt rett ut. Ny content-fil `content/hva_er_llm.md` + én ny `st.subheader`-seksjon i `app_logic.py`. Innholdet er **Andres egne ord** (levert i forespørselen), kun formatert - derfor ingen UTKAST-markør. Ingen ny FR/NFR (content-fyll i eksisterende §FR-3.11/§FR-3.12-modul). Ingen emojis (§1.7) / em-dash (§1.8). Verifisert: py_compile + AppTest, 0 feil.
- **v0.39** – Design-konformitets-audit (DESIGN_GUIDE vs faktiske sider) + remediering av trygge avvik. `#0B5BB5` (en tredje, off-palett blåfarge brukt som hovedaksent) → azur `#1F6FC4` i `components/sidebar.py`, `pages_content/forside.py`, `modules/shared/ui.py`, `modules/oppvarming/app_logic.py`. `gruppeoppgave_2` fikk manglende `crumb` + `next_module_cta_for("memory_md")` (§8-struktur). DESIGN_GUIDE rettet for intern motsigelse/drift: §6+§9 beskriver nå custom sidebar (ikke `st.navigation()`, jf. §11), §0 fjernet døde referanser til `Designsystem.html`/`design_preview.html` (ekstern/ligger ikke i repoet), §10-sjekkliste callout-typer → info/tip/warn, §11 modultall gjort tallfritt. Eier-beslutninger: `test_skills_html` (modul 36) beholdes som sandbox i «Test»-nav (isolert iframe), og favicon-emojien (`app.py`) beholdes - begge sanksjonerte unntak. §1.8 utvidet til også å forby en-dash (`–`); appen renset (1 forekomst). Resten av appen er konform (0 emoji i sidetekst, 0 em-dash/en-dash, Arial, ingen mørke rester, ingen banned `st.*`).
- **v0.38** – Modul 15 (`tilgjengelige_modeller`) fylt med innhold (FR-3.11, FR-3.12): forklaring av forskjellen mellom **Opus** og **Sonnet** i Cortex Code. Fire content-filer (`intro`, `oversikt`, `valg`, `eksempel`) gikk fra placeholder til UTKAST-innhold; `app_logic.py` urørt. `oversikt.md` er en markdown-sammenligningstabell (kapabilitet/hastighet/kostnad/passer-til), `valg.md` gir «Sonnet som standard, Opus når kompleksitet/risiko rettferdiggjør kostnaden», `eksempel.md` en generisk/fiktiv bank-kontrast. Drafted på eksplisitt forespørsel (innholds-unntaket i CLAUDE.md), konseptuelt holdt (ingen fabrikkerte modellnavn/versjoner/priser), bank-rammet, ingen emojis (§1.7) / em-dash (§1.8), alt merket UTKAST. Hands-on-oppgaven (modul 16) er fortsatt placeholder. Verifisert: AppTest, 0 feil.
- **v0.37** – Designsystem v1-komponenter implementert + rullet ut (gap-analyse mot `Designsystem.html`). Nye helpere i `modules/shared/ui.py`: **`module_header(title, *, subtitle, eyebrow)`** (modul-hero: azur eyebrow + tung marine display-H1 + azur undertittel — erstatter `st.title()` + `st.caption()`), **`feature_hero()`** (fersken signaturkort + 52px marine disc + prikkliste), **`feature_card()`** (hvitt kort + 40px disc), **`dotlist()`**, **`inject_global_css()`** (marine primær-/form-knapper radius 7px + hover marine-dyp, hvit-marine sekundærknapp, azur-tint inline-kode — kalt én gang fra `app.py`). `card()`/`metric_card()` fikk `SHADOW_1`. Sidebar fast bredde 280px + border-right. **`module_header()` rullet ut på alle 34 moduler** (migrasjons-workflow): `st.title()`+`st.caption("Modul N · …")` → `module_header(title, subtitle="…")`; interaktive gate-skjermer (deltakerkode) beholder `st.title()`. Død `render_module_header()` (gammel `hub.py`-lenke) fjernet. DESIGN_GUIDE §8 oppdatert. Verifisert: 36 sider AppTest, 0 feil. **Åpent:** font (Libre Franklin avventes — Arial-tilnærming for display-H1); funksjonskort-innhold per modul (f.eks. cortex_in_snowsight) er Andres domene — helperne er klare.
- **v0.37** – Innholds- og regelrunde fra eier. Tre nye/​skjerpede designregler i DESIGN_GUIDE: §1.7 (ingen emojis), §1.8 **ingen em-dash (`—`)** - fjernet fra 108 app-filer (207 forekomster, erstattet med vanlig bindestrek), og §1.9 **PowerPoint-nært** (slide-lik altitude; presentatør-metainnhold som snakkepunkter/varighet hører ikke hjemme på sidene). Snakkepunkter + forventet varighet fjernet fra `demo_1`, `demo_2`, `demo_bundled_skill`, `individuell_oppgave_5` (toggles/seksjoner + content). Modul-endringer: **Evolusjon** (modul 1) omdøpt fra «Fra Google til spesifikasjon» + tre innholdsblokker fra Andre. **Bli kjent**-intro endret til «Hvilke forkunnskaper har vi? Helt anonymt». **Resultater fra Bli kjent** (tidl. «Resultater fra Oppvarming») - fjernet auto-refresh/live-aggregering, kun «Refresh nå»-knapp. **Første demo** redesignet slide-likt (agenda m/kostnadsdashbord sist, workspace m/rolle+metadata, to Cortex Code-prompts, bokstavspørsmålet som AGENTS.md-teaser). **Individuell oppgave 1** fikk nytt steg #1 «Åpne Workspaces». **Snowsight vs CLI** forenklet (intro + to kort + takeaway; fjernet duplikat «Hva velger du?»-seksjon + sammenligningstabell).
- **v0.36** – Callout-typer standardisert til Designsystemets trio **INFO / TIPS / ADVARSEL** + dempet `subtle`. Den grønne typen omdøpt fra `success` (sjekkmerke) til **`tip`** (lyspære-ikon, som allerede fantes i `_SVG_ICONS` men var ukoblet). Kanoniske `kind`-navn er nå `info`/`tip`/`warn`/`subtle`; deprecated aliaser (`success`/`highlight`→`tip`, `warning`→`warn`) beholdt for bakoverkomp. Alle 38 førsteparts-`callout()`-kall migrert til kanoniske navn (tidligere blandet `warning` 21× / `warn` 4×, `highlight` 4× / `success` 3×). DESIGN_GUIDE §7-tabell + det utdaterte kode-eksemplet (feil signatur + gamle bokstav-badger) rettet. PRD FR-3.15-linje 177 om «emojis tillatt i callout-titler» rettet (motsa §1.7/ingen-emoji-regelen).
- **v0.35** – SVG-linjeikoner adoptert som ikon-språk (eier-beslutning, jf. Designsystem v1). Ny helper `svg_icon(name, *, size, color, stroke)` i `modules/shared/ui.py` med ikon-sett (`info`, `warn`, `success`, `tip`, `code`, `dbt`, `chart`). `callout()` rendrer nå et hvitt SVG-linjeikon i den fargede badgen i stedet for et bokstav-/tegn (`i`/`!`/`✓`/`·`) — alle callouts i appen arver endringen. DESIGN_GUIDE §1.7 endret fra «ingen emojis eller ikoner» → «ingen emojis, men SVG-linjeikoner er ikon-språket»; §7 oppdatert med ikon-navn + disc-eksempel. **Emojis er fortsatt aldri tillatt.** Funksjonskort-disker og knapp-ikoner kan bruke samme helper (ikke retro-fittet i eksisterende modul-innhold — det er Andres domene). Font-avviket (spec Libre Franklin/IBM Plex Mono vs app Arial) står fortsatt åpent/avventet.
- **v0.34** – Visuelt tema reskinnet fra mørkt (v2 «Snowflake dark») til **lyst «Bankbrief» (Designsystem v1)** — marine `#0A2C72` primær, hvit canvas, azur `#1F6FC4` lenker, fersken signaturflate, avledet fra PowerPoint-malen (ekstern `Designsystem.html`). Seks tema-bærende filer endret: `.streamlit/config.toml` (`base="light"`), `modules/shared/ui.py` (fargekonstanter `COLOR_*`/`TEXT_*`/`BORDER` + callout-palett — navn beholdt, kun verdier endret, så alle komponenter arver), `components/sidebar.py`, `pages_content/forside.py`, `modules/oppvarming/app_logic.py` (Likert-grid + skala-pille), og `KATEGORI_FARGE` i `data/moduler.py` (azur/violett/grønn/oransje/grå som leser på hvitt). Øvrige sider arver via delte helpers — ingen import/signatur brutt. DESIGN_GUIDE.md: konkrete fargeverdier (§0/§2/§5/§7/§9/§10/§11) oppdatert til lyse; banner lagt til. DESIGN_GUIDE er avstemt mot den autoritative `Designsystem.html`: §1.7 skjerpet til **ingen emojis** (tidligere «ingen emojis eller ikoner»). To avvik mot spec'en er flagget for eier og *ikke* endret: (1) **font** — spec'en bruker Libre Franklin + IBM Plex Mono (webfonter), appen beholder Arial (v0.32, bankenes skrifttype-policy); (2) **SVG-ikoner** — spec'en bruker dekorative linjeikoner, appen er i dag ren tekst.
- **v0.33** – Tre nye hands-on-moduler lagt til (FR-3.11, FR-3.12) + to placeholdere fylt med UTKAST-innhold. Nye: **Individuell oppgave: Plan Mode** (modul 11, kategori P) i Plan Mode-seksjonen rett etter konsept-modulen — deltaker skrur på Plan Mode på en kompleks oppgave og leser planen før utførelse; **Demo: Bundled skill (lineage)** (modul 18, kategori I) og **Individuell oppgave: Bundled skill** (modul 19, kategori P) i skills.md-seksjonen mellom `skills_md` og `gruppeoppgave_2` — demoen viser «forstå skill-en før bruk → anvend på levende objekt», oppgaven lar deltaker gjøre `@(serverSkill:lineage)`-mønsteret selv. Fylt: `individuell_oppgave_2` (metadata-sjekk av ukjent tabell) og `gruppeoppgave_2` (lag datakvalitets-skill via `skill-development`-workflow) — innhold drafted som UTKAST, merket for Andres verifisering. Modul 11–29 (agents_md … avslutning) renummerert til 12–32; 19 wrapper-filer under `pages_content/modules/` renamet + 3 nye lagt til; crumb/caption-numre oppdatert. CTA-kjede rekoblet: `plan_mode`→`individuell_oppgave_plan_mode`→`agents_md`, og `skills_md`→`demo_bundled_skill`→`individuell_oppgave_bundled_skill`→`gruppeoppgave_2`. Slugs og DB-tabeller uberørt; URL-er for de 19 flyttede modulene endret. (Merk: FR-3.8 og FR-3.10 beskriver fortsatt en utdatert arkitektur — `hub.py`/`st.navigation` og en gammel modul-liste — og bør bringes i sync separat.)
- **v0.32** – Font byttet fra Inter tilbake til **Arial gjennomgående** (`Arial, Helvetica, sans-serif`). `[[theme.fontFaces]]`-blokken som lastet Inter fra Google Fonts er fjernet fra `.streamlit/config.toml`; `viz.py` Plotly-font og DESIGN_GUIDE §0/§3/§9/§10/§11 oppdatert. Ingen webfont-lasting lenger — Arial er forhåndsinstallert og samsvarer med bankenes skrifttype-policy.
- **v0.31** – Alle emojis/ikoner fjernet fra appen (overskrifter, `st.subheader`, `st.expander`-labels, callout-titler, crumbs, md-headere). Eneste tillatte ikon er den kvadratiske callout-badgen (`i`/`!`/`✓`/`·`). Ny designregel: DESIGN_GUIDE §1.7 + §7. ~45 filer berørt.
- **v0.30** – Seksjonen `Komme i gang` flyttet til rett etter `Introduksjon` (foran `@-mentions` og `Plan Mode`). Ny seksjonsrekkefølge: Introduksjon → Komme i gang → @-mentions → Plan Mode → AGENTS.md → … Modul 5–10 renummerert tilsvarende (arkitektur=5, demo_1=6, individuell_oppgave_1=7, at_mentions=8, individuell_oppgave_at_mentions=9, plan_mode=10); seks wrapper-filer under `pages_content/modules/` renamet og crumb/caption-numre oppdatert. «Fortsett →»-CTA-kjeden rekoblet til ny rekkefølge: `cortex_in_snowsight`→`arkitektur`, `individuell_oppgave_1`→`at_mentions`, `plan_mode`→`agents_md`. Slugs og DB-tabeller uberørt; URL-er for de seks flyttede modulene endret.
- **v0.29** – Plan Mode lagt til som ny konsept-modul (FR-3.11, FR-3.12), egen seksjon mellom `@-mentions` og `Komme i gang`. Plassert som modul 7 (kategori I) etter ønske om tidlig introduksjon av den trygge read-only-kjøremodusen. Innhold (tre kjøremoduser, aktivering, livssyklus, bruksområder) levert av Andre (HTML-utkast). Modul 7–28 (arkitektur … avslutning) renummerert til 8–29; 22 wrapper-filer under `pages_content/modules/` renamet og crumb/caption-numre oppdatert. `individuell_oppgave_at_mentions`-CTA peker nå til `plan_mode` (som igjen peker til `arkitektur`). URL-er for de 22 flyttede modulene endret; slugs og DB-tabeller uberørt. (Skills-modulen fra v0.28 er nå modul 16.)
- **v0.28** – Modul 15 (skills.md) fylt med innhold (FR-3.11, FR-3.12): Cortex Codes skill-mekanisme i åtte seksjoner (hva en skill er + fire-delt anatomi, SKILL.md, bundled vs. custom, plassering/presedens, når lage en, forstå før bruk, lage en ny, beste praksis). Innhold levert av Andre (HTML-utkast), ikke AI-fabrikkert. Ny gjenbrukbar helper `numbered_steps()` i `modules/shared/ui.py` (DESIGN_GUIDE v2 §4) for nummererte "1, 2, 3"-badge-bokser. Modulnummer, slug og URL uendret.
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
