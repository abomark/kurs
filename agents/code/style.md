# code/style.md — Kodestil

**Lesing:** Før du skriver eller endrer kode.

---

## Språk

- **Norsk:** kommentarer, docstrings, variabler som er domain-spesifikke (f.eks. `svar_tekst`)
- **Engelsk:** imports, funksjoner, klassenavn, generiske variables (`data`, `client`, `response`)

## Kommentarer

- **En kort linje**, ikke flerlinjers blokker — koden skal være selvforklarende
- **Kun når WHY er ikke-åpenbar** — verborgne regler, workarounds for spesifikke bugs, hidden constraints
- PRD-referanser når aktuelt (jf. CLAUDE.md): `# PRD §FR-3.4: skjul resultater til minst 3 svar`

Ikke skriv WHAT-kommentarer — funksjonnavn og variabler forteller allerede hva som skjer.

## Formatering

- **Import-rekkefølge:** `__future__` → `stdlib` → `third-party` → `local` (jf. PEP 8)
- **Typehints:** Bruk dem — prosjektet bruker type-sjekking
- **Docstrings:** Én linje hvis det holder; flerlinjer kun hvis nødvendig

## Når du legger til kode

- Ikke legg til feil-håndtering for scenarios som ikke kan skje (sikkerhet: kun grensesnitt, ikke internt)
- Ikke lag abstraksjonslag før du har 3+ identiske mønstre
- Slett død kode — ikke legg til `# removed` kommentarer eller omdøp til `_unused`

## Konvensjoner i dette prosjektet

- Filer i `modules/<navn>/` bruker **relative imports**: `from .config import ...`
- Wrappers i `pages_content/modules/` bruker **absolutt import**: `from modules.<slug>.app_logic import main as render`
- Streamlit-secrets alltid via `st.secrets[...]` — aldri hardkodert
