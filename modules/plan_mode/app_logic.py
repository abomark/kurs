"""Plan Mode i Cortex Code.

Implementerer PRD §FR-3.11 (presentasjons-modul) og §FR-3.12 (innhold i
markdown-filer under `content/`). Innføring i Plan Mode: arbeidsmåten der
agenten først legger fram en plan til godkjenning før den utfører noe.

Layout per DESIGN_GUIDE §8: intro-callout + tre subheader-seksjoner.

Eksponerer `main()` som kalles fra
`pages_content/modules/m09_plan_mode.py`.
"""

from __future__ import annotations

import streamlit as st

from modules.shared.ui import (
    callout,
    crumb,
    load_markdown,
    module_header,
    next_module_cta_for,
)


def main() -> None:
    crumb(["Kursmoduler", "09 · Plan Mode"])
    module_header(
        "Plan Mode",
        subtitle="Kjøremodusen som holder seg read-only mens den tenker, "
        "og leverer en plan til godkjenning før noe utføres",
    )
    st.divider()

    # --- Hva er Plan Mode? ---
    callout(
        load_markdown(__file__, "intro"),
        kind="info",
        title="Hva er Plan Mode?",
        key="plan_intro",
    )

    st.divider()

    # --- Når bør du bruke Plan Mode? ---
    st.subheader("Når bør du bruke Plan Mode?")
    st.markdown(load_markdown(__file__, "naar"))

    st.divider()

    # --- Hvordan bruker du det i Snowsight? ---
    st.subheader("Hvordan bruker du det i Snowsight?")
    st.markdown(load_markdown(__file__, "hvordan"))

    st.divider()

    # --- Hvorfor er det nyttig? ---
    st.subheader("Hvorfor er det nyttig?")
    st.markdown(load_markdown(__file__, "hvorfor"))

    st.divider()
    next_module_cta_for("individuell_oppgave_plan_mode")
