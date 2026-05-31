Når du sender prompten, henter Snowsight-laget proaktivt ut **full metadata
for hver `@`-mention** og injiserer det i agentens kontekst som
**strukturerte data**, ikke som tekst.

Det betyr at agenten ser:

- **Eksakt kolonnenavn og datatyper**
- **Eventuelle masking policies** som gjelder
- **Tags** (PII-klassifisering, sensitivitetsnivå)
- **Beskrivelser fra `schema.yml`** hvis det er en dbt-tabell
- **Lineage** hvis tilgjengelig
- **Sample-statistikk** (radantall, eventuelt distinct counts)

Med andre ord: agenten trenger ikke gjette eller slå opp — den får alt
servert som faktagrunnlag før den tenker på spørsmålet ditt.
