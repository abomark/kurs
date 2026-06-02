"""Test: forhåndsvisning av frittstående HTML-utforming «Skills i Cortex Code».

Midlertidig testside (modul 36) som Andre la inn for å se hvordan en
selvstendig HTML-side ser ut i appen. HTML-en rendres ISOLERT i en iframe
via `st.components.v1.html`, slik at dens egne globale CSS-regler (`*{}`-reset,
`body`, `:root`-variabler) holdes inne i sandboxen og ikke lekker ut i resten
av Streamlit-appen.

Innholdet ligger i `content/page.html` (FR-3.12: prosa/innhold utenfor
app_logic). Eksponeres som `main()` via
`pages_content/modules/m36_test_skills_html.py`.
"""

from __future__ import annotations

from pathlib import Path

import streamlit.components.v1 as components


def _load_html() -> str:
    path = Path(__file__).parent / "content" / "page.html"
    if not path.exists():
        return "<p>Mangler content/page.html</p>"
    return path.read_text(encoding="utf-8")


def main() -> None:
    # Isolert iframe: HTML-ens globale CSS påvirker ikke resten av appen.
    # Fast høyde + scrolling=True siden components.html ikke auto-sizer;
    # 3600px rommer hele siden, inner-scroll fanger evt. overskudd.
    components.html(_load_html(), height=3600, scrolling=True)
