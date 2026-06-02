# CONTENT_REVIEW - innholdsevaluering av kurset

> Generert av en multi-agent evaluering (34 modul-agenter + 18 web-verifikasjoner). Vurdering, ikke omskriving. **Faktuell score paa produktpaastander er begrenset** - der F har `?` er det en Cortex Code/Snowflake-produktpaastand som maa verifiseres mot Snowflakes egen dokumentasjon av Andre.

## Skala

- **F** faktuell (1-5, `?`=uverifisert produktpaastand) · **R** kilde-/fabrikasjonsrisiko (1-5, **hoy=daarlig**) · **Rel** relevans · **P** pedagogisk verdi · **Full** modenhet · **T** tone (1-5/n-a)

## Sammendrag (aggregat)

- Moduler vurdert: **34** · content-enheter: **177**

- Fullfoeringsgrad: ferdig **110**, UTKAST **14**, placeholder **53**, tom **0**

- Uverifiserte produktpaastander (F?): **70** enheter · enheter med hoy risiko (R>=4): **36**

- Produktpaastander ekstrahert totalt: **111** (hvorav 61 hoyrisiko)

- Web-verifikasjon av topp 18 hoyrisiko: stoettet **6**, delvis **10**, motsagt **2**, **ingen kilde funnet 0**

> **Viktig oppdagelse:** Cortex Code ER dokumentert offentlig (`docs.snowflake.com/en/user-guide/cortex-code/`, inkl. `/tools`, `/cli-reference`). De fleste «uverifiserte» paastandene kan derfor faktisk sjekkes mot offisiell kilde - de er ikke uverifiserbare, bare ikke-verifisert enda.

## Hovedfunn (prioritert)

### A. Sannsynlig FEIL - maa rettes (motsagt av offisiell docs)

1. **`arkitektur/tool_interface.md` (+ `kontekstbevissthet.md`): verktoynavnene er feil.** Innholdet lister ~15 verktoy i snake_case (`snowflake_object_search`, `system_execute_sql`, `snowsight_navigate`, `get_page_context`, `read_active_pane`, `data_to_chart` osv.). Offisiell docs (`/cortex-code/tools`) lister verktoyene i **PascalCase** (`Read`, `Write`, `Edit`, `Bash`, `SnowflakeSqlExecute`, `SnowflakeObjectSearch`, `EnterPlanMode` ...), og det finnes **ingen «Navigasjon»-kategori** - `snowsight_navigate`/`get_page_context`/`read_active_pane` eksisterer ikke i docs. Konseptene (verktoy-lag, kontekstbevissthet) er korrekte, men de konkrete navnene maa rettes mot docs eller gjoeres generiske. **Hoyest verdi aa fikse** (presenteres som fakta, vises i plenum).

2. **`cortex_code/content/term_best_practices.md`: over-paastand.** «Agenten vil ikke generere kode som bryter konvensjoner ... uten at du maa minne den paa dem.» Docs motsier garantien: ansvaret ligger paa brukeren (gjennomgaa diff, gi staaende instruksjoner via AGENTS.md). Nedjuster til «kjenner og kan foelge konvensjoner, men maa instrueres og kontrolleres».

### B. Bekreftet korrekt (bra - kan presenteres trygt)

- Server-side **skills-domenene** (cost-intelligence, data-governance, machine-learning, dbt, Streamlit/developing-with-snowflake, Iceberg) - fullt bekreftet i docs.
- **`@(serverSkill:lineage)`** er en reell, dokumentert bundled skill. **`skill-development`** finnes som eksakt slug.
- **`/plan`** aktiverer Plan Mode (CLI-referansen bekrefter). `@`-mention av katalogobjekter gir kontekst (tags, masking policies, lineage bekreftet).

### C. Modenhet

- **53 placeholder-enheter** (og 14 UTKAST) av 177 - mye innhold er enda ikke skrevet. Se §3. Disse er ikke faktafeil, men maa fylles av Andre foer kurs.

### D. Anbefalt handling

1. Rett verktoynavnene i `arkitektur` mot docs (eller gjoer dem generiske). [Andres beslutning / kan gjoeres paa forespoersel]
2. Mykne opp `term_best_practices.md`-garantien.
3. Verifiser resten av R>=4-paastandene (§2) mot `docs.snowflake.com/en/user-guide/cortex-code/` - na som vi vet kilden finnes.
4. Fyll placeholder-innhold (§3).


## 1. Modul-heatmap

| Nr | Modul | F | R | Rel | P | Full | T | #filer | #hoyrisiko |
|---:|---|--:|--:|--:|--:|---|--:|--:|--:|
| 0 | oppvarming | 5 | 1 | 4.5 | 2.5 | ferdig | 5 | 2 | 0 |
| 1 | evolusjon | 5 | 1 | 4 | 3.5 | blandet | 5 | 7 | 0 |
| 2 | cortex_code | 3.8 | 3.2 | 3.8 | 4.2 | ferdig | 5 | 10 | 6 |
| 3 | cortex_interaction | 4.5 | 2.3 | 4.5 | 3.8 | ferdig | 5 | 4 | 0 |
| 4 | cortex_in_snowsight | 0 | 1 | 0 | 0 | placeholder | n/a | 7 | 0 |
| 5 | arkitektur | 3.9 | 4 | 4 | 4.1 | ferdig | 5 | 7 | 12 |
| 6 | demo_1 | 4.5 | 2.2 | 4 | 3.8 | ferdig | 5 | 6 | 0 |
| 7 | individuell_oppgave_1 | 4 | 3 | 4 | 3 | ferdig | 5 | 1 | 0 |
| 8 | kostnader | 0 | 1 | 0 | 0 | placeholder | n/a | 7 | 0 |
| 9 | at_mentions | 3.5 | 3.5 | 4.75 | 4.5 | ferdig | 5 | 4 | 4 |
| 10 | individuell_oppgave_at_mentions | 4 | 2 | 4 | 3.5 | ferdig | 5 | 4 | 0 |
| 11 | plan_mode | 3.7 | 3.3 | 4 | 3.9 | ferdig | 5 | 7 | 7 |
| 12 | individuell_oppgave_plan_mode | 4.3 | 3 | 3.8 | 3.5 | ferdig | 5 | 4 | 1 |
| 13 | agents_md | 4.5 | 2 | 3.5 | 3.3 | blandet | 5 | 7 | 1 |
| 14 | gruppeoppgave_1 | 5 | 1.5 | 4 | 3.5 | ferdig | 5 | 3 | 0 |
| 16 | tilgjengelige_modeller | 4 | 2.6 | 4.4 | 4.4 | UTKAST | 5 | 5 | 1 |
| 17 | individuell_oppgave_modellvalg | 4.8 | 1.4 | 4.6 | 4.4 | ferdig | 5 | 5 | 0 |
| 18 | skills_md | 4.3 | 3.1 | 4 | 4.1 | ferdig | 5 | 14 | 10 |
| 19 | demo_bundled_skill | 3.75 | 4 | 4.6 | 4.2 | UTKAST | 5 | 5 | 6 |
| 20 | individuell_oppgave_bundled_skill | 3.7 | 3 | 4 | 4 | ferdig | 5 | 3 | 4 |
| 21 | gruppeoppgave_2 | 3 | 4.3 | 4.7 | 4 | UTKAST | 5 | 3 | 4 |
| 22 | memory_md | 3.7 | 3.5 | 4 | 4 | blandet | 5 | 8 | 4 |
| 23 | gruppeoppgave_3 | 5 | 1 | 4.3 | 3.3 | ferdig | 5 | 3 | 0 |
| 25 | context_engineering | 5 | 1 | 3 | 2 | placeholder | 5 | 8 | 0 |
| 26 | individuell_oppgave_2 | 3 | 3.7 | 5 | 4 | UTKAST | 5 | 3 | 2 |
| 28 | demo_2 | 5 | 1 | 3 | 2 | placeholder | 4 | 6 | 0 |
| 30 | autonomous_loop | 5 | 1 | 3 | 2 | placeholder | 4 | 7 | 0 |
| 32 | individuell_oppgave_kohort | 4 | 2 | 4.5 | 3.5 | blandet | 5 | 4 | 1 |
| 34 | individuell_oppgave_konkurrent (gruppeoppgave) | 5 | 1 | 4.3 | 3 | blandet | 5 | 4 | 0 |
| 35 | avslutning | 5 | 1 | 2 | 1 | placeholder | 4 | 4 | 0 |

## 2. Filer som MAA verifiseres for kurs (R>=4)

| R | Modul | Fil | F | Rel | P | Note |
|--:|---|---|--:|--:|--:|---|
| 5 | arkitektur | tool_interface.md | 3? | 4 | 4 | Hoy fabrikasjonsrisiko: tabellen lister ~15 eksakte verktoynavn (snowflake_object_search, system_execute_sql, snowflake_multi_cortex_analyst, data_to_chart osv. |
| 5 | arkitektur | skills_system.md | 3? | 4 | 4 | Server_skill/client-side-skille og stien .snowflake/cortex/skills/ med SKILL.md er konkrete produktpastander som ma verifiseres. Konseptet 'plug-in ekspertise'  |
| 5 | arkitektur | kontekstbevissthet.md | 4? | 4 | 4 | Tre navngitte mekanismer (get_page_context, read_active_pane, highlighted text) er konkrete Cortex/Snowsight-pastander - ma verifiseres. God 'syn inn i UI'-meta |
| 5 | cortex_code | quote.md | 3? | 4 | 4 | Engelsk 'dokumentasjons'-sitat med tette produktpaastander: 'autonomous agent framework', 'deep understanding of RBAC, schemas, best practices', 'agent-building |
| 5 | cortex_code | term_agent_building.md | 3? | 3 | 3 | Paastand om at Cortex Code kan 'bygge agenter paa Snowflakes egen agentinfrastruktur' er svaert produktspesifikk og uverifisert. Maa sjekkes mot Snowflake-doc - |
| 5 | cortex_code | term_best_practices.md | 2? | 3 | 3 | Sterk paastand: agenten 'vil ikke generere kode som bryter konvensjoner Snowflake anbefaler'. Filen flagger selv 'Paastanden er at...', men formuleringen er en  |
| 5 | demo_bundled_skill | segment_3.md | 3? | 5 | 4 | Hurtigtast 'Ctrl + P' / '/plan' og paastand om at Plan Mode holder seg read-only er konkrete produktdetaljer med hoey fabrikasjonsrisiko - MAA sjekkes mot Snowf |
| 5 | gruppeoppgave_2 | steg.md | 3? | 5 | 4 | Konkret steg-for-steg med tidsbokser - bra pedagogikk. Men flere uverifiserte produktdetaljer: prompt-syntaksen '[Skill Attached: skill-development]', begrepet  |
| 5 | memory_md | how_it_works.md | 3? | 4 | 4 | Svært spesifikke produktpåstander: env-var CORTEX_ENABLE_MEMORY=1, sti ~/.snowflake/cortex/memory/, og en eksakt operasjonsliste (view/create/str_replace/insert |
| 5 | plan_mode | aktiver.md | 3? | 4 | 4 | Konkrete hurtigtaster: Ctrl+P, /plan for read-only, Shift+Tab for automatikk. Høy fabrikasjonsrisiko - eksakte tastaturbindinger MÅ verifiseres mot Cortex Code- |
| 5 | plan_mode | moduser.md | 3? | 4 | 5 | Tre kjoeremoduser (Interaktiv/Plan/Automatisert) med navn, default-status og aktivering (Ctrl+P, /plan, Shift+Tab). Sentral produktpaastand - at Cortex Code har |
| 5 | skills_md | hvor.md | 4? | 4 | 4 | Tabell med eksakte filstier (~/.snowflake/cortex/skills/, ~/.cortex/skills/, .cortex/skills/). Hoey fabrikasjonsrisiko - eksakte stier maa verifiseres mot docs  |
| 4 | agents_md | how_it_works.md | 4? | 4 | 4 | Påstand om at innholdet auto-injiseres som systemkontekst i ALLE samtaler er produktspesifikk for Cortex Code/agentens implementasjon - verifiser mot Snowflake- |
| 4 | arkitektur | intro.md | 4? | 4 | 4 | Pastand om 'enkelt-agent-arkitektur' og 'fem integrerte lag' er en produktspesifikk karakteristikk av Cortex Code som ma verifiseres. Konseptuelt ryddig og nokt |
| 4 | arkitektur | oppgavestyring.md | 4? | 4 | 4 | Verktoynavn system_todo_write og statusflyt pending/in_progress/completed er produktspesifikt - ma verifiseres. dbt-parentes er nyttig for bank-publikum. Bra av |
| 4 | at_mentions | what_agent_sees.md | 3? | 5 | 4 | Sterk paastand om at Snowsight injiserer full metadata (kolonnenavn, datatyper, masking policies, tags, schema.yml-beskrivelser, lineage, sample-statistikk) som |
| 4 | at_mentions | why_it_matters.md | 3? | 5 | 5 | Treffende bank-vinkling (masking/PII). Men paastand 'masking policies og PII-tags kommer KUN automatisk med @-mention' er sterk og uverifisert - kan vaere feil. |
| 4 | cortex_code | example.md | 3? | 5 | 5 | Sterkt bank-relevant (kundefrafall, RBAC, review). Generiske tabellnavn - bra. MEN konkret 5-stegs autonom loop ('validerer at resultatet ser fornuftig ut') er  |
| 4 | demo_bundled_skill | agenda.md | 4? | 4 | 4 | Bra pedagogisk mal (forstaa skill foer bruk -> anvend paa levende objekt). Naevner @(serverSkill:lineage) og BASELINE_ACTIVE_KUNDE_TRUST - sistnevnte er trygt f |
| 4 | demo_bundled_skill | segment_1.md | 4? | 4 | 5 | God ide: la agenten forklare skillen foerst. Paastand om at skillen 'alltid' returnerer faste outputs og @(serverSkill:lineage)-syntaksen er produktspesifikk og |
| 4 | demo_bundled_skill | segment_2.md | 4? | 5 | 4 | Lineage paa et objekt (opphav/avhengigheter/nedstroems) er hoeyt relevant for bank/regulatorisk sporing. Skill-navn og at den strukturerer svaret slik maa verif |
| 4 | gruppeoppgave_2 | oppgave.md | 3? | 5 | 4 | Oppgaven (lag custom skill for datakvalitet: duplikater/NULL-andel/utliggere) er svaert bank-relevant og nokternt formulert. Men 'skill-development'-arbeidsflyt |
| 4 | gruppeoppgave_2 | forventet.md | 3? | 4 | 4 | Tydelig forventet resultat + god refleksjonsvinkel (skill vs. prompte paa nytt). Avhenger av at 'SKILL.md' under '.cortex/skills/' faktisk er Cortex Code-konven |
| 4 | individuell_oppgave_2 | oppgave.md | 3? | 5 | 4 | God, banknær oppgave (PII/masking-fokus). Antar at Cortex Code kan hente tags, masking policies, eier og radantall for en tabell - produktspesifikk evne som maa |
| 4 | individuell_oppgave_2 | steg.md | 3? | 5 | 4 | UTKAST-markert. Konkrete, gode steg. Prompt-eksempelet bruker @DATABASE.SCHEMA.TABELL-syntaks og antar agenten henter masking/tags/eier/radantall - maa verifise |
| 4 | individuell_oppgave_bundled_skill | steg.md | 3? | 4 | 4 | Konkrete steg med `/lineage`-syntaks. Må verifiseres: finnes `/lineage` som slash/bundled skill, og er `/lineage <table>`-invokasjonen riktig? Merk inkonsistens |
| 4 | individuell_oppgave_plan_mode | steg.md | 4? | 4 | 4 | Konkrete steg. Pastandene 'Apne Cortex Code i Snowsight', 'Skru pa Plan Mode. Agenten gar i read only' og 'Godkjenn/juster/avvis' er produktspesifikk atferd som |
| 4 | memory_md | where_to_place.md | 3? | 3 | 3 | Sti ~/.snowflake/cortex/ med undermapper agents/ og memory/ er produktspesifikk og uverifisert. Konseptet 'memory følger deg, ikke prosjektet' er pedagogisk gre |
| 4 | plan_mode | intro.md | 4? | 4 | 4 | Beskriver Plan Mode som read-only modus som legger fram plan til godkjenning. Konseptuelt sannsynlig, men 'en av flere kjøremoduser i Cortex Code CLI' er produk |
| 4 | skills_md | intro.md | 4? | 4 | 4 | God, nøktern definisjon av skill-konsept. Men paastanden om at en skill kalles med @(serverSkill:lineage) er produktspesifikk syntaks som maa verifiseres mot Sn |
| 4 | skills_md | typer.md | 4? | 4 | 4 | Bundled vs custom er nyttig skille. Konkrete bundled-navn (Dynamic Tables, Semantic views, Agents, Lineage) og kommandoen /skill list er produktspesifikke og ma |
| 4 | skills_md | precedence.md | 4? | 3 | 4 | Presedens project > user > bundled er plausibel men produktspesifikk regel som maa verifiseres. Raadet om project skill er fornuftig og generelt. |
| 4 | skills_md | lage.md | 4? | 3 | 4 | Paastaar at Cortex Code har en innebygd skill-development-arbeidsflyt for scaffolding. Produktspesifikk funksjon som maa verifiseres. Raadet om aa definere inpu |
| 4 | skills_md | lage_prompt.md | 4? | 4 | 4 | Konkret, bank-aktuelt eksempel (AP-invoices Dynamic Table). Bruker [Skill Attached: skill-development] og .cortex/skills/ - produktspesifikk syntaks/sti som maa |
| 4 | skills_md | tips_plan.md | 4? | 5 | 4 | Bank-relevant (read-only foer utfoerelse paa kjernetabeller). Men Plan Mode-hurtigtast Ctrl+P / /plan og read-only-oppfoersel er produktspesifikt og maa verifis |
| 4 | tilgjengelige_modeller | intro.md | 3? | 4 | 3 | Paastanden 'Cortex Code kjorer paa Claude, og du kan velge modell' er produktspesifikk og maa verifiseres mot Snowflake-docs. Avveining kapabilitet vs fart/kost |

## 3. Tomt / placeholder (53 enheter - maa fylles av Andre)

| Modul | Fil | Status |
|---|---|---|
| evolusjon | era_1_googling.md | placeholder |
| evolusjon | era_2_assistanse.md | placeholder |
| cortex_in_snowsight | intro.md | placeholder |
| cortex_in_snowsight | section_1_location.md | placeholder |
| cortex_in_snowsight | section_2_interface.md | placeholder |
| cortex_in_snowsight | section_3_tasks.md | placeholder |
| cortex_in_snowsight | section_4_example.md | placeholder |
| cortex_in_snowsight | section_5_tips.md | placeholder |
| cortex_in_snowsight | app_logic.py | placeholder |
| kostnader | intro.md | placeholder |
| kostnader | kostnadsmodell.md | placeholder |
| kostnader | kostnadsdrivere.md | placeholder |
| kostnader | spore_forbruk.md | placeholder |
| kostnader | resource_monitors.md | placeholder |
| kostnader | best_practices.md | placeholder |
| agents_md | example.md | placeholder |
| agents_md | transition.md | placeholder |
| memory_md | example.md | placeholder |
| context_engineering | intro.md | placeholder |
| context_engineering | anatomi.md | placeholder |
| context_engineering | agents_vs_inline.md | placeholder |
| context_engineering | anti_patterns.md | placeholder |
| context_engineering | eksempel_sammenligning.md | placeholder |
| context_engineering | iterativ.md | placeholder |
| context_engineering | sql_spesifikt.md | placeholder |
| demo_2 | agenda.md | placeholder |
| demo_2 | segment_1.md | placeholder |
| demo_2 | segment_2.md | placeholder |
| demo_2 | segment_3.md | placeholder |
| demo_2 | diskusjon.md | placeholder |
| autonomous_loop | intro.md | placeholder |
| autonomous_loop | step_plan.md | placeholder |
| autonomous_loop | step_act.md | placeholder |
| autonomous_loop | step_observe.md | placeholder |
| autonomous_loop | step_reflect.md | placeholder |
| autonomous_loop | example.md | placeholder |
| individuell_oppgave_kohort | steg.md | placeholder |
| individuell_oppgave_kohort | forventet.md | placeholder |
| individuell_oppgave_konkurrent | steg.md | placeholder |
| individuell_oppgave_konkurrent | forventet.md | placeholder |
| avslutning | oppsummering.md | placeholder |
| avslutning | neste_steg.md | placeholder |
| avslutning | holdning_revisit.md | placeholder |

## 4. Lav relevans/verdi (Rel<=2 eller P<=2, ferdig/UTKAST)

| Modul | Fil | Rel | P | Note |
|---|---|--:|--:|---|
| agents_md | app_logic.py | 3 | 2 | Kun layout-prosa: crumb '13 · AGENTS.md', subtitle 'Hva er AGENTS.md, og hvorfor trenger vi det?', subheaders og lenke til agents.md. Noeytr |
| autonomous_loop | app_logic.py | 3 | 2 | Kun layout-prosa: subtitle «Hva skjer egentlig inne i agenten?», crumb «30 · Autonomous loop i dybden», subheaders «De fire fasene»/«Konkret |
| avslutning | app_logic.py | 2 | 1 | Ren layout-prosa: subtitle 'Hva na? - oppsummering og veien videre', subheaders 'Oppsummering'/'Neste steg'/'Holdning - har den flyttet seg? |
| context_engineering | subheader) | 3 | 2 | Eneste faktiske prosa: subtitle 'Anatomi, monstre og iterativ forbedring av prompts', subheader 'For og etter'. Nokternt, ingen hype. Merk:  |
| demo_2 | subheader) | 3 | 2 | Subtitle 'Live-demo: realistisk bank-use-case med Cortex Code.', crumb '28 · Demo 2', subheader 'Diskusjon etter demoen'. Nøktern ramme, ing |
| gruppeoppgave_1 | app_logic.py | 3 | 2 | Prosa: module_header 'Gruppeoppgave 1 - AGENTS.md', crumb '14 · Gruppeoppgave 1', anonymitets-caption. Korrekt og nøktern. Liten drift: docs |
| individuell_oppgave_at_mentions | app_logic.py | 3 | 2 | Kun layout-prosa (crumb, subtitle, subheaders). Merk inkonsistens: crumb sier '10 ·' men docstring sier 'modul 6' og next-cta peker til plan |
| individuell_oppgave_konkurrent | app_logic.py | 3 | 2 | Kun layout-prosa (crumb, subtitle, subheaders 'Steg'/'Forventet resultat'). Nøktern, ingen hype, ingen produktpåstand. Korrekt PRD-referanse |
| individuell_oppgave_plan_mode | app_logic.py | 3 | 2 | Kun prosa: subtitle, crumb og subheaders. Nokternt, ingen hype. Merk crumb sier '12' mens docstring sier 'modul 8' - liten intern inkonsiste |
| kostnader | app_logic.py | 2 | 1 | Kun layout: crumb, module_header("Kostnader"), callout "Gjennomgang i PowerPoint." og next-CTA. Nøkternt, ingen prosa-paastander. Content-md |
| memory_md | transition.md | 2 | 2 | Fila er DOC-kilder (to docs.snowflake.com-lenker for memory-stien og tool-operasjoner), ikke en overgangstekst. app_logic bruker den som avs |
| oppvarming | app_logic.py | 4 | 2 | Kun UI-prosa: header 'Bli kjent', subtitle 'Hvilke forkunnskaper har vi? Helt anonymt.', crumb, skala-pille (1=uenig/5=enig), kvitterings- o |

## 5. Web-verifikasjon av hoyrisiko-paastander (topp 18)

| Verdikt | Modul | Paastand | Kilde | Note |
|---|---|---|---|---|
| motsagt |  | Navigasjon: snowsight_navigate, get_page_context, read_active_pane (navigasjons- | [lenke](https://docs.snowflake.com/en/user-guide/cortex-code/tools) | Den autoritative siden "Cortex Code CLI agent tools" (docs.snowflake.com) lister opp hele verktøysettet i PascalCase: Fi |
| motsagt |  | agenten ikke vil generere kode som bryter konvensjoner Snowflake anbefaler. Den  | [lenke](https://www.snowflake.com/en/developers/guides/best-practices-cortex-code-cli/) | Offisiell Snowflake-dokumentasjon stoetter ikke garantien i paastanden, og motsier den paa flere punkter. Produktsiden/d |
| delvis støttet |  | Sok-verktoy i Snowflake Cortex Code: snowflake_object_search, snowflake_product_ | [lenke](https://docs.snowflake.com/en/user-guide/cortex-code/tools) | Den offisielle siden "Cortex Code CLI agent tools" lister Snowflake-verktoyene: SnowflakeSqlExecute, SnowflakeObjectSear |
| delvis støttet |  | Utførelse-verktøy i Cortex Code: snowflake_sql_execute, system_execute_sql, bash | [lenke](https://docs.snowflake.com/en/user-guide/cortex-code/tools) | Den offisielle docs-siden "Cortex Code CLI agent tools" lister verktøy i PascalCase, ikke snake_case. To av tre i påstan |
| delvis støttet |  | Spesialiserte: snowflake_multi_cortex_analyst, pivot_table, notebook_action, dat | [lenke](https://docs.snowflake.com/en/user-guide/cortex-code/tools) | Den offisielle siden "Cortex Code CLI agent tools" (docs.snowflake.com) lister de innebygde verktoyene. Av de fire pasta |
| delvis støttet |  | Server-side skills (server_skill) ... Dekker spesifikke domener: kostnadsanalyse | [lenke](https://docs.snowflake.com/en/user-guide/cortex-code/bundled-skills) | Domenelista stemmer fullt ut. Den offisielle docs-siden bekrefter alle seks innebygde skills: cost-intelligence (kostnad |
| delvis støttet |  | Sidekontekst (get_page_context): Hvilken side brukeren er pa (Notebook, Workshee | [lenke](https://docs.snowflake.com/en/user-guide/cortex-code/cortex-code) | Det OVERORDNEDE konseptet er støttet: Snowflakes offisielle docs bekrefter at Cortex Code har "Context awareness" og "kn |
| delvis støttet |  | Aktive resultater (read_active_pane): SQL-resultater som vises i Results-panelet | [lenke](https://docs.snowflake.com/en/user-guide/cortex-code/cortex-code-snowsight) | Verktoynavnet "read_active_pane" finnes IKKE i offisiell Snowflake-dokumentasjon. Jeg sjekket docs-sidene for Cortex Cod |
| delvis støttet |  | agenten ser: Eksakt kolonnenavn og datatyper, Eventuelle masking policies, Tags  | [lenke](https://docs.snowflake.com/en/user-guide/cortex-code/cortex-code-snowsight) | Offisiell Snowflake-dok bekrefter @-mention av katalogobjekter (tabeller/schemas/views) som kontekst, og at responser ka |
| delvis støttet |  | Hva gjør `@(serverSkill:lineage)`-skillen? (fra modul demo_bundled_skill, segmen | [lenke](https://docs.snowflake.com/en/user-guide/cortex-code/bundled-skills) | Selve lineage-skillen er reell og dokumentert som en bundled skill i Cortex Code CLI. Offisiell beskrivelse: "Analyze da |
| delvis støttet |  | skru på Plan Mode (`Ctrl + P` / `/plan`) før du lar en skill endre noe | [lenke](https://docs.snowflake.com/en/user-guide/cortex-code/keyboard-shortcuts) | Delvis riktig. `/plan` er korrekt: CLI-referansen (https://docs.snowflake.com/en/user-guide/cortex-code/cli-reference) l |
| delvis støttet |  | Bruk [Skill Attached: skill-development] til a bygge en project skill (fra modul | [lenke](https://docs.snowflake.com/en/user-guide/cortex-code/extensibility) | Substansen i påstanden er støttet av offisiell Snowflake-dokumentasjon. Det FINNES en innebygd skill med eksakt slug 'sk |
| støttet |  | Client-side skills (.snowflake/cortex/skills/) ... En mappe med en SKILL.md-fil  | [lenke](https://docs.snowflake.com/en/user-guide/cortex-code/extensibility) | Begge delene av påstanden er bekreftet i offisiell Snowflake-dokumentasjon. (1) SKILL.md/mappe: extensibility-doc sier o |
| støttet |  | Cortex Code is an AI-driven intelligent agent integrated into the Snowflake plat | [lenke](https://docs.snowflake.com/en/user-guide/cortex-code/cortex-code) | Den offisielle Snowflake-dokumentasjonen (docs.snowflake.com) gjengir påstanden ordrett som åpningsdefinisjonen av Corte |
| støttet |  | It uses an autonomous agent framework to interact directly with your Snowflake e | [lenke](https://docs.snowflake.com/en/user-guide/cortex-code/cortex-code) | Påstanden er ordrett hentet fra Snowflakes offisielle dokumentasjon (docs.snowflake.com, "Cortex Code"-siden). Setningen |
| støttet |  | Cortex Code kan hjelpe deg å bygge agenter på Snowflakes egen agentinfrastruktur | [lenke](https://docs.snowflake.com/en/user-guide/cortex-code-agent-sdk/cortex-code-agent-sdk) | Begge ledd i påstanden bekreftes av offisiell Snowflake-dokumentasjon. Cortex Code-siden (docs.snowflake.com/en/user-gui |
| støttet |  | Da holder Cortex Code seg read-only mens den tenker, og legger fram en strukture | [lenke](https://www.snowflake.com/en/developers/guides/cortex-code-foundations/) | Nesten ordrett match mot offisiell Snowflake-kilde. Cortex Code Foundations-guiden (snowflake.com) skriver: "Plan Mode s |
| støttet |  | Legg den under `.cortex/skills/` (plassering av en project skill i Snowflake Cor | [lenke](https://docs.snowflake.com/en/user-guide/cortex-code/extensibility) | Den offisielle Snowflake-dokumentasjonen (Cortex Code CLI extensibility) bekrefter at prosjekt-lokale skills plasseres i |
