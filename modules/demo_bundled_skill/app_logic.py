"""Demo: Bundled skill (lineage) – modul 18.

Implementerer PRD §FR-3.11 (presentasjons-modul) og §FR-3.12 (innhold i
markdown-filer under `content/`). Presentatør-runbook: vis hvordan man
først lar Cortex Code forklare en bundled skill (`@(serverSkill:lineage)`),
og deretter anvender den på et levende objekt — gjerne kombinert med Plan
Mode. Speiler runbook-strukturen i `demo_1`/`demo_2`.

Eksponerer `main()` som kalles fra
`pages_content/modules/m18_demo_bundled_skill.py`.
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
    crumb(["Kursmoduler", "18 · Demo: Bundled skill"])
    st.title("🎬 Demo: Bundled skill (lineage)")
    st.caption("Modul 18 · Live-demo: forstå en bundled skill, så anvend den på et levende objekt.")
    st.divider()

    callout(
        load_markdown(__file__, "agenda"),
        kind="info",
        key="demo_skill_agenda",
    )
    st.caption(
        "Presentatør-runbook — skjul/vis snakkepunkter med knappen under."
    )

    show_notes = st.toggle("Vis snakkepunkter", value=True, key="demo_skill_show_notes")
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
            key="demo_skill_hidden",
        )

    st.divider()
    next_module_cta_for("individuell_oppgave_bundled_skill")
