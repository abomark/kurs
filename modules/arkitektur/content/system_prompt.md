**Hva er et system-prompt?**

Et system-prompt er et sett med instruksjoner som gis til språkmodellen
_før_ brukeren begynner å interagere. Det definerer:

- **Hvem agenten er** - navn, rolle, tone
- **Hva den kan og ikke kan** - regler, begrensninger, sikkerhet
- **Hvordan den skal oppføre seg** - arbeidsflyt, verktøybruk, formatering
- **Hvilke verktøy som er tilgjengelige** og når de skal brukes

Brukeren ser normalt ikke system-promptet - det er "backstage-instruksjonene"
som styrer agentens oppførsel i hver samtale.

**For Cortex Code definerer system-promptet:**

- Oppførsel, tone, sikkerhetsregler og begrensninger
- Domenespesifikke regler (Snowflake, dbt, SQL, notebooks)
- Prioriteringsregler ved konflikter
- Konkrete krav: vær kortfattet, bruk TODO-lister, valider SQL før levering,
  avslør aldri hemmeligheter
