"""Første demo - modul 6.

Implementerer PRD §FR-3.11 (presentasjons-modul) og §FR-3.12 (innhold i
markdown-filer under `content/`). Layout her - innhold i `content/*.md`.

Kun en slide-lik agenda. Selve demoen kjøres live i plenum; detalj-
segmentene (Workspace, Cortex Code, kostnadsdashbord) er fjernet fra
siden (eier-beslutning). Ingen snakkepunkter eller varighet på siden
(DESIGN_GUIDE §1.9) - det er presentatørens egne notater.

Eksponerer `main()` som kalles fra `pages/demo_1.py`.
"""

from __future__ import annotations

import streamlit as st

from modules.shared.ui import (
    callout,
    crumb,
    load_markdown,
    module_header,
    next_module_cta_for,
)


def main() -> None:
    crumb(["Kursmoduler", "06 · Første demo"])
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
    next_module_cta_for("pages/individuell_oppgave_1.py")
