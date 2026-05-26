"""Individuell oppgave 2 – modul 19 (Beskrive ukjent tabell).

Implementerer PRD §FR-3.11 (presentasjons-modul) og §FR-3.12 (innhold i
markdown-filer under `content/`). Hands-on: deltaker bruker Cortex Code
til å beskrive en ukjent tabell — utforskningsoppgave med lav terskel.

Eksponerer `main()` som kalles fra `pages/individuell_oppgave_2.py`.
"""

from __future__ import annotations

import streamlit as st

from modules.shared.ui import callout, crumb, load_markdown, next_module_cta_for


def main() -> None:
    crumb(["Kursmoduler", "19 · Individuell oppgave 2"])
    st.title("🔍 Individuell oppgave 2")
    st.caption("Modul 19 · Hands-on: beskrive en ukjent tabell med Cortex Code.")
    st.divider()

    callout(
        load_markdown(__file__, "oppgave"),
        kind="info",
        title="🎯 Oppgave",
        key="ind2_oppgave",
    )

    st.divider()

    st.subheader("🪜 Steg")
    st.markdown(load_markdown(__file__, "steg"))

    st.divider()

    st.subheader("✅ Forventet resultat")
    st.markdown(load_markdown(__file__, "forventet"))

    st.divider()
    next_module_cta_for("pages/individuell_oppgave_3.py")
