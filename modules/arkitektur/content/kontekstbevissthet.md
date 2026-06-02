**Hva er Kontekstbevissthet?**

Kontekstbevissthet er agentens evne til å vite **hva brukeren ser og gjør
akkurat nå** i Snowsight-grensesnittet.

**To mekanismer:**

**1. Sidekontekst (`get_page_context`)**
- Hvilken side brukeren er på (Notebook, Worksheet, Dashboard, osv.)
- Aktivt innhold på siden

**2. Aktive resultater (`read_active_pane`)**
- SQL-resultater som vises i Results-panelet
- Feilmeldinger fra kjøring
- Kolonnedefinisjoner og data

**Hvorfor det er viktig:**

Uten dette ville agenten vært "blind" - den måtte spørre brukeren om alt.
Med kontekstbevissthet kan den:

- Se en feilmelding og foreslå en fiks direkte
- Forstå hvilken notebook du jobber i
- Vite hvilke resultater du ser på

Det er agentens **"syn" inn i brukergrensesnittet** - den ser det du ser,
og kan svare deretter.
