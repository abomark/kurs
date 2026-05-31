"""Individuell oppgave 4 – modul 24 (Optimaliser treig query).

Implementerer PRD §FR-3.11 og §FR-3.12. Hands-on: deltaker gir Cortex
Code en bevisst dårlig SQL og ber om optimalisering. Demonstrerer
agenten som kritikk-partner, ikke bare generator.

Eksponerer `main()` som kalles fra `pages/individuell_oppgave_4.py`.
"""

from __future__ import annotations

import streamlit as st

from modules.shared.ui import callout, crumb, load_markdown, next_module_cta_for


def main() -> None:
    crumb(["Kursmoduler", "25 · Individuell oppgave 4"])
    st.title("⚡ Individuell oppgave 4")
    st.caption("Modul 25 · Hands-on: optimaliser en treig query med Cortex Code.")
    st.divider()

    callout(
        load_markdown(__file__, "oppgave"),
        kind="info",
        title="🎯 Oppgave",
        key="ind4_oppgave",
    )

    st.divider()

    st.subheader("🪜 Steg")
    st.markdown(load_markdown(__file__, "steg"))

    st.divider()

    st.subheader("✅ Forventet resultat")
    st.markdown(load_markdown(__file__, "forventet"))

    st.divider()
    next_module_cta_for("pages/individuell_oppgave_5.py")
