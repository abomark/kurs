"""Resultater Gruppeoppgave 1 - modul 12 (åpen for alle).

Implementerer PRD §FR-3.13: offentlig, read-only visning av
hovedresultatene fra Gruppeoppgave 1. Ingen passord-gate. Ingen
moderering, eksport eller sletting - det ligger fortsatt i admin-siden.

Datatilgang: bruker `service_client()` server-side via
`modules.gruppeoppgave_1.views`. Service-role-keyen lekker ikke til
nettleseren - brukerne ser kun ferdig-renderte grafer.

Eksponerer `main()` som kalles fra `pages/gruppeoppgave_1_resultater.py`.
"""

from __future__ import annotations

import streamlit as st
from streamlit_autorefresh import st_autorefresh

from modules.gruppeoppgave_1.config import REFRESH_INTERVAL_MS
from modules.gruppeoppgave_1.views import render_results
from modules.shared.ui import crumb, module_header, next_module_cta_for


def main() -> None:
    crumb(["Kursmoduler", "15 · Resultater Gruppeoppgave 1"])
    module_header("Resultater · Gruppeoppgave 1")
    st.caption(
        "Live aggregerte svar fra Gruppeoppgave 1. Oppdateres automatisk. "
        "Enkeltsvar vises aldri - kun ordskyer og fordeling."
    )

    cols = st.columns([3, 1, 1])
    with cols[1]:
        auto = st.toggle(
            "Auto-refresh (10 s)",
            value=True,
            key="auto_public_results",
        )
    with cols[2]:
        if st.button("Refresh nå", key="refresh_public_results"):
            st.cache_data.clear()
            st.rerun()
    if auto:
        st_autorefresh(interval=REFRESH_INTERVAL_MS, key="public_results_refresh")

    render_results()

    st.divider()
    # Etter Resultater Gruppeoppgave 1 går vi inn i skills.md-blokken
    # (neste konsept i den nye pedagogiske rekkefølgen).
    next_module_cta_for("tilgjengelige_modeller")
