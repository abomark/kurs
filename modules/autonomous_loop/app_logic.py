"""Autonomous loop i dybden – modul 23.

Implementerer PRD §FR-3.11 og §FR-3.12. Konseptuell utdyping av sløyfen
som ble nevnt kort i modul 1 (Cortex Code) — Planning → Action →
Observation → Reflection.

Eksponerer `main()` som kalles fra `pages/autonomous_loop.py`.
"""

from __future__ import annotations

import streamlit as st

from modules.shared.ui import (
    crumb,
    load_markdown,
    load_titled_markdown,
    next_module_cta_for,
)

LOOP_STEPS = [
    "step_plan",
    "step_act",
    "step_observe",
    "step_reflect",
]


def main() -> None:
    crumb(["Kursmoduler", "23 · Autonomous loop i dybden"])
    st.title("🌀 Autonomous loop i dybden")
    st.caption("Modul 23 · Hva skjer egentlig inne i agenten?")
    st.divider()

    # --- Intro ---
    st.markdown(load_markdown(__file__, "intro"))

    st.divider()

    # --- De fire fasene ---
    st.subheader("🌀 De fire fasene")
    show_all = st.toggle(
        "Vis alle fasene",
        value=False,
        help="Bra for slides/screenshot. Av som default for live-presentasjon.",
        key="autonomous_loop_show_all",
    )

    for name in LOOP_STEPS:
        title, body = load_titled_markdown(__file__, name)
        with st.expander(title or name, expanded=show_all):
            st.markdown(body)

    st.divider()

    # --- Konkret eksempel ---
    st.subheader("🎯 Konkret eksempel")
    with st.container(border=True):
        st.markdown(load_markdown(__file__, "example"))

    st.divider()
    next_module_cta_for("individuell_oppgave_5")
