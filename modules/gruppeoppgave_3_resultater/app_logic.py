"""Resultater Gruppeoppgave 3 – modul 19 (åpen for alle).

Implementerer PRD §FR-3.13: offentlig, read-only visning av
hovedresultatene fra Gruppeoppgave 3 (memory.md). Ingen passord-gate.
Ingen moderering, eksport eller sletting — det ligger fortsatt i
admin-siden.

Datatilgang: bruker `service_client()` server-side via
`modules.gruppeoppgave_3.views`. Service-role-keyen lekker ikke til
nettleseren — brukerne ser kun ferdig-renderte grafer.

Eksponerer `main()` som kalles fra
`pages_content/modules/m10_gruppeoppgave_3_resultater.py`.
"""

from __future__ import annotations

import streamlit as st
from streamlit_autorefresh import st_autorefresh

from modules.gruppeoppgave_3.config import REFRESH_INTERVAL_MS
from modules.gruppeoppgave_3.views import render_results
from modules.shared.ui import crumb, next_module_cta_for


def main() -> None:
    crumb(["Kursmoduler", "23 · Resultater Gruppeoppgave 3"])
    st.title("Resultater · Gruppeoppgave 3 — memory.md")
    st.caption(
        "Live aggregerte svar fra Gruppeoppgave 3. Oppdateres automatisk. "
        "Enkeltsvar vises aldri — kun ordskyer og fordeling."
    )

    cols = st.columns([3, 1, 1])
    with cols[1]:
        auto = st.toggle(
            "Auto-refresh (10 s)",
            value=True,
            key="g3r_auto_public_results",
        )
    with cols[2]:
        if st.button("Refresh nå", key="g3r_refresh_public_results"):
            st.cache_data.clear()
            st.rerun()
    if auto:
        st_autorefresh(interval=REFRESH_INTERVAL_MS, key="g3r_public_results_refresh")

    render_results()

    st.divider()
    # Etter Resultater Gruppeoppgave 3 går vi ut av memory.md-blokken
    # og inn i Anvendt praksis-seksjonen.
    # Etter memory.md-blokken går vi inn i prompt_engineering-seksjonen.
    next_module_cta_for("prompt_engineering")
