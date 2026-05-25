"""Demo 2 – modul 17 (Realistisk bank-use-case).

Implementerer PRD §FR-3.11 og §FR-3.12. Presentatør-runbook for live
walkthrough av en realistisk bank-case (kredittscoring/churn/etc.) —
oppfølger til Demo 1 nå som deltakere har prøvd agenten selv.

Eksponerer `main()` som kalles fra `pages/demo_2.py`.
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
    "segment_1",
    "segment_2",
    "segment_3",
]


def main() -> None:
    crumb(["Kursmoduler", "17 · Demo 2"])
    st.title("🎬 Demo 2")
    st.caption("Modul 17 · Live-demo: realistisk bank-use-case med Cortex Code.")
    st.divider()

    callout(
        load_markdown(__file__, "agenda"),
        kind="info",
        key="demo2_agenda",
    )
    st.caption(
        "Presentatør-runbook — skjul/vis snakkepunkter med knappen under."
    )

    show_notes = st.toggle("Vis snakkepunkter", value=True, key="demo_2_show_notes")
    st.divider()

    if show_notes:
        for name in DEMO_FILES:
            title, body = load_titled_markdown(__file__, name)
            with st.container(border=True):
                st.markdown(f"### {title}")
                st.markdown(body)

        st.divider()

        st.subheader("🤔 Diskusjon etter demoen")
        st.markdown(load_markdown(__file__, "diskusjon"))
    else:
        callout(
            "Snakkepunkter er skjult. Slå på for å se runbook.",
            kind="warning",
            key="demo2_hidden",
        )

    st.divider()
    next_module_cta_for("pages/autonomous_loop.py")
