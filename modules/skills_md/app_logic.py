"""skills.md – modul 11.

Implementerer PRD §FR-3.11 (presentasjons-modul) og §FR-3.12 (innhold i
markdown-filer under `content/`). Konseptuell innføring i skills.md-
mekanismen, parallelt med AGENTS.md (modul 10).

Layout per DESIGN_GUIDE v2 §8.

Eksponerer `main()` som kalles fra `pages/skills_md.py`.
"""

from __future__ import annotations

import streamlit as st

from modules.shared.ui import callout, card, crumb, load_markdown, next_module_cta_for


def main() -> None:
    crumb(["Kursmoduler", "11 · skills.md"])
    st.title("🛠️ skills.md")
    st.caption("Modul 11 · Hva er skills.md, og hvordan skiller den seg fra AGENTS.md?")
    st.divider()

    # --- Seksjon 1: Hva er det? ---
    callout(
        load_markdown(__file__, "what_is_it"),
        kind="info",
        title="📍 Hva er skills.md?",
        key="skills_what",
    )

    st.divider()

    # --- Seksjon 2: Hvordan fungerer den? ---
    st.subheader("⚙️ Hvordan fungerer den?")
    st.markdown(load_markdown(__file__, "how_it_works"))

    st.divider()

    # --- Seksjon 3: Hvor plasserer man den? ---
    st.subheader("📂 Hvor plasserer man den?")
    st.markdown(load_markdown(__file__, "where_to_place"))

    st.divider()

    # --- Seksjon 4: skills.md vs AGENTS.md ---
    st.subheader("skills.md vs AGENTS.md")
    st.markdown(load_markdown(__file__, "vs_agents_md"))

    st.divider()

    # --- Seksjon 5: Eksempel-fil (i kort) ---
    st.subheader("📄 Eksempel-fil")
    with card(key="skills_example"):
        st.markdown(load_markdown(__file__, "example"))

    st.divider()

    # --- Seksjon 6: Overgang til Gruppeoppgave 1 ---
    # CTA-kortet henter beskrivelsen fra MODULES i home.py — Andres tekst.
    next_module_cta_for("pages/gruppeoppgave_1.py")
