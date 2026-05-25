"""Supabase-klient og dataaksess.

Implementerer PRD §DM-5.1 (responses-tabell) og §NFR-4.2 (RLS / minimal returning).

To klienter eksponeres:
  - `anon_client()` for deltakerens INSERT (RLS tillater kun innsetting).
  - `service_client()` for admin (SELECT/DELETE — service_role-key må holdes hemmelig).
"""

from __future__ import annotations

import streamlit as st
from supabase import Client, create_client
from supabase.client import ClientOptions

# PRD §DM-5.2: ett Postgres-schema per modul; må også eksponeres via Supabase API.
SCHEMA = "kurs"


@st.cache_resource
def anon_client() -> Client:
    return create_client(
        st.secrets["SUPABASE_URL"],
        st.secrets["SUPABASE_ANON_KEY"],
        options=ClientOptions(schema=SCHEMA),
    )


@st.cache_resource
def service_client() -> Client:
    return create_client(
        st.secrets["SUPABASE_URL"],
        st.secrets["SUPABASE_SERVICE_KEY"],
        options=ClientOptions(schema=SCHEMA),
    )


def insert_text_response(question_id: int, answer_text: str) -> None:
    anon_client().table("responses").insert(
        {"question_id": question_id, "answer_text": answer_text.strip()},
        returning="minimal",  # PRD §NFR-4.2: anon har ikke SELECT-rettighet
    ).execute()


def insert_choice_response(question_id: int, answer_choice: str) -> None:
    anon_client().table("responses").insert(
        {"question_id": question_id, "answer_choice": answer_choice},
        returning="minimal",  # PRD §NFR-4.2: anon har ikke SELECT-rettighet
    ).execute()


def fetch_text_answers(question_id: int) -> list[str]:
    res = (
        service_client()
        .table("responses")
        .select("answer_text")
        .eq("question_id", question_id)
        .execute()
    )
    return [row["answer_text"] for row in res.data if row.get("answer_text")]


def fetch_choice_counts(question_id: int, options: list[str]) -> dict[str, int]:
    res = (
        service_client()
        .table("responses")
        .select("answer_choice")
        .eq("question_id", question_id)
        .execute()
    )
    counts = {opt: 0 for opt in options}
    for row in res.data:
        choice = row.get("answer_choice")
        if choice in counts:
            counts[choice] += 1
    return counts


def fetch_all_responses() -> list[dict]:
    res = (
        service_client()
        .table("responses")
        .select("*")
        .order("created_at", desc=True)
        .execute()
    )
    return res.data


def delete_response(response_id: int) -> None:
    service_client().table("responses").delete().eq("id", response_id).execute()


def delete_all_responses() -> None:
    service_client().table("responses").delete().neq("id", -1).execute()
