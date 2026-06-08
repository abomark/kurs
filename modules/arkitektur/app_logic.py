"""Under panseret - modul 7.

Implementerer PRD §FR-3.11 (presentasjons-modul) og §FR-3.12 (innhold i
markdown-filer under `content/`). Visuell oversikt over Cortex Codes
fem integrerte lag, hver presentert som en klikkbar ekspander.

Eksponerer `main()` som kalles fra `pages_content/modules/m05_arkitektur.py`.
"""

from __future__ import annotations

import streamlit as st

from modules.shared.ui import callout, crumb, load_markdown, module_header, next_module_cta_for


def main() -> None:
    crumb(["Kursmoduler", "05 · Under panseret"])
    module_header("Under panseret", subtitle="Hvordan Cortex Code er bygget - en LLM med integrerte lag.")
    st.divider()

    # --- Intro ---
    st.markdown(load_markdown(__file__, "intro"))

    st.divider()

    # --- De fem lagene som klikkbare ekspandere ---
    st.subheader("Lagene")
    st.caption("Klikk på et lag for å se mer.")

    with st.expander("1. System Prompt"):
        st.markdown(load_markdown(__file__, "system_prompt"))

    with st.expander("2. Tools (Verktøylag)"):
        st.markdown(load_markdown(__file__, "tool_interface"))

    with st.expander("3. Skills"):
        st.markdown(load_markdown(__file__, "skills_system"))

    with st.expander("4. Oppgavestyring (TODO)"):
        st.markdown(load_markdown(__file__, "oppgavestyring"))

    with st.expander("5. Kontekstbevissthet"):
        st.markdown(load_markdown(__file__, "kontekstbevissthet"))

    st.divider()

    # --- Demo til sist: la agenten beskrive sin egen arkitektur ---
    callout(
        load_markdown(__file__, "demo"),
        kind="info",
        title="Demo: spør agenten om seg selv",
        key="arkitektur_demo",
    )

    st.divider()
    next_module_cta_for("demo_1")
