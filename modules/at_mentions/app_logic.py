"""@-mentions – modul 5.

Implementerer PRD §FR-3.11 (presentasjons-modul) og §FR-3.12 (innhold i
markdown-filer under `content/`). Konseptuell innføring i hvordan
@-mentions fungerer i Cortex Code i Snowsight: hva som faktisk skjer
under panseret når du @-refererer en katalog-ressurs vs. når du skriver
fullt navn i prompten.

Eksponerer `main()` som kalles fra
`pages_content/modules/m05_at_mentions.py`.
"""

from __future__ import annotations

import streamlit as st

from modules.shared.ui import callout, card, crumb, load_markdown, next_module_cta_for


def main() -> None:
    crumb(["Kursmoduler", "08 · @-mentions"])
    st.title("@-mentions")
    st.caption("Modul 8 · Hvordan @-tegnet endrer hva agenten faktisk ser.")
    st.divider()

    # --- Seksjon 1: Hva er @-mentions? ---
    callout(
        load_markdown(__file__, "what_is_it"),
        kind="info",
        title="Hva er @-mentions?",
        key="atmen_what",
    )

    st.divider()

    # --- Seksjon 2: Hva agenten ser ---
    st.subheader("Hva agenten faktisk ser")
    st.markdown(load_markdown(__file__, "what_agent_sees"))

    st.divider()

    # --- Seksjon 3: Med vs. uten @-mention ---
    st.subheader("Med @-mention vs. uten")
    with card(key="atmen_compare"):
        st.markdown(load_markdown(__file__, "with_vs_without"))

    st.divider()

    # --- Seksjon 4: Hvorfor det betyr noe ---
    callout(
        load_markdown(__file__, "why_it_matters"),
        kind="warn",
        title="Hvorfor det betyr noe",
        key="atmen_why",
    )

    st.divider()
    next_module_cta_for("individuell_oppgave_at_mentions")
