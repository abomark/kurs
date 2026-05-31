"""Individuell oppgave 5 – modul 26 (Refleksjon).

Implementerer PRD §FR-3.11 og §FR-3.12. Refleksjons-oppgave (ikke
handlings-oppgave): deltaker sammenligner Cortex Codes output med
sin egen tilnærming og tenker over forskjellene.

Forutsetter at deltakeren har gjort minst én tidligere oppgave (typisk
oppgave 2, 3 eller 4) som referanse.

Eksponerer `main()` som kalles fra `pages/individuell_oppgave_5.py`.
"""

from __future__ import annotations

import streamlit as st

from modules.shared.ui import callout, crumb, load_markdown, next_module_cta_for


def main() -> None:
    crumb(["Kursmoduler", "27 · Individuell oppgave 5"])
    st.title("🪞 Individuell oppgave 5")
    st.caption("Modul 27 · Refleksjon: sammenlign agentens output med din egen.")
    st.divider()

    callout(
        load_markdown(__file__, "oppgave"),
        kind="info",
        title="🎯 Oppgave",
        key="ind5_oppgave",
    )

    st.divider()

    st.subheader("🪞 Refleksjonsspørsmål")
    st.markdown(load_markdown(__file__, "sporsmal"))

    st.divider()

    st.subheader("💬 Snakkepunkter (for presentatør)")
    st.markdown(load_markdown(__file__, "notater"))

    st.divider()
    # Før avslutning kommer Kostnader-modulen (operasjonell forberedelse).
    next_module_cta_for("kostnader")
