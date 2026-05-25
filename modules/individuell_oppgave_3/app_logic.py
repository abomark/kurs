"""Individuell oppgave 3 – modul 16 (Datakvalitetssjekk).

Implementerer PRD §FR-3.11 og §FR-3.12. Hands-on: deltaker bruker
Cortex Code til å finne duplikater, NULL-er eller andre kvalitetsfeil
i en gitt tabell.

Eksponerer `main()` som kalles fra `pages/individuell_oppgave_3.py`.
"""

from __future__ import annotations

import streamlit as st

from modules.shared.ui import callout, crumb, load_markdown, next_module_cta_for


def main() -> None:
    crumb(["Kursmoduler", "16 · Individuell oppgave 3"])
    st.title("🩺 Individuell oppgave 3")
    st.caption("Modul 16 · Hands-on: datakvalitetssjekk med Cortex Code.")
    st.divider()

    callout(
        load_markdown(__file__, "oppgave"),
        kind="info",
        title="🎯 Oppgave",
        key="ind3_oppgave",
    )

    st.divider()

    st.subheader("🪜 Steg")
    st.markdown(load_markdown(__file__, "steg"))

    st.divider()

    st.subheader("✅ Forventet resultat")
    st.markdown(load_markdown(__file__, "forventet"))

    st.divider()
    next_module_cta_for("pages/individuell_oppgave_4.py")
