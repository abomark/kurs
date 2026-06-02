# Kurs

Interaktive kursmoduler bygget med Streamlit + Supabase. PRD og struktur-regler i [`PRD.md`](PRD.md) og [`CLAUDE.md`](CLAUDE.md).

URL-er (under deploy):
- `/` – forside med modul-oversikt
- `/oppvarming` – Bli kjent (oppvarming, før modul 1)
- `/oppvarming_resultater` – Resultater Bli kjent
- `/cortex_code` – Modul 1: Cortex Code
- `/cortex_interaction` – Modul 2: Snowsight vs CLI
- `/cortex_in_snowsight` – Modul 3: Cortex Code i Snowsight
- `/demo_1` – Modul 4: Første demo (runbook)
- `/agents_md` – Modul 5: AGENTS.md (konsept)
- `/skills_md` – Modul 6: skills.md (konsept)
- `/gruppeoppgave_1` – Modul 7: Gruppeoppgave 1 (workshop om AGENTS.md)
- `/gruppeoppgave_1_resultater` – Modul 8: Resultater Gruppeoppgave 1 (offentlig, kun grafer)
- `/individuell_oppgave_1` – Modul 9: Individuell oppgave 1 (Git repo setup)
- `/individuell_oppgave_2` – Modul 10: Beskrive ukjent tabell
- `/demo_2` – Modul 14: Demo 2 (realistisk bank-use-case)
- `/autonomous_loop` – Modul 15: Autonomous loop i dybden
- `/avslutning` – Modul 16: Avslutning
- `/admin_gruppeoppgave_1` – Presentatør-side for Gruppeoppgave 1 (passordbeskyttet)

## Struktur

```
kurs/
├── hub.py                          # Entry: st.navigation (streamlit run hub.py)
├── home.py                         # Forside-innhold (modul-katalog)
├── pages/                          # Streamlit multipage – URL per fil
│   ├── cortex_code.py
│   ├── cortex_interaction.py
│   ├── cortex_in_snowsight.py
│   ├── demo_1.py
│   ├── agents_md.py
│   ├── skills_md.py
│   ├── gruppeoppgave_1.py
│   └── admin_gruppeoppgave_1.py
├── modules/
│   ├── oppvarming/                 # Bli kjent (interaktiv, tabell=kurs.oppvarming_responses)
│   ├── oppvarming_resultater/      # Resultater Bli kjent (offentlig read-only)
│   ├── cortex_code/                # Modul 1 (presentasjon)
│   ├── cortex_interaction/         # Modul 2
│   ├── cortex_in_snowsight/        # Modul 3
│   ├── demo_1/                     # Modul 4
│   ├── agents_md/                  # Modul 5 (presentasjon)
│   ├── skills_md/                  # Modul 6 (presentasjon)
│   ├── gruppeoppgave_1/            # Modul 7 (interaktiv, bruker Supabase)
│   ├── gruppeoppgave_1_resultater/ # Modul 8 (offentlig read-only)
│   ├── individuell_oppgave_1/      # Modul 9 (Git repo setup)
│   ├── individuell_oppgave_2/      # Modul 10 (Beskrive ukjent tabell)
│   ├── demo_2/                     # Modul 14 (Realistisk bank-use-case)
│   ├── autonomous_loop/            # Modul 15 (Loop i dybden)
│   ├── avslutning/                 # Modul 16 (Hva nå?)
│   └── shared/                     # Felles loader-helpers (FR-3.12)
├── .streamlit/secrets.toml         # IKKE i git
├── requirements.txt
└── README.md
```

## Komme i gang

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .streamlit/secrets.toml.example .streamlit/secrets.toml
# Fyll inn Supabase-keys og passord i .streamlit/secrets.toml
streamlit run hub.py
```

Se [`modules/gruppeoppgave_1/README.md`](modules/gruppeoppgave_1/README.md) for detaljer om Supabase-oppsett (schema, RLS, eksponering) for den interaktive modulen.

## Legge til en ny modul

Se [`CLAUDE.md`](CLAUDE.md) "Når du legger til en ny modul" for full sjekkliste. Kort versjon:

1. Lag mappa `modules/<navn>/` med `__init__.py`, `app_logic.py` og `content/`-mappe (FR-3.12).
2. Lag `pages/<navn>.py` som tynn wrapper (set_page_config + `from modules.<navn>.app_logic import main; main()`).
3. Legg modulen til i `hub.py` og `home.py`.
4. Hvis modulen trenger database: lag tabell `kurs.<navn>_responses` (felles `kurs`-schema, PRD §DM-5.2). Kjør tilhørende SQL i Supabase. Ingen dashboard-endring nødvendig.
