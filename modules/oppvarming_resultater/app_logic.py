"""Resultater Oppvarming – offentlig read-only visning.

Implementerer PRD §FR-3.13: aggregerte grafer uten passord-gate. Bruker
`service_client()` server-side via `modules.oppvarming.views`.

Layout per DESIGN_GUIDE v2 §8: crumb, H1, kort intro, deretter
metric-kort og Likert-diagrammer (rendret av `render_results`).
"""

from __future__ import annotations

import streamlit as st
from streamlit_autorefresh import st_autorefresh

from modules.oppvarming.config import REFRESH_INTERVAL_MS
from modules.oppvarming.views import render_results
from modules.shared.ui import crumb, next_module_cta_for


def main() -> None:
    crumb(["Oversikt", "Resultater · Bli kjent"])
    st.title("Resultater fra Oppvarming")
    st.caption(
        "Live aggregerte svar fra oppvarmings-spørsmålene. Oppdateres "
        "automatisk. Enkeltsvar vises aldri — kun fordelinger."
    )

    cols = st.columns([3, 1, 1])
    with cols[1]:
        auto = st.toggle(
            "Auto-refresh (10 s)",
            value=True,
            key="auto_oppvarming_results",
        )
    with cols[2]:
        if st.button("Refresh nå", key="refresh_oppvarming_results"):
            st.cache_data.clear()
            st.rerun()
    if auto:
        st_autorefresh(
            interval=REFRESH_INTERVAL_MS, key="oppvarming_results_refresh"
        )

    render_results()

    st.divider()
    next_module_cta_for("pages/cortex_code.py")
