"""Kanonisk modul-liste for Cortex Code-kurset.

Hver modul er en dict med felt:
- nr:       int, 1–26. Sekvensnummer i kurset.
- slug:     str, matcher mappenavn under `modules/<slug>/` slik at
            wrapper-importene i `pages_content/modules/` finner riktig
            `main()` å aliasere som `render()`.
- tittel:   str, vist navn i sidebaren.
- kategori: str, en av "I" | "K" | "P" | "G" | "F".

Endrer du rekkefølgen her, endres rekkefølgen i sidebaren OG i forsidens
modul-grid. Ikke endre nummereringen uten å oppdatere filnavn under
`pages_content/modules/m{nr:02d}_{slug}.py` tilsvarende.

Se DESIGN_GUIDE.md §11 for kategori-betydning og fargevalg.
"""

from __future__ import annotations

MODULER = [
    {"nr":  1, "slug": "evolusjon",                  "tittel": "Fra Google til spesifikasjon", "kategori": "I"},
    {"nr":  2, "slug": "cortex_code",                "tittel": "Cortex Code",                "kategori": "I"},
    {"nr":  3, "slug": "cortex_interaction",         "tittel": "Snowsight vs CLI",           "kategori": "I"},
    {"nr":  4, "slug": "cortex_in_snowsight",        "tittel": "Cortex Code i Snowsight",    "kategori": "I"},
    {"nr":  5, "slug": "arkitektur",                 "tittel": "Arkitekturoversikt",         "kategori": "I"},
    {"nr":  6, "slug": "demo_1",                     "tittel": "Første demo",                "kategori": "I"},
    {"nr":  7, "slug": "individuell_oppgave_1",      "tittel": "Individuell oppgave 1",      "kategori": "P"},
    {"nr":  8, "slug": "agents_md",                  "tittel": "AGENTS.md",                  "kategori": "K"},
    {"nr":  9, "slug": "gruppeoppgave_1",            "tittel": "Gruppeoppgave 1",            "kategori": "G"},
    {"nr": 10, "slug": "gruppeoppgave_1_resultater", "tittel": "Resultater Gruppeoppgave 1", "kategori": "G"},
    {"nr": 11, "slug": "tilgjengelige_modeller",     "tittel": "Tilgjengelige modeller",     "kategori": "K"},
    {"nr": 12, "slug": "individuell_oppgave_modellvalg", "tittel": "Individuell oppgave: Modellvalg", "kategori": "P"},
    {"nr": 13, "slug": "skills_md",                  "tittel": "skills.md",                  "kategori": "K"},
    {"nr": 14, "slug": "gruppeoppgave_2",            "tittel": "Gruppeoppgave 2",            "kategori": "G"},
    {"nr": 15, "slug": "memory_md",                  "tittel": "memory.md",                  "kategori": "K"},
    {"nr": 16, "slug": "gruppeoppgave_3",            "tittel": "Gruppeoppgave 3",            "kategori": "G"},
    {"nr": 17, "slug": "gruppeoppgave_3_resultater", "tittel": "Resultater Gruppeoppgave 3", "kategori": "G"},
    {"nr": 18, "slug": "prompt_engineering",         "tittel": "Prompt engineering",         "kategori": "K"},
    {"nr": 19, "slug": "individuell_oppgave_2",      "tittel": "Individuell oppgave 2",      "kategori": "P"},
    {"nr": 20, "slug": "individuell_oppgave_3",      "tittel": "Individuell oppgave 3",      "kategori": "P"},
    {"nr": 21, "slug": "demo_2",                     "tittel": "Demo 2",                     "kategori": "F"},
    {"nr": 22, "slug": "individuell_oppgave_4",      "tittel": "Individuell oppgave 4",      "kategori": "P"},
    {"nr": 23, "slug": "autonomous_loop",            "tittel": "Autonomous loop",            "kategori": "F"},
    {"nr": 24, "slug": "individuell_oppgave_5",      "tittel": "Individuell oppgave 5",      "kategori": "P"},
    {"nr": 25, "slug": "kostnader",                  "tittel": "Kostnader",                  "kategori": "F"},
    {"nr": 26, "slug": "avslutning",                 "tittel": "Avslutning",                 "kategori": "F"},
]

KATEGORI_NAVN = {
    "I": "Innføring",
    "K": "Konfigurasjon",
    "P": "Praksis",
    "G": "Gruppe",
    "F": "Fordypning",
}

KATEGORI_FARGE = {
    "I": "#7EB5D2",  # Frost
    "K": "#B197FC",  # Lavendel
    "P": "#66D9A8",  # Mynt
    "G": "#FFAD80",  # Korall
    "F": "#94A3B8",  # Sky
}


def page_id(modul: dict) -> str:
    """Returner sluggen som brukes i `?page=...` for en gitt modul."""
    return f"m{modul['nr']:02d}_{modul['slug']}"


# Seksjons-gruppering for sidebar (DESIGN_GUIDE §11 utvidet).
#
# Seksjon != kategori. Kategorien (I/K/P/G/F) sier hva slags type modul
# det er (konseptmodul, gruppeoppgave, individuell oppgave, ...) og styrer
# prikk-fargen. Seksjonen sier hvilken temporal blokk av kurset modulen
# tilhører, og styrer vertikal gruppering + "DU ER HER"-aktiv-markering
# i sidemenyen.
#
# `modules` lister `page_id()`-strenger, ikke nr — så stabil over om-
# nummerering av modul-listen.
SECTIONS = [
    {
        "id": "introduksjon",
        "label": "Introduksjon",
        "modules": [
            "m01_evolusjon",
            "m02_cortex_code",
            "m03_cortex_interaction",
            "m04_cortex_in_snowsight",
            "m05_arkitektur",
            "m06_demo_1",
            "m07_individuell_oppgave_1",
        ],
    },
    {
        "id": "agents_md",
        "label": "AGENTS.md",
        "modules": [
            "m08_agents_md",
            "m09_gruppeoppgave_1",
            "m10_gruppeoppgave_1_resultater",
        ],
    },
    {
        "id": "modellvalg",
        "label": "Modellvalg",
        "modules": [
            "m11_tilgjengelige_modeller",
            "m12_individuell_oppgave_modellvalg",
        ],
    },
    {
        "id": "skills_md",
        "label": "skills.md",
        "modules": [
            "m13_skills_md",
            "m14_gruppeoppgave_2",
        ],
    },
    {
        "id": "memory_md",
        "label": "memory.md",
        "modules": [
            "m15_memory_md",
            "m16_gruppeoppgave_3",
            "m17_gruppeoppgave_3_resultater",
        ],
    },
    {
        "id": "prompt_engineering",
        "label": "Prompt engineering",
        "modules": [
            "m18_prompt_engineering",
        ],
    },
    {
        "id": "anvendt_praksis",
        "label": "Anvendt praksis",
        "modules": [
            "m19_individuell_oppgave_2",
            "m20_individuell_oppgave_3",
        ],
    },
    {
        "id": "dybde",
        "label": "Dybde",
        "modules": [
            "m21_demo_2",
            "m22_individuell_oppgave_4",
            "m23_autonomous_loop",
            "m24_individuell_oppgave_5",
        ],
    },
    {
        "id": "avslutning",
        "label": "Avslutning",
        "modules": [
            "m25_kostnader",
            "m26_avslutning",
        ],
    },
]


def section_for_page(page_id_str: str) -> dict | None:
    """Returner seksjonen et `page_id` tilhører, eller None om ukjent."""
    return next((s for s in SECTIONS if page_id_str in s["modules"]), None)


def find_by_page_id(page_id_str: str) -> dict | None:
    """Slå opp en modul fra `?page=m05_agents_md`. Returnerer None hvis ukjent."""
    if not page_id_str.startswith("m"):
        return None
    try:
        nr = int(page_id_str[1:3])
    except ValueError:
        return None
    for modul in MODULER:
        if modul["nr"] == nr:
            return modul
    return None
