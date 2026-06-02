# Gruppeoppgave 1 - AGENTS.md

Interaktiv workshop om AGENTS.md med live ordskyer og barcharts. Brukes som modul 7 i kursrekken, etter konseptuelle innføringer i modul 5 (AGENTS.md) og modul 6 (skills.md). Entry-point er `hub.py` på repo-rot.

## Hva den gjør

Stiller fire spørsmål:

1. Hva bør være i AGENTS.md? *(fritekst → ordsky, topp 10)*
2. Hva bør IKKE være i AGENTS.md? *(fritekst → ordsky, topp 10)*
3. Bør AGENTS.md være personlig eller felles? *(valg → barchart)*
4. Vil AGENTS.md øke eller redusere kostnader? *(valg → barchart)*

Alle svar lagres anonymt i Supabase. Presentatøren ser live oppdaterte visualiseringer på admin-siden, inkludert en "Hva glemte vi?"-tab som viser begreper Claude foreslo (for bank-/analysekontekst) men deltakere ikke nevnte.

## Filer

```
modules/gruppeoppgave_1/
├── app_logic.py            # Deltaker-skjema (kalt fra pages/gruppeoppgave_1.py)
├── admin_logic.py          # Admin (kalt fra pages/admin_gruppeoppgave_1.py)
├── db.py                   # Supabase-klient (schema: kurs)
├── reducer.py              # MVP: ren-Python ordreduksjon
├── viz.py                  # Wordcloud + barchart (topp 10)
├── config.py               # Spørsmål, alternativer, stopwords
├── claude_answers.py       # Referansesvar for "Hva glemte vi?"
└── supabase_schema.sql     # Tabell + RLS-policy
```

## Supabase-oppsett

1. Opprett prosjekt på [supabase.com](https://supabase.com).
2. Kjør innholdet i [`supabase_schema.sql`](supabase_schema.sql) i SQL Editor - lager `kurs`-schema, `responses`-tabell og RLS-policy.
3. **Eksponer schemaet:** Project Settings → API → "Data API Settings" → "Exposed schemas" → legg til `kurs` (komma-separert med `public, graphql_public`), lagre.
4. Kopier `Project URL`, `anon public key` og `service_role key` til `.streamlit/secrets.toml` på repo-rot.

## Sikkerhet

- `anon`-key kan kun INSERT (RLS-policy). Trygt å eksponere i klienten.
- `service_role`-key leses kun av admin_logic. Aldri commit secrets.
- `db.py` bruker `returning="minimal"` på inserts så anon ikke trenger SELECT-rettigheter.
- `PARTICIPANT_CODE` i secrets.toml gir et muntlig delt soft-gate foran deltakersiden (valgfritt).

## Bytte til AI-reduksjon

I MVP reduseres svar via `reducer.py` (stopword-filter). For AI-versjon:

1. Lag `reducer_ai.py` med samme signatur (`reduce_answers(list[str]) -> list[str]`) som kaller Claude med prompten i kursnotatene.
2. Endre import i `admin_logic.py` fra `from .reducer import` til `from .reducer_ai import`.

## Personvern

- Ingen identifikatorer lagres (ingen IP, session-ID, cookies).
- Deltakere oppfordres til ikke å skrive navn eller bedriftshemmeligheter.
- Resultater vises kun når minst 3 svar er inne (MIN_RESPONSES_BEFORE_REVEAL).
- Presentatør kan slette enkeltsvar via Moderering-fanen.
