-- Kjør i Supabase SQL Editor.
-- Implementerer PRD §DM-5.1 (responses-tabell) og §NFR-4.2 (RLS: anon kun INSERT).
-- Oppretter `kurs`-schema, responses-tabellen, indeks og RLS-policy.
--
-- VIKTIG manuelt steg etterpå:
--   Gå til Project Settings → API → "Data API Settings" → "Exposed schemas"
--   og legg til "kurs" (komma-separert). Uten dette vil PostgREST/supabase-py
--   ikke kunne nå tabellen.

create schema if not exists kurs;

grant usage on schema kurs to anon, authenticated, service_role;

create table if not exists kurs.responses (
  id            bigserial primary key,
  question_id   smallint     not null check (question_id between 1 and 4),
  answer_text   text,
  answer_choice text,
  created_at    timestamptz  not null default now(),
  check (
    (answer_text is not null and answer_choice is null)
    or (answer_text is null and answer_choice is not null)
  )
);

create index if not exists responses_question_created_idx
  on kurs.responses (question_id, created_at desc);

-- service_role: full tilgang (brukes av admin-siden)
grant select, insert, update, delete on kurs.responses to service_role;

-- anon: kan kun sette inn nye svar (krever også sequence-tilgang for bigserial)
grant insert on kurs.responses to anon;
grant usage, select on sequence kurs.responses_id_seq to anon;

alter table kurs.responses enable row level security;

drop policy if exists "anon can insert" on kurs.responses;
create policy "anon can insert"
  on kurs.responses
  for insert
  to anon
  with check (true);

-- Ingen anon-SELECT-policy: lesing skjer kun via service_role (admin).
