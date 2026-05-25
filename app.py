"""Hovedinngang. Leser `?page=...` fra URL og dispatcher til riktig side.

Erstatter den tidligere `hub.py` (som brukte `st.navigation()`). Vi bruker
nå en custom sidebar med kategori-prikker (se DESIGN_GUIDE §11) og styrer
navigasjon via URL query params.

Kjør: `streamlit run app.py` fra repo-rot.
"""

from __future__ import annotations

import importlib

import streamlit as st

from components.sidebar import render_sidebar
from data.moduler import find_by_page_id, page_id

st.set_page_config(
    page_title="Cortex Code Kurs 2026",
    page_icon="❄",
    layout="centered",
    initial_sidebar_state="expanded",
)


def _load_page(slug: str):
    """Returner modul-objekt med `render`-callable. Returnerer None hvis ikke funnet."""
    # Faste sider på rot
    if slug == "forside":
        return importlib.import_module("pages_content.forside")
    if slug == "bli_kjent":
        return importlib.import_module("pages_content.bli_kjent")
    if slug == "resultater":
        return importlib.import_module("pages_content.resultater")
    if slug == "admin":
        return importlib.import_module("pages_content.admin")

    # Modul-sider: m05_agents_md → pages_content/modules/m05_agents_md.py
    if slug.startswith("m") and find_by_page_id(slug):
        try:
            return importlib.import_module(f"pages_content.modules.{slug}")
        except ImportError:
            return None

    return None


def main() -> None:
    # Hent gjeldende side fra URL — default til forsiden.
    active_slug = st.query_params.get("page", "forside")

    # Sidebar rendres alltid, før innholdet.
    render_sidebar(active_slug=active_slug)

    # Dispatch til sideinnhold.
    page = _load_page(active_slug)
    if page is None:
        st.error(f"Fant ikke side: `{active_slug}`")
        st.markdown('[← Tilbake til forsiden](?page=forside)')
        return
    page.render()


main()
