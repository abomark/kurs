"""Snowsight vs CLI – modul 2.

Implementerer PRD §FR-3.11 (presentasjons-modul) og §FR-3.12 (innhold i
markdown-filer under `content/`). Layout her — innhold i `content/*.md`.

Eksponerer `main()` som kalles fra `pages/cortex_interaction.py`.
"""

from __future__ import annotations

import streamlit as st

from modules.shared.ui import callout, crumb, load_markdown, next_module_cta_for


def main() -> None:
    crumb(["Kursmoduler", "02 · Snowsight vs CLI"])
    st.title("🔀 Snowsight vs CLI")
    st.caption("Modul 2 · To måter å samhandle med Cortex Code på")
    st.divider()

    st.markdown(load_markdown(__file__, "intro"))

    st.divider()

    # --- Side-by-side sammenligning ---
    col1, col2 = st.columns(2)
    with col1:
        with st.container(border=True):
            st.markdown(load_markdown(__file__, "snowsight_card"))
    with col2:
        with st.container(border=True):
            st.markdown(load_markdown(__file__, "cli_card"))

    st.divider()

    # --- Sammenligningstabell ---
    st.subheader("📊 Kjapp oversikt")
    st.markdown(load_markdown(__file__, "comparison_table"))

    st.divider()

    # --- Praktisk veiledning ---
    st.subheader("🤔 Hva velger du?")
    col3, col4 = st.columns(2)
    with col3:
        callout(
            load_markdown(__file__, "when_snowsight"),
            kind="info",
            key="ci_when_snowsight",
        )
    with col4:
        callout(
            load_markdown(__file__, "when_cli"),
            kind="info",
            key="ci_when_cli",
        )

    st.divider()

    # --- Avsluttende note ---
    callout(
        load_markdown(__file__, "closing"),
        kind="highlight",
        key="ci_closing",
    )

    st.divider()
    next_module_cta_for("pages/cortex_in_snowsight.py")
