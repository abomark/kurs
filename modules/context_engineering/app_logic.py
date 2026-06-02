"""Context engineering - modul 24.

Implementerer PRD §FR-3.11 (presentasjons-modul) og §FR-3.12 (innhold i
markdown-filer under `content/`). Strukturen følger eierens innhold: hva det
er, hva en god prompt sier, en prompt-mal, daarlig vs bedre prompt, vanlige
feil, hvor konteksten legges, og en hovedregel.

Layout: crumb, H1 + intro (hva er det), seksjoner med subheaders/callouts.
Prompt-kodeblokker rendres via `render_markdown_wrapped_code` (wrap, ingen
horisontal scroll). Innhold ligger i `content/*.md` (jf. §FR-3.12).

Eksponerer `main()` som kalles fra `pages_content/modules/m24_context_engineering.py`.
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
    render_markdown_wrapped_code,
)


def main() -> None:
    crumb(["Kursmoduler", "24 · Context engineering"])

    # --- Hva er det (intro under H1) ---
    title, intro_body = load_titled_markdown(__file__, "intro")
    module_header(title or "Context engineering", subtitle="Riktig kontekst, på riktig sted, til riktig tid")
    st.divider()
    st.markdown(intro_body)

    st.divider()

    # --- En god prompt bør si ---
    st.subheader("En god prompt bør si")
    st.markdown(load_markdown(__file__, "god_prompt"))

    st.divider()

    # --- Enkel prompt-mal ---
    st.subheader("Enkel prompt-mal")
    render_markdown_wrapped_code(load_markdown(__file__, "mal"))

    st.divider()

    # --- Daarlig vs bedre prompt (to kolonner) ---
    st.subheader("Dårlig prompt vs bedre prompt")
    col_daarlig, col_bedre = st.columns(2, gap="medium")
    with col_daarlig:
        st.markdown("**Dårlig**")
        render_markdown_wrapped_code(load_markdown(__file__, "daarlig"))
    with col_bedre:
        st.markdown("**Bedre**")
        render_markdown_wrapped_code(load_markdown(__file__, "bedre"))

    st.divider()

    # --- Vanlige feil ---
    callout(
        load_markdown(__file__, "vanlige_feil"),
        kind="warn",
        title="Vanlige feil",
        key="ce_vanlige_feil",
    )

    st.divider()

    # --- Hvor legger vi konteksten ---
    st.subheader("Hvor legger vi konteksten?")
    st.markdown(load_markdown(__file__, "hvor"))

    st.divider()

    # --- Hovedregel ---
    callout(
        load_markdown(__file__, "hovedregel"),
        kind="tip",
        title="Hovedregel",
        key="ce_hovedregel",
    )

    st.divider()
    next_module_cta_for("individuell_oppgave_kohort")
