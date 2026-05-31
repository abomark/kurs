"""Tilgjengelige modeller – modul 13.

Implementerer PRD §FR-3.11 (presentasjons-modul) og §FR-3.12 (innhold i
markdown-filer under `content/`). Layout her — innhold i `content/*.md`
(Andre fyller dem inn selv).

Eksponerer `main()` som kalles fra `pages/tilgjengelige_modeller.py`.
"""

from __future__ import annotations

import streamlit as st

from modules.shared.ui import crumb, load_markdown, next_module_cta_for


def main() -> None:
    crumb(["Kursmoduler", "14 · Tilgjengelige modeller"])
    st.title("🧠 Tilgjengelige modeller")
    st.caption("Modul 14 · Hvilke modeller står til rådighet, og når velger du hvilken?")
    st.divider()

    # --- Intro ---
    st.markdown(load_markdown(__file__, "intro"))

    st.divider()

    # --- Seksjon 1: Oversikt over modellene ---
    st.subheader("📋 Oversikt")
    st.markdown(load_markdown(__file__, "oversikt"))

    st.divider()

    # --- Seksjon 2: Når velger du hvilken ---
    st.subheader("🤔 Når velger du hvilken")
    st.markdown(load_markdown(__file__, "valg"))

    st.divider()

    # --- Seksjon 3: Praktisk eksempel ---
    st.subheader("🎯 Eksempel")
    with st.container(border=True):
        st.markdown(load_markdown(__file__, "eksempel"))

    st.divider()
    next_module_cta_for("individuell_oppgave_modellvalg")
