-- Kjør i Supabase SQL Editor for Oppvarming-modulen (modul 0 — Likert-variant).
-- Implementerer PRD §DM-5.1 og §NFR-4.2.
--
-- Tabellen ligger i det FELLES `kurs`-schemaet (PRD §DM-5.2).
-- Kolonnen `answer_value` er heltall 1–5 (Likert-skala der 1 = uenig, 5 = enig).
--
-- Forutsetninger:
--   - `kurs`-schemaet eksisterer allerede (opprettet av gruppeoppgave_1).
--   - `kurs` er allerede i Supabase "Exposed schemas".
--
-- VIKTIG: hvis du har eksisterende `oppvarming_responses`-tabell med
-- `answer_choice text`-kolonne fra forrige iterasjon, må du droppe og
-- gjenoppbygge. Kjør hele blokken nedenfor.

drop table if exists kurs.oppvarming_responses cascade;

create table kurs.oppvarming_responses (
  id            bigserial primary key,
  question_id   smallint     not null check (question_id between 1 and 15),
  answer_value  smallint     not null check (answer_value between 1 and 5),
  created_at    timestamptz  not null default now()
);

create index oppvarming_responses_question_created_idx
  on kurs.oppvarming_responses (question_id, created_at desc);

grant insert on kurs.oppvarming_responses to anon;
grant select, insert, update, delete on kurs.oppvarming_responses to service_role;
grant usage, select on sequence kurs.oppvarming_responses_id_seq to anon, service_role;

alter table kurs.oppvarming_responses enable row level security;

drop policy if exists "anon can insert" on kurs.oppvarming_responses;
create policy "anon can insert"
  on kurs.oppvarming_responses
  for insert
  to anon
  with check (true);

-- Ingen anon-SELECT-policy: lesing skjer via service_role server-side.

notify pgrst, 'reload schema';
