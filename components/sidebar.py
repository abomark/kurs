"""Custom sidebar med kategori-prikker.

Erstatter `st.navigation()` fordi vi trenger full kontroll over rendering
av prikkene. Bruker query params (`?page=...`) for navigasjon mellom sider.

Se DESIGN_GUIDE.md §11 for spec.
"""

from __future__ import annotations

import streamlit as st

from data.moduler import KATEGORI_FARGE, KATEGORI_NAVN, MODULER, page_id


SIDEBAR_CSS = """
<style>
:root {
    --kat-i: #7EB5D2;
    --kat-k: #B197FC;
    --kat-p: #66D9A8;
    --kat-g: #FFAD80;
    --kat-f: #94A3B8;
}

/* Skjul Streamlit sin default sidebar-navigasjon. */
[data-testid="stSidebarNav"] { display: none; }

section[data-testid="stSidebar"] > div:first-child {
    padding-top: 1rem;
}

/* Streamlit's stVerticalBlock i sidebaren har default `gap: 1rem`
   mellom hvert element. Vi vil ha tight pakking — overrid til 0. */
section[data-testid="stSidebar"] [data-testid="stVerticalBlock"] {
    gap: 0 !important;
}
section[data-testid="stSidebar"] [data-testid="stElementContainer"] {
    margin: 0 !important;
    padding: 0 !important;
}
section[data-testid="stSidebar"] [data-testid="stMarkdown"] {
    margin: 0 !important;
}
section[data-testid="stSidebar"] [data-testid="stMarkdownContainer"] {
    margin: 0 !important;
}
section[data-testid="stSidebar"] [data-testid="stMarkdownContainer"] p {
    margin: 0 !important;
}

.sb-brand {
    display: flex;
    align-items: center;
    gap: 10px;
    padding: 0 16px 14px;
    border-bottom: 1px solid rgba(255, 255, 255, 0.06);
    margin-bottom: 6px;
}
.sb-brand-mark {
    width: 28px; height: 28px;
    border-radius: 6px;
    background: #005AA4;
    display: flex; align-items: center; justify-content: center;
    font-size: 11px; font-weight: 600; color: white;
}
.sb-brand-text { font-size: 13px; font-weight: 600; color: #F4F6FB; line-height: 1.2; }
.sb-brand-text small {
    display: block;
    font-size: 10px; font-weight: 400;
    color: #6B7691; margin-top: 2px;
}

.sb-section {
    font-size: 10px; font-weight: 600;
    letter-spacing: 0.08em; text-transform: uppercase;
    color: #6B7691;
    padding: 12px 16px 4px;
}

.sb-item,
.sb-item:hover,
.sb-item:focus,
.sb-item:visited,
.sb-item:active {
    text-decoration: none !important;
}

.sb-item {
    display: flex;
    align-items: center;
    gap: 10px;
    padding: 6px 16px;
    font-size: 13px;
    color: #F4F6FB;
    border-left: 3px solid transparent;
    cursor: pointer;
    transition: background 0.12s ease;
}
.sb-item:hover {
    background: rgba(0, 90, 164, 0.10);
    color: #F4F6FB;
}
.sb-item.active {
    background: rgba(0, 90, 164, 0.18);
    border-left-color: #005AA4;
    font-weight: 600;
    padding-left: 13px;
}

.sb-num {
    font-family: ui-monospace, 'JetBrains Mono', monospace;
    font-size: 11px;
    color: #6B7691;
    min-width: 18px;
}
.sb-item.active .sb-num { color: #7EB5D2; }

.sb-dot {
    width: 7px; height: 7px;
    border-radius: 50%;
    flex-shrink: 0;
}

.sb-divider {
    height: 1px;
    background: rgba(255, 255, 255, 0.06);
    margin: 8px 16px;
}
</style>
"""


def render_sidebar(active_slug: str | None = None) -> None:
    """Render hele sidemenyen. Kall denne fra app.py før sideinnhold."""
    with st.sidebar:
        st.markdown(SIDEBAR_CSS, unsafe_allow_html=True)

        # Brand
        st.markdown(
            '<div class="sb-brand">'
            '<div class="sb-brand-mark">CC</div>'
            '<div class="sb-brand-text">Cortex Code'
            '<small>Kurs 2026</small></div>'
            '</div>',
            unsafe_allow_html=True,
        )

        # Forside (uten gruppe-header)
        _render_link("Forside", "forside", active_slug)
        st.markdown('<div class="sb-divider"></div>', unsafe_allow_html=True)

        # Oversikt
        st.markdown('<div class="sb-section">Oversikt</div>', unsafe_allow_html=True)
        _render_link("Bli kjent", "bli_kjent", active_slug)
        _render_link("Resultater", "resultater", active_slug)

        # Kursmoduler
        st.markdown('<div class="sb-section">Kursmoduler</div>', unsafe_allow_html=True)
        for modul in MODULER:
            _render_modul(modul, active_slug)

        # Footer
        st.markdown('<div class="sb-divider"></div>', unsafe_allow_html=True)
        _render_link("Administrasjon", "admin", active_slug, dimmed=True)


def _render_link(
    tittel: str,
    slug: str,
    active_slug: str | None,
    dimmed: bool = False,
) -> None:
    is_active = (slug == active_slug)
    klass = "sb-item active" if is_active else "sb-item"
    style = ' style="color: #6B7691;"' if dimmed and not is_active else ""
    href = f"?page={slug}"
    st.markdown(
        f'<a class="{klass}" href="{href}" target="_self"{style}>{tittel}</a>',
        unsafe_allow_html=True,
    )


def _render_modul(modul: dict, active_slug: str | None) -> None:
    slug = page_id(modul)
    is_active = (slug == active_slug)
    klass = "sb-item active" if is_active else "sb-item"
    farge = KATEGORI_FARGE[modul["kategori"]]
    href = f"?page={slug}"
    nr = f"{modul['nr']:02d}"
    st.markdown(
        f'<a class="{klass}" href="{href}" target="_self">'
        f'<span class="sb-dot" style="background: {farge};"'
        f' title="{KATEGORI_NAVN[modul["kategori"]]}"></span>'
        f'<span class="sb-num">{nr}</span>'
        f'{modul["tittel"]}</a>',
        unsafe_allow_html=True,
    )
