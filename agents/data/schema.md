# data/schema.md — Database og Supabase

**Lesing:** Før du arbeider med database, Supabase, eller brukerdata.

---

## Grunnleggende

- **Schema:** `kurs` (alle tabeller lever i samme schema)
- **RLS (Row Level Security):** Aktivert — `anon_client` kan kun INSERT; `service_client` brukes for SELECT/DELETE (holdes hemmelig)
- **Minimal returning:** Alltid `returning="minimal"` på INSERT fra anon (PRD §NFR-4.2)

## Klienter

Fra `modules/<modul>/db.py`:

```python
from modules.<modul>.db import anon_client, service_client

# Deltaker: kun INSERT
anon_client().table("<table>").insert({...}, returning="minimal").execute()

# Admin: SELECT, DELETE
service_client().table("<table>").select("*").execute()
```

## Tabeller per modul

Hvis en interaktiv modul trenger å lagre brukerrespons:

- **Tabell:** `kurs.<modul>_responses`
- **Fil:** `modules/<modul>/db.py` (jf. `modules/gruppeoppgave_1/db.py` som mal)
- **Secrets:** `SUPABASE_URL` og `SUPABASE_ANON_KEY` (anon) eller `SUPABASE_SERVICE_KEY` (admin) fra `.streamlit/secrets.toml`

## Admin-panelet

Hver modul med data kan ha et `admin_logic.py` som:
- Henter `fetch_all_responses()` via `service_client`
- Viser resultater i tabeller/grafer (jf. `modules/gruppeoppgave_1_resultater/views.py`)
- Tillater sletting via `delete_response()` eller `delete_all_responses()`

## Når du lager en ny tabell

1. Definér schema i `modules/<modul>/supabase_schema.sql` (om nødvendig)
2. Eksponér via Supabase dashboard (schema `kurs` må være i "Exposed schemas")
3. Opprett klient-funksjoner i `modules/<modul>/db.py`
4. Dokumenter tabell-struktur i PRD §DM-5

**Merk:** Ingen hardkodede credentials. Alltid `st.secrets`.
