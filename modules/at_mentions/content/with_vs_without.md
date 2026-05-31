### Med `@`-mention

> Lag en spørring som joiner `@KURS_CORTEX_2026.MART.CUSTOMERS` med
> `@KURS_CORTEX_2026.MART.TRANSACTIONS`

Snowsight gjenkjenner referansene → henter metadata → injiserer struktur
i konteksten. Agenten **vet** hvilke kolonner som finnes, hvilke tags som
gjelder, og hvordan tabellene henger sammen.

### Uten `@`-mention

> Lag en spørring som joiner KURS_CORTEX_2026.MART.CUSTOMERS med
> KURS_CORTEX_2026.MART.TRANSACTIONS

Cortex Code leser det som tekst. Den vil _sannsynligvis_ forstå at det
er tabellnavn og slå dem opp i Horizon Catalog — men det er en **inferens
den gjør**, ikke faktagrunnlag den får servert.
