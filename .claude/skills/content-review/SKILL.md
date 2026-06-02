---
name: content-review
description: >-
  Evaluer alt kursinnhold i dette repoet (faktuell korrekthet, kilde-/fabrikasjonsrisiko,
  relevans, pedagogisk verdi, fullføringsgrad, tone) og produser en scoret rapport
  (CONTENT_REVIEW.md). Bruk når Andre ber om en innholds-gjennomgang/vurdering, "score
  innholdet", "er innholdet riktig/relevant", faktasjekk av modulene, eller en
  oppdatert CONTENT_REVIEW. Kjører en multi-agent workflow (1 agent per modul) +
  web-verifiserer høyrisiko Cortex Code/Snowflake-produktpåstander.
---

# Innholdsrevisjon av kurset

Produserer en scoret kvalitetsrapport over ALT kursinnhold i `modules/*/`. Dette er en
**vurdering, ikke en omskriving** - endre aldri innhold som del av denne skillen (jf.
CLAUDE.md «Andre skriver innholdet selv»).

## Scoring-rubrikk (1-5 der ikke annet er nevnt; høyere = bedre unntatt R)

| Metrikk | Hva | Skala |
|---|---|---|
| **F** faktuell | Er påstandene sanne? | 5 = utvilsomt/web-verifisert · 3 = trolig men uverifisert produktpåstand · 1 = sannsynlig feil. `F_unverified=true` for Cortex Code/Snowflake-produktspesifikke påstander du ikke kan verifisere fra generell kunnskap. `null` for tom/placeholder. |
| **R** risiko | Kilde-/fabrikasjonsrisiko (jf. CLAUDE.md) - **høy=dårlig** | 5 = spesifikk, AI-draftet, uverifisert produktpåstand som MÅ sjekkes · 1 = generelt/trivielt/Andres ord |
| **Rel** relevans | Treffer bank-analytiker-målgruppen | 5 = direkte nyttig · 1 = generisk fyll |
| **P** pedagogisk verdi | Lærer deltakeren noe konkret | 5 = høy · 1 = ingen |
| **Full** fullføring | Modenhet | `ferdig` / `UTKAST` / `placeholder` / `tom` |
| **T** tone | Nøktern bank-tone, ikke tech-bro | 5 = treffer · 1 = bommer · `n/a` for placeholder |

## Scope (hva som vurderes)

- `modules/*/content/*.md` (primært)
- `modules/*/config.py` med `QUESTIONS`/`STATEMENTS` (deltaker-spørsmål)
- `modules/*/claude_answers.py` (referansesvar)
- `module_header(subtitle=...)`, `crumb`, `st.subheader`-prosa i `app_logic.py` (ikke kode-logikk)

## Fremgangsmåte

1. **Finn modulene** (datakilden kan ha endret seg siden sist):
   ```bash
   for d in $(find modules -maxdepth 1 -mindepth 1 -type d | sort); do
     n=$(basename "$d"); [ "$n" = "shared" ] && continue
     { [ -d "$d/content" ] && [ -n "$(find "$d/content" -name '*.md')" ]; } || \
       { [ -f "$d/config.py" ] && grep -qE "QUESTIONS|STATEMENTS" "$d/config.py"; } && echo "$n"
   done
   ```
2. **Kjør workflowen** `eval_workflow.js` (i denne skill-mappa). Sett `MODULES`-arrayen øverst i scriptet til lista fra steg 1 (bruk Edit), og kjør via `Workflow({scriptPath: "<sti til eval_workflow.js>"})`. Den fan-out-er 1 score-agent per modul (schema-validert output), samler høyrisiko-påstander (R≥4, web-verifiserbare), og web-verifiserer topp ~18 mot `docs.snowflake.com/en/user-guide/cortex-code/`.
   - Merk: ikke stol på `args`-innsending til workflowen (har vært ustabil) - rediger `MODULES` direkte.
3. **Bygg rapporten:** kjør `build_report.py <workflow-output-fil>` (output-fila er `…/tasks/<taskid>.output`; resultatet ligger under nøkkelen `result`). Den skriver `CONTENT_REVIEW.md` med: aggregat, modul-heatmap (alle moduler × metrikkene), §2 «må verifiseres» (R≥4), §3 tomt/placeholder, §4 lav relevans/verdi, §5 web-verifikasjon.
4. **Legg til Hovedfunn:** les ut `motsagt` + `delvis støttet`-verifikasjonene fra output-fila, spor hver til kildefil (`grep` på sitatet), og skriv en kort, prioritert «Hovedfunn»-seksjon øverst i `CONTENT_REVIEW.md` (sannsynlig feil → må rettes; bekreftet korrekt; modenhet; anbefalt handling).
5. **Verifiser rapporten:** bekreft at antall heatmap-rader = antall moduler, og stikkprøv 2-3 flaggede sitater mot kildefil.

## Viktige forbehold (skal stå i rapporten)

- Faktuell score på produktpåstander er begrenset; web-verdikt gjøres av agenter mot offentlige docs - Andre bør selv sjekke `motsagt`-funn mot sitert URL.
- Cortex Code ER dokumentert (`docs.snowflake.com/en/user-guide/cortex-code/`, inkl. `/tools`, `/cli-reference`) - de fleste «uverifiserte» påstandene er sjekkbare.
- UTKAST/placeholder straffes på Fullføring, ikke på Faktuell.

## Output

`CONTENT_REVIEW.md` i repo-rot + et kort sammendrag i chat (topp-funn + hva som må verifiseres/fylles før kurs). Ingen innholdsendringer.
