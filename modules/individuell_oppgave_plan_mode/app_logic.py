"""Individuell oppgave: Plan Mode - modul 8.

Implementerer PRD §FR-3.11 (presentasjons-modul) og §FR-3.12 (innhold i
markdown-filer under `content/`). Hands-on i Plan Mode-seksjonen: deltaker
gir Cortex Code en kompleks oppgave, skrur på Plan Mode og leser planen
*før* utførelse - for å se hvordan agenten resonnerer.

Eksponerer `main()` som kalles fra
`pages_content/modules/m08_individuell_oppgave_plan_mode.py`.
"""

from __future__ import annotations

import streamlit as st

from modules.shared.ui import callout, crumb, load_markdown, module_header, next_module_cta_for


def main() -> None:
    crumb(["Kursmoduler", "11 · Individuell oppgave: Plan Mode"])
    module_header("Individuell oppgave: Plan Mode", subtitle="Hands-on: skru på Plan Mode og les planen før utførelse.")
    st.divider()

    callout(
        load_markdown(__file__, "oppgave"),
        kind="info",
        title="Oppgave",
        key="ind_planmode_oppgave",
    )

    st.divider()

    st.subheader("Steg")
    st.markdown(load_markdown(__file__, "steg"))

    st.divider()

    st.subheader("Noen mulige observasjoner")
    st.markdown(load_markdown(__file__, "forventet"))

    st.divider()
    next_module_cta_for("kostnader")
