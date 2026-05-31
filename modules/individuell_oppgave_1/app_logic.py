"""Individuell oppgave 1 – modul 9.

Implementerer PRD §FR-3.11 (presentasjons-modul) og §FR-3.12 (innhold i
markdown-filer under `content/`). Individuell hands-on oppgave:
deltakere skal selv legge til Analyse GIT repo i sitt Snowflake-miljø.

Eksponerer `main()` som kalles fra `pages/individuell_oppgave_1.py`.
"""

from __future__ import annotations

import streamlit as st

from modules.shared.ui import callout, crumb, load_markdown, next_module_cta_for


def main() -> None:
    crumb(["Kursmoduler", "07 · Individuell oppgave 1"])
    st.title("Individuell oppgave 1")
    st.caption("Modul 7 · Hands-on: hver deltaker gjør dette på egen maskin.")
    st.divider()

    callout(
        "**Legg til MT-ANALYSE GIT repo**",
        kind="info",
        title="Oppgave",
        key="ind1_oppgave",
    )

    st.divider()

    st.subheader("Steg")
    st.markdown(load_markdown(__file__, "instructions"))

    st.divider()
    next_module_cta_for("at_mentions")
