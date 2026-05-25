-- Kjør i Supabase SQL Editor.
-- Implementerer PRD §DM-5.2 (felles `kurs`-schema, tabell-prefix per modul)
-- og §NFR-4.2 (RLS: anon kun INSERT).
--
-- `kurs`-schema er allerede opprettet og eksponert via Supabase API.

create table if not exists kurs.gruppeoppgave_3_responses (
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

create index if not exists gruppeoppgave_3_responses_question_created_idx
  on kurs.gruppeoppgave_3_responses (question_id, created_at desc);

-- service_role: full tilgang (brukes av admin-siden)
grant select, insert, update, delete on kurs.gruppeoppgave_3_responses to service_role;

-- anon: kan kun sette inn nye svar (krever også sequence-tilgang for bigserial)
grant insert on kurs.gruppeoppgave_3_responses to anon;
grant usage, select on sequence kurs.gruppeoppgave_3_responses_id_seq to anon;

alter table kurs.gruppeoppgave_3_responses enable row level security;

drop policy if exists "anon can insert" on kurs.gruppeoppgave_3_responses;
create policy "anon can insert"
  on kurs.gruppeoppgave_3_responses
  for insert
  to anon
  with check (true);

-- Ingen anon-SELECT-policy: lesing skjer kun via service_role (admin / resultater-side).
