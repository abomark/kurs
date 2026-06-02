"""Individuell oppgave: @-mentions - modul 6.

Implementerer PRD §FR-3.11 (presentasjons-modul) og §FR-3.12 (innhold i
markdown-filer under `content/`). Hands-on i @-mentions-seksjonen:
deltaker sammenligner samme prompt med og uten `@`-mention og observerer
forskjellen i hva agenten ser.

Eksponerer `main()` som kalles fra
`pages_content/modules/m06_individuell_oppgave_at_mentions.py`.
"""

from __future__ import annotations

import streamlit as st

from modules.shared.ui import callout, crumb, load_markdown, module_header, next_module_cta_for


def main() -> None:
    crumb(["Kursmoduler", "09 · Individuell oppgave: @-mentions"])
    module_header("Individuell oppgave: @-mentions", subtitle="Hands-on: prøv samme prompt med og uten `@`.")
    st.divider()

    callout(
        load_markdown(__file__, "oppgave"),
        kind="info",
        title="Oppgave",
        key="ind_atmen_oppgave",
    )

    st.divider()

    st.subheader("Steg")
    st.markdown(load_markdown(__file__, "steg"))

    st.divider()

    st.subheader("Forventet resultat")
    st.markdown(load_markdown(__file__, "forventet"))

    st.divider()
    next_module_cta_for("plan_mode")
