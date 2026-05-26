"""Fra Google til spesifikasjon – modul 1.

Implementerer PRD §FR-3.11 (presentasjons-modul) og §FR-3.12 (innhold i
markdown-filer under `content/`). Kort, motiverende intro-modul som
setter rammen for hele kurset: tre epoker i hvordan vi skriver kode.

Layout per DESIGN_GUIDE v2 §8: crumb, H1 fra intro.md, brødtekst, tre
kort med epokene side om side, dempet refleksjons-callout, CTA til
neste modul.

Eksponerer `main()` som kalles fra `pages_content/modules/m01_evolusjon.py`.
"""

from __future__ import annotations

import streamlit as st

from modules.shared.ui import (
    callout,
    card,
    crumb,
    load_markdown,
    load_titled_markdown,
    next_module_cta_for,
)


ERA_FILES = [
    "era_1_googling",
    "era_2_assistanse",
    "era_3_spesifikasjon",
]


def main() -> None:
    crumb(["Kursmoduler", "01 · Evolusjon"])

    # Tittel + intro hentes fra første # H1-linje i intro.md slik at Andre
    # kan styre wording uten å åpne Python-fila.
    title, intro_body = load_titled_markdown(__file__, "intro")
    st.title(title or "📈 Fra Google til spesifikasjon")
    st.caption("Modul 1 · Tre epoker i hvordan vi skriver kode")
    st.divider()
    st.markdown(intro_body)

    st.divider()

    # --- Tre epoker side om side ---
    cols = st.columns(3, gap="medium")
    for col, era_name in zip(cols, ERA_FILES):
        era_title, era_body = load_titled_markdown(__file__, era_name)
        with col:
            with card(key=f"evolusjon_{era_name}"):
                st.markdown(f"#### {era_title}")
                st.markdown(era_body)

    st.divider()

    # --- Refleksjon — ingen datainnsamling, kun tankevekker ---
    callout(
        load_markdown(__file__, "hvor_er_du"),
        kind="subtle",
        title="🪞 Hvor er du i dag?",
        key="evolusjon_hvor_er_du",
    )

    st.divider()
    next_module_cta_for("cortex_code")
