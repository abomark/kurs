"""Plan Mode i Cortex Code – modul 7.

Implementerer PRD §FR-3.11 (presentasjons-modul) og §FR-3.12 (innhold i
markdown-filer under `content/`). Innføring i Cortex Codes kjøremoduser med
vekt på Plan Mode: read-only-modusen som tenker gjennom en kompleks oppgave
og legger fram en strukturert flertrinnsplan til godkjenning før noe utføres.

Layout per DESIGN_GUIDE v2 §8. Livssyklusen bruker `numbered_steps`-helperen
(DESIGN_GUIDE v2 §4) for "1, 2, 3"-badge-bokser.

Eksponerer `main()` som kalles fra
`pages_content/modules/m07_plan_mode.py`.
"""

from __future__ import annotations

import streamlit as st

from modules.shared.ui import (
    COLOR_FROST,
    COLOR_SYRIN,
    COLOR_VANN,
    TEXT_PRIMARY,
    TEXT_SECONDARY,
    TEXT_TERTIARY,
    callout,
    card,
    crumb,
    load_markdown,
    load_split_markdown,
    next_module_cta_for,
    numbered_steps,
)


def main() -> None:
    crumb(["Kursmoduler", "07 · Plan Mode"])
    st.title("📋 Plan Mode")
    st.caption(
        "Modul 7 · Kjøremodusen som holder seg read-only mens den tenker, "
        "og leverer en plan til godkjenning før noe utføres"
    )
    st.divider()

    # --- Seksjon 1: Hva er Plan Mode? ---
    callout(
        load_markdown(__file__, "intro"),
        kind="info",
        title="📍 Hva er Plan Mode?",
        key="plan_intro",
    )

    st.divider()

    # --- Seksjon 2: De tre kjøremodusene ---
    st.subheader("🎚️ De tre kjøremodusene")
    st.markdown(
        "Modusene spenner fra mest kontroll og bekreftelse til mest "
        "automatikk. Plan Mode ligger i midten — den tenker fritt, men "
        "handler ikke uten godkjenning."
    )
    _spectrum_label()
    _mode_cards(load_split_markdown(__file__, "moduser"))

    st.divider()

    # --- Seksjon 3: Slik aktiverer du ---
    st.subheader("⌨️ Slik aktiverer du Plan Mode")
    _two_cards(load_split_markdown(__file__, "aktiver"), key="plan_aktiver")

    st.divider()

    # --- Seksjon 4: Slik fungerer Plan Mode ---
    st.subheader("🔄 Slik fungerer Plan Mode")
    st.markdown(load_markdown(__file__, "flyt"))
    steg = [t for t in load_split_markdown(__file__, "flyt_steg") if t]
    numbered_steps(steg, key="plan_flyt_steg")

    st.divider()

    # --- Seksjon 5: Når bør du bruke den? ---
    st.subheader("🧭 Når bør du bruke Plan Mode?")
    _two_cards(load_split_markdown(__file__, "naar"), key="plan_naar")
    callout(
        load_markdown(__file__, "kobling"),
        kind="success",
        title="🔗 Kobling til skills",
        key="plan_kobling",
    )

    st.divider()

    # Plan Mode → arkitektur (resten av "Komme i gang"-flyten).
    next_module_cta_for("arkitektur")


def _spectrum_label() -> None:
    """Liten akse-etikett: mest kontroll til venstre, mest automatikk til høyre."""
    st.markdown(
        f"<div style='display:flex;justify-content:space-between;"
        f"font-size:12px;font-weight:600;letter-spacing:0.06em;"
        f"text-transform:uppercase;color:{TEXT_TERTIARY};"
        f"margin:6px 2px 10px;'>"
        f"<span>← Mest kontroll</span><span>Mest automatikk →</span></div>",
        unsafe_allow_html=True,
    )


def _mode_cards(moduser: dict[str, str]) -> None:
    """Render de tre kjøremodusene som tre kort. Plan Mode-kortet framheves.

    `moduser` er `{tittel: body}` fra `load_split_markdown`. Tittelen som
    inneholder "Plan Mode" får Vann-aksent + "Denne modulen"-merke; de andre
    får en dempet topp-stripe.
    """
    items = [(t, body) for t, body in moduser.items() if t]
    if not items:
        return
    # Topp-stripe-farge per modus, i samme rekkefølge som content-fila.
    stripes = [COLOR_FROST, COLOR_VANN, COLOR_SYRIN]
    cols = st.columns(len(items), gap="medium")
    for i, (col, (tittel, body)) in enumerate(zip(cols, items)):
        focus = "Plan Mode" in tittel
        stripe = stripes[i] if i < len(stripes) else COLOR_FROST
        title_color = COLOR_VANN if focus else TEXT_PRIMARY
        badge = (
            f"<span style='font-size:10px;font-weight:700;letter-spacing:0.08em;"
            f"text-transform:uppercase;color:#FFFFFF;background:{COLOR_VANN};"
            f"padding:3px 9px;border-radius:99px;margin-left:8px;'>"
            f"Denne modulen</span>"
            if focus
            else ""
        )
        with col, card(key=f"plan_mode_{i}", padding="0 20px 18px"):
            st.markdown(
                f"<div style='height:5px;border-radius:0 0 99px 99px;"
                f"background:{stripe};margin:0 -20px 14px;'></div>"
                f"<div style='font-size:17px;font-weight:700;"
                f"color:{title_color};line-height:1.3;'>{tittel}{badge}</div>",
                unsafe_allow_html=True,
            )
            st.markdown(body)


def _two_cards(sections: dict[str, str], *, key: str) -> None:
    """Render to markdown-seksjoner side-ved-side som kort (tittel + body)."""
    items = [(t, body) for t, body in sections.items() if t]
    if not items:
        return
    cols = st.columns(len(items), gap="medium")
    for i, (col, (tittel, body)) in enumerate(zip(cols, items)):
        with col, card(key=f"{key}_{i}"):
            st.markdown(
                f"<div style='font-size:15px;font-weight:700;"
                f"color:{COLOR_VANN};margin-bottom:8px;'>{tittel}</div>",
                unsafe_allow_html=True,
            )
            st.markdown(body)
