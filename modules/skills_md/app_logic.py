"""Skills i Cortex Code – modul 15.

Implementerer PRD §FR-3.11 (presentasjons-modul) og §FR-3.12 (innhold i
markdown-filer under `content/`). Innføring i Cortex Codes skill-mekanisme:
hva en skill er, anatomien (SKILL.md), bundled vs. custom, plassering og
presedens, når man bør lage en custom skill, og beste praksis.

Layout per DESIGN_GUIDE v2 §8. Nummererte steg/sjekklister bruker
`numbered_steps`-helperen (DESIGN_GUIDE v2 §4) for "1, 2, 3"-badge-bokser.

Eksponerer `main()` som kalles fra `pages/skills_md.py`.
"""

from __future__ import annotations

import streamlit as st

from modules.shared.ui import (
    TEXT_PRIMARY,
    TEXT_SECONDARY,
    callout,
    card,
    crumb,
    load_markdown,
    load_split_markdown,
    load_titled_markdown,
    next_module_cta_for,
    numbered_steps,
)


def main() -> None:
    crumb(["Kursmoduler", "16 · skills.md"])

    title, intro_body = load_titled_markdown(__file__, "intro")
    st.title(title or "🛠️ Skills i Cortex Code")
    st.caption(
        "Modul 16 · Gjenbrukbare arbeidsflyter som forteller Cortex Code "
        "hvordan en Snowflake-oppgave skal håndteres"
    )
    st.divider()

    # --- Seksjon 1: Hva er en skill? + de fire delene ---
    st.subheader("📍 Hva er en skill?")
    st.markdown(intro_body)
    st.caption("En skill leverer fire ting:")
    _anatomy_grid(load_split_markdown(__file__, "anatomi_deler"))

    st.divider()

    # --- Seksjon 2: Anatomien — SKILL.md ---
    st.subheader("🧩 Anatomien: SKILL.md")
    with card(key="skills_skillmd"):
        st.markdown(load_markdown(__file__, "skill_md"))

    st.divider()

    # --- Seksjon 3: Bundled vs. custom skills (to kolonner) ---
    st.subheader("⚖️ Bundled vs. custom skills")
    typer = load_split_markdown(__file__, "typer")
    titles = [t for t in typer if t]  # dropp evt. pre-header-blokk
    col_bundled, col_custom = st.columns(2, gap="medium")
    for col, t in zip((col_bundled, col_custom), titles):
        with col, card(key=f"skills_type_{t[:8]}"):
            st.markdown(f"**{t}**")
            st.markdown(typer[t])

    st.divider()

    # --- Seksjon 4: Hvor bor skills? + presedens ---
    st.subheader("📂 Hvor bor skills?")
    st.markdown(load_markdown(__file__, "hvor"))
    callout(
        load_markdown(__file__, "precedence"),
        kind="info",
        title="🥇 Presedens",
        key="skills_precedence",
    )

    st.divider()

    # --- Seksjon 5: Når bør du lage en custom skill? ---
    st.subheader("🧭 Når bør du lage en custom skill?")
    st.markdown(load_markdown(__file__, "naar"))
    steg = [t for t in load_split_markdown(__file__, "naar_steg") if t]
    numbered_steps(steg, key="skills_naar_steg")

    st.divider()

    # --- Seksjon 6: Forstå en skill før du bruker den ---
    st.subheader("🔍 Forstå en skill før du bruker den")
    st.markdown(load_markdown(__file__, "forstaa"))
    st.caption("Eksempel-prompt")
    st.code(load_markdown(__file__, "forstaa_prompt"), language="text")
    callout(
        load_markdown(__file__, "tips_plan"),
        kind="success",
        title="💡 Tips: kombiner med Plan Mode",
        key="skills_tips_plan",
    )

    st.divider()

    # --- Seksjon 7: Lage en ny skill ---
    st.subheader("🏗️ Lage en ny skill")
    st.markdown(load_markdown(__file__, "lage"))
    st.caption("Eksempel-prompt")
    st.code(load_markdown(__file__, "lage_prompt"), language="text")

    st.divider()

    # --- Seksjon 8: Beste praksis (nummererte sjekkpunkter) ---
    st.subheader("✅ Beste praksis for pålitelige custom skills")
    st.caption("Hold en custom skill smal og forutsigbar:")
    praksis = load_split_markdown(__file__, "beste_praksis")
    numbered_steps(
        [(t, praksis[t]) for t in praksis if t],
        key="skills_beste_praksis",
    )

    st.divider()

    # skills.md → Gruppeoppgave 2 (lag en datakvalitets-skill) er den
    # naturlige neste øvelsen i modul-rekkefølgen.
    next_module_cta_for("gruppeoppgave_2")


def _anatomy_grid(deler: dict[str, str]) -> None:
    """Render de fire delene en skill leverer som fire små kort i én rad.

    `deler` er `{tittel: body}` fra `load_split_markdown` der tittelen
    inkluderer ledende emoji (f.eks. "🧭 Domenekontekst").
    """
    items = [(t, body) for t, body in deler.items() if t]
    if not items:
        return
    cols = st.columns(len(items), gap="small")
    for col, (tittel, body) in zip(cols, items):
        with col, card(key=f"skills_anatomy_{tittel[:8]}", padding="18px 16px"):
            st.markdown(
                f"<div style='font-size:15px;font-weight:700;"
                f"color:{TEXT_PRIMARY};line-height:1.35;'>{tittel}</div>"
                f"<div style='font-size:13px;color:{TEXT_SECONDARY};"
                f"margin-top:6px;line-height:1.5;'>{body}</div>",
                unsafe_allow_html=True,
            )
