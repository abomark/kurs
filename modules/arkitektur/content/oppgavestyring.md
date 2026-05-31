**Hva er Oppgavestyring?**

Oppgavestyring er agentens innebygde mekanisme for å **planlegge og spore
fremdrift** på komplekse oppgaver.

**Slik fungerer det:**

- Verktøyet `system_todo_write` lar agenten opprette en TODO-liste
- Hver oppgave har en status: `pending` → `in_progress` → `completed`
- Kun én oppgave skal være `in_progress` om gangen

**Når det brukes:**

- Oppgaven har 3+ steg
- Brukeren gir flere ting å gjøre
- Komplekse oppgaver som krever planlegging

**Eksempel** — bruker sier: _"Bygg en dbt-modell, test den, og deploy den"_

Agenten lager:

```
[x] Undersøk eksisterende prosjektstruktur   (completed)
[~] Skriv dbt-modellen                         (in_progress)
[ ] Legg til tester                            (pending)
[ ] Kjør dbt build                             (pending)
```

**Det er ikke:**

- En separat modul eller ekstern tjeneste
- En egen planner-/executor-arkitektur

Det er bare en **strukturert tekstliste agenten vedlikeholder for seg selv**,
synlig for brukeren, som sikrer at ingen steg glemmes i en flerstegsoppgave.
