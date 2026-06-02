**Prompt - lim inn i Cortex Code:**

```
Skriv en SQL-spørring som finner topp 10 % kunder etter transaksjonsvolum siste 90 dager, gruppert per kunde. Returner kundenr, alderssegment, volum og rank.
```

En relativt grei oppgave hvor begge modeller sannsynligvis treffer. Legg merke til hvordan hver av dem definerer "topp 10 %" (PERCENT_RANK, NTILE, QUALIFY ...) og om de håndterer 90-dagers-vinduet likt.
