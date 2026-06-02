"""Evolusjon - modul 1.

Implementerer PRD §FR-3.11 (presentasjons-modul) og §FR-3.12 (innhold i
markdown-filer under `content/`). Kort, motiverende intro-modul som
setter rammen for hele kurset: tre epoker (Før / Nå / Snart) i hvordan vi
skriver kode og gjør analyser.

Layout per DESIGN_GUIDE v2 §8: crumb, H1 fra intro.md, brødtekst, tre
signaturkort med epokene side om side, Snowflake-illustrasjon, to refleksjons-
callouts (tankevekkere, ingen datainnsamling), CTA til neste modul.

Eksponerer `main()` som kalles fra `pages_content/modules/m01_evolusjon.py`.
"""

from __future__ import annotations

import os

import streamlit as st

from modules.shared.ui import (
    callout,
    crumb,
    load_markdown,
    load_titled_markdown,
    module_header,
    next_module_cta_for,
    signature_card,
)

_HERE = os.path.dirname(__file__)


ERA_FILES = [
    "epoke_1_for",
    "epoke_2_naa",
    "epoke_3_snart",
]


def _image_or_placeholder(filename: str, label: str) -> None:
    """Vis bildet hvis det finnes i content/, ellers en stiplet placeholder.

    Bildefilen legges i `modules/evolusjon/content/` av Andre.
    """
    path = os.path.join(_HERE, "content", filename)
    if os.path.exists(path):
        st.image(path, width="stretch")
    else:
        st.markdown(
            "<div style='border:1px dashed #D5DEEA;border-radius:10px;"
            "padding:56px 24px;text-align:center;color:#6B7280;"
            "background:#F7F8FB;font-size:14px;'>"
            f"Bilde settes inn her: {label}</div>",
            unsafe_allow_html=True,
        )


def main() -> None:
    crumb(["Kursmoduler", "01 · Evolusjon"])

    # Tittel + intro hentes fra første # H1-linje i intro.md slik at Andre
    # kan styre wording uten å åpne Python-fila.
    title, intro_body = load_titled_markdown(__file__, "intro")
    module_header(title or "Evolusjon", subtitle="Tre epoker i hvordan vi skriver kode og gjør analyser")
    st.divider()
    st.markdown(intro_body)

    st.divider()

    # --- Tre epoker side om side (varm fersken signaturflate, nummerert) ---
    cols = st.columns(3, gap="medium")
    for nr, (col, era_name) in enumerate(zip(cols, ERA_FILES), start=1):
        era_title, era_body = load_titled_markdown(__file__, era_name)
        with col:
            with signature_card(number=nr, title=era_title, key=f"evolusjon_{era_name}"):
                st.markdown(era_body)

    st.divider()

    # --- Illustrasjon: vibe coding vs strukturert agent-arbeid (med analytiker-ramme) ---
    _image_or_placeholder("vibe_vs_agentic_sdlc.png", "vibe coding vs agentisk arbeidsflyt")
    st.caption(load_markdown(__file__, "bilde_ramme"))

    st.divider()

    # --- Refleksjon - ingen datainnsamling, kun tankevekkere ---
    callout(
        load_markdown(__file__, "losninger_rundt_oss"),
        kind="subtle",
        title="Tenk igjennom",
        key="evolusjon_losninger",
    )

    # Diskusjonsspørsmål til deltakerne (presentatør stiller det muntlig).
    callout(
        load_markdown(__file__, "rolle_sporsmaal"),
        kind="info",
        title="Spørsmål til deg",
        key="evolusjon_rolle",
    )

    st.divider()
    next_module_cta_for("cortex_code")
