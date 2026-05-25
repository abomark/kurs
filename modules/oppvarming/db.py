"""Supabase-klient for Oppvarming-modulen (Likert-variant).

Implementerer PRD §DM-5.2 (felles `kurs`-schema) og §NFR-4.2 (RLS / minimal returning).

Tabell: `kurs.oppvarming_responses`. Kolonner: id, question_id (1–5),
answer_value (1–5 heltall — Likert), created_at.
"""

from __future__ import annotations

import streamlit as st
from supabase import Client, create_client
from supabase.client import ClientOptions

# PRD §DM-5.2: alle moduler deler schema `kurs`. Tabellen navngis per modul.
SCHEMA = "kurs"
TABLE = "oppvarming_responses"


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


def insert_likert_responses(values: dict[int, int]) -> None:
    """Bulk-insert: alle 5 påstandssvar på én gang.

    `values` er {question_id: answer_value} der answer_value er 1–5.
    """
    rows = [
        {"question_id": qid, "answer_value": val}
        for qid, val in values.items()
    ]
    anon_client().table(TABLE).insert(
        rows,
        returning="minimal",  # PRD §NFR-4.2: anon har ikke SELECT-rettighet
    ).execute()


def fetch_value_counts(question_id: int) -> dict[int, int]:
    """Tell hvor mange svar som har valgt hver verdi 1–5 for et spørsmål."""
    res = (
        service_client()
        .table(TABLE)
        .select("answer_value")
        .eq("question_id", question_id)
        .execute()
    )
    counts = {v: 0 for v in range(1, 6)}
    for row in res.data:
        val = row.get("answer_value")
        if val in counts:
            counts[val] += 1
    return counts


def delete_all_responses() -> None:
    service_client().table(TABLE).delete().neq("id", -1).execute()
