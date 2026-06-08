"""Kostnader - modul 8.

Presentasjons-modul (PRD §FR-3.11). Selve gjennomgangen av kostnader skjer i
PowerPoint i plenum, så denne siden er bevisst minimal og peker bare dit.
Innholds-markdownen under `content/` er foreløpig ubrukt (beholdt om temaet
skal bygges ut som egen side senere).

Eksponerer `main()` som kalles fra `pages_content/modules/m08_kostnader.py`.
"""

from __future__ import annotations

import streamlit as st

from modules.shared.ui import callout, crumb, module_header, next_module_cta_for


def main() -> None:
    crumb(["Kursmoduler", "12 · Kostnader"])
    module_header("Kostnader")
    st.divider()

    callout("Gjennomgang i PowerPoint.", kind="info", key="kostnader_ppt")

    st.divider()
    next_module_cta_for("agents_md")
