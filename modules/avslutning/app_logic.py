"""Avslutning – modul 28 (Hva nå?).

Implementerer PRD §FR-3.11 og §FR-3.12. Siste modul i kursrekken:
oppsummering av kjernepunkter, konkrete neste steg, og evt. en kobling
tilbake til Q5 i oppvarming for å vise om holdningen har flyttet seg.

Eksponerer `main()` som kalles fra `pages/avslutning.py`.
"""

from __future__ import annotations

import streamlit as st

from modules.shared.ui import crumb, load_markdown


def main() -> None:
    crumb(["Kursmoduler", "29 · Avslutning"])
    st.title("🏁 Avslutning")
    st.caption("Modul 29 · Hva nå? — oppsummering og veien videre.")
    st.divider()

    st.subheader("💡 Oppsummering")
    st.markdown(load_markdown(__file__, "oppsummering"))

    st.divider()

    st.subheader("➡️ Neste steg")
    st.markdown(load_markdown(__file__, "neste_steg"))

    st.divider()

    st.subheader("🔁 Holdning — har den flyttet seg?")
    st.markdown(load_markdown(__file__, "holdning_revisit"))
