"""Felles UI-komponenter og helpers på tvers av kursmoduler.

Implementerer PRD §FR-3.12 (markdown-loader for innhold/layout-separasjon)
og §FR-3.15 (designsystem-helpers per DESIGN_GUIDE v2).
"""

from __future__ import annotations

from contextlib import contextmanager
from pathlib import Path
from typing import Iterator, Sequence

import streamlit as st
from streamlit_extras.stylable_container import stylable_container

HUB_URL = "/"

# Designsystem v1 "Bankbrief" - lyst marine + fersken-uttrykk.
# Avledet fra PowerPoint-malen (se Designsystem.html). Navnene er
# beholdt for bakoverkompatibilitet; verdiene er reskinnet til lyst tema.
COLOR_CANVAS = "#FFFFFF"     # hvit canvas
COLOR_SURFACE_1 = "#FFFFFF"  # kort / sidebar
COLOR_SURFACE_2 = "#F7F8FB"  # dempet flate / hover
COLOR_SURFACE_3 = "#EAF1FB"  # azur tint

COLOR_VANN = "#0A2C72"   # Marine (primær)
COLOR_FJELL = "#071E50"  # Marine dyp
COLOR_FROST = "#1F6FC4"  # Azur
COLOR_SAND = "#F8E6D5"   # Fersken (signaturflate)
COLOR_SYRIN = "#C9821B"  # Amber (brukt til warn-callout)

TEXT_PRIMARY = "#16203A"    # Blekk
TEXT_SECONDARY = "#3B4256"  # Brødtekst
TEXT_TERTIARY = "#6B7280"   # Dempet

BORDER = "#E3E8F1"
BORDER_STRONG = "#D5DEEA"

# Skygge (Designsystem v1 shadow-1) - løfter hvite kort fra canvas.
SHADOW_1 = "0 1px 2px rgba(12, 26, 64, 0.05)"


# --- Footer ---
# (Modul-headere bruker nå module_header() lenger ned - den gamle
#  render_module_header() med hub.py-lenke er fjernet som død kode.)


def render_footer() -> None:
    st.divider()
    st.caption("Kurs · Streamlit + Supabase")


def inject_global_css() -> None:
    """Globale CSS-regler (Designsystem v1) - kalles EN gang fra `app.py`.

    Styler Streamlit-primitiver som ikke går via våre helpers: knapper
    (primær / sekundær / form-submit) og inline-kode i markdown. Holdes ett
    sted så vi slipper å gjenta CSS per side.
    """
    st.markdown(
        f"""
        <style>
        /* Primærknapp + form-submit → marine, radius 7px, hover marine-dyp. */
        [data-testid="stButton"] button[kind="primary"],
        [data-testid="stFormSubmitButton"] button {{
            background-color: {COLOR_VANN};
            color: #FFFFFF;
            border: 1px solid {COLOR_VANN};
            border-radius: 7px;
            padding: 11px 22px;
            font-weight: 700;
        }}
        [data-testid="stButton"] button[kind="primary"]:hover,
        [data-testid="stFormSubmitButton"] button:hover {{
            background-color: {COLOR_FJELL};
            border-color: {COLOR_FJELL};
            color: #FFFFFF;
        }}
        /* Sekundærknapp → hvit, marine kontur, hover azur tint. */
        [data-testid="stButton"] button[kind="secondary"] {{
            background-color: #FFFFFF;
            color: {COLOR_VANN};
            border: 1px solid {COLOR_VANN};
            border-radius: 7px;
            padding: 11px 22px;
            font-weight: 700;
        }}
        [data-testid="stButton"] button[kind="secondary"]:hover {{
            background-color: {COLOR_SURFACE_3};
            color: {COLOR_VANN};
            border-color: {COLOR_VANN};
        }}
        /* Inline-kode i markdown → azur tint, marine tekst, radius 5px. */
        [data-testid="stMarkdownContainer"] code:not(pre code) {{
            background-color: {COLOR_SURFACE_3};
            color: {COLOR_VANN};
            border-radius: 5px;
            padding: 2px 6px;
            font-size: 0.88em;
        }}
        </style>
        """,
        unsafe_allow_html=True,
    )


# --- Markdown-loader (FR-3.12) ---


def load_markdown(module_file: str, name: str) -> str:
    """Last markdown fra `<module_dir>/content/<name>.md`."""
    path = Path(module_file).parent / "content" / f"{name}.md"
    if not path.exists():
        return f"_Mangler innhold: `content/{name}.md`_"
    return path.read_text(encoding="utf-8")


def load_titled_markdown(module_file: str, name: str) -> tuple[str, str]:
    """Som `load_markdown`, men leser tittel fra første `# `-linje."""
    raw = load_markdown(module_file, name)
    lines = raw.lstrip().splitlines()
    if lines and lines[0].startswith("# "):
        title = lines[0][2:].strip()
        body = "\n".join(lines[1:]).strip()
        return (title, body)
    return ("", raw)


def load_split_markdown(
    module_file: str,
    name: str,
    splitter: str = "## ",
) -> dict[str, str]:
    """Last markdown og split på `##`-headere (eller annet prefix).

    Returnerer ordnet dict `{seksjonstittel: body}`. Innhold før første
    splitter-header havner under nøkkelen `""`. Brukes f.eks. til å
    rendere `## Før` og `## Etter` i to kolonner uten å duplisere filer.
    """
    raw = load_markdown(module_file, name)
    sections: dict[str, str] = {}
    current_title = ""
    current_lines: list[str] = []
    for line in raw.splitlines():
        if line.startswith(splitter):
            if current_lines or current_title:
                sections[current_title] = "\n".join(current_lines).strip()
            current_title = line[len(splitter):].strip()
            current_lines = []
        else:
            current_lines.append(line)
    if current_lines or current_title:
        sections[current_title] = "\n".join(current_lines).strip()
    return sections


# --- Callout (FR-3.15 / DESIGN_GUIDE v2 §7) ---

# SVG-linjeikoner (Designsystem v1 «Bankbrief»). 24×24 viewBox,
# stroke=currentColor så fargen styres av containeren. Ingen emojis
# (§1.7) - dette er det sanksjonerte ikon-språket i appen.
_SVG_ICONS: dict[str, str] = {
    "info":    '<circle cx="12" cy="12" r="9"/><path d="M12 11v5"/><path d="M12 7.5v.01"/>',
    "warn":    '<path d="M12 3l9 16H3z"/><path d="M12 10v4"/><path d="M12 17v.01"/>',
    "success": '<circle cx="12" cy="12" r="9"/><path d="M8.5 12.5l2.5 2.5 4.5-5"/>',
    "tip":     '<path d="M9 18h6"/><path d="M10 21h4"/><path d="M12 3a6 6 0 0 0-4 10.5c.7.7 1 1.3 1 2.5h6c0-1.2.3-1.8 1-2.5A6 6 0 0 0 12 3z"/>',
    "code":    '<polyline points="9 8 5 12 9 16"/><polyline points="15 8 19 12 15 16"/>',
    "dbt":     '<circle cx="6" cy="6" r="2.4"/><circle cx="18" cy="6" r="2.4"/><circle cx="12" cy="18" r="2.4"/><path d="M6 8.5v3a2 2 0 0 0 2 2h8a2 2 0 0 0 2-2v-3"/><path d="M12 13.5v2"/>',
    "chart":   '<path d="M4 18l5-5 3 3 6-7"/><path d="M4 4v16h16"/>',
}


def svg_icon(
    name: str,
    *,
    size: int = 18,
    color: str = "currentColor",
    stroke: float = 2.2,
) -> str:
    """Returner et inline SVG-linjeikon (Designsystem v1 ikon-språk).

    Brukes i `unsafe_allow_html`-kontekst (callout-badger, funksjonskort-
    disker, knapper). Ingen emojis (§1.7) - dette er den sanksjonerte
    ikon-formen. Ukjent navn returnerer tom streng.
    """
    paths = _SVG_ICONS.get(name)
    if not paths:
        return ""
    return (
        f'<svg viewBox="0 0 24 24" width="{size}" height="{size}" fill="none" '
        f'stroke="{color}" stroke-width="{stroke}" stroke-linecap="round" '
        f'stroke-linejoin="round">{paths}</svg>'
    )


# Callout-palett: (aksentfarge, bakgrunn, ikon-navn). Tre primære, semantiske
# typer som matcher Designsystemet (INFO / TIPS / ADVARSEL), pluss en dempet
# "subtle" for empty-states. Se DESIGN_GUIDE §7.
_CALLOUT_PALETTE: dict[str, tuple[str, str, str]] = {
    "info":      (COLOR_VANN,    "#EAF1FB", "info"),  # Marine / azur tint - fakta, definisjon
    "tip":       ("#1E9E6A",     "#E7F5EE", "tip"),   # Grønn - råd, anbefaling, beste praksis
    "warn":      ("#C9821B",     "#FBF1DF", "warn"),  # Amber - risiko, fallgruve
    "subtle":    (TEXT_TERTIARY, "#F2F5FA", "info"),  # Dempet grå - tomme tilstander (intern)
}

# Deprecated alias-navn. Behold for bakoverkomp, men nye kall skal bruke de
# kanoniske navnene (info/tip/warn/subtle). Den grønne typen ble omdøpt fra
# "success" til "tip" (jf. spec), så success/highlight peker nå til "tip".
_CALLOUT_ALIASES = {
    "success": "tip",
    "highlight": "tip",
    "warning": "warn",
}


def callout(
    body: str,
    *,
    kind: str = "info",
    title: str | None = None,
    key: str | None = None,
) -> None:
    """Render en stilet callout-boks per DESIGN_GUIDE v2 §7.

    Args:
        body: Markdown-tekst som rendres med `st.markdown`.
        kind: Kanonisk: "info" (marine - fakta/definisjon), "tip" (grønn -
            råd/anbefaling), "warn" (amber - risiko/fallgruve), eller
            "subtle" (dempet grå - empty-states). Deprecated aliaser:
            "success"/"highlight" → "tip", "warning" → "warn".
        title: Valgfri fet overskrift. Vises sammen med et kvadratisk
            ikon i venstre kolonne.
        key: Unik nøkkel for stylable_container. Auto-avledet hvis None.
    """
    resolved = _CALLOUT_ALIASES.get(kind, kind)
    border, bg, icon_name = _CALLOUT_PALETTE.get(resolved, _CALLOUT_PALETTE["info"])

    derived_key = key or f"callout_{resolved}_{abs(hash((title or '', body[:40]))) % 100000}"
    # CSS-list: hvert element prefikses med stylable_container sin scoped
    # selektor. Tidligere brukte vi en enkelt streng, men da lekket
    # `p:first-child`-reglene ut globalt og påvirket all markdown på siden.
    css = [
        # 1) Selve callout-boksen - bakgrunn, venstre-kant, radius, padding.
        f"""{{
            background-color: {bg};
            border-left: 3px solid {border};
            border-radius: 10px;
            padding: 18px 22px;
            margin: 8px 0;
        }}""",
        # 2) Nullstill Streamlits egen inner-padding på vertikal-blokk.
        #    Uten dette får callout-en ekstra ~80px venstre-indent.
        """ [data-testid="stVerticalBlock"] {
            padding: 0 !important;
            gap: 0.5rem !important;
        }""",
        # 3) Nullstill element-container padding/margin.
        """ [data-testid="stElementContainer"], .element-container {
            padding: 0 !important;
            margin: 0 !important;
        }""",
        # 4) Nullstill margin på stMarkdown-wrapper og første/siste paragraf.
        #    Bruker :first-of-type/:last-of-type (matcher uansett om det er
        #    andre elementer foran/etter <p>). `:first-child` mislyktes fordi
        #    Streamlit av og til putter andre wrappere inni stMarkdownContainer.
        """ [data-testid="stMarkdown"] {
            margin: 0 !important;
        }""",
        """ [data-testid="stMarkdownContainer"] {
            margin: 0 !important;
        }""",
        """ [data-testid="stMarkdownContainer"] p:first-of-type {
            margin-top: 0 !important;
        }""",
        """ [data-testid="stMarkdownContainer"] p:last-of-type {
            margin-bottom: 0 !important;
        }""",
    ]
    with stylable_container(key=derived_key, css_styles=css):
        if title:
            # Ikon + tittel i en flex-rad. margin-bottom holder body-teksten
            # ren - uten den klistrer body seg opp mot icon-raden.
            icon_html = (
                f"<div style='display:flex;align-items:center;"
                f"margin-bottom:12px;'>"
                f"<div style='"
                f"display:flex;align-items:center;justify-content:center;"
                f"width:28px;height:28px;border-radius:7px;"
                f"background:{border};color:#FFFFFF;line-height:0;"
                f"margin-right:12px;flex-shrink:0;'>"
                f"{svg_icon(icon_name, size=17, color='#FFFFFF')}</div>"
                f"<span style='font-weight:700;font-size:16px;"
                f"color:{TEXT_PRIMARY};line-height:1.3;'>{title}</span>"
                f"</div>"
            )
            st.markdown(icon_html, unsafe_allow_html=True)
        st.markdown(body)


# --- Modul-hero-header (Designsystem v1 §3) ---


def module_header(
    title: str,
    *,
    subtitle: str | None = None,
    eyebrow: str | None = "For analytikere i bank",
) -> None:
    """Render modul-hero per Designsystem v1: eyebrow + display-H1 + undertittel.

    Erstatter `st.title()` + `st.caption("Modul N · …")`-mønsteret. Plasseres
    etter `crumb()` og før `st.divider()`.

    - eyebrow: azur versaler med vid sperring (skru av med eyebrow=None)
    - title: tung marine display-H1
    - subtitle: azur undertittel (typisk modulens tidligere caption-tekst)

    Arial-begrensning: spec'en bruker vekt 900 (Libre Franklin). Arial topper
    på 700 (bold) - vi bruker 800 (degraderer til bold) + stor størrelse +
    stram sperring for å tilnærme display-uttrykket. Font-bytte avventes.
    """
    blocks: list[str] = []
    if eyebrow:
        blocks.append(
            f"<div style='font-size:13px;font-weight:700;letter-spacing:0.18em;"
            f"text-transform:uppercase;color:{COLOR_FROST};"
            f"margin:0 0 10px;'>{eyebrow}</div>"
        )
    blocks.append(
        f"<div style='font-size:42px;font-weight:800;letter-spacing:-0.02em;"
        f"color:{COLOR_VANN};line-height:1.04;margin:0;'>{title}</div>"
    )
    if subtitle:
        blocks.append(
            f"<div style='font-size:18px;color:{COLOR_FROST};"
            f"line-height:1.5;margin:14px 0 0;'>{subtitle}</div>"
        )
    st.markdown(
        f"<div style='margin:0 0 4px;'>{''.join(blocks)}</div>",
        unsafe_allow_html=True,
    )


# --- Funksjonskort (Designsystem v1 §3) ---


def _disc(icon: str, *, diameter: int, icon_size: int) -> str:
    """Sirkulær marine disc med hvitt SVG-linjeikon (Designsystem v1)."""
    return (
        f"<div style='width:{diameter}px;height:{diameter}px;border-radius:50%;"
        f"background:{COLOR_VANN};display:grid;place-items:center;flex:0 0 auto;"
        f"box-shadow:0 1px 2px rgba(12,26,64,.12);line-height:0;'>"
        f"{svg_icon(icon, size=icon_size, color='#FFFFFF')}</div>"
    )


def _dotlist_html(items: Sequence[str], *, color: str = COLOR_VANN, top_margin: int = 0) -> str:
    """Returner `<ul>`-HTML med marine prikker (Designsystem v1 dotlist)."""
    lis = "".join(
        f"<li style='position:relative;padding-left:26px;font-size:16px;"
        f"color:{TEXT_PRIMARY};margin:12px 0 0;line-height:1.5;'>"
        f"<span style='position:absolute;left:6px;top:9px;width:7px;height:7px;"
        f"border-radius:50%;background:{color};'></span>{it}</li>"
        for it in items
    )
    return f"<ul style='list-style:none;margin:{top_margin}px 0 0;padding:0;'>{lis}</ul>"


def dotlist(items: Sequence[str], *, color: str = COLOR_VANN) -> None:
    """Render en prikkliste med marine prikker (Designsystem v1).

    Frittstående variant av punktlisten i `feature_hero` - bruk der du vil ha
    designsystemets prikker uten et helt funksjonskort rundt.
    """
    st.markdown(_dotlist_html(items, color=color), unsafe_allow_html=True)


def feature_hero(
    title: str,
    items: Sequence[str],
    *,
    icon: str = "code",
) -> None:
    """Fersken hero-funksjonskort: marine disc + tittel + punktliste.

    Designsystem v1: signaturflate (fersken) med azur venstrestrek, en 52px
    disc med hvitt ikon, tittel (22px marine), og en prikkliste.
    """
    html = (
        f"<div style='background:{COLOR_SAND};border-left:5px solid #1F6FC4;"
        f"border-radius:11px;padding:30px 32px;'>"
        f"<div style='display:flex;align-items:center;gap:16px;'>"
        f"{_disc(icon, diameter=52, icon_size=24)}"
        f"<div style='font-size:22px;font-weight:800;letter-spacing:-0.01em;"
        f"color:{COLOR_VANN};'>{title}</div></div>"
        f"{_dotlist_html(items, top_margin=18)}</div>"
    )
    st.markdown(html, unsafe_allow_html=True)


def feature_card(title: str, body: str, *, icon: str = "info") -> None:
    """Hvitt funksjonskort: 40px marine disc + tittel + brødtekst.

    Designsystem v1: hvit flate, azur venstrestrek, subtil skygge.
    """
    html = (
        f"<div style='background:#FFFFFF;border:1px solid {BORDER};"
        f"border-left:5px solid #1F6FC4;border-radius:11px;padding:22px 24px;"
        f"box-shadow:0 1px 2px rgba(12,26,64,.05);'>"
        f"<div style='display:flex;align-items:center;gap:14px;'>"
        f"{_disc(icon, diameter=40, icon_size=19)}"
        f"<div style='font-size:18px;font-weight:800;letter-spacing:-0.01em;"
        f"color:{COLOR_VANN};'>{title}</div></div>"
        f"<p style='margin:14px 0 0;font-size:14.5px;color:{TEXT_SECONDARY};"
        f"line-height:1.6;'>{body}</p></div>"
    )
    st.markdown(html, unsafe_allow_html=True)


# --- Metric-kort (DESIGN_GUIDE v2 §4) ---


def metric_card(label: str, value: str, sub: str | None = None) -> None:
    """Render et metric-kort med uppercase-label, stor verdi og valgfri trend.

    Brukes for viktige tall øverst på resultat-sider, dashboard-overskrifter,
    KPI-er. Se DESIGN_GUIDE v2 §4.
    """
    key = f"metric_{abs(hash((label, value))) % 100000}"
    css = f"""
        {{
            background-color: {COLOR_SURFACE_1};
            border: 1px solid {BORDER};
            border-radius: 10px;
            padding: 18px 20px;
            min-height: 110px;
            box-shadow: {SHADOW_1};
        }}
    """
    sub_html = (
        f"<div style='font-size:13px;color:{COLOR_FROST};margin-top:6px;'>{sub}</div>"
        if sub
        else ""
    )
    html = (
        f"<div style='font-size:11px;font-weight:600;letter-spacing:0.08em;"
        f"text-transform:uppercase;color:{TEXT_TERTIARY};'>{label}</div>"
        f"<div style='font-size:32px;font-weight:700;color:{TEXT_PRIMARY};"
        f"font-variant-numeric:tabular-nums;line-height:1.15;margin-top:6px;'>"
        f"{value}</div>"
        f"{sub_html}"
    )
    with stylable_container(key=key, css_styles=css):
        st.markdown(html, unsafe_allow_html=True)


def metric_row(metrics: Sequence[tuple[str, str] | tuple[str, str, str]]) -> None:
    """Render flere metric-kort side-ved-side. Inputs er (label, value) eller (label, value, sub)."""
    if not metrics:
        return
    cols = st.columns(len(metrics))
    for col, m in zip(cols, metrics):
        with col:
            if len(m) == 3:
                metric_card(m[0], m[1], m[2])
            else:
                metric_card(m[0], m[1])


# --- Card (generell container, DESIGN_GUIDE v2 §4) ---


@contextmanager
def card(key: str | None = None, padding: str = "24px") -> Iterator[None]:
    """Context manager for et standard kort (surface-1, border, radius).

    Brukes til å pakke diagrammer, seksjoner, eller alt annet som ellers
    ville flytt fritt over canvas. Se DESIGN_GUIDE v2 §4.
    """
    derived = key or f"card_{abs(hash(padding)) % 100000}"
    css = f"""
        {{
            background-color: {COLOR_SURFACE_1};
            border: 1px solid {BORDER};
            border-radius: 10px;
            padding: {padding};
            margin: 8px 0;
            box-shadow: {SHADOW_1};
        }}
    """
    with stylable_container(key=derived, css_styles=css):
        yield


@contextmanager
def signature_card(
    number: int | str | None = None,
    *,
    key: str | None = None,
    padding: str = "24px 26px",
) -> Iterator[None]:
    """Varmt signaturkort: fersken-flate + azur venstrekant (Designsystem v1).

    Som `card()`, men med designsystemets varme signaturflate (fersken) i
    stedet for hvit - samme språk som `feature_hero`. Valgfritt nummer-badge
    (marine disc) øverst, til ordnede sekvenser (epoker, faser, steg).
    Innhold rendres som vanlig med `st.markdown` inni context-manageren, så
    markdown (kursiv, lister) bevares - i motsetning til `feature_card` som
    tar ferdig HTML-streng.
    """
    derived = key or f"sigcard_{abs(hash((str(number), padding))) % 100000}"
    css = f"""
        {{
            background-color: {COLOR_SAND};
            border-left: 5px solid {COLOR_FROST};
            border-radius: 11px;
            padding: {padding};
            margin: 8px 0;
            box-shadow: {SHADOW_1};
        }}
    """
    with stylable_container(key=derived, css_styles=css):
        if number is not None:
            st.markdown(
                f"<div style='width:36px;height:36px;border-radius:50%;"
                f"background:{COLOR_VANN};color:#FFFFFF;display:grid;"
                f"place-items:center;font-weight:800;font-size:16px;"
                f"font-variant-numeric:tabular-nums;line-height:1;"
                f"box-shadow:0 1px 2px rgba(12,26,64,.12);margin-bottom:6px;'>"
                f"{number}</div>",
                unsafe_allow_html=True,
            )
        yield


# --- Nummererte steg / sjekkpunkter (DESIGN_GUIDE v2 §4) ---


def numbered_steps(
    items: Sequence[str | tuple[str, str]],
    *,
    key: str | None = None,
    accent: str | None = None,
) -> None:
    """Render en nummerert liste med runde badge-tall (1, 2, 3 …) i ett kort.

    Brukes til steg-for-steg-prosesser og sjekklister der rekkefølgen eller
    antallet er poenget. Hvert element er enten:

    - `str` - kun en tittel-linje, eller
    - `(tittel, beskrivelse)` - tittel i fet + dempet beskrivelse under.

    Args:
        items: sekvens av strenger eller (tittel, body)-tupler.
        key: unik nøkkel for kort-containeren. Auto-avledet hvis None.
        accent: badge-farge. Default Vann.
    """
    accent = accent or COLOR_VANN
    last = len(items) - 1
    rows: list[str] = []
    for i, item in enumerate(items):
        if isinstance(item, (tuple, list)):
            title, body = item[0], (item[1] if len(item) > 1 else "")
        else:
            title, body = item, ""
        border = "none" if i == last else f"1px solid {BORDER}"
        body_html = (
            f"<div style='font-size:14px;color:{TEXT_SECONDARY};"
            f"margin-top:3px;line-height:1.5;'>{body}</div>"
            if body
            else ""
        )
        rows.append(
            f"<div style='display:flex;gap:14px;align-items:flex-start;"
            f"padding:13px 0;border-bottom:{border};'>"
            f"<div style='flex:none;width:30px;height:30px;border-radius:8px;"
            f"background:{accent};color:#FFFFFF;font-weight:700;font-size:14px;"
            f"display:flex;align-items:center;justify-content:center;'>{i + 1}</div>"
            f"<div style='padding-top:3px;'>"
            f"<div style='font-weight:700;font-size:15px;color:{TEXT_PRIMARY};"
            f"line-height:1.4;'>{title}</div>{body_html}</div>"
            f"</div>"
        )
    html = "".join(rows)
    with card(key=key or f"steps_{abs(hash(html)) % 100000}", padding="4px 22px"):
        st.markdown(html, unsafe_allow_html=True)


# --- Crumb / breadcrumb (DESIGN_GUIDE v2 §8) ---


def crumb(parts: Sequence[str]) -> None:
    """Render en navigasjonscrumb øverst på en modul-side.

    Eksempel: `crumb(["Kursmoduler", "05 · AGENTS.md"])`.
    """
    sep = f"<span style='color:{TEXT_TERTIARY};margin:0 8px;'>/</span>"
    spans = sep.join(
        f"<span style='color:{TEXT_SECONDARY};font-size:13px;'>{p}</span>"
        for p in parts
    )
    st.markdown(
        f"<div style='margin-bottom:4px;'>{spans}</div>",
        unsafe_allow_html=True,
    )


# --- CTA-kort til neste modul (DESIGN_GUIDE v2 §8) ---


def next_module_cta(
    title: str,
    description: str,
    href: str | None = None,
    button_label: str = "Fortsett →",
) -> None:
    """Render et "neste modul"-kort med klikkbar lenke til neste side.

    Args:
        title: f.eks. "02 · Snowsight vs CLI"
        description: kort overgang/beskrivelse
        href: URL - typisk `?page=m02_cortex_interaction` (relativ)
        button_label: tekst på lenke

    Bruker Streamlits native `st.container(border=True)` for å sikre at
    boksen auto-sizer til innholdet (stylable_container med `:has()`-CSS
    klarte ikke å vokse - multi-line description rant utenfor).
    Navigerer via vanlig `<a href>` (query-param-router i app.py).
    """
    with st.container(border=True):
        cols = st.columns([4, 1], vertical_alignment="center")
        with cols[0]:
            st.markdown(
                f"<div style='font-size:11px;font-weight:600;letter-spacing:0.08em;"
                f"text-transform:uppercase;color:{TEXT_TERTIARY};'>NESTE MODUL</div>"
                f"<div style='font-size:18px;font-weight:700;color:{TEXT_PRIMARY};"
                f"margin-top:4px;line-height:1.3;'>{title}</div>"
                f"<div style='font-size:14px;color:{TEXT_SECONDARY};margin-top:6px;"
                f"line-height:1.5;'>{description}</div>",
                unsafe_allow_html=True,
            )
        with cols[1]:
            if href:
                st.markdown(
                    f'<a href="{href}" target="_self" '
                    f'style="display:inline-block;padding:8px 16px;'
                    f'background:{COLOR_VANN};color:#FFFFFF;'
                    f'border-radius:8px;text-decoration:none;'
                    f'font-weight:600;font-size:14px;">'
                    f"{button_label}</a>",
                    unsafe_allow_html=True,
                )


def next_module_cta_for(modul_slug: str, *, button_label: str = "Fortsett →") -> None:
    """Slå opp neste modul i `data.moduler.MODULER` og render CTA-kort.

    `modul_slug` er kort-formen brukt i MODULER (f.eks. "cortex_interaction",
    "agents_md", "gruppeoppgave_1"). For bakoverkompatibilitet aksepteres
    også gammel `"pages/<slug>.py"`-form fra første migrasjon.

    Returnerer stille hvis sluggen ikke finnes - da skal du fikse kallet.
    """
    # Lazy-import for å unngå at modules/shared/ui.py blir avhengig av data/.
    from data.moduler import MODULER, page_id  # noqa: PLC0415

    # Bakoverkomp: "pages/cortex_interaction.py" → "cortex_interaction".
    if modul_slug.startswith("pages/") and modul_slug.endswith(".py"):
        modul_slug = modul_slug[len("pages/") : -len(".py")]

    mod = next((m for m in MODULER if m["slug"] == modul_slug), None)
    if mod is None:
        # Ikke en kursmodul - kan være en fast side (oppvarming_resultater,
        # bli_kjent, admin, forside). Bygg en enkel lenke uten oppslag.
        special = {
            "oppvarming_resultater": ("Resultater · Bli kjent", "resultater"),
            "oppvarming": ("Bli kjent", "bli_kjent"),
        }
        target = special.get(modul_slug)
        if target is None:
            return  # ukjent slug - hopper over CTA (fiks kallet)
        title, href_slug = target
        next_module_cta(
            title=title,
            description="",
            href=f"?page={href_slug}",
            button_label=button_label,
        )
        return

    title = f"{mod['nr']:02d} · {mod['tittel']}"
    href = f"?page={page_id(mod)}"
    next_module_cta(
        title=title,
        description="",  # MODULER har ikke description-felt; Andre fyller selv via next_module_cta direkte hvis ønskelig
        href=href,
        button_label=button_label,
    )
