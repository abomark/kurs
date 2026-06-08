"""Avslutning - modul 28 (Hva nå?).

Implementerer PRD §FR-3.11 og §FR-3.12. Siste modul i kursrekken:
oppsummering av kjernepunkter, konkrete neste steg, og evt. en kobling
tilbake til Q5 i oppvarming for å vise om holdningen har flyttet seg.

Eksponerer `main()` som kalles fra `pages/avslutning.py`.
"""

from __future__ import annotations

import streamlit as st

from modules.shared.ui import crumb, load_markdown, module_header


def main() -> None:
    crumb(["Kursmoduler", "25 · Avslutning"])
    module_header("Avslutning", subtitle="Hva nå? - veien videre.")
    st.divider()

    st.subheader("Fra i morgen")
    st.markdown(load_markdown(__file__, "fra_i_morgen"))
