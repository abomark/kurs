"""Individuell oppgave 2 - modul 21 (Beskrive ukjent tabell).

Implementerer PRD §FR-3.11 (presentasjons-modul) og §FR-3.12 (innhold i
markdown-filer under `content/`). Hands-on: deltaker bruker Cortex Code
til å beskrive en ukjent tabell - utforskningsoppgave med lav terskel.

Eksponerer `main()` som kalles fra `pages/individuell_oppgave_2.py`.
"""

from __future__ import annotations

import streamlit as st

from modules.shared.ui import callout, crumb, load_markdown, module_header, next_module_cta_for


def main() -> None:
    crumb(["Kursmoduler", "25 · Individuell oppgave 2"])
    module_header("Individuell oppgave 2", subtitle="Hands-on: beskrive en ukjent tabell med Cortex Code.")
    st.divider()

    callout(
        load_markdown(__file__, "oppgave"),
        kind="info",
        title="Oppgave",
        key="ind2_oppgave",
    )

    st.divider()

    st.subheader("Steg")
    st.markdown(load_markdown(__file__, "steg"))

    st.divider()

    st.subheader("Forventet resultat")
    st.markdown(load_markdown(__file__, "forventet"))

    st.divider()
    next_module_cta_for("demo_2")
