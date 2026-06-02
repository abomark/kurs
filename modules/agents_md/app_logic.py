"""AGENTS.md - modul 10.

Implementerer PRD §FR-3.11 (presentasjons-modul), §FR-3.12 (innhold i
markdown-filer) og §FR-3.15 (designsystem-helpers fra DESIGN_GUIDE v2).

Layout per DESIGN_GUIDE v2 §8: crumb øverst, H1, metadata-caption,
seksjoner med callouts/cards, CTA-kort til neste modul.

Eksponerer `main()` som kalles fra `pages/agents_md.py`.
"""

from __future__ import annotations

import streamlit as st

from modules.shared.ui import callout, card, crumb, load_markdown, module_header, next_module_cta_for


def main() -> None:
    crumb(["Kursmoduler", "12 · AGENTS.md"])
    module_header("AGENTS.md", subtitle="Hva er AGENTS.md, og hvorfor trenger vi det?")
    st.divider()

    # --- Seksjon 1: Hva er det? ---
    st.subheader("Hva er AGENTS.md?")
    callout(load_markdown(__file__, "what_is_it"), kind="info", key="agents_what")

    st.divider()

    # --- Seksjon 2: Hvordan fungerer den? ---
    st.subheader("Hvordan fungerer den?")
    st.markdown(load_markdown(__file__, "how_it_works"))

    st.divider()

    # --- Seksjon 3: Hvor plasserer man den? ---
    st.subheader("Hvor plasserer man den?")
    st.markdown(load_markdown(__file__, "where_to_place"))

    st.divider()

    # --- Seksjon 4: Hva skjer uten? ---
    st.subheader("Hva skjer uten?")
    callout(load_markdown(__file__, "without_it"), kind="warn", key="agents_without")

    st.divider()

    # --- Seksjon 5: Eksempel-fil (i kort for å elevere det) ---
    st.subheader("Eksempel-fil")
    with card(key="agents_example"):
        st.markdown(load_markdown(__file__, "example"))

    st.divider()

    # --- Seksjon 6: Overgang til Gruppeoppgave 1 ---
    # Pedagogisk valg: AGENTS.md → praktisk workshop (skipper skills.md i sekvensen).
    # CTA-kortet henter beskrivelsen fra MODULES i home.py - Andres tekst.
    next_module_cta_for("pages/gruppeoppgave_1.py")

    st.caption("Les mer: [agents.md](https://agents.md/)")
