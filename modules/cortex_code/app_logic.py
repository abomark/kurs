"""Cortex Code - modul 2.

Implementerer PRD §FR-3.11 (presentasjons-modul) og §FR-3.12 (innhold i
markdown-filer under `content/`). Layout her - innhold i `content/*.md`.
Følger DESIGN_GUIDE.md for callouts og emoji-bruk.

Eksponerer `main()` som kalles fra `pages/cortex_code.py`.
"""

from __future__ import annotations

import streamlit as st

from modules.shared.ui import (
    callout,
    crumb,
    load_markdown,
    load_titled_markdown,
    module_header,
    next_module_cta_for,
)

TERM_FILES = [
    "term_intelligent",
    "term_intelligent_agent",
    "term_autonomous",
    "term_best_practices",
    "term_context_aware",
]


def main() -> None:
    crumb(["Kursmoduler", "03 · Cortex Code"])
    module_header("Cortex Code", subtitle="Hva er Cortex Code egentlig?")
    st.divider()

    # --- Oversikt: Hva / Hvorfor / Hvordan ---
    st.subheader("Hva er Cortex Code?")
    st.markdown(load_markdown(__file__, "hva_er"))

    st.divider()

    st.subheader("Hvorfor bruke Cortex Code?")
    st.markdown(load_markdown(__file__, "hvorfor"))

    st.divider()

    st.subheader("Hvordan kan vi bruke det?")
    st.markdown(load_markdown(__file__, "hvordan"))

    st.divider()

    # --- Seksjon 1: Dokumentasjonssitatet ---
    callout(
        load_markdown(__file__, "quote"),
        kind="info",
        title="Dokumentasjonen sier",
        key="cortex_quote",
    )

    st.divider()

    # --- Seksjon 2: Begrep for begrep ---
    st.subheader("Begrep for begrep")
    for name in TERM_FILES:
        title, body = load_titled_markdown(__file__, name)
        with st.expander(title or name, expanded=False):
            st.markdown(body)

    st.divider()

    # --- Seksjon 3: Klartekst ---
    callout(
        load_markdown(__file__, "summary"),
        kind="tip",
        title="Kort oppsummert",
        key="cortex_summary",
    )

    st.divider()

    # --- Seksjon 4: Konkret eksempel ---
    st.subheader("Et konkret eksempel")
    with st.container(border=True):
        st.markdown(load_markdown(__file__, "example"))

    st.divider()
    next_module_cta_for("pages/cortex_interaction.py")
