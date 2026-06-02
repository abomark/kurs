"""Oppvarming - modul 0 (Bli kjent, Likert-variant).

Deltakerflyt: ti påstander, alle vurderes på 1-5-skala (1 = uenig,
5 = enig). Alle besvares samtidig i en form med en submit-knapp.
Hver innsending lagrer ti rader i `kurs.oppvarming_responses` (en
per påstand).

Implementerer PRD §FR-3.1 (variant), §FR-3.2 (innsending), §NFR-4.1
(anonymitet).

Eksponerer `main()` som kalles fra `pages/oppvarming.py`.
"""

from __future__ import annotations

import streamlit as st
from streamlit_extras.stylable_container import stylable_container

from modules.shared.ui import callout, crumb, module_header, next_module_cta_for

from .config import SCALE_MAX, SCALE_MIN, STATEMENTS
from .db import insert_likert_responses

# Venstre kolonne (spørsmål) får mest plass; høyre kolonne (segmentert
# Likert + uenig/enig-labels) krymper til ~280px ekvivalent.
COL_WIDTHS = [3, 2]

# Scoped CSS for den segmenterte Likert-kontrollen. Alle reglene prefikses
# av stylable_container med en unik scope-klasse, så `[data-testid=...]`
# slår ikke ut på resten av appen.
_LIKERT_CSS = [
    # Hver rad (st.columns ⇒ stHorizontalBlock): strammere rytme,
    # 1px skille-linje i stedet for st.divider, hover- og besvart-tint.
    """[data-testid="stHorizontalBlock"] {
        align-items: center;
        padding: 14px 16px;
        border-bottom: 1px solid #EEF1F6;
        border-radius: 10px;
        transition: background 0.12s ease;
    }""",
    """[data-testid="stHorizontalBlock"]:hover {
        background: #F7FAFE;
    }""",
    # Azur-tint når raden er besvart (CSS :has() - ingen rerun nødvendig).
    """[data-testid="stHorizontalBlock"]:has(input:checked) {
        background: #EAF1FB;
    }""",
    # stRadio får stå der Streamlit naturlig plasserer den (typisk venstre i
    # sin kolonne). Forsøk på å pushe den helt til høyre via margin-left:auto
    # eller flex justify-content:flex-end fungerte ikke pålitelig - heller
    # justeres uenig/enig-labelen til samme posisjon som baren (se under).
    """[data-testid="stRadio"] {
        width: fit-content;
    }""",
    # Skjul collapsed label-widget - den tar plass selv om den ikke vises.
    """[data-testid="stRadio"] > label[data-testid="stWidgetLabel"] {
        display: none !important;
    }""",
    # Segmentert container rundt de fem radio-knappene.
    """[data-testid="stRadio"] > div[role="radiogroup"] {
        display: flex;
        background: #F2F5FA;
        border: 1px solid #E3E8F1;
        border-radius: 8px;
        padding: 3px;
        gap: 2px;
        width: fit-content;
    }""",
    # Hvert segment: 36×30px, sentrert tall, ingen native margin.
    """[data-testid="stRadio"] label {
        margin: 0 !important;
        padding: 0 !important;
        width: 36px;
        height: 30px;
        border-radius: 5px;
        display: flex;
        align-items: center;
        justify-content: center;
        cursor: pointer;
        transition: background 0.12s ease, color 0.12s ease;
    }""",
    # Skjul BaseWeb sin radio-sirkel - tallet alene er kontrollen.
    """[data-testid="stRadio"] label > div:first-child {
        display: none !important;
    }""",
    # Markdown-wrapperen rundt tallet må selv sentreres, ellers blir
    # tallet venstrejustert i sin 36px-rute selv om labelen er flex-center.
    """[data-testid="stRadio"] label [data-testid="stMarkdownContainer"] {
        width: 100%;
        text-align: center;
    }""",
    """[data-testid="stRadio"] label [data-testid="stMarkdownContainer"] p {
        color: #3B4256;
        font-size: 13px;
        font-weight: 500;
        margin: 0 !important;
        line-height: 1;
        text-align: center;
    }""",
    """[data-testid="stRadio"] label:hover {
        background: #EAF1FB;
    }""",
    """[data-testid="stRadio"] label:hover [data-testid="stMarkdownContainer"] p {
        color: #0A2C72;
    }""",
    # Valgt segment: Marine-fyll, hvit tekst, subtil shadow.
    """[data-testid="stRadio"] label:has(input:checked) {
        background: #0A2C72;
        box-shadow: 0 1px 2px rgba(12, 26, 64, 0.18);
    }""",
    """[data-testid="stRadio"] label:has(input:checked) [data-testid="stMarkdownContainer"] p {
        color: #FFFFFF;
        font-weight: 600;
    }""",
]


def _render_skala_pille() -> None:
    """Kompakt inline pille som erstatter det tidligere skala-callout-banneret."""
    st.markdown(
        '<div style="display:inline-flex;align-items:center;'
        'background:#F2F5FA;'
        'border-left:2px solid #1F6FC4;'
        'border-radius:6px;padding:6px 12px;'
        'font-size:12px;color:#3B4256;margin:8px 0 24px;">'
        '<strong style="color:#16203A;font-weight:700;'
        'margin-right:8px;">Skala</strong>'
        '<span>· 1 = uenig · 5 = enig</span>'
        '<span style="color:#CBD3E0;margin:0 10px;">|</span>'
        '<span>Velg ett tall per påstand</span>'
        '</div>',
        unsafe_allow_html=True,
    )


def _render_question_cell(sid: int, statement: str) -> None:
    """Q-badge + spørsmålstekst i en linje (left cell)."""
    st.markdown(
        f'<div>'
        f'<span style="display:inline-block;'
        f'font-family:ui-monospace,\'JetBrains Mono\',monospace;'
        f'font-size:11px;color:#6B7280;'
        f'background:#EAF1FB;'
        f'padding:2px 7px;border-radius:4px;'
        f'margin-right:10px;vertical-align:middle;">Q{sid}</span>'
        f'<span style="font-size:14px;color:#16203A;'
        f'line-height:1.45;vertical-align:middle;">{statement}</span>'
        f'</div>',
        unsafe_allow_html=True,
    )


def _render_endpoint_labels() -> None:
    """uenig/enig-labels rett over Likert-baren - kun på første rad.

    Bredden (196px) = barens ytre bredde: 1px border + 3px padding +
    5×36px segmenter + 4×2px gap + 3px padding + 1px border. Padding 0 4px
    tilsvarer barens indre venstre/høyre-kant, så `uenig` flukter med
    segment 1 og `enig` med segment 5.

    Ingen `margin-left: auto` - labelen sitter til venstre i sin
    markdown-container, samme x-posisjon som baren under (som også sitter
    til venstre i sin element-container).
    """
    st.markdown(
        '<div style="display:flex;justify-content:space-between;'
        'font-size:10px;text-transform:uppercase;'
        'letter-spacing:0.05em;color:#6B7280;'
        'width:196px;margin:0 0 4px 0;padding:0 4px;'
        'box-sizing:border-box;">'
        '<span>uenig</span><span>enig</span></div>',
        unsafe_allow_html=True,
    )


def _render_likert_grid() -> dict[int, int | None]:
    """Render påstander som grid; returner deltakerens valg per ID."""
    answers: dict[int, int | None] = {}

    with stylable_container(key="bk_likert_grid", css_styles=_LIKERT_CSS):
        for i, (sid, statement) in enumerate(STATEMENTS.items()):
            col_text, col_likert = st.columns(COL_WIDTHS, vertical_alignment="center")
            with col_text:
                _render_question_cell(sid, statement)
            with col_likert:
                # uenig/enig kun øverst - gjentakelse på hver rad ble visuelt støy.
                if i == 0:
                    _render_endpoint_labels()
                answers[sid] = st.radio(
                    label=statement,
                    options=list(range(SCALE_MIN, SCALE_MAX + 1)),
                    horizontal=True,
                    index=None,
                    key=f"stmt_{sid}",
                    label_visibility="collapsed",
                )

    return answers


def main() -> None:
    crumb(["Oversikt", "Bli kjent"])
    module_header("Bli kjent", subtitle="Hvilke forkunnskaper har vi? Helt anonymt.")

    _render_skala_pille()

    if st.session_state.get("oppvarming_submitted"):
        callout(
            "Takk! Svarene er lagret. Du kan svare på nytt om du vil korrigere.",
            kind="tip",
            key="oppvarming_submitted_ok",
        )
        if st.button("Svar på nytt"):
            st.session_state["oppvarming_submitted"] = False
            for sid in STATEMENTS:
                st.session_state.pop(f"stmt_{sid}", None)
            st.rerun()
        st.divider()
        next_module_cta_for("pages/oppvarming_resultater.py")
        return

    with st.form("oppvarming_form"):
        answers = _render_likert_grid()
        st.divider()
        submitted = st.form_submit_button("Send inn alle svar", type="primary")

    if submitted:
        if any(v is None for v in answers.values()):
            callout(
                "Alle påstander må besvares før du kan sende inn. "
                "Sjekk at hver rad har et valg.",
                kind="warn",
                key="oppvarming_missing",
            )
            return
        try:
            values = {sid: int(val) for sid, val in answers.items()}
            insert_likert_responses(values)
            st.session_state["oppvarming_submitted"] = True
            st.toast(f"Takk! Alle {len(STATEMENTS)} svar lagret.")
            st.rerun()
        except Exception as exc:  # noqa: BLE001
            callout(
                f"Kunne ikke lagre svar: {exc}",
                kind="warn",
                key="oppvarming_error",
            )
