"""Første demo – modul 8.

Implementerer PRD §FR-3.11 (presentasjons-modul) og §FR-3.12 (innhold i
markdown-filer under `content/`). Layout her — innhold i `content/*.md`.

Runbook for tre demo-segmenter: Workspace → Cortex Code → bokstavspørsmål.
Toggle "Vis snakkepunkter"styrer om hele runbooken vises (live) eller
skjules (når man rent presenterer på storskjerm).

Eksponerer `main()` som kalles fra `pages/demo_1.py`.
"""

from __future__ import annotations

import streamlit as st

from modules.shared.ui import (
    callout,
    crumb,
    load_markdown,
    load_titled_markdown,
    next_module_cta_for,
)

DEMO_FILES = [
    "demo_1_workspace",
    "demo_2_cortex_code",
    "demo_3_bokstav",
]


def main() -> None:
    crumb(["Kursmoduler", "06 · Første demo"])
    st.title("Første demo")
    st.caption("Modul 6 · Live-demo: workspace, Cortex Code, og bokstavspørsmålet")
    st.divider()

    # --- Oversikt ---
    callout(
        load_markdown(__file__, "agenda"),
        kind="info",
        key="demo1_agenda",
    )
    st.caption(
        "Denne siden er ment som presentatør-runbook. Skjul/vis "
        "snakkepunkter under demoen ved å bruke knappen under."
    )

    show_notes = st.toggle("Vis snakkepunkter", value=True)
    st.divider()

    if show_notes:
        # --- Demo-segmenter ---
        for name in DEMO_FILES:
            title, body = load_titled_markdown(__file__, name)
            with st.container(border=True):
                st.markdown(f"### {title}")
                st.markdown(body)

        st.divider()

        # --- Diskusjon ---
        st.subheader("Diskusjon etter demoen")
        st.markdown(load_markdown(__file__, "diskusjon"))

        st.divider()

        # --- Avklaring trengs ---
        callout(
            load_markdown(__file__, "avklaring"),
            kind="warning",
            key="demo1_avklaring",
        )
    else:
        callout(
            "Snakkepunkter er skjult. Slå på for å se runbook.",
            kind="warning",
            key="demo1_hidden",
        )

    st.divider()
    next_module_cta_for("pages/individuell_oppgave_1.py")
