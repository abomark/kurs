**Prompt - lim inn i Cortex Code:**

```
Skriv en SQL-spørring som finner kunder som var aktive første halvår 2025 (minst en transaksjon i januar-juni), men som ikke har noen transaksjoner i andre halvår (juli-desember). Beregn frafallsrate per alderssegment: antall frafalte delt på antall aktive i første halvår. Returner alderssegment, antall aktive i H1, antall frafalt og frafallsrate, sortert synkende på frafallsrate.
```

Denne er mer krevende. Her må modellen håndtere anti-join, to tidsvinduer og riktig beregningsnivå per segment.
