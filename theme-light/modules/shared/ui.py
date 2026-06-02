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

# Designsystem v1 "Bankbrief" — lyst marine + fersken-uttrykk.
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


# --- Header/footer ---


def render_module_header(title: str, subtitle: str = "") -> None:
    """Tittel + lenke tilbake til kurs-forsiden. Kall først på en modul-side."""
    cols = st.columns([6, 1])
    with cols[0]:
        st.title(title)
        if subtitle:
            st.caption(subtitle)
    with cols[1]:
        st.page_link("hub.py", label="← Til forsiden")
    st.divider()


def render_footer() -> None:
    st.divider()
    st.caption("Kurs · Streamlit + Supabase")


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

# (border-color, background, icon-text, kind-class)
# v2 har tre primære typer + en dempet for empty-state.
# Aliaser fra v1 ("highlight"→success, "warning"→warn) holder
# bakoverkompatibilitet med eksisterende moduler.
_CALLOUT_PALETTE: dict[str, tuple[str, str, str]] = {
    "info":      (COLOR_VANN,  "#EAF1FB", "i"),   # Marine ikon / azur tint
    "warn":      ("#C9821B",   "#FBF1DF", "!"),   # Amber
    "success":   ("#1E9E6A",   "#E7F5EE", "✓"),   # Grønn
    "subtle":    (TEXT_TERTIARY, "#F2F5FA", "·"),
}

# v1-aliaser (DESIGN_GUIDE v2 §0 har nye navn, men eksisterende kall fungerer).
_CALLOUT_ALIASES = {
    "highlight": "success",
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
        kind: "info" (Vann), "warn" (Syrin), "success" (Frost) eller
            "subtle" (dempet, for empty-states). Aliaser fra v1
            ("highlight" → success, "warning" → warn) støttes.
        title: Valgfri fet overskrift. Vises sammen med et kvadratisk
            ikon i venstre kolonne.
        key: Unik nøkkel for stylable_container. Auto-avledet hvis None.
    """
    resolved = _CALLOUT_ALIASES.get(kind, kind)
    border, bg, icon = _CALLOUT_PALETTE.get(resolved, _CALLOUT_PALETTE["info"])

    derived_key = key or f"callout_{resolved}_{abs(hash((title or '', body[:40]))) % 100000}"
    # CSS-list: hvert element prefikses med stylable_container sin scoped
    # selektor. Tidligere brukte vi én enkelt streng, men da lekket
    # `p:first-child`-reglene ut globalt og påvirket all markdown på siden.
    css = [
        # 1) Selve callout-boksen — bakgrunn, venstre-kant, radius, padding.
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
            # Ikon + tittel i én flex-rad. margin-bottom holder body-teksten
            # ren — uten den klistrer body seg opp mot icon-raden.
            icon_html = (
                f"<div style='display:flex;align-items:center;"
                f"margin-bottom:12px;'>"
                f"<div style='"
                f"display:flex;align-items:center;justify-content:center;"
                f"width:28px;height:28px;border-radius:6px;"
                f"background:{border};color:#FFFFFF;"
                f"font-weight:700;font-size:14px;line-height:1;"
                f"margin-right:12px;flex-shrink:0;'>"
                f"{icon}</div>"
                f"<span style='font-weight:700;font-size:16px;"
                f"color:{TEXT_PRIMARY};line-height:1.3;'>{title}</span>"
                f"</div>"
            )
            st.markdown(icon_html, unsafe_allow_html=True)
        st.markdown(body)


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
        }}
    """
    with stylable_container(key=derived, css_styles=css):
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

    - `str` — kun en tittel-linje, eller
    - `(tittel, beskrivelse)` — tittel i fet + dempet beskrivelse under.

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
        href: URL — typisk `?page=m02_cortex_interaction` (relativ)
        button_label: tekst på lenke

    Bruker Streamlits native `st.container(border=True)` for å sikre at
    boksen auto-sizer til innholdet (stylable_container med `:has()`-CSS
    klarte ikke å vokse — multi-line description rant utenfor).
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

    Returnerer stille hvis sluggen ikke finnes — da skal du fikse kallet.
    """
    # Lazy-import for å unngå at modules/shared/ui.py blir avhengig av data/.
    from data.moduler import MODULER, page_id  # noqa: PLC0415

    # Bakoverkomp: "pages/cortex_interaction.py" → "cortex_interaction".
    if modul_slug.startswith("pages/") and modul_slug.endswith(".py"):
        modul_slug = modul_slug[len("pages/") : -len(".py")]

    mod = next((m for m in MODULER if m["slug"] == modul_slug), None)
    if mod is None:
        # Ikke en kursmodul — kan være en fast side (oppvarming_resultater,
        # bli_kjent, admin, forside). Bygg en enkel lenke uten oppslag.
        special = {
            "oppvarming_resultater": ("Resultater · Bli kjent", "resultater"),
            "oppvarming": ("Bli kjent", "bli_kjent"),
        }
        target = special.get(modul_slug)
        if target is None:
            return  # ukjent slug — hopper over CTA (fiks kallet)
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
