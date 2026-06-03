"""Individuell oppgave: Kohortanalyse + heatmap.

Implementerer PRD §FR-3.11 (presentasjons-modul) og §FR-3.12 (innhold i
markdown-filer under `content/`). Hands-on: deltaker bruker Cortex Code til
å lage en kohortanalyse mot @KURS_TRANSAKSJON og visualisere den som heatmap
i en Streamlit-app i Workspace.

Eksponerer `main()` som kalles fra
`pages_content/modules/m31_individuell_oppgave_kohort.py`.
"""

from __future__ import annotations

import streamlit as st

from modules.shared.ui import callout, crumb, load_markdown, module_header, next_module_cta_for


def main() -> None:
    crumb(["Kursmoduler", "22 · Individuell oppgave: Kohortanalyse"])
    module_header(
        "Individuell oppgave: Kohortanalyse",
        subtitle="Hands-on: kohortanalyse mot @KURS_TRANSAKSJON, visualisert som heatmap.",
    )
    st.divider()

    callout(
        load_markdown(__file__, "oppgave"),
        kind="info",
        title="Oppgave",
        key="ind_kohort_oppgave",
    )

    st.divider()

    st.subheader("Steg")
    st.markdown(load_markdown(__file__, "steg"))

    st.divider()

    st.subheader("Forventet resultat")
    st.markdown(load_markdown(__file__, "forventet"))

    st.divider()
    next_module_cta_for("individuell_oppgave_konkurrent")
