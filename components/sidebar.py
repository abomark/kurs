"""Custom sidebar med kategori-prikker og seksjonsgruppering.

Erstatter `st.navigation()` fordi vi trenger full kontroll over rendering
av prikkene og seksjons-containerne. Bruker query params (`?page=...`) for
navigasjon mellom sider.

Modulene grupperes visuelt i seksjoner (Innføring, Konfigurasjon,
Gruppearbeid, Dybde, Avslutning) per `data.moduler.SECTIONS`. Den aktive
seksjonen får Vann-stripe og "DU ER HER"-badge. Modulnummereringen er
fortsatt sekvensiell (01 og oppover, styrt av `MODULER`-rekkefølgen).

Se DESIGN_GUIDE.md §11 for spec.
"""

from __future__ import annotations

import streamlit as st

from data.moduler import (
    KATEGORI_FARGE,
    KATEGORI_NAVN,
    MODULER,
    SECTIONS,
    page_id,
)


# Fast sidebar-bredde. Endre denne ene verdien for å justere bredden
# (jf. DESIGN_GUIDE «fast sidebar-bredde»).
SIDEBAR_WIDTH = "320px"

_SIDEBAR_WIDTH_CSS = f"""
<style>
/* Fast bredde + skillelinje mot innholdet (lyst Bankbrief-tema). */
section[data-testid="stSidebar"] {{
    width: {SIDEBAR_WIDTH} !important;
    min-width: {SIDEBAR_WIDTH} !important;
    border-right: 1px solid #E3E8F1;
}}
section[data-testid="stSidebar"] > div {{
    width: {SIDEBAR_WIDTH} !important;
}}
</style>
"""


SIDEBAR_CSS = """
<style>
:root {
    --kat-i: #1F6FC4;
    --kat-k: #6B5BD2;
    --kat-p: #1E9E6A;
    --kat-g: #E08A3C;
    --kat-f: #8A93A6;
}

/* Skjul Streamlit sin default sidebar-navigasjon. */
[data-testid="stSidebarNav"] { display: none; }

section[data-testid="stSidebar"] > div:first-child {
    padding-top: 1rem;
}

/* Streamlit's stVerticalBlock i sidebaren har default `gap: 1rem`
   mellom hvert element. Vi vil ha tight pakking - overrid til 0. */
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
    border-bottom: 1px solid #E3E8F1;
    margin-bottom: 6px;
}
.sb-brand-mark {
    width: 28px; height: 28px;
    border-radius: 6px;
    background: #0A2C72;
    display: flex; align-items: center; justify-content: center;
    font-size: 11px; font-weight: 700; color: white;
}
.sb-brand-text { font-size: 13px; font-weight: 700; color: #0A2C72; line-height: 1.2; }
.sb-brand-text small {
    display: block;
    font-size: 10px; font-weight: 400;
    color: #6B7280; margin-top: 2px;
}

/* "Oversikt"-header over de faste sidene før Kursmoduler. */
.sb-section {
    font-size: 10px; font-weight: 700;
    letter-spacing: 0.08em; text-transform: uppercase;
    color: #6B7280;
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
    color: #3B4256;
    border-left: 3px solid transparent;
    cursor: pointer;
    transition: background 0.12s ease;
}
.sb-item:hover {
    background: #F2F5FA;
    color: #16203A;
}
/* Aktiv modul: azur tint-fyll + azur aksent-strek. */
.sb-item.active {
    background: #EAF1FB;
    border-radius: 3px;
    font-weight: 700;
    color: #0A2C72;
}

.sb-num {
    font-family: ui-monospace, 'JetBrains Mono', monospace;
    font-size: 11px;
    color: #6B7280;
    min-width: 18px;
}
.sb-item.active .sb-num { color: #1F6FC4; }

.sb-dot {
    width: 7px; height: 7px;
    border-radius: 50%;
    flex-shrink: 0;
}

.sb-divider {
    height: 1px;
    background: #E3E8F1;
    margin: 8px 16px;
}

/* === Kursseksjoner (Innføring, Konfigurasjon, ...) === */

.kurs-section {
    border-left: 2px solid #E3E8F1;
    padding-left: 10px;
    margin: 0 4px 14px 6px;
}
.kurs-section.active {
    border-left: 3px solid #1F6FC4;   /* Azur strek */
    padding-left: 9px;                 /* kompenser for tykkere border */
}
.kurs-section-head {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 2px 0 6px;
    gap: 8px;
}
.kurs-section-title {
    font: 700 11px/1 Arial, sans-serif;
    letter-spacing: 0.08em;
    color: #6B7280;
    text-transform: uppercase;
}
.kurs-section.active .kurs-section-title {
    color: #0A2C72;                    /* Marine */
}
.kurs-badge {
    font: 700 9px/1 Arial, sans-serif;
    letter-spacing: 0.05em;
    background: #0A2C72;
    color: #fff;
    padding: 3px 6px;
    border-radius: 3px;
    text-transform: uppercase;
    white-space: nowrap;
}
</style>
"""


def render_sidebar(active_slug: str | None = None) -> None:
    """Render hele sidemenyen. Kall denne fra app.py før sideinnhold."""
    with st.sidebar:
        st.markdown(SIDEBAR_CSS, unsafe_allow_html=True)
        st.markdown(_SIDEBAR_WIDTH_CSS, unsafe_allow_html=True)

        # Brand
        st.markdown(
            '<div class="sb-brand">'
            '<div class="sb-brand-mark">CC</div>'
            '<div class="sb-brand-text">Cortex Code'
            '<small>Kurs 2026</small></div>'
            '</div>',
            unsafe_allow_html=True,
        )

        st.markdown('<div class="sb-divider"></div>', unsafe_allow_html=True)

        # Oversikt (uberørt av seksjonsgruppering)
        st.markdown('<div class="sb-section">Oversikt</div>', unsafe_allow_html=True)
        _render_link("Bli kjent", "bli_kjent", active_slug)
        _render_link("Resultater", "resultater", active_slug)

        # Kursmoduler - gruppert i seksjoner
        st.markdown('<div class="sb-section">Kursmoduler</div>', unsafe_allow_html=True)
        # Slå opp moduler ved page_id en gang så vi unngår O(n²)-loop.
        moduler_by_page_id = {page_id(m): m for m in MODULER}
        for seksjon in SECTIONS:
            _render_seksjon(seksjon, moduler_by_page_id, active_slug)

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
    style = ' style="color: #9AA1AD;"' if dimmed and not is_active else ""
    href = f"?page={slug}"
    st.markdown(
        f'<a class="{klass}" href="{href}" target="_self"{style}>{tittel}</a>',
        unsafe_allow_html=True,
    )


def _render_seksjon(
    seksjon: dict,
    moduler_by_page_id: dict[str, dict],
    active_slug: str | None,
) -> None:
    """Render en seksjons-container (header + alle moduler) som en HTML-blob.

    Vi MÅ bygge alt som en markdown-streng - Streamlit pakker hver
    `st.markdown`-kall i sin egen `stMarkdownContainer`, så et "åpent" div
    fra en kall vil auto-lukkes der og ikke wrappe påfølgende elementer.
    Konsekvens: `.kurs-section`-stripen vil ikke spenne over modulene
    hvis vi splitter på flere kall.
    """
    is_active = active_slug in seksjon["modules"]
    klass = "kurs-section active" if is_active else "kurs-section"
    badge = (
        '<span class="kurs-badge">Du er her</span>' if is_active else ""
    )

    modul_links = []
    for slug in seksjon["modules"]:
        modul = moduler_by_page_id.get(slug)
        if modul is None:
            # Defensiv - page_id i SECTIONS som ikke matcher MODULER betyr
            # at noen har endret slug eller nr uten å oppdatere SECTIONS.
            continue
        modul_links.append(_modul_html(modul, active_slug))

    html = (
        f'<div class="{klass}">'
        f'<div class="kurs-section-head">'
        f'<span class="kurs-section-title">{seksjon["label"]}</span>'
        f'{badge}'
        f'</div>'
        f'{"".join(modul_links)}'
        f'</div>'
    )
    st.markdown(html, unsafe_allow_html=True)


def _modul_html(modul: dict, active_slug: str | None) -> str:
    """Returner HTML for en modul-lenke (uten å rendre den)."""
    slug = page_id(modul)
    is_active = (slug == active_slug)
    klass = "sb-item active" if is_active else "sb-item"
    farge = KATEGORI_FARGE[modul["kategori"]]
    href = f"?page={slug}"
    nr = f"{modul['nr']:02d}"
    return (
        f'<a class="{klass}" href="{href}" target="_self">'
        f'<span class="sb-dot" style="background: {farge};"'
        f' title="{KATEGORI_NAVN[modul["kategori"]]}"></span>'
        f'<span class="sb-num">{nr}</span>'
        f'{modul["tittel"]}</a>'
    )
