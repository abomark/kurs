"""Offentlige visualiseringsfunksjoner for Oppvarming-modulen.

Implementerer PRD §FR-3.13 (offentlig resultatvisning). Bruker
`service_client()` server-side via `modules.oppvarming.db`.

Layout per DESIGN_GUIDE v2 §4: viktige tall i metric-kort på toppen,
deretter Likert-diagrammer i kort med snitt-linje og heltallsticks.
"""

from __future__ import annotations

import streamlit as st
from modules.gruppeoppgave_1.viz import render_barchart
from modules.shared.ui import metric_row

from .config import MIN_RESPONSES_BEFORE_REVEAL, SCALE_MAX, SCALE_MIN, STATEMENTS
from .db import fetch_value_counts


# PRD §NFR-4.3: cache DB-spørringer 5 sek for å unngå hammer ved auto-refresh.
@st.cache_data(ttl=5)
def cached_value_counts(qid: int) -> dict[int, int]:
    return fetch_value_counts(qid)


def _mean(counts: dict[int, int]) -> float | None:
    total = sum(counts.values())
    if total == 0:
        return None
    weighted = sum(val * cnt for val, cnt in counts.items())
    return weighted / total


def _enighet_label(mean: float) -> str:
    if mean < 2.0:
        return "Lav enighet"
    if mean < 3.0:
        return "Moderat uenighet"
    if mean < 3.5:
        return "Nøytral"
    if mean < 4.0:
        return "Moderat enighet"
    return "Høy enighet"


def render_results() -> None:
    """Metric-rad øverst + en Likert-barchart i kort per påstand."""
    # --- Aggregert data for summary-strip ---
    all_counts: dict[int, dict[int, int]] = {
        sid: cached_value_counts(sid) for sid in STATEMENTS
    }
    total_answers = sum(sum(c.values()) for c in all_counts.values())
    # Antall unike "deltakere" = svar per spørsmål (siden hver innsending er 5 rader).
    n_per_q = total_answers // len(STATEMENTS) if STATEMENTS else 0

    means = [m for m in (_mean(c) for c in all_counts.values()) if m is not None]
    snitt_score = sum(means) / len(means) if means else None

    # --- Metric-kort (DESIGN_GUIDE v2 §4) ---
    metric_row(
        [
            (
                "TOTALT ANTALL SVAR",
                str(n_per_q),
                f"{total_answers} rader · {len(STATEMENTS)} spørsmål",
            ),
            (
                "SNITT-SCORE",
                f"{snitt_score:.2f}/5" if snitt_score is not None else "-",
                _enighet_label(snitt_score) if snitt_score is not None else "Venter på svar",
            ),
            (
                "SPØRSMÅL",
                str(len(STATEMENTS)),
                "Likert-skala 1-5",
            ),
        ]
    )

    st.caption(
        f"Resultatene vises når minst {MIN_RESPONSES_BEFORE_REVEAL} svar er inne. "
        "Skala: 1 = uenig · 5 = enig."
    )

    # --- Likert-diagrammer ---
    for sid, statement in STATEMENTS.items():
        counts_int = all_counts[sid]
        counts_str = {
            str(v): counts_int.get(v, 0)
            for v in range(SCALE_MIN, SCALE_MAX + 1)
        }
        mean = _mean(counts_int)
        title = f"{sid}. {statement}"
        render_barchart(
            counts_str,
            title,
            min_responses=MIN_RESPONSES_BEFORE_REVEAL,
            mean=mean,
            likert=True,
        )
