**Prompt - lim inn i Cortex Code:**

```
Skriv en SQL-spørring som finner kunder som var aktive første halvår 2025 (minst en transaksjon i januar-juni), men som ikke har noen transaksjoner i andre halvår (juli-desember). Beregn frafallsrate per alderssegment: antall frafalte delt på antall aktive i første halvår. Returner alderssegment, antall aktive i H1, antall frafalt og frafallsrate, sortert synkende på frafallsrate.
```

Her er det mer å feile på: anti-join (finne kunder *uten* aktivitet i en periode), to tidsvinduer, og en rate som må regnes på riktig nivå (per segment, ikke per kunde). Se spesielt om modellen **stopper og avklarer antakelser** (hva betyr "aktiv"? hele 2025?) framfor å gjette. Det er ofte her Opus skiller seg.
