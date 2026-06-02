"""Første demo - modul 6.

Implementerer PRD §FR-3.11 (presentasjons-modul) og §FR-3.12 (innhold i
markdown-filer under `content/`). Layout her - innhold i `content/*.md`.

Slide-lik agenda + tre demo-segmenter: Workspace → Cortex Code →
kostnadsdashbord. Ingen snakkepunkter eller varighet på siden
(DESIGN_GUIDE §1.9) - det er presentatørens egne notater.

Eksponerer `main()` som kalles fra `pages/demo_1.py`.
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
    "demo_1_workspace",
    "demo_2_cortex_code",
    "demo_4_kostnad",
]


def main() -> None:
    crumb(["Kursmoduler", "05 · Første demo"])
    module_header(
        "Første demo",
        subtitle="Workspace, Cortex Code og kostnad",
    )
    st.divider()

    # --- Agenda ---
    callout(
        load_markdown(__file__, "agenda"),
        kind="info",
        key="demo1_agenda",
    )

    st.divider()

    # --- Demo-segmenter ---
    for name in DEMO_FILES:
        title, body = load_titled_markdown(__file__, name)
        with st.container(border=True):
            st.markdown(f"### {title}")
            st.markdown(body)

    st.divider()
    next_module_cta_for("pages/individuell_oppgave_1.py")
