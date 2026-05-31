"""memory.md – modul 17.

Implementerer PRD §FR-3.11 (presentasjons-modul) og §FR-3.12 (innhold i
markdown-filer under `content/`). Konseptuell innføring i Cortex Codes
persistent-memory-mekanisme (parallelt med AGENTS.md/skills.md, men med
bruker-scope i stedet for prosjekt-scope).

Layout per DESIGN_GUIDE v2 §8.

Eksponerer `main()` som kalles fra `pages_content/modules/m08_memory_md.py`.
"""

from __future__ import annotations

import streamlit as st

from modules.shared.ui import callout, card, crumb, load_markdown, next_module_cta_for


def main() -> None:
    crumb(["Kursmoduler", "18 · memory.md"])
    st.title("📓 memory.md")
    st.caption("Modul 18 · Hvordan Cortex Code husker ting på tvers av sesjoner.")
    st.divider()

    # --- Seksjon 1: Hva er det? ---
    callout(
        load_markdown(__file__, "what_is_it"),
        kind="info",
        title="📍 Hva er memory?",
        key="memory_what",
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

    # --- Seksjon 4: memory vs AGENTS.md ---
    st.subheader("memory vs AGENTS.md")
    st.markdown(load_markdown(__file__, "vs_agents_md"))

    st.divider()

    # --- Seksjon 5: Hvorfor ikke en skill? ---
    st.subheader("🤔 Hvorfor er dette ikke en skill?")
    st.markdown(load_markdown(__file__, "why_not_skill"))

    st.divider()

    # --- Seksjon 6: Hva bør lagres? ---
    callout(
        load_markdown(__file__, "what_to_store"),
        kind="warn",
        title="⚖️ Hva bør lagres — og hva ikke?",
        key="memory_what_to_store",
    )

    st.divider()

    # --- Seksjon 7: Eksempel-fil (i kort) ---
    st.subheader("📄 Eksempel-fil")
    with card(key="memory_example"):
        st.markdown(load_markdown(__file__, "example"))

    st.divider()

    # --- Seksjon 8: Overgang til Gruppeoppgave 3 ---
    st.markdown(load_markdown(__file__, "transition"))
    next_module_cta_for("gruppeoppgave_3")
