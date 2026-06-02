"""Snowsight vs CLI - modul 3.

Implementerer PRD §FR-3.11 (presentasjons-modul) og §FR-3.12 (innhold i
markdown-filer under `content/`). Layout her - innhold i `content/*.md`.

Eksponerer `main()` som kalles fra `pages/cortex_interaction.py`.
"""

from __future__ import annotations

import os

import streamlit as st

from modules.shared.ui import crumb, load_markdown, module_header, next_module_cta_for

_HERE = os.path.dirname(__file__)


def _image_or_placeholder(filename: str, label: str) -> None:
    """Vis skjermbildet hvis det finnes i content/, ellers en stiplet placeholder.

    Bildefilene legges i `modules/cortex_interaction/content/` av Andre.
    """
    path = os.path.join(_HERE, "content", filename)
    if os.path.exists(path):
        st.image(path, width="stretch")
    else:
        st.markdown(
            "<div style='border:1px dashed #D5DEEA;border-radius:10px;"
            "padding:56px 24px;text-align:center;color:#6B7280;"
            "background:#F7F8FB;font-size:14px;'>"
            f"Skjermbilde av {label} settes inn her</div>",
            unsafe_allow_html=True,
        )


def main() -> None:
    crumb(["Kursmoduler", "03 · Snowsight vs CLI"])
    module_header("Snowsight vs CLI", subtitle="To måter å samhandle med Cortex Code på")
    st.divider()

    st.markdown(load_markdown(__file__, "intro"))

    st.divider()

    # --- Side-by-side: skjermbilde av hver flate ---
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("#### Snowsight")
        _image_or_placeholder("snowsight.png", "Snowsight")
    with col2:
        st.markdown("#### CLI")
        _image_or_placeholder("cli.png", "CLI")

    st.divider()

    # --- Lenke til dokumentasjon for CLI ---
    st.markdown(load_markdown(__file__, "cli_docs"))

    st.divider()
    next_module_cta_for("arkitektur")
