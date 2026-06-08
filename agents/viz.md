# viz.md — Visualiseringer og plott

**Lesing:** Før du lager, endrer, eller planlegger en visualisering (chart, diagram, wordcloud, osv.)

---

## Farger

Bruk fargekonstanter fra `modules/shared/ui.py`:

```python
from modules.shared.ui import COLOR_MARINE, COLOR_AZUR, COLOR_FERSKEN

# Bankbrief-palett:
# COLOR_MARINE = "#0A2C72" (primær)
# COLOR_AZUR = "#1F6FC4" (sekundær, lenker)
# COLOR_FERSKEN = "#F8E6D5" (signatur)
```

**IKKE hardkod farger.** Alt skal arve fra designsystemet via disse konstantene.

## Plotly

Mange moduler bruker Plotly (jf. `modules/gruppeoppgave_1/viz.py`):

```python
import plotly.graph_objects as go

fig = go.Figure()
fig.add_trace(go.Bar(
    x=..., y=...,
    marker=dict(color=COLOR_MARINE)
))
fig.update_layout(
    font=dict(family="Arial"),  # Bruk Arial, ikke standard
    paper_bgcolor="white",
    plot_bgcolor="white"
)
st.plotly_chart(fig, use_container_width=True)
```

## Streamlit-komponenter

- `st.bar_chart()`, `st.line_chart()` — enkel, rask, men mindre kontroll
- `plotly` — mer kontroll over farger og layout

Hvis du bruker Streamlit-natives: de arver ikke alltid designsystemets farger. **Foretrekk Plotly.**

## Wordclouds

Om du lager ordskyer: bruk `wordcloud`-biblioteket med Bankbrief-fargepaletten:

```python
from wordcloud import WordCloud
colormap = "viridis"  # eller lag custom basert på COLOR_MARINE/AZUR/FERSKEN
```

## Layout

- **Med på canvas:** Visualiseringer skal have god kontrast på hvit bakgrunn (Bankbrief er lyst tema)
- **Responsiv:** Bruk `use_container_width=True` på Streamlit-plots så de skalerer med siden
