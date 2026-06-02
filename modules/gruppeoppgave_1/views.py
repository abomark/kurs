"""Offentlige visualiseringsfunksjoner for Gruppeoppgave 1.

Implementerer PRD §FR-3.13 (offentlig resultatvisning): rendering-logikk
som er trygg å eksponere uten passord-gate. Bruker `service_client()`
server-side for å hente aggregerte data - service_role-keyen lekker
aldri til nettleseren, og brukerne ser kun ferdig-renderte grafer.

`admin_logic.py` (passordbeskyttet) og `gruppeoppgave_1_resultater`
(modul 13, offentlig) deler disse funksjonene for å unngå duplisering.

IKKE legg moderering, eksport eller sletting her - det hører hjemme i
`admin_logic.py`.
"""

from __future__ import annotations

import streamlit as st

from modules.shared.ui import callout

from .config import MIN_RESPONSES_BEFORE_REVEAL, QUESTIONS
from .db import fetch_choice_counts, fetch_text_answers
from .reducer import reduce_answers
from .viz import render_barchart, render_wordcloud


# PRD §NFR-4.3: cache DB-spørringer 5 sek for å unngå hammer ved auto-refresh.
@st.cache_data(ttl=5)
def cached_text_answers(qid: int) -> list[str]:
    return fetch_text_answers(qid)


# PRD §NFR-4.3: cache DB-spørringer 5 sek for å unngå hammer ved auto-refresh.
@st.cache_data(ttl=5)
def cached_choice_counts(qid: int, options_key: str) -> dict[str, int]:
    options = options_key.split("|")
    return fetch_choice_counts(qid, options)


def render_results() -> None:
    """Hovedresultater: ordskyer for Q1/Q2 + barcharts for Q3/Q4."""
    st.caption(
        f"Resultatene vises når minst {MIN_RESPONSES_BEFORE_REVEAL} svar er inne."
    )

    answers_1 = cached_text_answers(1)
    tokens_1 = reduce_answers(answers_1)
    render_wordcloud(tokens_1, QUESTIONS[1]["text"])
    st.caption(f"{len(answers_1)} svar · {len(tokens_1)} ord etter reduksjon")

    st.divider()

    answers_2 = cached_text_answers(2)
    tokens_2 = reduce_answers(answers_2)
    render_wordcloud(tokens_2, QUESTIONS[2]["text"])
    st.caption(f"{len(answers_2)} svar · {len(tokens_2)} ord etter reduksjon")

    callout(
        "Ordene er ekstrahert med enkel stopword-filtrering. "
        "Senere versjon vil bruke AI for å fange nyanser bedre.",
        kind="subtle",
        key="g1_views_reducer_note",
    )

    st.divider()

    col3, col4 = st.columns(2)
    with col3:
        opts_3 = QUESTIONS[3]["options"]
        counts_3 = cached_choice_counts(3, "|".join(opts_3))
        render_barchart(counts_3, QUESTIONS[3]["text"])
    with col4:
        opts_4 = QUESTIONS[4]["options"]
        counts_4 = cached_choice_counts(4, "|".join(opts_4))
        render_barchart(counts_4, QUESTIONS[4]["text"])
