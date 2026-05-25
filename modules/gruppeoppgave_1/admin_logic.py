"""Presentatør-/admin-logikk for Gruppeoppgave 1 (workshop om AGENTS.md).

Implementerer PRD §FR-3.7 (admin-tabs), §FR-3.4 (visualisering),
§FR-3.6 ("Hva glemte vi?"-diff) og §NFR-4.2 (passord-gate).

Hovedresultater (Resultater-tab) ligger i `views.py` slik at modul 13
(offentlig resultatvisning) kan dele samme rendering uten å duplisere.

Eksponerer `main()` som kalles fra `pages/admin_gruppeoppgave_1.py`. Setter
IKKE `st.set_page_config` — det gjøres i wrapperen.
"""

from __future__ import annotations

import csv
import hmac
import io

import streamlit as st
from streamlit_autorefresh import st_autorefresh

from .claude_answers import CLAUDE_ANSWERS_Q1, CLAUDE_ANSWERS_Q2
from .config import QUESTIONS, REFRESH_INTERVAL_MS
from .db import delete_all_responses, delete_response, fetch_all_responses
from modules.shared.ui import callout, crumb

from .reducer import reduce_answers
from .views import cached_text_answers, render_results
from .viz import render_wordcloud


def _check_password() -> bool:
    # PRD §NFR-4.2: konstant-tid passordsjekk via hmac.compare_digest.
    if st.session_state.get("admin_ok"):
        return True

    st.title("Presentatør-innlogging")
    pwd = st.text_input("Passord", type="password")
    if st.button("Logg inn", type="primary"):
        expected = st.secrets.get("ADMIN_PASSWORD", "")
        if expected and hmac.compare_digest(pwd, expected):
            st.session_state.admin_ok = True
            st.rerun()
        else:
            callout("Feil passord.", kind="warning", key="admin_login_error")
    return False


# PRD §NFR-4.3: cache DB-spørringer 5 sek for å unngå hammer ved auto-refresh.
@st.cache_data(ttl=5)
def _cached_all_responses() -> list[dict]:
    return fetch_all_responses()


def _diff_tokens(claude_tokens: list[str], user_tokens: list[str]) -> list[str]:
    # PRD §FR-3.6: tokens som finnes i Claude-svar men ikke i deltakersvar.
    # Duplikater fra Claude beholdes — frekvens styrer størrelse i diff-skyen.
    user_set = set(user_tokens)
    return [t for t in claude_tokens if t not in user_set]


def _render_forgotten() -> None:
    st.caption(
        "Ordsky over begreper Claude nevnte (i bank-/analysekontekst) "
        "som ikke dukket opp i deltakernes svar. Bruk som diskusjonsfôr — "
        "ikke som fasit."
    )

    answers_1 = cached_text_answers(1)
    user_tokens_1 = reduce_answers(answers_1)
    claude_tokens_1 = reduce_answers(CLAUDE_ANSWERS_Q1)
    diff_1 = _diff_tokens(claude_tokens_1, user_tokens_1)
    render_wordcloud(diff_1, f"Glemt – {QUESTIONS[1]['text']}")
    st.caption(
        f"{len(set(claude_tokens_1))} unike Claude-ord · "
        f"{len(set(user_tokens_1))} unike deltaker-ord · "
        f"{len(set(diff_1))} unike begreper kun fra Claude"
    )

    st.divider()

    answers_2 = cached_text_answers(2)
    user_tokens_2 = reduce_answers(answers_2)
    claude_tokens_2 = reduce_answers(CLAUDE_ANSWERS_Q2)
    diff_2 = _diff_tokens(claude_tokens_2, user_tokens_2)
    render_wordcloud(diff_2, f"Glemt – {QUESTIONS[2]['text']}")
    st.caption(
        f"{len(set(claude_tokens_2))} unike Claude-ord · "
        f"{len(set(user_tokens_2))} unike deltaker-ord · "
        f"{len(set(diff_2))} unike begreper kun fra Claude"
    )


def _render_moderation() -> None:
    st.subheader("🧹 Moderering")
    st.caption("Slett enkeltsvar hvis noe upassende dukker opp.")

    rows = _cached_all_responses()
    if not rows:
        st.write("Ingen svar ennå.")
        return

    for row in rows:
        content = row.get("answer_text") or row.get("answer_choice") or "(tomt)"
        qid = row["question_id"]
        cols = st.columns([1, 1, 6, 1])
        cols[0].write(f"#{row['id']}")
        cols[1].write(f"Q{qid}")
        cols[2].write(content)
        if cols[3].button("Slett", key=f"del_{row['id']}"):
            delete_response(row["id"])
            st.cache_data.clear()
            st.rerun()


def _render_export() -> None:
    rows = _cached_all_responses()
    if not rows:
        st.write("Ingen data å eksportere.")
        return

    buf = io.StringIO()
    writer = csv.DictWriter(
        buf,
        fieldnames=["id", "question_id", "answer_text", "answer_choice", "created_at"],
    )
    writer.writeheader()
    for row in rows:
        writer.writerow({k: row.get(k, "") for k in writer.fieldnames})

    st.download_button(
        label="Last ned CSV",
        data=buf.getvalue(),
        file_name="gruppeoppgave_1_svar.csv",
        mime="text/csv",
    )


def _render_danger_zone() -> None:
    st.subheader("⚠️ Nullstill runde")
    callout(
        "Sletter ALLE svar. Bruk før ny kurssesjon.",
        kind="warning",
        key="admin_danger_notice",
    )
    confirm = st.text_input("Skriv 'SLETT' for å bekrefte")
    if st.button("Slett alle svar", type="primary", disabled=(confirm != "SLETT")):
        delete_all_responses()
        st.cache_data.clear()
        callout(
            "Alle svar slettet.",
            kind="highlight",
            key="admin_danger_done",
        )


def main() -> None:
    if not _check_password():
        return

    crumb(["Administrasjon", "Gruppeoppgave 1"])
    st.title("Presentatør · Gruppeoppgave 1")

    tab_results, tab_forgot, tab_mod, tab_export, tab_danger = st.tabs(
        ["Resultater", "Hva glemte vi?", "Moderering", "Eksport", "Nullstill"]
    )

    with tab_results:
        auto = st.toggle("Auto-refresh (10 sek)", value=True, key="auto_results")
        if auto:
            st_autorefresh(interval=REFRESH_INTERVAL_MS, key="results_refresh")
        if st.button("Refresh nå", key="refresh_results"):
            st.cache_data.clear()
            st.rerun()
        render_results()

    with tab_forgot:
        if st.button("Refresh nå", key="refresh_forgot"):
            st.cache_data.clear()
            st.rerun()
        _render_forgotten()

    with tab_mod:
        _render_moderation()

    with tab_export:
        _render_export()

    with tab_danger:
        _render_danger_zone()
