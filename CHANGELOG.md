# CHANGELOG

Referert av [DESIGN_GUIDE.md](DESIGN_GUIDE.md) — oppdateres ved hver design- eller modul-endring.

For detaljerte krav-endringer, se PRD.md §8.

---

## 2026-06-02 - «Under panseret» til Introduksjon, slettet «Cortex Code i Snowsight», full renummerering 1..31

- **«Arkitekturoversikt» flyttet** fra «Komme i gang» til **«Introduksjon»**, nå **nr 4** (etter «Snowsight vs CLI»).
- **Fanen omdøpt** «Arkitekturoversikt» → **«Under panseret»** (kun visningsnavn - MODULER-tittel, `module_header`, crumb; slug `arkitektur` uendret). Innholdet er agentens indre (fem lag + «spør agenten om seg selv»-demoen), så navnet er mer inviterende.
- **«Cortex Code i Snowsight» (`cortex_in_snowsight`) slettet** - var en tom placeholder. Modul-mappe, wrapper, MODULER- og SECTIONS-oppføring fjernet. `cortex_interaction`-CTA peker nå til `arkitektur` (var → cortex_in_snowsight).
- **Full sekvensiell renummerering til 1..31** (lukket også pre-eksisterende hull 27/29/31/33 i halen): 28 wrapper-filer renamet + crumb-nr oppdatert i hver berørte modul. CTA-kjeden er slug-basert og tålte renummereringen.
- **Komme i gang** er nå: Første demo (05), Individuell oppgave 1 (06), Kostnader (07).
- Verifisert: py_compile, konsistens (1..31 uten hull, alle wrappers finnes, hver modul i én seksjon), 0 `cortex_in_snowsight`-referanser, AppTest på berørte sider = 0 feil.

---

## 2026-06-02 - Evolusjon (modul 1): xkcd-tegneserie under epoke-kortene + analytiker-ramme + titler «I dag»/«Fremover»

- Lagt inn tegneserien «Vibe coding vs Agentic SDLC» under epoke-kortene, i stedet for den gamle «Bilde fra Snowflake settes inn her»-placeholderen (som er fjernet) - bildet passer bedre rett under før/i dag/fremover. Bildefil: `modules/evolusjon/content/vibe_vs_agentic_sdlc.png` (Andre la den inn).
- Ny helper `_image_or_placeholder` i `modules/evolusjon/app_logic.py` (speiler den i `cortex_interaction`): `st.image(..., width="stretch")` hvis fila finnes, ellers stiplet placeholder.
- **Analytiker-ramme:** ny `content/bilde_ramme.md` (UTKAST) vist som `st.caption` under bildet. Oversetter kontrasten (vibe vs rammer/kontroll + rolleskifte) til analytiker-/bank-språk og demper tech-bro-hypen - bildet er tungt SE-/hype-rammet, jf. CLAUDE.md «unngå tech-bro». Kobler guardrails til regulert data-hverdag.
- Epoke-titler endret: «Nå» -> «I dag», «Snart» -> «Fremover» (`epoke_2_naa.md` / `epoke_3_snart.md`).
- Ingen ny FR/NFR (content/layout i §FR-3.11/§FR-3.12). Ingen emoji/em-dash/`é`. Verifisert: py_compile + AppTest (m01): 1 bilde + bildetekst rendres, 0 feil.

---

## 2026-06-02 - Bli kjent: 4 nye påstander (11 -> 15)

- **Nye Q12-15** i "Bli kjent" (oppvarming) om agent-konfigurasjon: verktøy agenten har tilgjengelig, skills, hvordan lage personlige skills, og system prompt. Lagt til i `STATEMENTS` i `modules/oppvarming/config.py`.
- **Database:** CHECK-constraint i `modules/oppvarming/supabase_schema.sql` utvidet til `question_id between 1 and 15`. Må re-kjøres manuelt i Supabase SQL Editor (drop+recreate, nullstiller eksisterende svar - greit pre-kurs).
- Ingen Python-logikk endret (app_logic/db/views/resultater er generiske og looper over `STATEMENTS`). PRD §FR-3.14 oppdatert til 15 påstander (rettet samtidig en eksisterende 10/11-drift) + §8 v0.48. Verifisert: py_compile + struktur (15 nøkler 1-15) + smoke-import.

---

## 2026-06-02 - Cortex Code (modul 2): tre oversiktsseksjoner lagt til

Tre nye seksjoner øverst på siden (eier-innhold, additivt over den eksisterende «decode sitatet»-delen):

- **Hva er Cortex Code?** - AI-kodeagent, integrert i Snowflake, forstår roller/schemaer/beste praksis, aktivt workspace som kontekst (oversatt fra eierens engelske kladd til norsk).
- **Hvorfor bruke Cortex Code?** - resultater = prompts pluss data; fordelen kommer fra kontekst i miljø og data, derfor ikke et eksternt verktøy.
- **Hvordan kan vi bruke det?** - Streamlit-dashbord, SQL-spørringer, maskinlæring (utenfor scope), notebook-analyse.

Tre nye `content/`-filer (`hva_er`/`hvorfor`/`hvordan`) + tre `st.subheader`-seksjoner i `app_logic.py`. Eksisterende innhold (sitat, lytteklipp, begrep-expandere, oppsummering, eksempel) urørt. PRD §8 v0.50. Verifisert: AppTest (m02), 0 feil.

---

## 2026-06-02 - Snowsight vs CLI (modul 3): skjermbilder lagt inn

De to skjermbildene la inn i `modules/cortex_interaction/content/`: `snowsight.png` (Snowsight web-UI med Cortex Code-panel) og `cli.png` (Cortex Code v1.0.35 i terminal). `_image_or_placeholder`-helperen (fra v0.46) viser dem nå automatisk via `st.image`, så de stiplete placeholderne er borte. Ingen kodeendring. PRD §8 v0.49. Verifisert: AppTest (m03) viser 2 bilder, 0 feil.

---

## 2026-06-02 - Cortex Code (modul 2): ryddet layout

Tre justeringer etter eier-tilbakemelding (kun `modules/cortex_code/app_logic.py`, content urørt):

- Fjernet caption «La oss pakke ut hva som faktisk står her.» under dokumentasjons-callouten.
- Fjernet «Vis alle forklaringer»-toggle. Begrep-expanderne er nå alltid kollapset (`expanded=False`); brukeren klikker frem ett og ett.
- Flyttet «Lytteklipp: Snowflake RBAC» opp til rett under dokumentasjons-callouten (over «Begrep for begrep»).

PRD §8 v0.48. Verifisert: py_compile + AppTest (m02), 0 feil.

---

## 2026-06-01 - Oppgave-opprydding: slettet 4 oppgaver, konkurrent -> gruppeoppgave

- **Slettet** tre individuelle oppgaver (`individuell_oppgave_3`/`_4`/`_5`) og `individuell_oppgave_kurs_kunde` (dupliserte lineage-temaet som dekkes tidligere): mapper under `modules/` + wrappere `m27/m29/m31/m33_*` fjernet.
- **Konkurrent -> gruppeoppgave:** `individuell_oppgave_konkurrent` (nr 34) endret fra `kategori` P til G og tittel «Individuell oppgave: Konkurrent-signaler» -> «Gruppeoppgave: Konkurrent-signaler» (oransje «Gruppe»-prikk i sidebar). Slug/mappe/wrapper uendret; gruppe-innramming i content skriver Andre selv.
- **Ingen renummerering:** nr 27/29/31/33 står som hull (trygt - `find_by_page_id` matcher eksakt nr). 3 CTA-er rekoblet forbi de slettede (`individuell_oppgave_2`->`demo_2`, `autonomous_loop`->`individuell_oppgave_kohort`, `individuell_oppgave_kohort`->`individuell_oppgave_konkurrent`). SECTIONS trimmet.
- Oppdatert `data/moduler.py`, README, CONTENT_REVIEW, `scripts/lag_kursoversikt_xlsx.py`, PRD §8 (v0.47). Ingen ny/slettet FR/NFR. Kurset har nå 32 moduler. Verifisert: py_compile + wrapper-integritet (32 wrappere, 0 orphans), 0 døde referanser.

---

## 2026-06-01 - Snowsight vs CLI (modul 3): bilder + doc-lenke, fjernet fordeler/ulemper/når

Etter eier-tilbakemelding (informasjonen var ikke korrekt):

- **Fjernet** fordeler/ulemper/«når passer den best» for begge flater + «velg»-takeaway. Slettet content-filene `snowsight_card.md`, `cli_card.md`, `closing.md`.
- **Bilder i stedet for tekst:** to kolonner viser nå skjermbilde av Snowsight og CLI via `st.image` (ny `_image_or_placeholder`-helper, samme mønster som Evolusjon). Bildefilene legges i `modules/cortex_interaction/content/` som `snowsight.png` og `cli.png`; inntil de finnes vises en stiplet placeholder-boks.
- **Doc-lenke:** ny `content/cli_docs.md` lenker til offisiell Snowflake-dokumentasjon (`https://docs.snowflake.com/en/user-guide/cortex-code/cortex-code-cli`).
- `intro.md` beholdt. Ingen ny FR/NFR (content/layout i eksisterende §FR-3.11/§FR-3.12-modul). Ingen emoji/em-dash/`é`. Verifisert: py_compile + AppTest (m03), 0 feil; doc-lenke vises, fordeler/ulemper borte, placeholder vises.

---

## 2026-06-01 - Evolusjon reframet: Før / Nå / Snart + Snowflake-bilde + ny refleksjon

Evolusjon (modul 1) oppdatert med Andres innhold.

- **Undertittel:** «Tre epoker i hvordan vi skriver kode» -> «... kode og gjør analyser».
- **Epoke-kort:** «Era 1/2/3» -> **Før / Nå / Snart** med ny brødtekst. Content-filer omdøpt: `era_1_googling`->`epoke_1_for`, `era_2_assistanse`->`epoke_2_naa`, `era_3_spesifikasjon`->`epoke_3_snart` (ERA_FILES oppdatert).
- **Snowflake-bilde:** lagt til etter kortene som en merket placeholder-boks (dashed border). Andre bytter den ut med `st.image(...)` når bildefila er på plass.
- **Refleksjon:** ny callout «Tenk igjennom: Hva krever dette av løsninger rundt oss?» (`content/losninger_rundt_oss.md`) erstatter «Hvor er du i dag?». Rolle-spørsmålet beholdt. `hvor_er_du.md` nå ubrukt (beholdt).
- Ingen emoji/em-dash/en-dash/`é`. PRD §8 v0.45. Verifisert: py_compile + AppTest (m01), 0 feil.

---

## 2026-05-31 - «Kostnader» flyttet til «Komme i gang» + redusert til PowerPoint-peker

«Kostnader» er flyttet fra slutten av kurset (gammel nr 34) til seksjonen «Komme i gang», rett etter Individuell oppgave 1, og innholdet er redusert til en ren peker. Siden sier nå kun «Gjennomgang i PowerPoint» (resten tas i plenum).

- **Full renummerering:** kostnader ble nr 08; modulene som var 08-33 ble skjøvet +1 (til 09-34); Avslutning/Test beholdt 35/36.
- **Filer:** 27 wrapper-filer i `pages_content/modules/` flyttet (mNN_*), 26 crumb-numre i `modules/*/app_logic.py` justert, `data/moduler.py` (MODULER-nr + SECTIONS: `m08_kostnader` inn i `komme_i_gang`, ut av `avslutning`).
- **CTA-er rekoblet:** `individuell_oppgave_1` -> `kostnader`, `kostnader` -> `at_mentions`, `individuell_oppgave_konkurrent` -> `avslutning` (slug-baserte, så nummer i CTA-kortet auto-utledes).
- **`kostnader/app_logic.py`** strippet til crumb + header + info-callout «Gjennomgang i PowerPoint» + CTA. `kostnader/content/*.md` er nå ubrukt (beholdt, ikke slettet).
- **`scripts/lag_kursoversikt_xlsx.py`** reordnet/renummerert tilsvarende.
- **URL-er:** `?page=mNN_...` for de skjøvne modulene endret. Ingen DB-tabeller berørt.
- PRD §8 v0.44. Verifisert: py_compile + AppTest alle 36 sider, crumb-nr == MODULER-nr, 0 feil.

---

## 2026-05-31 - Ny designregel: ingen «é»-bokstav

Ny typografiregel (eier-beslutning), parallell til §1.7 (emoji) og §1.8 (em-/en-dash): bokstaven `é` (U+00E9) og `É` (U+00C9) skal aldri brukes - bruk alltid vanlig `e`/`E`. Vanligste tilfellet er ordet for tallet 1, som skrives «en» uten aksent.

- Lagt til som **DESIGN_GUIDE §1.10** + bullet i CLAUDE.md «Kort sammendrag».
- Authority-filenes egne forekomster ryddet samtidig: DESIGN_GUIDE (5, bl.a. «én tydelig idé» i §1.9) og CLAUDE.md (6, bl.a. «renummerér», «generér»).
- **Retroaktiv sweep utført (eier-godkjent):** alle forekomster i app-/innholds-/kodefiler ryddet (`é`→`e`, `É`→`E`) via `perl -CSD` over working-tree `.py`/`.md`. Alt var prosa/docstrings/kommentarer/visningstekst - ingen load-bearing dataliteraler. Working tree er nå `é`-fri bortsett fra de fire doc-filene: DESIGN_GUIDE.md/CLAUDE.md (kun selve regel-definisjonens `é`/`É`-tegn i backticks) og historiske CHANGELOG.md/PRD.md-entries (append-only records, holdt utenfor). `theme-light/` (untracked) urørt. Verifisert: 142 `.py` py_compile OK, AppTest på m25/m22/m05 rendrer uten feil.

Fylte modul 16 fra placeholder til en hands-on der deltakeren kjører samme prompt to ganger - én gang med Sonnet, én gang med Opus - og sammenligner. To oppgaver av ulik vanskegrad (drafted på eksplisitt forespørsel fra Andre; innholds-unntaket i CLAUDE.md).

**Endringer:**
- `app_logic.py`: utvidet fra én oppgave til to oppgave-seksjoner + "Slik gjør du" + "Hva du skal sammenligne". Docstring rettet (modul 14 -> 16, wrapper-sti m11 -> m16).
- `content/`: `oppgave.md` (ramme), `steg.md` (5 steg: velg modell, @-mention tabeller, lagre, bytt, sammenlign), nye `oppgave_1.md` (topp 10 % kunder per segment - prompt verbatim fra Andre) og `oppgave_2.md` (kundefrafall per segment - anti-join + to tidsvinduer, der Opus skal skille seg), `forventet.md` (5 sammenlignings-dimensjoner + refleksjon).
- Promptene referer `@KURS_KUNDE` / `@KURS_TRANSAKSJON`. Ingen ferdig SQL-fasit (unngår fabrikkering).

**Guardrails:** generiske/fiktive bank-eksempler (kundefrafall, segment), ingen PII, ingen emoji/en-dash/em-dash. Verifisert: AppTest 0 exceptions, fire subheaders + begge prompt-blokker rendrer.

**Forbehold (Andre bekrefter):** tabellnavn-konvensjon og eksakt modellbytte-mekanikk i Cortex Code.

---

## 2026-05-31 — Varmere epoke-kort på Evolusjon (ny `signature_card`)

De tre epoke-kortene på Evolusjon (modul 1) leste som «kalde» (hvit `card()`, tynn grå kant, ingen aksent). Byttet til designsystemets varme signaturflate.

- Ny helper **`signature_card(number=None)`** i `modules/shared/ui.py` (context manager): fersken-flate `#F8E6D5` + azur venstrekant `#1F6FC4` + valgfritt marine nummer-badge. Samme varme språk som `feature_hero`, men innhold rendres via `st.markdown` i `with`-blokken så markdown (kursiv) bevares.
- `modules/evolusjon/app_logic.py`: epoke-kortene bruker nå `signature_card(number=1/2/3)` i stedet for `card()`. Innhold urørt.
- DESIGN_GUIDE §8 oppdatert (funksjonskort-listen + «velg flate bevisst»-note). PRD §8 v0.42.
- Verifisert: py_compile + AppTest (m01), 0 feil.

---

## 2026-05-31 — Modul 24 omdøpt: «Prompt engineering» → «Context engineering»

Etter eier-avklaring (B1): modulens egentlige tema er *context engineering* (hvordan gi agenten riktig kontekst), ikke prompt engineering. Strukturell omdøping av identitet utført; **innholdsreframing gjenstår for Andre**.

- `git mv modules/prompt_engineering → modules/context_engineering`; `git mv pages_content/modules/m24_prompt_engineering.py → m24_context_engineering.py` (import oppdatert).
- `data/moduler.py`: MODULER slug `prompt_engineering`→`context_engineering`, tittel `Prompt engineering`→`Context engineering`; SECTIONS-seksjon id/label/page_id tilsvarende.
- `app_logic.py`: docstring, crumb og H1-fallback → «Context engineering». `intro.md` H1 → «# Context engineering». CTA rekoblet: `gruppeoppgave_3_resultater` → `next_module_cta_for("context_engineering")`. `scripts/lag_kursoversikt_xlsx.py` rad 24 oppdatert.
- **URL endret:** `?page=m24_prompt_engineering` → `?page=m24_context_engineering`. Ingen DB-tabeller berørt. `theme-light/` (untracked variant) urørt.
- **Gjenstår for Andre (innhold, ikke utført):** subtitle «...av prompts», expander-labels («Anatomi av en god prompt», «AGENTS.md vs skills.md vs inline prompt») og .md-innholdet er fortsatt prompt-rammet og må reframes til kontekst-vinkelen.
- Verifisert: `py_compile` OK, `find_by_page_id`/`section_for_page` konsistent, Streamlit AppTest rendrer uten exception, ingen «Prompt engineering» igjen i sidetekst. PRD §8 v0.41.

---

## 2026-05-31 — Modul 15: ny grunnlagsseksjon «Hva er en LLM»

Modul 15 (`tilgjengelige_modeller`) fikk en kort grunnlagsseksjon **«Hva er en LLM»** øverst, etter intro-hooken og før Oversikt-tabellen. Den definerer LLM (Large Language Model), next-token-prediksjon, parametere/datamengde, multimodalitet, plasserer Opus/Sonnet/Haiku som LLM-er fra Anthropic, og forklarer skillet mellom modellen som «tenker» og agenten (Cortex Code = modell + verktøy + loop). Dette begrepet var tidligere bare antydet i `arkitektur` (modul 5), aldri sagt rett ut.

- Ny `modules/tilgjengelige_modeller/content/hva_er_llm.md` (Andres egne ord, kun formatert - ingen UTKAST-markør).
- `app_logic.py`: én ny `st.subheader("Hva er en LLM")` + `load_markdown`-seksjon mellom intro og Oversikt. Ingen nye imports.
- Ingen emojis (§1.7) / em-dash (§1.8). PRD §8 v0.40.

---

## 2026-05-31 — Pedagogisk gjennomgang «forklart før brukt» + to framoverpekere

Gjennomgang av hele kursløpet (36 moduler i seksjonsrekkefølge) med ett spørsmål: introduseres begreper før de anvendes? De fleste kjernebegrepene er riktig sekvensert (system-prompt m05→m12, @-mentions m08, Plan Mode m10, modeller m15, memory m21). Funn og nøyaktige anbefalinger ligger i plan-fila; kun de to trygge navigasjons-grepene er utført her:

- **`demo_1/content/demo_3_bokstav.md`** (m06): AGENTS.md brukes som demo-poeng 6 moduler før den læres (m12). Lagt til framoverpeker: «Vi går grundig gjennom AGENTS.md i en egen modul senere i kurset».
- **`plan_mode/content/kobling.md`** (m10): omtaler «bundled skill» før skills læres (m17). Lagt til framoverpeker: «Skills får sin egen modul senere».

**Anbefalt, ikke utført (krever Andres prosa/beslutning):** prompt-grunnlag før første oppgave (prompt engineering ligger i m24, men prompts skrives fra m06/m07); definer `token`/`kontekstvindu` tidlig (brukes i m34-placeholder); gloss for `kohortanalyse`, `lineage`, `dbt`/`RBAC`/`Streamlit`; bro fra katalog-`@` til `@(serverSkill:…)`. Ingen omrokering i `data/moduler.py` (vurdert, men framoverpeker + tidlig primer er mindre invasivt).

**Oppfølging (eier-godkjente glosser, UTKAST - Andre verifiserer):** Etter avklaring fra Andre lagt inn korte begrepsglosser (generisk/konseptuell tekst, ingen produktspesifikke påstander):
- `tilgjengelige_modeller/content/hva_er_llm.md` (m15): la til **token**-kostnadsvinkel + **kontekstvindu** som to punkter i «Hva er en LLM»-lista (token var alt definert der). Flyttet hit etter eier-ønske (lå først i `intro.md`).
- `individuell_oppgave_kohort/oppgave.md` (m31): kort gloss på **kohortanalyse** + **Streamlit** i innledningen til oppgaven.
- `at_mentions/what_agent_sees.md` (m08): parentes-gloss på **lineage** ved første forekomst.
- `skills_md/intro.md` (m17): brosetning fra katalog-`@` (m08) til `@(serverSkill:…)`.
- `arkitektur/oppgavestyring.md` (m05): parentes-gloss på **dbt** ved første substansielle bruk.
- **RBAC** trengte ingen gloss - allerede utvidet («Role-Based Access Control (RBAC)») i `cortex_code/quote.md`.
- **B1 omdefinert:** temaet er *context engineering* (ikke prompt engineering); tidlige øvelser er bevisst uavhengige av dette, så det er ikke et rekkefølge-avvik. Modul 24 omdøpt (se egen toppseksjon).

---

## 2026-05-31 — Design-konformitets-audit + remediering av trygge avvik

Gjennomgang av DESIGN_GUIDE mot faktiske sidevisninger (statisk audit av 36 moduler + delte komponenter + faste sider). Appen var stort sett konform (0 emoji i sidetekst, 0 em-dash i innhold, Arial gjennomgående, ingen mørke canvas-rester, ingen `st.bar_chart`/`st.info`/`st.balloons`, ingen deprecated callout-kinds). De trygge avvikene er nå rettet:

- **`#0B5BB5`** (en tredje, off-palett blåfarge brukt som hovedaksent) → azur `#1F6FC4` i `components/sidebar.py`, `pages_content/forside.py`, `modules/shared/ui.py` (feature_hero/feature_card), `modules/oppvarming/app_logic.py`.
- **`gruppeoppgave_2`** manglet `crumb` + `next_module_cta` (alle andre moduler har begge) → lagt til `crumb` + `next_module_cta_for("memory_md")`.
- **DESIGN_GUIDE** rettet for intern motsigelse/drift: §6+§9 beskriver nå den faktiske custom-sidebaren (ikke `st.navigation()`, jf. §11); §0 fjernet døde referanser til `Designsystem.html`/`design_preview.html` (eksterne, ligger ikke i repoet); §10-sjekklista callout-typer → info/tip/warn; §11 modultall gjort tallfritt.

**Eier-beslutninger (2026-05-31):**
- `test_skills_html` (modul 36): **beholdes som sandbox** i «Test»-nav (isolert i iframe, CSS lekker ikke). Sanksjonert unntak fra stilreglene; kun stale docstring-ref (`m33`→`m36`) rettet.
- Favicon `page_icon="❄"`: **beholdes** som fane-branding (sanksjonert emoji-unntak; fane-metadata, ikke side-innhold).
- §1.8 utvidet til også å forby **en-dash (`–`)**; appen renset (1 forekomst i `data/moduler.py`-docstring).

---

## 2026-05-31 — Modul 15 (Tilgjengelige modeller): innhold om Opus vs Sonnet (UTKAST)

Modul 15 gikk fra fire tomme placeholder-content-filer til en forklaring av forskjellen mellom **Opus** og **Sonnet** i Cortex Code. Drafted som UTKAST på eksplisitt forespørsel fra Andre (innholds-unntaket i CLAUDE.md).

**Endringer (kun `modules/tilgjengelige_modeller/content/`, app_logic urørt):**
- `intro.md`: Cortex Code kjører på Claude; modellvalget er kapabilitet vs. fart/kost.
- `oversikt.md`: markdown-sammenligningstabell Opus vs Sonnet (kapabilitet, hastighet, kostnad, passer til); Haiku nevnt i én linje.
- `valg.md`: Sonnet som standard; Opus når kompleksitet/risiko rettferdiggjør kostnaden (gjerne med Plan Mode); tommelfingerregel.
- `eksempel.md`: én generisk/fiktiv bank-kontrast (rask SQL for kundeID 123 = Sonnet; fler-stegs refaktorering av rapporterings-pipeline = Opus).

**Guardrails:** konseptuelt (ingen fabrikkerte modellnavn/versjoner/priser eller påstander om Cortex Codes velger), bank-rammet, generiske eksempler, ingen emojis (§1.7), ingen em-dash (§1.8). Alt merket UTKAST. Andre legger inn eksakte produktspesifikke modellnavn selv. Verifisert: AppTest av siden, 0 feil; tabellen rendrer.

**Ikke tatt nå:** hands-on-oppgaven (modul 16 `individuell_oppgave_modellvalg`) er fortsatt placeholder.

---

## 2026-05-31 — Innholds- og regelrunde fra eier (em-dash, PowerPoint-altitude, modul-endringer)

**Nye globale regler (DESIGN_GUIDE §1):**
- §1.8 **Ingen em-dash (`—`).** Fjernet fra hele appen - 108 filer, 207 forekomster - erstattet med vanlig bindestrek `-`. Markdown-skillelinjer (`---`) og en-dash (`–`) er ikke rørt.
- §1.9 **PowerPoint-nært.** Hver modul-side leses som ett/få lysbilder: én idé per skjerm, luftig typografi, korte punkter. Presentatør-metainnhold (snakkepunkter, forventet varighet) hører ikke hjemme på sidene.

**Snakkepunkter + varighet fjernet:**
- `demo_1`, `demo_2`, `demo_bundled_skill`: fjernet «Vis snakkepunkter»-toggle + runbook-caption; segmentene vises nå alltid. `## Snakkepunkter`-seksjoner fjernet fra innhold.
- `individuell_oppgave_5`: fjernet «Snakkepunkter (for presentatør)»-seksjonen (+ slettet `notater.md`).

**Modul-endringer:**
- **Evolusjon** (modul 1): omdøpt fra «Fra Google til spesifikasjon». Tre innholdsblokker fra Andre (intro-setning, «hvor er du i dag»-refleksjon, diskusjonsspørsmålet «Når AI implementerer, hva blir da vår rolle?»).
- **Bli kjent**: intro endret til «Hvilke forkunnskaper har vi? Helt anonymt». (Ingen Likert-utsagn om skills/mcp/systemkontekst funnet - flagget for Andre.)
- **Resultater fra Bli kjent** (tidl. «Resultater fra Oppvarming»): fjernet auto-refresh + live-aggregerings-undertekst; kun «Refresh nå»-knapp. Gruppeoppgave-resultatsidene beholder live-aggregering (ikke berørt).
- **Første demo**: redesignet slide-likt. Agenda med kostnadsdashbord til sist; workspace-segment med rolle + metadata; Cortex Code-segment med to prompts; bokstavspørsmålet («Hvilken bokstav kommer etter 'b'?») som AGENTS.md-teaser. Fjernet toggle/varighet og `avklaring.md`.
- **Individuell oppgave 1**: nytt steg #1 «Åpne Workspaces».
- **Snowsight vs CLI**: forenklet betydelig - intro + to kort + takeaway. Fjernet duplikat «Hva velger du?»-seksjon og sammenligningstabell (+ slettet `comparison_table.md`/`when_snowsight.md`/`when_cli.md`).

**Merk:** ingen PowerPoint-skill er tilgjengelig i miljøet; «PowerPoint-nært» er kodet som designprinsipp, ikke generert via skill.

---

## 2026-05-31 — Designsystem v1-komponenter: modul-hero, funksjonskort, knapper (gap mot Designsystem.html lukket)

Etter en gap-analyse (Designsystem.html-target vs app) ble de manglende komponentene bygget og rullet ut. Største synlige løft: modul-sidene har nå en ekte **hero-header** (azur eyebrow + tung marine display-H1 + azur undertittel) i stedet for grå `st.title` + `st.caption`.

**Nye helpere i `modules/shared/ui.py`:**
- `module_header(title, *, subtitle, eyebrow="For analytikere i bank")` — modul-hero.
- `feature_hero(title, items, *, icon)` — fersken signaturkort, 52px marine disc + prikkliste.
- `feature_card(title, body, *, icon)` — hvitt kort, 40px disc + brødtekst.
- `dotlist(items)` — frittstående marine prikkliste.
- `inject_global_css()` — globale knapper (marine primær/form-submit, radius 7px, hover marine-dyp; hvit-marine sekundær) + azur-tint inline-kode. Kalt én gang fra `app.py`.

**Andre endringer:**
- `card()` og `metric_card()` fikk `SHADOW_1` (subtil løft) — matcher `feature_card`/forside.
- Sidebar: fast bredde 280px + `border-right` mot innholdet.
- **`module_header()` rullet ut på alle 34 moduler** (via migrasjons-workflow, én agent per modul + per-modul AppTest): `st.title()` + `st.caption("Modul N · …")` → `module_header(...)`. Interaktive gate-skjermer (deltakerkode) beholder `st.title()`.
- Fjernet død `render_module_header()` (pekte på gamle `hub.py`).
- `DESIGN_GUIDE.md` §8 oppdatert med module_header-mønster + funksjonskort-helpere.

**Verifisert:** 36 sider (alle moduler + faste sider) AppTest-et sentralt — 0 exceptions; 19 sider rendrer SVG-ikoner.

**Åpent / flagget:** ① **font** — Designsystem v1 vil ha Libre Franklin 900 (display); appen bruker Arial (maks 700), så H1 er en *tilnærming* til spec-vekten inntil font-spørsmålet avgjøres. ② **funksjonskort-innhold per modul** (f.eks. cortex_in_snowsight slik mockupen viser) er Andres innholds-domene — `feature_hero`/`feature_card`-helperne er klare til bruk.

---

## 2026-05-31 — Callout-typer standardisert til INFO / TIPS / ADVARSEL

Callout-typene er nå justert til Designsystemets trio (INFO / TIPS / ADVARSEL), pluss en dempet `subtle` for tomme tilstander.

**Hvorfor:** Koden hadde 4 typer + 2 alias-navn, og halvparten av kallene brukte legacy-aliaser (`warning` 21× vs `warn` 4×, `highlight`/`success` om hverandre). Den grønne typen het «success» med sjekkmerke, mens spec'en viser «Tips» med lyspære. Andre ville ha én standardisert modell som matcher Designsystemet.

**Endringer:**
- `modules/shared/ui.py`: den grønne callout-typen omdøpt fra `success` (sjekkmerke) til **`tip`** (lyspære-ikonet, som allerede fantes i `_SVG_ICONS` men var ukoblet). Kanoniske `kind`-navn: `info` / `tip` / `warn` / `subtle`. Deprecated aliaser (`success`/`highlight`→`tip`, `warning`→`warn`) beholdt for bakoverkomp; docstring oppdatert.
- Migrert alle 38 førsteparts-`callout()`-kall til kanoniske navn (12 filer).
- `DESIGN_GUIDE.md` §7: tabell oppdatert (Info/Tips/Advarsel + subtle-rad), og det utdaterte kode-eksemplet (feil signatur `callout(kind, title, content)` + gamle bokstav-badger `i`/`!`/`✓`) byttet til faktisk `callout(body, *, kind, title, key)`-bruk.
- `PRD.md` FR-3.15: kinds-listen oppdatert; linja som sa «emojis tillatt i callout-titler» rettet (motsa §1.7).

**Callout-typer i appen nå:** `info` (marine, fakta) · `tip` (grønn, råd/anbefaling) · `warn` (amber, risiko) · `subtle` (grå, empty-states).

---

## 2026-05-31 — SVG-linjeikoner adoptert (callouts m.m.) — fortsatt ingen emojis

Eier-beslutning: appen bruker nå **SVG-linjeikoner** fra Designsystem v1 som ikon-språk, i stedet for tekst-glyfer. Emojis er fortsatt aldri tillatt.

**Endringer:**
- Ny helper `svg_icon(name, *, size, color, stroke)` i `modules/shared/ui.py` + ikon-sett (`info`, `warn`, `success`, `tip`, `code`, `dbt`, `chart`). 24×24 viewBox, `stroke=currentColor`.
- `callout()` rendrer nå et hvitt SVG-linjeikon i den fargede badgen (28×28, radius 7px) i stedet for bokstav-/tegn (`i`/`!`/`✓`/`·`). Alle callouts i appen arver via den delte helperen.
- `DESIGN_GUIDE.md`: §1.7 «ingen emojis eller ikoner» → **«ingen emojis, men SVG-linjeikoner er ikon-språket»**; §7 oppdatert med ikon-navn + disc-eksempel; banner-flagget for ikoner løst.
- Funksjonskort-disker/knapp-ikoner kan bruke samme helper, men er ikke retro-fittet i eksisterende modul-innhold (Andres domene).

**Åpent:** font-avviket (Designsystem v1 = Libre Franklin/IBM Plex Mono, app = Arial pr. bankpolicy) avventer eier-beslutning.

---

## 2026-05-31 — Visuelt tema reskinnet til lyst «Bankbrief» (Designsystem v1)

Appen byttet fra det mørke v2-temaet (nær-svart canvas, Snowflake-aksenter) til et **lyst** marine + fersken-uttrykk avledet fra PowerPoint-malen: hvit canvas, marine `#0A2C72` primær, azur `#1F6FC4` lenker. Full token-mapping i [`theme-light/THEME_PATCH.md`](theme-light/THEME_PATCH.md); full spec i ekstern `Designsystem.html`.

**Hvorfor:** Lyst tema leser renere på projektor i kursrom og gir et nøkternt, bank-passende preg. Avledet fra kundens egen PowerPoint-mal.

**Endringer (6 tema-bærende filer):**
- `.streamlit/config.toml` — `base="light"`, marine primær, hvit canvas, azur lenker, lys sidebar.
- `modules/shared/ui.py` — fargekonstantene (`COLOR_*`, `TEXT_*`, `BORDER`) + callout-paletten reskinnet. **Konstantnavn beholdt, kun verdier endret** — alle komponenter (`callout`, `card`, `metric_card`, `numbered_steps`, `crumb`, `next_module_cta`) arver automatisk; ingen import eller signatur brutt.
- `components/sidebar.py` — lys sidebar, azur aktiv-tint + strek.
- `pages_content/forside.py` — hvite kort med azur venstrestrek + subtil skygge.
- `modules/oppvarming/app_logic.py` — Likert-grid + skala-pille reskinnet (eneste innholdsside med hardkodet mørk CSS).
- `data/moduler.py` — `KATEGORI_FARGE` til mettede farger som leser på hvitt (azur/violett/grønn/oransje/grå). MODULER/SECTIONS uberørt.
- `DESIGN_GUIDE.md` — konkrete fargeverdier (§0/§2/§5/§7/§9/§10/§11) oppdatert + banner. Avstemt mot autoritativ `Designsystem.html`; §1.7 skjerpet til **ingen emojis** (var «ingen emojis eller ikoner»). Flagget, ikke endret: font (spec Libre Franklin/IBM Plex Mono vs app Arial pr. bankpolicy) og dekorative SVG-ikoner (spec bruker dem, appen er ren tekst).

Øvrige sider (`bli_kjent`, `resultater`, `admin`, alle `mNN_*`-wrappere) bruker `st`-native + delte helpers og arver temaet uten egne endringer. Verifisert med AppTest på et utvalg sider — ingen exceptions.

---

## 2026-05-31 — Tre nye hands-on-moduler (Plan Mode-oppgave + bundled skill) + to placeholdere fylt

Kurset hadde konsepter for Plan Mode og skills, men manglet hands-on for flere av dem. Tre nye moduler lagt til, og to eksisterende tomme oppgaver fylt med UTKAST-innhold (merket `<!-- UTKAST – Andre verifiserer -->`, jf. eksplisitt avtale om draft denne gangen).

**Hvorfor:** Konsept-modulene (plan_mode modul 10, skills_md modul 17) forklarte allerede mønstrene — inkludert eksempel-promptene for `@(serverSkill:lineage)` og `skill-development` — men deltakerne fikk aldri øvd dem. Demoen på «levende objekt» er presentatør-styrt fordi det er tryggere enn at alle kjører mot egne kjernetabeller.

**Endringer:**
- Ny modul **Individuell oppgave: Plan Mode** (`modules/individuell_oppgave_plan_mode/`, modul 11, kategori P) i Plan Mode-seksjonen etter konseptet. Speiler P-oppgave-mønsteret (oppgave/steg/forventet).
- Ny modul **Demo: Bundled skill (lineage)** (`modules/demo_bundled_skill/`, modul 18, kategori I) i skills.md-seksjonen. Runbook med agenda + tre segmenter + diskusjon (speiler `demo_1`/`demo_2`). Presentatør-tips: `BASELINE_ACTIVE_KUNDE_TRUST` som levende objekt.
- Ny modul **Individuell oppgave: Bundled skill** (`modules/individuell_oppgave_bundled_skill/`, modul 19, kategori P) i skills.md-seksjonen.
- Pedagogisk progresjon i skills.md-seksjonen: konsept → demo → individuell oppgave → gruppeoppgave.
- Fylt `individuell_oppgave_2` (metadata-sjekk av ukjent tabell) og `gruppeoppgave_2` (lag datakvalitets-skill via `skill-development`-workflow).
- Renummerering: modul 11–29 → 12–32. 19 wrapper-filer under `pages_content/modules/` renamet, 3 nye lagt til, crumb/caption-numre bumpet. `data/moduler.py` `MODULER` + `SECTIONS` oppdatert (32 moduler).
- CTA-kjede rekoblet: `plan_mode`→`individuell_oppgave_plan_mode`→`agents_md`; `skills_md`→`demo_bundled_skill`→`individuell_oppgave_bundled_skill`→`gruppeoppgave_2`.

**URL-endringer:** bokmerker til de 19 flyttede modulene fungerer ikke lenger. Slugs og DB-tabeller uberørt.

---

## 2026-05-31 — Font byttet fra Inter til Arial gjennomgående

Appen brukte Inter (lastet fra Google Fonts) som primærfont, med Arial som fallback. Nå er **Arial** primær og eneste UI-font.

**Hvorfor:** Ønske fra Andre. Arial er forhåndsinstallert overalt (ingen webfont-lasting, ingen avhengighet av Google Fonts), renders konsistent på tvers av OS-er, og samsvarer med bankenes skrifttype-policy.

**Endringer:**
- `.streamlit/config.toml`: `font = "Arial, Helvetica, sans-serif"`; `[[theme.fontFaces]]`-blokken som lastet Inter er fjernet.
- `modules/gruppeoppgave_1/viz.py`: Plotly-font satt til Arial-stacken.
- `DESIGN_GUIDE.md` §3 omskrevet (Arial primær i stedet for Inter), + oppdatert §0-tabell, §9-config-eksempel, §10-sjekkliste og §11. `PRD.md` §6/§7-fontlinje oppdatert.
- Mono/kode forblir JetBrains Mono (uendret).

---

## 2026-05-31 — Fjernet alle emojis/ikoner (ny designregel)

Emoji-dekorasjonen i overskrifter, `st.subheader`, `st.expander`-labels, callout-titler, crumbs og markdown-headere er fjernet i hele appen. Designet er nå ren tekst.

**Hvorfor:** Ønske fra Andre. Emojier renders inkonsistent på tvers av OS-er og treffer feil tone for et bank-publikum. (Reverserer den mellomliggende «emojis påkrevd»-perioden.)

**Beholdt med vilje:**
- Den kvadratiske callout-badgen (`i` / `!` / `✓` / `·`) — settes automatisk av `callout()` ut fra `kind`. Dette er det eneste tillatte «ikonet».
- Typografiske piler (`→`, `←`) i prosa/flyt-etiketter, og box-drawing (`├──`, `└──`) i mappe-trær — tekst, ikke ikoner.
- Browser-fanens favicon (`page_icon="❄"` i `app.py`) — branding i fanen, ikke sideinnhold. Flagget for Andre; lett å fjerne hvis ønskelig.

**Endringer:**
- Kalibrert sweep fjernet emoji fra ~45 `app_logic.py`- og `content/*.md`-filer (titler, subheaders, expander-labels, callout-`title=`, md-headere).
- TODO-list-eksemplet i `modules/arkitektur/content/oppgavestyring.md` byttet fra status-emoji (✅🔄⬜) til tekstmarkører (`[x]`/`[~]`/`[ ]`) som bevarer betydningen.
- **Designregel lagt til:** `DESIGN_GUIDE.md` §1.7 (nytt kjerneprinsipp «Ingen emojis eller ikoner») + presisering i §7 (callout-badge er eneste unntak) + oppdatert §10-sjekkliste. `CLAUDE.md`-sammendraget oppdatert tilsvarende.

---

## 2026-05-31 — «Komme i gang» flyttet til rett etter Introduksjon

Seksjonen **Komme i gang** (Arkitekturoversikt, Første demo, Individuell oppgave 1) er flyttet opp slik at den kommer rett etter **Introduksjon**, foran **@-mentions** og **Plan Mode**.

**Ny seksjonsrekkefølge:** Introduksjon → Komme i gang → @-mentions → Plan Mode → AGENTS.md → …

**Hvorfor:** Ønske fra Andre om at deltakerne kommer raskere i gang med verktøyet (arkitektur + første demo + hands-on) før konsept-fordypningen i @-mentions og Plan Mode.

**Endringer:**
- `data/moduler.py`: `SECTIONS` reordnet og modul 5–10 renummerert (arkitektur=5, demo_1=6, individuell_oppgave_1=7, at_mentions=8, individuell_oppgave_at_mentions=9, plan_mode=10) så sidebar-numrene forblir sekvensielle.
- Seks wrapper-filer under `pages_content/modules/` renamet (`m05`–`m10`); crumb- og caption-numre i de seks modulenes `app_logic.py` oppdatert.
- «Fortsett →»-CTA-kjeden rekoblet til ny rekkefølge: `cortex_in_snowsight`→`arkitektur`, `individuell_oppgave_1`→`at_mentions`, `plan_mode`→`agents_md`. (CTA-ene slår opp nr dynamisk via slug, så kun de tre hopp-punktene måtte endres.)
- Slugs og DB-tabeller uberørt; URL-ene (`?page=mNN_<slug>`) for de seks flyttede modulene er endret.

---

## 2026-05-30 — Bugfix (oppfølging): ordsky kollapset fortsatt til en miniklump

Den forrige fiksen (`st.image(width="stretch")`) løste ikke problemet i praksis: inne i `card()`/`stylable_container` kollapset bildet til en liten klump i hjørnet, og ordskyen var bare lesbar via fullskjerm-overlayet. Ordskyene rendres nå korrekt i full bredde uten fullskjerm-avhengighet.

**Hvorfor:** Resultatsidene projiseres i plenum. Bildet må fylle kortet med en gang — fullskjerm-knappen skal ikke være nødvendig.

**Endringer:**
- `render_wordcloud` i `modules/gruppeoppgave_1/viz.py` (delt av begge gruppeoppgavene) bytter fra `st.image` til å embedde 1600×900-PNG-en direkte som en `<img style="width:100%">` (base64 data-URI via `st.markdown`). Dette omgår container-sizing-buggen i `st.image` og fjerner fullskjerm-knappen helt. Oppløsning uendret (PRD §FR-3.4).

---

## 2026-05-30 — Bugfix: ordskyer på resultatsider vises i full bredde by default

Ordskyene på resultatsidene for Gruppeoppgave 1 og 3 ble rendret i et lite format som krevde fullskjerm-klikk for å være lesbare i plenum. De vises nå i full kort-bredde med en gang.

**Hvorfor:** Resultatsidene projiseres for hele gruppen. En ordsky som må åpnes i fullskjerm for å leses bryter flyten i gjennomgangen.

**Endringer:**
- `render_wordcloud` i `modules/gruppeoppgave_1/viz.py` (delt av begge gruppeoppgavene) bytter fra `st.pyplot` til `st.image(wc.to_array(), width="stretch")`. `width="stretch"` brukes i stedet for den utdaterte `use_container_width=True` (deprecated i Streamlit 1.50). Selve ordsky-oppløsningen er uendret (1600×900, jf. PRD §FR-3.4).
- Fjernet nå ubrukt `import matplotlib.pyplot as plt` fra `viz.py` (matplotlib er fortsatt en transitiv avhengighet av `wordcloud`).

---

## 2026-05-29 — Plan Mode lagt til som egen seksjon (modul 7, etter @-mentions)

Ny konsept-modul **Plan Mode** lagt inn rett etter @-mentions-seksjonen. Forklarer Cortex Codes tre kjøremoduser (Interaktiv, Plan Mode, Automatisert), hvordan man aktiverer Plan Mode, livssyklusen, og når man bør bruke den. Innhold levert av Andre (HTML-utkast), portet til kursets mørke designsystem.

**Hvorfor:** Plan Mode er den trygge, read-only-først-kjøremodusen som er særlig relevant for et risikoavers bank-publikum — agenten legger fram en plan til godkjenning før den rører kjernetabeller. Plassert tidlig (etter @-mentions) så deltakerne kjenner modusen før de gjør hands-on-oppgaver. Knyttes til skills (Plan Mode + bundled skill på levende objekt).

**Endringer:**
- Ny mappe `modules/plan_mode/` (kategori I) med `app_logic.py` + sju content-filer (`intro`, `moduser`, `aktiver`, `flyt`, `flyt_steg`, `naar`, `kobling`). Layout: intro-callout, tre-modus-kort (Plan Mode framhevet med Vann-aksent + "Denne modulen"-merke og spektrum-etikett), to aktiverings-kort, `numbered_steps`-livssyklus, to "når"-kort + kobling-til-skills-callout.
- Ny wrapper `pages_content/modules/m07_plan_mode.py`.
- Ny seksjon `Plan Mode` i `SECTIONS` (mellom `@-mentions` og `Komme i gang`).
- Eksisterende moduler 7–28 (arkitektur … avslutning) skjøvet ned til 8–29. 22 wrapper-filer renamet (`m07…m28` → `m08…m29`); 22 `app_logic.py`-filer fikk crumb/caption-nummer bumpet.
- `individuell_oppgave_at_mentions` CTA endret: `arkitektur` → `plan_mode`. Plan Mode-CTA peker videre til `arkitektur`.

**URL-endringer:** bokmerker til de 22 flyttede modulene fungerer ikke lenger. Slugs og DB-tabeller uberørt.

---

## 2026-05-29 — skills.md (modul 15) fylt med innhold om Cortex Code-skills

Modul 15 (skills.md) gikk fra tomme placeholder-filer til et fullt innholdt oppslag om Cortex Codes skill-mekanisme. Innhold levert av Andre (HTML-utkast) og portet til kursets mørke designsystem — ikke AI-fabrikkert.

**Hvorfor:** Andre hadde et ferdig HTML-utkast om skills (hva en skill er, anatomi, bundled vs. custom, plassering/presedens, når lage en, beste praksis) og ba om å få det inn i skills-seksjonen med kursets UI og nummererte "1, 2, 3"-bokser.

**Endringer:**
- Ny helper `numbered_steps()` i `modules/shared/ui.py` (DESIGN_GUIDE v2 §4): nummerert liste med runde badge-tall i ett kort. Tar `str` (kun tittel) eller `(tittel, body)`-tupler. Brukes til steg-prosesser og sjekklister.
- `modules/skills_md/app_logic.py` omskrevet til åtte seksjoner: hva en skill er + fire-delt anatomi-grid, SKILL.md-kort, bundled vs. custom i to kolonner, plassering (tabell) + presedens-callout, når lage en (numbered_steps), forstå før bruk (eksempel-prompt + Plan Mode-tips), lage en ny (eksempel-prompt), beste praksis (numbered_steps).
- Content-filer: seks tomme placeholders fjernet; tretten nye `.md`-filer med Andres innhold (`intro`, `anatomi_deler`, `skill_md`, `typer`, `hvor`, `precedence`, `naar`, `naar_steg`, `forstaa`, `forstaa_prompt`, `tips_plan`, `lage`, `lage_prompt`, `beste_praksis`).
- Tittel/caption oppdatert: "🛠️ Skills i Cortex Code" (nav-label `skills.md` uendret).

**URL-endringer:** ingen. Slug og modulnummer (15) uberørt.

---

## 2026-05-26 — @-mentions-seksjon mellom Snowsight-intro og Komme i gang

Ny seksjon "@-mentions" lagt inn rett etter cortex_in_snowsight. Inneholder en konsept-modul som forklarer hvordan `@`-tegnet binder katalog-referanser strukturelt (vs. tekst-inferens), og en individuell oppgave hvor deltakeren sammenligner samme prompt med og uten `@`-mention.

**Hvorfor:** @-mentions er en sentral produktivitetsfeature i Snowsight som mange undervurderer — det er forskjellen mellom at agenten ser eksakte kolonner/tags/masking policies som strukturerte data, vs. å måtte gjette via inferens i Horizon Catalog. Bank-relevant pga. masking policies og PII-tags.

**Endringer:**
- Ny mappe `modules/at_mentions/` (konsept, kategori I) med `app_logic.py` + fire content-filer (`what_is_it`, `what_agent_sees`, `with_vs_without`, `why_it_matters`). Innhold drafted basert på Andres beskrivelse.
- Ny mappe `modules/individuell_oppgave_at_mentions/` (kategori P) med `app_logic.py` + tre content-filer (`oppgave`, `steg`, `forventet`). Oppgaven ber deltaker kjøre samme prompt med og uten `@`.
- Wrappers: `m05_at_mentions.py`, `m06_individuell_oppgave_at_mentions.py`.
- Eksisterende moduler 5–26 skjøvet ned til 7–28. 22 wrapper-filer renamet.
- 22 `app_logic.py`-filer fikk captions/crumbs/docstrings oppdatert.
- `cortex_in_snowsight` CTA endret: `pages/demo_1.py` → `at_mentions` (var stale `pages/`-form fra før).
- `SECTIONS` utvidet med to nye seksjoner: `@-mentions` (m05–m06) og `Komme i gang` (m07–m09, arkitektur/demo_1/individuell_oppgave_1 som tidligere lå i Introduksjon). Introduksjon-seksjonen krymper til m01–m04.

**URL-endringer:** bokmerker til 22 flyttede moduler fungerer ikke lenger. Slugs og DB-tabeller uberørt.

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
