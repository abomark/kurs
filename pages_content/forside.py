"""Forside: viser kursmoduler gruppert etter kategori.

Bruker `data.moduler.MODULER` som single source of truth (DESIGN_GUIDE §11).
Kategori-prikker matcher sidebaren.
"""

from __future__ import annotations

import streamlit as st

from data.moduler import KATEGORI_FARGE, KATEGORI_NAVN, MODULER, page_id


_CARD_CSS = """
<style>
.fs-card {
    display: flex;
    align-items: center;
    gap: 12px;
    padding: 14px 18px;
    margin-bottom: 8px;
    background-color: #0F1729;
    border: 1px solid rgba(126, 181, 210, 0.10);
    border-radius: 10px;
    text-decoration: none;
    color: #F4F6FB;
    transition: background 0.12s ease, border-color 0.12s ease;
}
.fs-card:hover {
    background-color: #131C33;
    border-color: rgba(126, 181, 210, 0.20);
}
.fs-card-dot {
    width: 10px; height: 10px;
    border-radius: 50%;
    flex-shrink: 0;
}
.fs-card-num {
    font-family: ui-monospace, 'JetBrains Mono', monospace;
    font-size: 12px;
    color: #6B7691;
    min-width: 22px;
}
.fs-card-title { font-size: 14px; font-weight: 500; }
.fs-cat-label {
    font-size: 10px; font-weight: 600;
    letter-spacing: 0.08em; text-transform: uppercase;
    color: #6B7691;
    margin: 24px 0 8px;
}
</style>
"""


def render() -> None:
    st.markdown(_CARD_CSS, unsafe_allow_html=True)
    st.markdown("# Cortex Code Kurs 2026")
    st.caption(
        "17 moduler organisert i fem kategorier. Velg en modul fra "
        "sidemenyen til venstre, eller bla nedover for full oversikt."
    )
    st.divider()

    for kat_kode, kat_navn in KATEGORI_NAVN.items():
        moduler = [m for m in MODULER if m["kategori"] == kat_kode]
        if not moduler:
            continue
        farge = KATEGORI_FARGE[kat_kode]
        st.markdown(
            f'<div class="fs-cat-label">'
            f'<span style="display:inline-block;width:8px;height:8px;'
            f'border-radius:50%;background:{farge};margin-right:8px;'
            f'vertical-align:middle;"></span>{kat_navn}</div>',
            unsafe_allow_html=True,
        )
        for mod in moduler:
            href = f"?page={page_id(mod)}"
            st.markdown(
                f'<a class="fs-card" href="{href}" target="_self">'
                f'<span class="fs-card-dot" style="background:{farge};"></span>'
                f'<span class="fs-card-num">{mod["nr"]:02d}</span>'
                f'<span class="fs-card-title">{mod["tittel"]}</span>'
                f'</a>',
                unsafe_allow_html=True,
            )
