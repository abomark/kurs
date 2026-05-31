"""Presentatør-/admin-logikk for Gruppeoppgave 3 (workshop om memory.md).

Implementerer PRD §FR-3.7 (admin-tabs), §FR-3.4 (visualisering)
og §NFR-4.2 (passord-gate).

Hovedresultater (Resultater-tab) ligger i `views.py` slik at
gruppeoppgave_3_resultater (offentlig) kan dele samme rendering uten å
duplisere.

Eksponerer `main()` som kalles fra `pages_content/admin.py`. Setter
IKKE `st.set_page_config`.
"""

from __future__ import annotations

import csv
import hmac
import io

import streamlit as st
from streamlit_autorefresh import st_autorefresh

from modules.shared.ui import callout, crumb

from .config import REFRESH_INTERVAL_MS
from .db import delete_all_responses, delete_response, fetch_all_responses
from .views import render_results


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
            callout("Feil passord.", kind="warning", key="g3_admin_login_error")
    return False


@st.cache_data(ttl=5)
def _cached_all_responses() -> list[dict]:
    return fetch_all_responses()


def _render_moderation() -> None:
    st.subheader("Moderering")
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
        if cols[3].button("Slett", key=f"g3_del_{row['id']}"):
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
        file_name="gruppeoppgave_3_svar.csv",
        mime="text/csv",
    )


def _render_danger_zone() -> None:
    st.subheader("Nullstill runde")
    callout(
        "Sletter ALLE svar. Bruk før ny kurssesjon.",
        kind="warning",
        key="g3_admin_danger_notice",
    )
    confirm = st.text_input("Skriv 'SLETT' for å bekrefte")
    if st.button("Slett alle svar", type="primary", disabled=(confirm != "SLETT")):
        delete_all_responses()
        st.cache_data.clear()
        callout(
            "Alle svar slettet.",
            kind="success",
            key="g3_admin_danger_done",
        )


def main() -> None:
    if not _check_password():
        return

    crumb(["Administrasjon", "Gruppeoppgave 3"])
    st.title("Presentatør · Gruppeoppgave 3 — memory.md")

    tab_results, tab_mod, tab_export, tab_danger = st.tabs(
        ["Resultater", "Moderering", "Eksport", "Nullstill"]
    )

    with tab_results:
        auto = st.toggle("Auto-refresh (10 sek)", value=True, key="g3_auto_results")
        if auto:
            st_autorefresh(interval=REFRESH_INTERVAL_MS, key="g3_results_refresh")
        if st.button("Refresh nå", key="g3_refresh_results"):
            st.cache_data.clear()
            st.rerun()
        render_results()

    with tab_mod:
        _render_moderation()

    with tab_export:
        _render_export()

    with tab_danger:
        _render_danger_zone()
