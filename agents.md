# agents.md — Instruksjoner for Claude på dette prosjektet

## Grunnleggende

Du skal jobbe med **Norsk Bankkurs** — en Streamlit-app for analytikere og data scientists i norske banker.

**Autoritet:** Les [PRD.md](PRD.md) før du gjør større endringer. Koden skal alltid være i sync med PRD-en.

**Språk:** Norsk i markdown og kommentarer; engelsk kun i kode (variabelnavn, funksjoner, imports).

---

## Når du skal gjøre noe spesifikt

- **Før du endrer visuell stil eller layout:** Les [agents/design/style.md](agents/design/style.md)
- **Før du skriver eller endrer kode:** Les [agents/code/style.md](agents/code/style.md)
- **Før du svarer eller forklarer noe:** Les [agents/communication.md](agents/communication.md)
- **Før du lager en ny modul eller side:** Les [agents/modules.md](agents/modules.md)
- **Før du jobber med database eller Supabase:** Les [agents/data/schema.md](agents/data/schema.md)
- **Før du lager en visualisering (plot, diagram, etc.):** Les [agents/viz.md](agents/viz.md)

---

## Hvis du er usikker

1. Sjekk PRD.md → CLAUDE.md → den relevante undermodulen
2. Hvis PRD og kode divergerer: avklar med eier før endring
3. Aldri silent drift — si fra hvis noe er uklart

---

## Åpne filer som referanse

Du har tilgang til:
- `CLAUDE.md` — generelle regler for prosjektet
- `DESIGN_GUIDE.md` — visuell stil og designsystem
- `.streamlit/config.toml` — aktuelt tema
- `data/moduler.py` — modul-registry
