"""Arkitekturoversikt – modul 7.

Implementerer PRD §FR-3.11 (presentasjons-modul) og §FR-3.12 (innhold i
markdown-filer under `content/`). Visuell oversikt over Cortex Codes
fem integrerte lag, hver presentert som en klikkbar ekspander.

Eksponerer `main()` som kalles fra `pages_content/modules/m04_arkitektur.py`.
"""

from __future__ import annotations

import streamlit as st

from modules.shared.ui import callout, crumb, load_markdown, next_module_cta_for


def main() -> None:
    crumb(["Kursmoduler", "08 · Arkitekturoversikt"])
    st.title("🏗️ Arkitekturoversikt")
    st.caption("Modul 8 · Hvordan Cortex Code er bygget — én LLM med fem integrerte lag.")
    st.divider()

    # --- Intro ---
    st.markdown(load_markdown(__file__, "intro"))

    st.divider()

    # --- De fem lagene som klikkbare ekspandere ---
    st.subheader("🧩 De fem lagene")
    st.caption("Klikk på et lag for å se mer.")

    with st.expander("📜 1. Instruksjonslag (System Prompt)"):
        st.markdown(load_markdown(__file__, "system_prompt"))

    with st.expander("🔧 2. Verktøylag (Tool Interface)"):
        st.markdown(load_markdown(__file__, "tool_interface"))

    with st.expander("🧱 3. Skills-system (Utvidelsesmekanisme)"):
        st.markdown(load_markdown(__file__, "skills_system"))

    with st.expander("✅ 4. Oppgavestyring (TODO-liste)"):
        st.markdown(load_markdown(__file__, "oppgavestyring"))

    with st.expander("👁️ 5. Kontekstbevissthet"):
        st.markdown(load_markdown(__file__, "kontekstbevissthet"))

    st.divider()

    # --- Forbehold ---
    callout(
        load_markdown(__file__, "forbehold"),
        kind="subtle",
        title="ℹ️ Forbehold",
        key="arkitektur_forbehold",
    )

    st.divider()
    next_module_cta_for("demo_1")
