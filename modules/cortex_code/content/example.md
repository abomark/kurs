**Du skriver:** *«Lag en månedsrapport over kundefrafall siste år.»*

**Cortex Code (autonom loop):**

1. Sjekker hvilken **rolle og database** du er logget inn med
2. Finner relevante tabeller (`customers`, `churn_events`) i schemaet
3. Skriver SQL som **respekterer dine RBAC-rettigheter**
4. Kjører spørringen, **validerer at resultatet ser fornuftig ut**
5. Returnerer både koden og resultatet, klar for review

_Poenget: du sa hva du ville ha - agenten bestemte selv stegene som skulle til._
