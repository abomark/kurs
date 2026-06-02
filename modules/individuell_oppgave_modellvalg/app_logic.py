"""Individuell oppgave: Modellvalg - modul 16.

Implementerer PRD §FR-3.11 (presentasjons-modul) og §FR-3.12 (innhold i
markdown-filer under `content/`). Hands-on i Modellvalg-seksjonen: deltaker
kjører samme prompt to ganger - en gang med Sonnet, en gang med Opus - og
sammenligner hvordan modellene løser to SQL-oppgaver av ulik vanskegrad.

Eksponerer `main()` som kalles fra
`pages_content/modules/m16_individuell_oppgave_modellvalg.py`.
"""

from __future__ import annotations

import streamlit as st

from modules.shared.ui import (
    callout,
    crumb,
    load_markdown,
    module_header,
    next_module_cta_for,
    render_markdown_wrapped_code,
)


def main() -> None:
    crumb(["Kursmoduler", "16 · Individuell oppgave: Modellvalg"])
    module_header(
        "Individuell oppgave: Modellvalg",
        subtitle="Hands-on: kjør samme oppgave med Sonnet og Opus, og sammenlign.",
    )
    st.divider()

    callout(
        load_markdown(__file__, "oppgave"),
        kind="info",
        title="Oppgave",
        key="ind_modellvalg_oppgave",
    )

    st.divider()

    st.subheader("Slik gjør du")
    st.markdown(load_markdown(__file__, "steg"))

    st.divider()

    st.subheader("Oppgave 1: Topp 10 % kunder per segment")
    render_markdown_wrapped_code(load_markdown(__file__, "oppgave_1"))

    st.divider()

    st.subheader("Oppgave 2: Kundefrafall per segment")
    render_markdown_wrapped_code(load_markdown(__file__, "oppgave_2"))

    st.divider()

    st.subheader("Hva du skal sammenligne")
    st.markdown(load_markdown(__file__, "forventet"))

    st.divider()
    next_module_cta_for("skills_md")
