"""Kostnader – modul 25.

Implementerer PRD §FR-3.11 (presentasjons-modul) og §FR-3.12 (innhold i
markdown-filer under `content/`). Operasjonell forberedelse før Avslutning:
kostnadsmodell, drivere, intern sporing (tabell + dashboard), resource
monitors og best practices.

Layout per DESIGN_GUIDE v2 §8: crumb, H1+intro, expanders for konsepter,
en praktisk seksjon med SQL-eksempel og dashboard-lenke, info-callout for
resource monitors, best-practices-expander, CTA til Avslutning.

Eksponerer `main()` som kalles fra `pages_content/modules/m25_kostnader.py`.
"""

from __future__ import annotations

import streamlit as st

from modules.shared.ui import (
    callout,
    card,
    crumb,
    load_markdown,
    load_titled_markdown,
    next_module_cta_for,
)


# Andre fyller inn faktisk URL til intern Streamlit-dashboard senere.
KOSTNADS_DASHBOARD_URL = "https://placeholder.intern.bank/cortex-code-kostnader"


def main() -> None:
    crumb(["Kursmoduler", "25 · Kostnader"])

    title, intro_body = load_titled_markdown(__file__, "intro")
    st.title(title or "💰 Kostnader")
    st.caption("Modul 25 · Kostnadsmodell, sporing og produksjonskontroller")
    st.divider()
    st.markdown(intro_body)

    st.divider()

    # --- Kostnadsmodell ---
    with st.expander("📐 Kostnadsmodellen"):
        st.markdown(load_markdown(__file__, "kostnadsmodell"))

    # --- Drivere ---
    with st.expander("⚡ Hva driver kostnaden?"):
        st.markdown(load_markdown(__file__, "kostnadsdrivere"))

    st.divider()

    # --- Praktisk: slik sporer vi forbruk ---
    st.subheader("🔎 Slik sporer vi forbruk")
    st.markdown(load_markdown(__file__, "spore_forbruk"))

    with card(key="kostnader_sql"):
        st.markdown("**Eksempel-spørring** _(Andre fyller inn faktisk tabellnavn og kolonner)_")
        st.code(
            """-- Andre fyller inn faktisk tabellnavn og kolonner
select user_name, model, sum(credits_used) as credits
from <kostnadstabell>
where created_at >= dateadd(day, -7, current_timestamp())
group by 1, 2
order by credits desc;""",
            language="sql",
        )

    st.link_button(
        "📊 Åpne kostnads-dashboard",
        url=KOSTNADS_DASHBOARD_URL,
        help="Internt Streamlit-dashboard som viser nåværende forbruk per bruker/modell.",
    )

    st.divider()

    # --- Resource monitors som info-callout ---
    callout(
        load_markdown(__file__, "resource_monitors"),
        kind="info",
        title="🛡️ Resource monitors",
        key="kostnader_resource_monitors",
    )

    # --- Best practices ---
    with st.expander("✅ Best practices for kostnadskontroll"):
        st.markdown(load_markdown(__file__, "best_practices"))

    st.divider()
    next_module_cta_for("avslutning")
