"""Gruppeoppgave 2 — lag en skill (datakvalitets-sjekk).

Implementerer PRD §FR-3.11 (presentasjons-modul) og §FR-3.12 (innhold i
markdown-filer under `content/`). Ren presentasjon — ingen datainnsamling.
Refleksjon skjer muntlig i plenum etterpå.

Eksponerer `main()` som kalles fra `pages_content/modules/m11_gruppeoppgave_2.py`.
"""

from __future__ import annotations

import streamlit as st

from modules.shared.ui import callout, load_markdown


def main() -> None:
    st.title("🧑‍🤝‍🧑 Gruppeoppgave 2")
    st.caption("Modul 11 · Lag en skill: datakvalitets-sjekk")
    st.divider()

    callout(
        load_markdown(__file__, "oppgave"),
        kind="info",
        title="🎯 Oppgave",
        key="g2_oppgave",
    )

    st.divider()

    st.subheader("🪜 Steg")
    st.markdown(load_markdown(__file__, "steg"))

    st.divider()

    st.subheader("✅ Forventet resultat")
    st.markdown(load_markdown(__file__, "forventet"))
