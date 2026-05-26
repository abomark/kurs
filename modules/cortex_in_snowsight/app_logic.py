"""Cortex Code i Snowsight – modul 4.

Implementerer PRD §FR-3.11 (presentasjons-modul) og §FR-3.12 (innhold i
markdown-filer under `content/`). Layout her — innhold i `content/*.md`.

Fyll inn `content/*.md` etter hvert.

Eksponerer `main()` som kalles fra `pages/cortex_in_snowsight.py`.
"""

from __future__ import annotations

import streamlit as st

from modules.shared.ui import crumb, load_markdown, next_module_cta_for


def main() -> None:
    crumb(["Kursmoduler", "04 · Cortex Code i Snowsight"])
    st.title("🌐 Cortex Code i Snowsight")
    st.caption("Modul 4 · Hvordan bruke Cortex Code gjennom Snowflakes web-UI")
    st.divider()

    # --- Intro ---
    st.markdown(load_markdown(__file__, "intro"))

    st.divider()

    # --- Seksjon 1: Hvor finner du den ---
    st.subheader("📍 Hvor finner du Cortex Code")
    st.markdown(load_markdown(__file__, "section_1_location"))

    st.divider()

    # --- Seksjon 2: Grensesnittet ---
    st.subheader("🖥️ Grensesnittet")
    st.markdown(load_markdown(__file__, "section_2_interface"))

    st.divider()

    # --- Seksjon 3: Typiske oppgaver ---
    st.subheader("💬 Hva kan du be om")
    st.markdown(load_markdown(__file__, "section_3_tasks"))

    st.divider()

    # --- Seksjon 4: Eksempel-flyt ---
    st.subheader("🎯 Eksempel-flyt")
    st.markdown(load_markdown(__file__, "section_4_example"))

    st.divider()

    # --- Seksjon 5: Tips og fallgruver ---
    st.subheader("⚠️ Tips og fallgruver")
    st.markdown(load_markdown(__file__, "section_5_tips"))

    st.divider()
    next_module_cta_for("pages/demo_1.py")
