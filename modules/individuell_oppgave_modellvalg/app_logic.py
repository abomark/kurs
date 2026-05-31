"""Individuell oppgave: Modellvalg – modul 14.

Implementerer PRD §FR-3.11 (presentasjons-modul) og §FR-3.12 (innhold i
markdown-filer under `content/`). Hands-on i Modellvalg-seksjonen: deltaker
øver på å velge riktig modell for en gitt oppgave i Cortex Code.

Eksponerer `main()` som kalles fra
`pages_content/modules/m11_individuell_oppgave_modellvalg.py`.
"""

from __future__ import annotations

import streamlit as st

from modules.shared.ui import callout, crumb, load_markdown, next_module_cta_for


def main() -> None:
    crumb(["Kursmoduler", "15 · Individuell oppgave: Modellvalg"])
    st.title("🎚️ Individuell oppgave: Modellvalg")
    st.caption("Modul 15 · Hands-on: velg riktig modell for oppgaven din.")
    st.divider()

    callout(
        load_markdown(__file__, "oppgave"),
        kind="info",
        title="🎯 Oppgave",
        key="ind_modellvalg_oppgave",
    )

    st.divider()

    st.subheader("🪜 Steg")
    st.markdown(load_markdown(__file__, "steg"))

    st.divider()

    st.subheader("✅ Forventet resultat")
    st.markdown(load_markdown(__file__, "forventet"))

    st.divider()
    next_module_cta_for("skills_md")
