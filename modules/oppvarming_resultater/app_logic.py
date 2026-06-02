"""Resultater Oppvarming - offentlig read-only visning.

Implementerer PRD §FR-3.13: aggregerte grafer uten passord-gate. Bruker
`service_client()` server-side via `modules.oppvarming.views`.

Layout per DESIGN_GUIDE v2 §8: crumb, H1, kort intro, deretter
metric-kort og Likert-diagrammer (rendret av `render_results`).
"""

from __future__ import annotations

import streamlit as st

from modules.oppvarming.views import render_results
from modules.shared.ui import crumb, module_header, next_module_cta_for


def main() -> None:
    crumb(["Oversikt", "Resultater · Bli kjent"])
    module_header("Resultater fra Bli kjent")
    st.caption(
        "Aggregerte svar fra Bli kjent. Enkeltsvar vises aldri - kun fordelinger."
    )

    if st.button("Refresh nå", key="refresh_oppvarming_results"):
        st.cache_data.clear()
        st.rerun()

    render_results()

    st.divider()
    next_module_cta_for("pages/cortex_code.py")
