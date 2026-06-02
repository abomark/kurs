# DESIGN GUIDE v2 — Cortex Code Kursplattform

> **Til AI-agenten som leser denne fila:** Dette er den eneste sannheten for visuell stil. Versjon 2 prioriterer *visuelt hierarki* og *container-struktur* over ren brand-disiplin. Når du må velge mellom "merkevarekonsistens" og "ser profesjonelt ut", velg sistnevnte. Konkret betyr det: pakk alt i kort, og gi tall sin egen plass.

> **⟳ Tema: lyst «Bankbrief» (Designsystem v1).** Appen kjører et **lyst** marine + fersken-uttrykk (hvit canvas, marine `#0A2C72` primær, azur `#1F6FC4` lenker) avledet fra PowerPoint-malen. Token-mappingen ligger i [`theme-light/THEME_PATCH.md`](theme-light/THEME_PATCH.md); den opprinnelige `Designsystem.html`-mockupen er ekstern og ligger ikke i repoet. Fargeverdiene i denne guiden (§0/§2/§5/§7/§9/§10/§11) er avstemt mot Bankbrief-paletten. **SVG-ikoner er adoptert** (eier-beslutning 2026-05-31): appen bruker SVG-linjeikoner via `svg_icon()` (callout-badger, funksjonskort-disker, knapper) — se §1.7 og §7. Emojis er fortsatt aldri tillatt. **Ett åpent avvik mot Designsystem.html, avventer eier:** **Font** — spec'en bruker Libre Franklin + IBM Plex Mono (Google-webfonter), men appen beholder **Arial** (PRD §8 v0.32, bankenes skrifttype-policy). Ikke endret.

---

## 0. Hva som endret seg fra v1

v1 var en brand-disiplinguide. v2 er en *produkt*-design guide. Forskjellen:

| Aspekt | v1 (feil) | v2 (riktig) |
|---|---|---|
| Sidebakgrunn | Fjell `#002776` heldekkende | Hvit `#FFFFFF` (lyst Bankbrief-tema) |
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
7. **Ingen emojis - bruk SVG-linjeikoner.** Overskrifter (H1/H2/H3), `st.subheader`, `st.expander`-labels, callout-titler, crumbs og brødtekst skal aldri ha emoji-dekorasjon (📌🎯⚠️). Hvorfor: emojier renders inkonsistent på tvers av OS-er (Apple vs Windows vs Linux) og trekker tonen i en uønsket retning for et bank-publikum. Ikon-språket er i stedet **SVG-linjeikoner** (Designsystem v1) via `svg_icon()` i `modules/shared/ui.py` - brukt i callout-badger (se §7), funksjonskort-disker og knapper. Typografiske piler (`→`, `←`) er ok i prosa. Kort: aldri emoji, men SVG-ikon er den sanksjonerte ikon-formen. **Ett emoji-unntak:** nettleserfanens favicon (`page_icon` i `st.set_page_config`, [`app.py`](app.py)) - der er `❄` (Snowflake-nikk) bevisst beholdt, fordi det er fane-metadata og ikke side-innhold (eier-beslutning 2026-05-31).
8. **Ingen em-dash (`—`) eller en-dash (`–`).** Verken den lange tankestreken (`—`, U+2014) eller den mellomlange (`–`, U+2013) skal brukes noe sted i appen - heller ikke i overskrifter, brødtekst, captions, kode-strenger, docstrings eller kommentarer. Bruk vanlig bindestrek `-`, komma eller kolon i stedet. Gjelder tegnene `—` (U+2014) og `–` (U+2013); vanlig bindestrek `-` og markdown-skillelinjer (`---`) er uberørt. (Eier-beslutning 2026-05-31: en-dash lagt til; tidligere kun em-dash.)
9. **PowerPoint-nært.** Kurset gjennomgås som en presentasjon - hver modul-side leses som ett (eller få) lysbilde i plenum, ikke som en tett dokumentasjons-side. Konsekvenser: en tydelig ide per "skjerm", stor og luftig typografi, korte punkter framfor lange avsnitt, og visuelle elementer (kort, hero, callout, diagram) framfor vegger av tekst. Presentatør-rettet metainnhold (snakkepunkter, forventet varighet o.l.) hører IKKE hjemme på sidene - de er for presentatørens egne notater, ikke lysbildet.
10. **Ingen `é`/`É`.** Bokstaven `é` (U+00E9) og `É` (U+00C9) skal aldri brukes noe sted i appen - heller ikke i overskrifter, brødtekst, captions, kode-strenger, docstrings eller kommentarer. Bruk alltid vanlig `e`/`E` i stedet. Det desidert vanligste tilfellet er ordet for tallet 1, som skal skrives «en» (uten aksent); regelen gjelder alle ord (skriv «ide», «validere», «komite», «kafe»). (Eier-beslutning 2026-05-31.)

---

## 2. Fargesystem — REVIDERT

### Canvas og overflater (NY hierarki)

```
--canvas:      #FFFFFF   /* Sidens bakgrunn - hvit */
--surface-1:   #FFFFFF   /* Kort, sidebar */
--surface-2:   #F7F8FB   /* Dempet flate / hover */
--surface-3:   #EAF1FB   /* Azur tint (aktiv-fyll, Q-badge) */
```

**Hvorfor:** Det lyse «Bankbrief»-uttrykket er avledet fra PowerPoint-malen og leser rent på projektor i et kursrom. Hvit canvas med azur-tintede aktiv-flater og en marine primærfarge gir et nøkternt, bank-passende preg.

### Brand-farger (lyst Bankbrief-tema)

| Navn (konstant) | HEX | Bruk |
|---|---|---|
| **Vann** (Marine) | `#0A2C72` | Primær aksent: knapper, ikon-disker, venstre-kant på aktiv sidebar-item, info-callouts |
| **Fjell** (Marine dyp) | `#071E50` | Hover på primær, dype aksenter |
| **Frost** (Azur) | `#1F6FC4` | Lenker, sekundær aksent, snitt-linje i diagrammer |
| **Sand** (Fersken) | `#F8E6D5` | Signaturflate / varm aksentflate |
| **Syrin** (Amber) | `#C9821B` | Advarsel-callouts (warn) |

### Tekst-hierarki

```
--text-primary:    #16203A   /* Blekk - hovedtekst */
--text-secondary:  #3B4256   /* Brødtekst, beskrivelser */
--text-tertiary:   #6B7280   /* Captions, metadata, akse-labels */
```

På hvit canvas er hovedteksten blekk `#16203A`. Sand/Fersken er en *flate*-farge, ikke tekstfarge.

### Borders og dividers

```
--border:         #E3E8F1   /* Standard kort-border */
--border-strong:  #D5DEEA   /* Mer synlig avgrensning */
--divider:        #E3E8F1   /* Subtile horisontale linjer */
```

### Forbudt

- Mørk/«nær-svart» canvas (temaet er lyst)
- Tilfeldige hue-er utenfor paletten + de fem kategorifargene (§11)
- Gradienter mellom forskjellige hue-er (purple→pink, blue→green osv.)
- Fersken/Sand som hovedtekstfarge

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
        color="#0A2C72",
        line=dict(width=0),
    ),
    text=[str(c) if c > 0 else "" for c in counts],  # Skjul "0"-labels
    textposition="outside",
    textfont=dict(size=13, color="#16203A"),
))

# Y-akse: heltall, ikke decimaler
max_y = max(counts)
fig.update_yaxes(
    dtick=1,
    range=[0, max_y + 0.5],
    showgrid=True,
    gridcolor="#E3E8F1",
    zeroline=False,
    title_text="",
)

# X-akse: kategorinavn, ikke tall
fig.update_xaxes(
    tickmode="array",
    tickvals=[1, 2, 3, 4, 5],
    ticktext=["1<br><span style='font-size:10px;color:#6B7280'>uenig</span>",
              "2", "3", "4",
              "5<br><span style='font-size:10px;color:#6B7280'>enig</span>"],
    showgrid=False,
)

# Snitt som vertikal linje
fig.add_vline(
    x=mean_value,
    line=dict(color="#C9821B", width=1, dash="dash"),
    annotation_text=f"snitt {mean_value:.1f}",
    annotation_position="top",
    annotation_font=dict(color="#C9821B", size=11),
)

# Layout
fig.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    paper_bgcolor="rgba(0,0,0,0)",
    font=dict(family="Arial, Helvetica, sans-serif", color="#16203A"),
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

Appen bruker **IKKE** `st.navigation()`. Sidebaren er en custom komponent
([`components/sidebar.py`](components/sidebar.py)) som leser den kanoniske
modul-lista fra [`data/moduler.py`](data/moduler.py) (`MODULER` + `SECTIONS`)
og rendrer kategori-prikker, seksjons-headere og «Du er her»-markering selv.
Navigasjon skjer via `?page=<slug>` (lest i [`app.py`](app.py)). Se §11 for
hvorfor vi unngår `st.navigation()`-dict (det ville sprette modulnumrene
mellom grupper).

---

## 7. Callout-mønstre (forbedret)

### Tre typer + en dempet — klar semantikk

Matcher Designsystemet (INFO / TIPS / ADVARSEL). `kind`-argumentet til `callout()` er den kanoniske nøkkelen:

| Type | `kind` | Bakgrunn | Aksent | Ikon (`svg_icon`) | Bruk |
|---|---|---|---|---|---|
| **Info** | `"info"` | `#EAF1FB` (azur tint) | Marine `#0A2C72` | `info` (sirkel-i) | Definisjoner, fakta, nøkkelpunkter |
| **Tips** | `"tip"` | `#E7F5EE` (grønn tint) | Grønn `#1E9E6A` | `tip` (lyspære) | Råd, anbefaling, beste praksis |
| **Advarsel** | `"warn"` | `#FBF1DF` (amber tint) | Amber `#C9821B` | `warn` (trekant) | Risiko, fallgruver, "uten dette skjer X" |
| _Dempet_ | `"subtle"` | `#F2F5FA` (grå) | Tertiær `#6B7280` | `info` | Tomme tilstander / "venter på svar" — intern bruk, ikke en av de tre primære |

**Deprecated alias-navn** (virker fortsatt, men ikke bruk i ny kode): `"success"`/`"highlight"` → `"tip"`, `"warning"` → `"warn"`.

### Ikon: SVG-linjeikon i kvadratisk disc

Callout-badgen er en 28×28px avrundet (radius 7px) disc med aksentfarge-bakgrunn og et **hvitt SVG-linjeikon** (Designsystem v1). Den settes automatisk av `callout()`-helperen ut fra `kind` — `title`-argumentet skal være ren tekst uten emoji.

Ikoner hentes fra `svg_icon(name, *, size, color, stroke)` i `modules/shared/ui.py`. Tilgjengelige navn: `info`, `warn`, `success`, `tip`, `code`, `dbt`, `chart`. Bruk samme helper til funksjonskort-disker og knapp-ikoner.

```python
from modules.shared.ui import svg_icon
# Hvitt kode-ikon på marine disc:
st.markdown(
    f'<div style="width:52px;height:52px;border-radius:50%;background:#0A2C72;'
    f'display:grid;place-items:center;">{svg_icon("code", size=24, color="#FFFFFF")}</div>',
    unsafe_allow_html=True,
)
```

**Emojis er aldri tillatt** (§1.7) — SVG-linjeikon er den sanksjonerte ikon-formen.

### Streamlit-implementasjon

Bruk den ferdige helperen `callout()` i [`modules/shared/ui.py`](modules/shared/ui.py) — ikke lag din egen. Den eier paletten, SVG-badgen og CSS-resetene. Signatur:

```python
def callout(body: str, *, kind: str = "info", title: str | None = None, key: str | None = None) -> None
```

- `body` — markdown (rendres med `st.markdown`).
- `kind` — `"info"` | `"tip"` | `"warn"` | `"subtle"` (kanonisk). Aksentfarge, bakgrunn og SVG-ikon settes automatisk ut fra denne.
- `title` — valgfri fet overskrift, **ren tekst uten emoji** (§1.7).
- `key` — unik nøkkel for `stylable_container`; auto-avledet hvis utelatt.

Bruk:
```python
from modules.shared.ui import callout

callout("**Plasseres i prosjektrot.** Leses automatisk av agenten.",
        kind="info", title="Hva er AGENTS.md?")

callout("Be Cortex forklare spørringen i klartekst før du endrer noe.",
        kind="tip", title="Tips")

callout("Cortex respekterer RBAC — men sjekk alltid diff før produksjon.",
        kind="warn", title="Vær oppmerksom")
```

---

## 8. Modul-sidens struktur

```
1. crumb([...])                         (navigasjonskontekst)
2. module_header(title, subtitle=…)     (modul-hero: eyebrow + display-H1 + azur sub)
3. st.divider()
4. Innholdsseksjoner (callouts, feature_hero/feature_card, code, ev. video)
5. CTA-kort "Til neste modul" via next_module_cta_for(slug)
```

### Modul-hero: `module_header()`

Bruk `module_header(title, *, subtitle=None, eyebrow="For analytikere i bank")` fra
`modules/shared/ui.py` — IKKE `st.title()` + `st.caption()`. Den rendrer:

- **eyebrow** — azur (`#1F6FC4`), 13px, versaler, sperring `.18em`. Default er audience-
  taglinen «For analytikere i bank» (sett `eyebrow=None` for å skru av).
- **H1** — tung marine display (`#0A2C72`, 42px, vekt 800, sperring `-.02em`).
- **subtitle** — azur, 18px (typisk modulens tidligere `Modul N · …`-beskrivelse, uten
  «Modul N ·»-prefikset; modulnummeret står i crumb).

Interaktive gate-skjermer (deltakerkode) beholder vanlig `st.title()`.

**Arial-note:** Designsystem v1 bruker Libre Franklin 900. Arial topper på 700 (bold); vi
bruker 800 + stor størrelse + stram sperring som tilnærming. Font-bytte avventes.

### Funksjonskort: `feature_hero()` / `feature_card()` / `dotlist()`

Designsystemets funksjonskort er helpere i `modules/shared/ui.py`:

- `feature_hero(title, items, *, icon="code")` — fersken signaturflate, 52px marine disc-
  ikon, tittel + prikkliste. For den fremhevede hovedfunksjonen.
- `feature_card(title, body, *, icon="info")` — hvitt kort, 40px disc, tittel + brødtekst.
- `signature_card(number=None)` — **context manager**: fersken signaturflate + azur
  venstrekant (samme varme språk som `feature_hero`), valgfritt marine nummer-badge
  (1/2/3 …) øverst. I motsetning til `feature_card` (ferdig HTML-streng) rendres innholdet
  med `st.markdown` inni `with`-blokken, så markdown (kursiv, lister, kvotering) bevares.
  Bruk for ordnede, prosa-tunge kort-sekvenser (epoker, faser, steg) der den hvite `card()`
  blir for kjølig. Eksempel: de tre epoke-kortene i Evolusjon (modul 1).
- `dotlist(items)` — frittstående marine prikkliste.

Disc-ikoner via `svg_icon()` (`code`/`dbt`/`chart` m.fl.). Legg flere kort i `st.columns`
for grid-oppsett (mockup bruker 1.4fr / 1fr).

**Velg flate bevisst:** hvit `card()` for nøytrale beholdere (diagrammer, seksjoner);
fersken `feature_hero`/`signature_card` for *fremhevede* eller fortellende flater. Bland
sparsomt - fersken er en signaturflate, ikke standard kortbakgrunn.

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
base = "light"
primaryColor = "#0A2C72"               # Marine
backgroundColor = "#FFFFFF"            # Hvit canvas
secondaryBackgroundColor = "#F7F8FB"   # Surface: side / dempet flate
textColor = "#16203A"                  # Blekk
linkColor = "#1F6FC4"                  # Azur
codeBackgroundColor = "#EEF2F8"        # Lys kode-flate
font = "Arial, Helvetica, sans-serif"
baseFontSize = 16
baseRadius = "10px"
borderColor = "#E3E8F1"

[theme.sidebar]
backgroundColor = "#FFFFFF"
secondaryBackgroundColor = "#F7F8FB"
textColor = "#3B4256"
borderColor = "#E3E8F1"
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
- ✅ Custom sidebar (`components/sidebar.py`) som leser `data/moduler.py` — IKKE `st.navigation()` (se §6/§11)
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
- [ ] Canvas er hvit (lyst Bankbrief-tema), ikke mørk
- [ ] Alle komponenter er inni kort
- [ ] Ingen emojis noe sted (jf. §1.7) — eneste tegn-element er callout-badgen (`i`/`!`/`✓`/`·`) og typografiske piler i prosa
- [ ] Arial gjennomgående — ingen andre fonter (ingen Inter/webfonter)
- [ ] Callout-typer brukt korrekt (info/tip/warn; `subtle` for empty-states) - jf. §7

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

Kurset har mange moduler hvor noen typer (individuelle oppgaver, demoer) er flettet inn i sekvensen, ikke samlet i blokker. Ren tematisk gruppering ville sprett nummereringen rundt innenfor hver gruppe og ødelagt sekvensfølelsen. Vi løser det ved å beholde en sekvensiell liste (nummerert fortløpende fra 01) og legge til en farget prikk foran hver modul som angir kategori.

### Kategorier

Fem kategorier, hver med en dedikert farge. Disse fargene brukes KUN til prikker i sidemenyen og forsidens modul-grid — ikke gjenbruk til knapper, callouts eller annet.

| Kode | Navn | Hex | Bruk |
|---|---|---|---|
| I | Innføring | `#1F6FC4` | Azur — teori, konseptmoduler, intro-demoer |
| K | Konfigurasjon | `#6B5BD2` | Violett — AGENTS.md, skills.md, tilgjengelige modeller |
| P | Praksis | `#1E9E6A` | Grønn — individuelle oppgaver, hands-on |
| G | Gruppe | `#E08A3C` | Oransje — gruppeoppgaver, plenum-gjennomganger |
| F | Fordypning | `#8A93A6` | Grå — avanserte demoer, dypdykk, avslutning |

### Visuell spec

- Prikk: 7×7px sirkel i sidebaren, 10×10px i forsidens grid
- Plassering: 16px fra venstre, 10px før modul-nummer
- Modul-nummer: 2 siffer, mono-font, `#6B7280` (active: `#1F6FC4`)
- Tittel: 13px, Arial/system-sans, `#3B4256` (active: marine `#0A2C72`)
- Aktiv tilstand: bakgrunn azur tint `#EAF1FB`, tekst marine `#0A2C72`
- Hover: bakgrunn `#F2F5FA`
- Tooltip på prikk: viser kategorinavnet (via `title`-attributt)

### Kanonisk datakilde

[`data/moduler.py`](data/moduler.py) er det eneste stedet modul-listen defineres. Endringer i rekkefølge, tittel eller kategori gjøres KUN der. Alle andre komponenter (sidebar, forside-grid, framtidige breadcrumbs, "neste modul"-CTA) importerer fra denne fila.

```python
# Korrekt - en datakilde
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

1. Velg en farge som (a) skiller seg tydelig fra de fem eksisterende og (b) fungerer på hvit `#FFFFFF` bakgrunn (kontrast ≥ 3:1).
2. Legg til i `KATEGORI_NAVN`, `KATEGORI_FARGE`, og som CSS-var i `components/sidebar.py`.
3. Oppdater tabellen og legenden i denne seksjonen.
4. Vurder om vi har for mange — over 6 kategorier blir prikker forvirrende, og du bør i stedet bruke filter-chips eller view-toggle.

---

*Når i tvil: følg token-verdiene i §2 og [`theme-light/THEME_PATCH.md`](theme-light/THEME_PATCH.md). (Den originale `Designsystem.html`-mockupen ligger ikke i repoet.)*
