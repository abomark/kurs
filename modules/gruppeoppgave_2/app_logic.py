"""Gruppeoppgave 2 - lag en skill (datakvalitets-sjekk).

Implementerer PRD §FR-3.11 (presentasjons-modul) og §FR-3.12 (innhold i
markdown-filer under `content/`). Ren presentasjon - ingen datainnsamling.
Refleksjon skjer muntlig i plenum etterpå.

Eksponerer `main()` som kalles fra `pages_content/modules/m12_gruppeoppgave_2.py`.
"""

from __future__ import annotations

import streamlit as st

from modules.shared.ui import callout, crumb, load_markdown, module_header, next_module_cta_for


def main() -> None:
    crumb(["Kursmoduler", "21 · Gruppeoppgave 2"])
    module_header("Gruppeoppgave 2", subtitle="Lag en skill: datakvalitets-sjekk")
    st.divider()

    callout(
        load_markdown(__file__, "oppgave"),
        kind="info",
        title="Oppgave",
        key="g2_oppgave",
    )

    st.divider()

    st.subheader("Steg")
    st.markdown(load_markdown(__file__, "steg"))

    st.divider()

    st.subheader("Forventet resultat")
    st.markdown(load_markdown(__file__, "forventet"))

    st.divider()
    next_module_cta_for("context_engineering")
