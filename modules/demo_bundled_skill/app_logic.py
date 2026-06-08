"""Demo: Bundled skill (lineage) - modul 18.

Implementerer PRD §FR-3.11 (presentasjons-modul) og §FR-3.12 (innhold i
markdown-filer under `content/`). Presentatør-runbook: vis hvordan man
først lar Cortex Code forklare en bundled skill (`@(serverSkill:lineage)`),
og deretter anvender den på et levende objekt. Speiler runbook-strukturen
i `demo_1`.

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
    module_header,
    next_module_cta_for,
)

DEMO_FILES = [
    "segment_1",
    "segment_2",
]


def main() -> None:
    crumb(["Kursmoduler", "19 · Demo: Bundled skill"])
    module_header("Demo: Bundled skill - lineage", subtitle="Live-demo: forstå en bundled skill, så anvend den på et objekt.")
    st.divider()

    callout(
        load_markdown(__file__, "formaal"),
        kind="info",
        title="Formål",
        key="demo_skill_formaal",
    )

    st.divider()

    for name in DEMO_FILES:
        title, body = load_titled_markdown(__file__, name)
        with st.container(border=True):
            st.markdown(f"### {title}")
            st.markdown(body)

    st.divider()
    next_module_cta_for("individuell_oppgave_bundled_skill")
