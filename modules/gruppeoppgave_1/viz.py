"""Visualiseringer: ordsky for fritekst, barchart for valg/Likert.

Implementerer PRD §FR-3.4. Stil per DESIGN_GUIDE v2 §5:
- Plotly (ikke st.bar_chart)
- Heltallsticks på Y-akse, ingen decimaler
- Tomme kategorier vises som tick-merker, ikke som "0"-tall
- Snitt visualisert som stiplet vertikal linje (når mean er gitt)
- Diagrammet ligger i et kort (ikke flytende over canvas)
"""

from __future__ import annotations

import base64
from collections import Counter
from io import BytesIO

import plotly.graph_objects as go
import streamlit as st
from wordcloud import WordCloud

from modules.shared.ui import (
    BORDER,
    COLOR_FROST,
    COLOR_SURFACE_2,
    COLOR_SYRIN,
    COLOR_VANN,
    TEXT_PRIMARY,
    TEXT_TERTIARY,
    callout,
    card,
)


def render_wordcloud(tokens: list[str], title: str, max_words: int = 10) -> None:
    # PRD §FR-3.4 / §NFR-4.1: vent på minst 3 svar før reveal.
    st.subheader(title)
    if len(tokens) < 3:
        callout(
            "Venter på flere svar…",
            kind="subtle",
            key=f"wc_wait_{title}",
        )
        return

    # PRD §FR-3.4: kun de N hyppigste ordene (default 10).
    top = Counter(tokens).most_common(max_words)
    freq = dict(top)

    wc = WordCloud(
        # PRD §FR-3.4: 16:9 slide-format
        width=1600,
        height=900,
        background_color="white",
        collocations=False,
        prefer_horizontal=0.9,
        margin=10,
        max_font_size=300,
        min_font_size=40,
        relative_scaling=0.6,
        max_words=max_words,
    ).generate_from_frequencies(freq)

    with card(key=f"wc_card_{title}"):
        # PRD §FR-3.4: render rasteret i full kort-bredde, lesbart i plenum.
        # Både st.pyplot og st.image(width="stretch") kollapset bildet til en
        # miniklump inne i kortet (stylable_container) og krevde fullskjerm-
        # klikk for å vises. Vi embedder derfor 1600×900-PNG-en direkte som en
        # <img> med width:100% - fyller bredden uten fullskjerm-avhengighet.
        buf = BytesIO()
        wc.to_image().save(buf, format="PNG")
        b64 = base64.b64encode(buf.getvalue()).decode("ascii")
        st.markdown(
            f'<img src="data:image/png;base64,{b64}" '
            'style="width:100%;height:auto;display:block;border-radius:6px;" '
            f'alt="Ordsky: {title}" />',
            unsafe_allow_html=True,
        )
        ranked = ", ".join(f"{w} ({c})" for w, c in top)
        st.caption(f"Topp {len(top)}: {ranked}")


def render_barchart(
    counts: dict[str, int],
    title: str,
    min_responses: int = 3,
    *,
    mean: float | None = None,
    likert: bool = False,
) -> None:
    """Render barchart i Plotly per DESIGN_GUIDE v2 §5.

    Args:
        counts: ordnet dict {label: count}. For Likert: nøkler "1".."5".
        title: vises som st.subheader over diagrammet.
        min_responses: skjul diagrammet til så mange svar er inne (FR-3.4).
        mean: hvis gitt, tegnes som stiplet vertikal Frost/Syrin-linje.
        likert: hvis True, x-akse får "uenig"/"enig"-undertekster på 1 og 5.
    """
    # PRD §FR-3.4 / §NFR-4.1: default-terskel er 3 (privacy-by-timing).
    st.subheader(title)
    total = sum(counts.values())
    if total < min_responses:
        callout(
            "Venter på flere svar…",
            kind="subtle",
            key=f"bc_wait_{title}",
        )
        return

    labels = list(counts.keys())
    values = list(counts.values())
    max_y = max(values) if values else 1

    # Tekstlabels: skjul "0" så tomme kategorier ikke skaper visuell støy.
    text_labels = [str(v) if v > 0 else "" for v in values]

    fig = go.Figure()
    fig.add_trace(
        go.Bar(
            x=labels,
            y=values,
            marker=dict(color=COLOR_VANN, line=dict(width=0)),
            text=text_labels,
            textposition="outside",
            textfont=dict(size=13, color=TEXT_PRIMARY),
            hovertemplate="%{x}: %{y}<extra></extra>",
            cliponaxis=False,
        )
    )

    # Y-akse: kun heltall, ingen decimaler.
    fig.update_yaxes(
        dtick=1,
        range=[0, max_y + 0.7],
        showgrid=True,
        gridcolor="rgba(126, 181, 210, 0.10)",
        zeroline=False,
        title_text="",
        tickfont=dict(color=TEXT_TERTIARY, size=11),
    )

    # X-akse: Likert får "uenig"/"enig"-ankere på 1 og 5.
    if likert and set(labels) >= {"1", "5"}:
        ticktext = []
        for label in labels:
            if label == "1":
                ticktext.append(
                    f"1<br><span style='font-size:10px;color:{TEXT_TERTIARY}'>uenig</span>"
                )
            elif label == "5":
                ticktext.append(
                    f"5<br><span style='font-size:10px;color:{TEXT_TERTIARY}'>enig</span>"
                )
            elif label == "3":
                ticktext.append(
                    f"3<br><span style='font-size:10px;color:{TEXT_TERTIARY}'>nøytral</span>"
                )
            else:
                ticktext.append(label)
        fig.update_xaxes(
            tickmode="array",
            tickvals=labels,
            ticktext=ticktext,
            showgrid=False,
            tickfont=dict(color=TEXT_PRIMARY, size=13),
        )
    else:
        fig.update_xaxes(
            showgrid=False,
            tickfont=dict(color=TEXT_PRIMARY, size=13),
        )

    # Snitt-linje (kun meningsfullt når kategoriene er numeriske).
    if mean is not None and likert:
        fig.add_vline(
            x=mean,
            line=dict(color=COLOR_SYRIN, width=1, dash="dash"),
            annotation_text=f"snitt {mean:.1f}",
            annotation_position="top",
            annotation_font=dict(color=COLOR_SYRIN, size=11),
        )

    fig.update_layout(
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        font=dict(family="Arial, Helvetica, sans-serif", color=TEXT_PRIMARY),
        margin=dict(l=20, r=20, t=30, b=20),
        height=280,
        showlegend=False,
        bargap=0.45,
    )

    with card(key=f"bc_card_{title}"):
        st.plotly_chart(
            fig, use_container_width=True, key=f"barchart_{title}"
        )
        st.caption(f"Totalt {total} svar")
