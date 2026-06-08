"""Hvordan kode assistenter fungerer - modul 2.

Implementerer PRD §FR-3.11 (presentasjons-modul) og §FR-3.12 (innhold i
markdown-filer under `content/`). Generell, produkt-uavhengig mental modell i
fire takter: (1) en oppgave brytes ned i kontekst -> plan -> handling, (2) en
modell alene kan bare skrive, (3) loesningen er en dialog av verktoykall, og
(4) dette kalles Tool Use.

Skilt ut fra "Under panseret" (arkitektur) slik at den generelle mekanikken
laeres foer det Cortex Code-spesifikke. Eksponerer `main()` som kalles fra
`pages_content/modules/m02_kodeassistenter.py`.
"""

from __future__ import annotations

import os

import streamlit as st

from modules.shared.ui import (
    callout,
    crumb,
    load_markdown,
    load_split_markdown,
    module_header,
    next_module_cta_for,
    numbered_steps,
)

_HERE = os.path.dirname(__file__)


def _image_or_placeholder(filename: str, label: str) -> None:
    """Vis bildet hvis det finnes i content/, ellers en stiplet placeholder.

    Bildefilene legges i `modules/kodeassistenter/content/` av Andre.
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
    crumb(["Kursmoduler", "02 · Kode-assistenter"])
    # Subtittel: Andre fyller ut ved behov (innhold er Andres domene).
    module_header("Hvordan kode assistenter fungerer")
    st.divider()

    # --- Lead-diagram: hele mekanismen i ett bilde ---
    _image_or_placeholder("assistant.png", "kode-assistent: spraakmodell + verktoy i en lokke")
    st.caption(load_markdown(__file__, "bilde_assistant"))

    st.divider()

    # --- Takt 1: oppgaven brytes ned i tre steg ---
    st.subheader("Fra oppgave til handling")
    steg_oppgave = load_split_markdown(__file__, "steg_oppgave")
    numbered_steps(
        [(t, steg_oppgave[t]) for t in steg_oppgave if t],
        key="kodeass_steg_oppgave",
    )
    callout(
        load_markdown(__file__, "steg_note"),
        kind="warn",
        title="Steg 1 og 3 berører omverdenen",
        key="kodeass_steg_note",
    )

    st.divider()

    # --- Takt 2: en modell alene kan bare skrive ---
    st.subheader("En modell alene kan bare skrive")
    _image_or_placeholder("llm.png", "spraakmodell alene, uten kode-assistent")
    st.caption(load_markdown(__file__, "bilde_llm"))
    st.markdown(load_markdown(__file__, "overgang_sporsmaal"))

    st.divider()

    # --- Takt 3: loesningen er en dialog av verktoykall ---
    st.subheader("Løsningen: en dialog av verktøykall")
    steg_lokke = [t for t in load_split_markdown(__file__, "steg_lokke") if t]
    numbered_steps(steg_lokke, key="kodeass_steg_lokke")
    _image_or_placeholder("flyt.png", "meldingsflyt for et verktoykall")
    st.caption(load_markdown(__file__, "bilde_flyt"))

    st.divider()

    # --- Takt 4: dette kalles Tool Use ---
    st.subheader("Dette kalles Tool Use")
    callout(
        load_markdown(__file__, "tool_use"),
        kind="info",
        title="Tool Use",
        key="kodeass_tool_use",
    )
    callout(
        load_markdown(__file__, "claude_bro"),
        kind="tip",
        title="Claude er sterk på verktøy",
        key="kodeass_claude_bro",
    )

    st.divider()
    next_module_cta_for("cortex_code")
