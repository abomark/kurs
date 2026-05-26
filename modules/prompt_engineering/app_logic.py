"""Prompt engineering – modul 18.

Implementerer PRD §FR-3.11 (presentasjons-modul) og §FR-3.12 (innhold i
markdown-filer under `content/`). Bygger bro fra konsept-blokkene
(AGENTS.md / skills.md / memory.md) til praktisk daglig bruk: hvordan
deltakeren faktisk skriver en god prompt.

Layout per DESIGN_GUIDE v2 §8: crumb, H1+intro, expanders for hvert tema,
warn-callout for anti-patterns, og to-kolonners eksempel-sammenligning
(Før/Etter) som splittes ut av én markdown-fil via `load_split_markdown`.

Eksponerer `main()` som kalles fra `pages_content/modules/m18_prompt_engineering.py`.
"""

from __future__ import annotations

import streamlit as st

from modules.shared.ui import (
    callout,
    crumb,
    load_markdown,
    load_split_markdown,
    load_titled_markdown,
    next_module_cta_for,
)


def main() -> None:
    crumb(["Kursmoduler", "18 · Prompt engineering"])

    title, intro_body = load_titled_markdown(__file__, "intro")
    st.title(title or "✍️ Prompt engineering")
    st.caption("Modul 18 · Anatomi, mønstre og iterativ forbedring av prompts")
    st.divider()
    st.markdown(intro_body)

    st.divider()

    # --- Anatomi ---
    with st.expander("🧬 Anatomi av en god prompt"):
        st.markdown(load_markdown(__file__, "anatomi"))

    # --- SQL-spesifikt ---
    with st.expander("❄️ SQL- og Snowflake-spesifikke mønstre"):
        st.markdown(load_markdown(__file__, "sql_spesifikt"))

    # --- Anti-patterns som warn-callout ---
    callout(
        load_markdown(__file__, "anti_patterns"),
        kind="warn",
        title="🚫 Anti-patterns",
        key="pe_anti_patterns",
    )

    # --- Iterativ ---
    with st.expander("🔁 Iterativ forbedring – pingpong med agenten"):
        st.markdown(load_markdown(__file__, "iterativ"))

    # --- AGENTS.md vs skills.md vs inline ---
    with st.expander("⚖️ AGENTS.md vs skills.md vs inline prompt"):
        st.markdown(load_markdown(__file__, "agents_vs_inline"))

    st.divider()

    # --- Eksempel-sammenligning: én fil, to ## -seksjoner, to kolonner ---
    st.subheader("🔍 Før og etter")
    sections = load_split_markdown(__file__, "eksempel_sammenligning")
    col_for, col_etter = st.columns(2, gap="medium")
    with col_for:
        st.markdown("**Før**")
        st.markdown(sections.get("Før", "_Mangler `## Før`-seksjon i `eksempel_sammenligning.md`._"))
    with col_etter:
        st.markdown("**Etter**")
        st.markdown(sections.get("Etter", "_Mangler `## Etter`-seksjon i `eksempel_sammenligning.md`._"))

    st.divider()
    next_module_cta_for("individuell_oppgave_2")
