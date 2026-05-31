# DESIGN GUIDE v2 — Cortex Code Kursplattform

> **Til AI-agenten som leser denne fila:** Dette er den eneste sannheten for visuell stil. Versjon 2 prioriterer *visuelt hierarki* og *container-struktur* over ren brand-disiplin. Når du må velge mellom "merkevarekonsistens" og "ser profesjonelt ut", velg sistnevnte. Konkret betyr det: bruk ikke Fjell som heldekkende bakgrunn, pakk alt i kort, og gi tall sin egen plass.

---

## 0. Hva som endret seg fra v1

v1 var en brand-disiplinguide. v2 er en *produkt*-design guide. Forskjellen:

| Aspekt | v1 (feil) | v2 (riktig) |
|---|---|---|
| Sidebakgrunn | Fjell `#002776` heldekkende | Nær-svart `#0A0F1F` |
| Brand-bruk | Mest dominant farge | Aksent og container |
| Komponenter | Custom HTML inline | Kort med tydelig struktur |
| Tall i diagrammer | Y-akse 0–1 med decimalticks | Heltallsticks, snitt visualisert |
| Tomme kategorier | "0" tall som visuell støy | Diskrete tick-merker |
| Font | Arial obligatorisk | Arial obligatorisk (ingen webfonter) |
| Sidebar | Flat liste med emojis | Seksjonert med headers + venstrekant-aktiv |

---

## 1. Kjerneprinsipper (i denne rekkefølgen)

1. **Hierarki først.** Det viktigste tallet skal ha størst skriftstørrelse. Det viktigste innholdet skal være øverst.
2. **Containere gir struktur.** Alt vises inni et kort med padding og border. Aldri fritt-flytende.
3. **Brand støtter, dominerer ikke.** Vann og Fjell er aksenter — ikke lerret.
4. **Tilbakeholdenhet i farge.** En side skal ha ett dominerende farget element, ikke fem.
5. **Tall fortjener sin egen plass.** Antall svar, snitt, prosent — disse er kongene, ikke fotnoter.
6. **Norsk språk, men engelske tekniske termer.**
7. **Ingen emojis eller ikoner.** Overskrifter (H1/H2/H3), `st.subheader`, `st.expander`-labels, callout-titler, crumbs og brødtekst skal være ren tekst — ingen 📌🎯⚠️-dekorasjon. Eneste tillatte unntak er den kvadratiske callout-badgen (`i` / `!` / `✓` / `·`, se §7) og typografiske piler (`→`, `←`) der de bærer mening i prosa. Hvorfor: emojier renders inkonsistent på tvers av OS-er (Apple vs Windows vs Linux) og trekker tonen i en uønsket retning for et bank-publikum.

---

## 2. Fargesystem — REVIDERT

### Canvas og overflater (NY hierarki)

```
--canvas:      #0A0F1F   /* Sidens bakgrunn - nær-svart, ikke Fjell */
--surface-1:   #0F1729   /* Kort, sidebar - ett trinn lysere enn canvas */
--surface-2:   #131C33   /* Nestede elementer (chart-stats inni kort) */
--surface-3:   #1A2542   /* Code-block headers, tooltip-bakgrunner */
```

**Hvorfor:** Profesjonelle dark mode-design (Linear, Vercel, Datadog) bruker nær-svart canvas og elevation-trinn med subtile lysere overflater. Fjell `#002776` som hele lerretet ble for tungt og fikk produktet til å se utdatert ut.

### Brand-farger (samme paletten, ny bruk)

| Navn | HEX | Bruk |
|---|---|---|
| **Vann** | `#005AA4` | Primær aksent: knapper, lenker, venstre-kant på aktiv sidebar-item, info-callouts |
| **Fjell** | `#002776` | Subtil gradient i logo/header, *aldri* heldekkende bakgrunn |
| **Frost** | `#7EB5D2` | Suksess-callouts, sekundære lenker, snitt-linje i diagrammer, frostige aksenter |
| **Sand** | `#F8E9DD` | *Tekst* primært (på mørk bakgrunn), kode-tekst |
| **Syrin** | `#D3D3EA` | Advarsel-callouts, sekundærtekst-aksent |

### Tekst-hierarki (NY — manglet i v1)

```
--text-primary:    #F4F6FB   /* Hovedtekst */
--text-secondary:  #A8B3C7   /* Brødtekst, beskrivelser */
--text-tertiary:   #6B7691   /* Captions, metadata, akse-labels */
```

Bruk *aldri* Sand `#F8E9DD` som hovedtekstfarge. Sand er for varmt — gir et nostalgisk preg som motvirker det profesjonelle uttrykket. Bruk det for kode (på Fjell-bakgrunn) der det fungerer.

### Borders og dividers

```
--border:         rgba(126, 181, 210, 0.10)   /* Standard kort-border */
--border-strong:  rgba(126, 181, 210, 0.20)   /* Mer synlig avgrensning */
--divider:        rgba(255, 255, 255, 0.06)   /* Subtle horisontale linjer */
```

### Forbudt

- Heldekkende Fjell `#002776` som canvas
- Rødt, grønt, oransje, gult, lilla, rosa
- Gradienter mellom forskjellige hue-er (purple→pink, blue→green osv.)
- Sand som hovedtekstfarge

---

## 3. Typografi — REVIDERT

### Primær: Arial

```css
font-family: Arial, Helvetica, sans-serif;
```

**Hvorfor:** Arial er obligatorisk i kurset. Den er forhåndsinstallert overalt (ingen webfont-lasting, ingen avhengighet av Google Fonts), renders konsistent på tvers av OS-er, og samsvarer med bankenes skrifttype-policy. Ingen eksterne fonter (ikke Inter, ikke Roboto).

For å unngå et "tungt/90-talls" inntrykk med Arial:

- Bruk negativ `letter-spacing` på headings (`-0.01em` til `-0.02em`)
- Hold headings på vekt 700 (ikke gå tyngre uten grunn)
- Bruk `font-feature-settings: "tnum"` / `font-variant-numeric: tabular-nums` på alle tall

### Skala (uendret fra v1)

| Rolle | Størrelse | Vekt |
|---|---|---|
| H1 (sidetittel) | 32px | 700 |
| H2 (seksjon) | 24px | 700 |
| H3 (underseksjon) | 18px | 600 |
| Brødtekst | 16px | 400 |
| Liten / metadata | 13px | 400 |
| Mono / kode | 14px | 400 (JetBrains Mono) |

### Regler

- Aldri mer enn ett H1 per side
- Negativ `letter-spacing` på alle headings (`-0.01em` til `-0.02em`)
- Tabular numbers på alle tall i tabeller og metrikker (`font-variant-numeric: tabular-nums`)

---

## 4. Container-system (NY i v2)

**Alt** skal være inni en container. Ingen fritt-flytende komponenter på canvas.

### Kort (default container)

```css
.card {
    background: var(--surface-1);
    border: 1px solid var(--border);
    border-radius: 10px;
    padding: 24px;
}
```

### Metric-kort (for viktige tall)

Brukes for sammendrag øverst på resultat-sider, dashboard-overskrifter, KPI-er:

```html
<div class="metric">
  <div class="metric-label">TOTALT ANTALL SVAR</div>
  <div class="metric-value">2</div>
  <div class="metric-trend">av 12 påmeldte</div>
</div>
```

Spesifikasjoner:
- Label: 12px, uppercase, letter-spacing 0.05em, tertiær tekstfarge
- Verdi: 32px, font-weight 700, tabular-nums
- Trend/sub: 13px, frost-farget

### Layout-regel

```
[Sammendrag-rad med 3 metric-kort]
[Hovedinnhold-kort]
[Sekundærinnhold-kort]
```

Aldri:
```
[H1]
[Stor graf flytende på canvas]
[Tall som tekstlinjer under]
```

---

## 5. Diagrammer (NY dedikert seksjon)

Diagrammer avslører manglende håndverk umiddelbart. Følg disse reglene.

### Bibliotek

Bruk **Plotly** i Streamlit, ikke `st.bar_chart`. Plotly gir kontroll over alle aksene.

### Standard bar chart-konfigurasjon

```python
import plotly.graph_objects as go

fig = go.Figure()
fig.add_trace(go.Bar(
    x=[1, 2, 3, 4, 5],
    y=counts,
    marker=dict(
        color="#005AA4",
        line=dict(width=0),
    ),
    text=[str(c) if c > 0 else "" for c in counts],  # Skjul "0"-labels
    textposition="outside",
    textfont=dict(size=13, color="#F4F6FB"),
))

# Y-akse: heltall, ikke decimaler
max_y = max(counts)
fig.update_yaxes(
    dtick=1,
    range=[0, max_y + 0.5],
    showgrid=True,
    gridcolor="rgba(126, 181, 210, 0.1)",
    zeroline=False,
    title_text="",
)

# X-akse: kategorinavn, ikke tall
fig.update_xaxes(
    tickmode="array",
    tickvals=[1, 2, 3, 4, 5],
    ticktext=["1<br><span style='font-size:10px;color:#6B7691'>uenig</span>",
              "2", "3", "4",
              "5<br><span style='font-size:10px;color:#6B7691'>enig</span>"],
    showgrid=False,
)

# Snitt som vertikal linje
fig.add_vline(
    x=mean_value,
    line=dict(color="#D3D3EA", width=1, dash="dash"),
    annotation_text=f"snitt {mean_value:.1f}",
    annotation_position="top",
    annotation_font=dict(color="#D3D3EA", size=11),
)

# Layout
fig.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    paper_bgcolor="rgba(0,0,0,0)",
    font=dict(family="Arial, Helvetica, sans-serif", color="#F4F6FB"),
    margin=dict(l=40, r=20, t=40, b=40),
    height=280,
    showlegend=False,
)

st.plotly_chart(fig, use_container_width=True)
```

### Diagram-regler

- ❌ Aldri Y-akse med decimaltick når data er heltall
- ❌ Aldri vis "0"-labels for tomme kategorier — bruk diskrete tick-merker
- ❌ Aldri grafer over sidens bakgrunn — alltid inni et kort
- ✅ Snitt skal visualiseres som linje, ikke bare som tekst under
- ✅ Tomme kategorier skal være synlige (så hierarkiet 1-5 er klart), men ikke dominere
- ✅ Tall-labels på toppen av søyler, ikke under

---

## 6. Sidebar-struktur (NY dedikert seksjon)

### Anatomi

```
[Brand-blokk: logo + produktnavn]
─────────────────────────
[Seksjons-header: OVERSIKT]
  - Forside
  - Oppvarming
  - Resultater
─────────────────────────
[Seksjons-header: KURSMODULER]
  - 01 · Cortex Code
  - 02 · Snowsight vs CLI
  - ...
─────────────────────────
[Footer-element: Administrasjon]
```

### Seksjons-headers

```css
.sidebar-section-title {
    font-size: 11px;
    font-weight: 600;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    color: var(--text-tertiary);
    padding: 0 20px 8px;
}
```

### Item-tilstander

**Default:**
```css
padding: 8px 20px;
color: var(--text-secondary);
border-left: 3px solid transparent;
```

**Hover:** bakgrunn `var(--vann-soft)`, tekstfarge blir primær

**Active:** bakgrunn `var(--vann-soft)`, **venstre-kant `var(--vann)`**, tekst er bold

### Modul-nummerering

Bruk to-sifrede tall i mono-font, ikke emojis:

```html
<span class="sidebar-item-num">05</span><span>AGENTS.md</span>
```

Hvorfor: emojier renders inkonsistent på tvers av OS-er (Apple vs Windows vs Linux). To-sifrede tall i mono ser stramt og profesjonelt ut.

### Streamlit-implementering

```python
# Bruk st.navigation() med ikoner, ikke radio
pages = {
    "Oversikt": [
        st.Page("pages/00_forside.py", title="Forside"),
        st.Page("pages/01_oppvarming.py", title="Oppvarming"),
        st.Page("pages/02_resultater.py", title="Resultater"),
    ],
    "Kursmoduler": [
        st.Page("pages/m01_cortex_code.py", title="01 · Cortex Code"),
        st.Page("pages/m02_snowsight_vs_cli.py", title="02 · Snowsight vs CLI"),
        # ...
    ],
}
pg = st.navigation(pages)
pg.run()
```

`st.navigation()` med dict-input gir seksjons-headers gratis.

---

## 7. Callout-mønstre (forbedret)

### Tre typer, klar semantikk

| Type | Bakgrunn | Venstrekant | Ikon-bg | Bruk |
|---|---|---|---|---|
| **Info** | `rgba(0,90,164,0.12)` | Vann | Vann | Definisjoner, fakta, nøkkelpunkter |
| **Advarsel** | `rgba(211,211,234,0.12)` | Syrin | Syrin | Risiko, fallgruver, "uten dette skjer X" |
| **Suksess** | `rgba(126,181,210,0.15)` | Frost | Frost | Beste praksis, anbefalt mønster |

### Ikon: kvadratisk, ikke emoji

```html
<div class="callout callout-info">
  <div class="callout-icon">i</div>
  <div class="callout-body">
    <div class="callout-title">Tittel her</div>
    <div class="callout-content">Innhold her.</div>
  </div>
</div>
```

Ikon-spec: 28×28px kvadrat, border-radius 6px, brand-farge bakgrunn, hvit eller Fjell-farget tekst.

**Dette er det eneste tillatte "ikonet" i appen** (jf. §1.7). Bokstav-/tegn-badgen (`i` / `!` / `✓` / `·`) settes av `callout()`-helperen selv ut fra `kind` — `title`-argumentet skal være ren tekst uten emoji.

### Streamlit-implementasjon

Lag en `components.py` med helpers:

```python
from streamlit_extras.stylable_container import stylable_container
import streamlit as st

def callout(kind: str, title: str, content: str):
    """kind: 'info' | 'warn' | 'success'"""
    config = {
        "info":    ("#005AA4", "rgba(0,90,164,0.12)",   "i"),
        "warn":    ("#D3D3EA", "rgba(211,211,234,0.12)", "!"),
        "success": ("#7EB5D2", "rgba(126,181,210,0.15)", "✓"),
    }
    color, bg, icon = config[kind]
    with stylable_container(
        key=f"callout_{kind}_{hash(title)}",
        css_styles=f"""
            {{
                background: {bg};
                border-left: 3px solid {color};
                border-radius: 10px;
                padding: 20px 24px;
            }}
        """,
    ):
        st.markdown(f"**{icon}  {title}**")
        st.markdown(content)
```

Bruk:
```python
callout("info", "Hva er AGENTS.md?", "1. Plasseres i prosjektrot...")
```

---

## 8. Modul-sidens struktur

```
1. Crumb (navigasjonskontekst)
2. H1 (modul-tittel)
3. Subtittel (metadata: nr, lesetid, vanskelighetsgrad)
4. Kort introsetning (1-3 setninger prosa)
5. Innholdsseksjoner (callouts, code, ev. video)
6. CTA-kort "Til neste modul"
```

### CTA-kort til neste (erstatter "---" + tekstlinje)

```html
<div class="next-cta">
  <div>
    <div class="next-label">NESTE MODUL</div>
    <div class="next-title">06 · skills.md</div>
    <div class="next-desc">Hvordan kodifisere konkrete arbeidsflyter for agenten.</div>
  </div>
  <button class="next-button">Fortsett →</button>
</div>
```

---

## 9. Streamlit-spesifikt — REVIDERT

### `.streamlit/config.toml`

```toml
[theme]
base = "dark"
primaryColor = "#005AA4"
backgroundColor = "#0A0F1F"            # ← NY: nær-svart, ikke Fjell
secondaryBackgroundColor = "#0F1729"   # ← NY: surface-1
textColor = "#F4F6FB"                  # ← NY: text-primary, ikke Sand
linkColor = "#7EB5D2"
codeBackgroundColor = "#131C33"
font = "Arial, Helvetica, sans-serif"
baseFontSize = 16
baseRadius = "10px"
borderColor = "rgba(126, 181, 210, 0.10)"

[theme.sidebar]
backgroundColor = "#0F1729"
secondaryBackgroundColor = "#131C33"
textColor = "#A8B3C7"
```

### Påkrevde biblioteker

```
streamlit>=1.36
streamlit-extras>=0.4
plotly>=5.18
```

### Bruk

- ✅ `streamlit-extras.stylable_container` for alle callouts og kort
- ✅ Plotly for alle diagrammer
- ✅ `st.navigation()` med dict for sidebar
- ✅ `st.columns()` for metric-rader

### Unngå

- ❌ `st.info/warning/success/error` — bruk custom callouts
- ❌ `st.bar_chart/line_chart` — bruk Plotly
- ❌ `st.metric` med default styling — wrap i stylable_container
- ❌ Emojis i sidebar-items — bruk to-sifrede mono-nummer
- ❌ `st.balloons/snow`

---

## 10. Sjekkliste før release av en modul

Visuelt:
- [ ] Canvas er nær-svart, ikke Fjell
- [ ] Alle komponenter er inni kort
- [ ] Ingen emojis/ikoner noe sted (jf. §1.7) — eneste unntak er callout-badgen (`i`/`!`/`✓`/`·`) og typografiske piler i prosa
- [ ] Arial gjennomgående — ingen andre fonter (ingen Inter/webfonter)
- [ ] Tre callout-typer brukt korrekt (info/warn/success)

Hierarki:
- [ ] H1 er øverst, største skriftstørrelse
- [ ] Crumb øverst gir kontekst
- [ ] Metadata under tittel (lesetid, nr.)
- [ ] Viktige tall (hvis side har data) i metric-kort på toppen

Diagrammer:
- [ ] Plotly, ikke `st.bar_chart`
- [ ] Heltallsticks på Y-akse
- [ ] Tomme kategorier vises som tick-merker, ikke "0"
- [ ] Snitt visualisert som linje
- [ ] Diagrammet er inni et kort

Sidebar:
- [ ] Seksjons-headers ("OVERSIKT", "KURSMODULER")
- [ ] Aktiv side har venstre-kant i Vann
- [ ] Tosifret mono-nummerering på moduler
- [ ] Administrasjon i footer-seksjon

Innhold:
- [ ] All tekst på norsk
- [ ] Tekniske termer på engelsk (RBAC, context window, prompt)
- [ ] Ingen mock-data som ligner ekte kunde-info
- [ ] CTA-kort til neste modul nederst

---

## 11. Modul-navigasjon med kategori-prikker

### Hvorfor

Kurset har 22 moduler hvor noen typer (individuelle oppgaver, demoer) er flettet inn i sekvensen, ikke samlet i blokker. Ren tematisk gruppering ville sprett nummereringen rundt innenfor hver gruppe og ødelagt sekvensfølelsen. Vi løser det ved å beholde én sekvensiell liste (01–22) og legge til en farget prikk foran hver modul som angir kategori.

### Kategorier

Fem kategorier, hver med en dedikert farge. Disse fargene brukes KUN til prikker i sidemenyen og forsidens modul-grid — ikke gjenbruk til knapper, callouts eller annet.

| Kode | Navn | Hex | Bruk |
|---|---|---|---|
| I | Innføring | `#7EB5D2` | Frost — teori, konseptmoduler, intro-demoer |
| K | Konfigurasjon | `#B197FC` | Lavendel — AGENTS.md, skills.md, tilgjengelige modeller |
| P | Praksis | `#66D9A8` | Mynt — individuelle oppgaver, hands-on |
| G | Gruppe | `#FFAD80` | Korall — gruppeoppgaver, plenum-gjennomganger |
| F | Fordypning | `#94A3B8` | Sky — avanserte demoer, dypdykk, avslutning |

### Visuell spec

- Prikk: 7×7px sirkel i sidebaren, 10×10px i forsidens grid
- Plassering: 16px fra venstre, 10px før modul-nummer
- Modul-nummer: 2 siffer, mono-font, `#6B7691` (active: `#7EB5D2`)
- Tittel: 13px, Arial/system-sans, `#F4F6FB`
- Aktiv tilstand: bakgrunn `rgba(0, 90, 164, 0.18)`, venstrekant `#005AA4` 3px
- Hover: bakgrunn `rgba(0, 90, 164, 0.10)`
- Tooltip på prikk: viser kategorinavnet (via `title`-attributt)

### Kanonisk datakilde

[`data/moduler.py`](data/moduler.py) er det eneste stedet modul-listen defineres. Endringer i rekkefølge, tittel eller kategori gjøres KUN der. Alle andre komponenter (sidebar, forside-grid, framtidige breadcrumbs, "neste modul"-CTA) importerer fra denne fila.

```python
# Korrekt — én datakilde
from data.moduler import MODULER, KATEGORI_FARGE

for modul in MODULER:
    render_modul(modul, active_slug)
```

```python
# Feil — tematisk gruppering bryter nummerorden
pages = {
    "Innføring": [...],
    "Praksis": [...]
}
st.navigation(pages)
```

### Ikke gjør dette

- **Ikke bruk emoji-prikker** (🟢, 🟣 osv.). De renders inkonsistent på tvers av OS-er og fontvarianter. Bruk farget `<div>`.
- **Ikke gruppere moduler tematisk i `st.navigation()`-dict.** Vi bruker custom sidebar nettopp for å unngå at modulnumrene spretter mellom grupper.
- **Ikke hardkode kategorifarger andre steder** enn `data/moduler.py` og `components/sidebar.py`. Hvis du trenger fargen i en ny komponent, importer `KATEGORI_FARGE`.

### Filstruktur

```
app.py                          # Entry: les ?page=..., dispatch til pages_content
data/moduler.py                 # KANONISK modul-liste
components/sidebar.py           # Custom sidebar med kategori-prikker
pages_content/
├── forside.py                  # Modul-grid gruppert etter kategori
├── bli_kjent.py                # Wrapper til modules.oppvarming
├── resultater.py               # Wrapper til modules.oppvarming_resultater
├── admin.py                    # Wrapper til modules.gruppeoppgave_1.admin_logic
└── modules/
    ├── m01_cortex_code.py      # Wrapper til modules.cortex_code.app_logic
    ├── m02_cortex_interaction.py
    └── ...
```

Hver `pages_content/`-fil eksponerer en `render()`-callable. For modul-wrappers er det bare `from modules.<slug>.app_logic import main as render`.

### Når legge til en ny kategori

Hvis kursinnholdet vokser med en sjette kategori-type:

1. Velg en farge som (a) skiller seg tydelig fra de fem eksisterende og (b) fungerer på `#0A0F1F` bakgrunn (kontrast ≥ 3:1).
2. Legg til i `KATEGORI_NAVN`, `KATEGORI_FARGE`, og som CSS-var i `components/sidebar.py`.
3. Oppdater tabellen og legenden i denne seksjonen.
4. Vurder om vi har for mange — over 6 kategorier blir prikker forvirrende, og du bør i stedet bruke filter-chips eller view-toggle.

---

*Når i tvil: åpne `design_preview.html` og sammenlign visuelt. Designet skal være umulig å skille fra mockupen.*
