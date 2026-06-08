"""Gruppeoppgave: Konkurrent-signaler.

Implementerer PRD §FR-3.11 (presentasjons-modul) og §FR-3.12 (innhold i
markdown-filer under `content/`). Hands-on: deltaker utforsker om agenten
kan flagge signaler på utgående transaksjoner til konkurrenter.

Eksponerer `main()` som kalles fra
`pages_content/modules/m33_individuell_oppgave_konkurrent.py`.
"""

from __future__ import annotations

import streamlit as st

from modules.shared.ui import callout, crumb, load_markdown, module_header, next_module_cta_for


def main() -> None:
    crumb(["Kursmoduler", "24 · Gruppeoppgave: Konkurrent-signaler"])
    module_header(
        "Gruppeoppgave: Konkurrent-signaler",
        subtitle="Hands-on: kan agenten flagge utgående transaksjoner til konkurrenter?",
    )
    st.divider()

    callout(
        load_markdown(__file__, "oppgave"),
        kind="info",
        title="Oppgave",
        key="ind_konkurrent_oppgave",
    )

    st.divider()
    next_module_cta_for("avslutning")
