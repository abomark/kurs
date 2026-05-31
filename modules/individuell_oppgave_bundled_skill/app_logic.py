"""Individuell oppgave: Bundled skill – modul 19.

Implementerer PRD §FR-3.11 (presentasjons-modul) og §FR-3.12 (innhold i
markdown-filer under `content/`). Hands-on i skills.md-seksjonen: deltaker
ber først Cortex Code forklare en bundled skill (`@(serverSkill:lineage)`),
og anvender den deretter på en tabell de har tilgang til.

Eksponerer `main()` som kalles fra
`pages_content/modules/m19_individuell_oppgave_bundled_skill.py`.
"""

from __future__ import annotations

import streamlit as st

from modules.shared.ui import callout, crumb, load_markdown, next_module_cta_for


def main() -> None:
    crumb(["Kursmoduler", "19 · Individuell oppgave: Bundled skill"])
    st.title("🧩 Individuell oppgave: Bundled skill")
    st.caption("Modul 19 · Hands-on: forstå en bundled skill, så anvend den selv.")
    st.divider()

    callout(
        load_markdown(__file__, "oppgave"),
        kind="info",
        title="🎯 Oppgave",
        key="ind_bundled_oppgave",
    )

    st.divider()

    st.subheader("🪜 Steg")
    st.markdown(load_markdown(__file__, "steg"))

    st.divider()

    st.subheader("✅ Forventet resultat")
    st.markdown(load_markdown(__file__, "forventet"))

    st.divider()
    next_module_cta_for("gruppeoppgave_2")
