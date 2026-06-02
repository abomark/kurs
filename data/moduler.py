"""Kanonisk modul-liste for Cortex Code-kurset.

Hver modul er en dict med felt:
- nr:       int, 1-28. Sekvensnummer i kurset.
- slug:     str, matcher mappenavn under `modules/<slug>/` slik at
            wrapper-importene i `pages_content/modules/` finner riktig
            `main()` å aliasere som `render()`.
- tittel:   str, vist navn i sidebaren.
- kategori: str, en av "I" | "K" | "P" | "G" | "F".

Endrer du rekkefølgen her, endres rekkefølgen i sidebaren. Ikke endre
nummereringen uten å oppdatere filnavn under
`pages_content/modules/m{nr:02d}_{slug}.py` tilsvarende.

Se DESIGN_GUIDE.md §11 for kategori-betydning og fargevalg.
"""

from __future__ import annotations

MODULER = [
    {"nr":  1, "slug": "evolusjon",                  "tittel": "Evolusjon",                  "kategori": "I"},
    {"nr":  2, "slug": "cortex_code",                "tittel": "Cortex Code",                "kategori": "I"},
    {"nr":  3, "slug": "cortex_interaction",         "tittel": "Snowsight vs CLI",           "kategori": "I"},
    {"nr":  4, "slug": "arkitektur",                 "tittel": "Under panseret",             "kategori": "I"},
    {"nr":  5, "slug": "demo_1",                     "tittel": "Første demo",                "kategori": "I"},
    {"nr":  6, "slug": "individuell_oppgave_1",      "tittel": "Individuell oppgave 1",      "kategori": "P"},
    {"nr":  7, "slug": "at_mentions",                "tittel": "@-mentions",                 "kategori": "I"},
    {"nr":  8, "slug": "individuell_oppgave_at_mentions", "tittel": "Individuell oppgave: @-mentions", "kategori": "P"},
    {"nr":  9, "slug": "plan_mode",                   "tittel": "Plan Mode",                  "kategori": "I"},
    {"nr": 10, "slug": "individuell_oppgave_plan_mode", "tittel": "Individuell oppgave: Plan Mode", "kategori": "P"},
    {"nr": 11, "slug": "kostnader",                  "tittel": "Kostnader",                  "kategori": "F"},
    {"nr": 12, "slug": "agents_md",                  "tittel": "AGENTS.md",                  "kategori": "K"},
    {"nr": 13, "slug": "gruppeoppgave_1",            "tittel": "Gruppeoppgave 1",            "kategori": "G"},
    {"nr": 14, "slug": "gruppeoppgave_1_resultater", "tittel": "Resultater Gruppeoppgave 1", "kategori": "G"},
    {"nr": 15, "slug": "tilgjengelige_modeller",     "tittel": "Tilgjengelige modeller",     "kategori": "K"},
    {"nr": 16, "slug": "individuell_oppgave_modellvalg", "tittel": "Individuell oppgave: Modellvalg", "kategori": "P"},
    {"nr": 17, "slug": "skills_md",                  "tittel": "skills.md",                  "kategori": "K"},
    {"nr": 18, "slug": "demo_bundled_skill",         "tittel": "Demo: Bundled skill",        "kategori": "I"},
    {"nr": 19, "slug": "individuell_oppgave_bundled_skill", "tittel": "Individuell oppgave: Bundled skill", "kategori": "P"},
    {"nr": 20, "slug": "gruppeoppgave_2",            "tittel": "Gruppeoppgave 2",            "kategori": "G"},
    {"nr": 21, "slug": "memory_md",                  "tittel": "memory.md",                  "kategori": "K"},
    {"nr": 22, "slug": "gruppeoppgave_3",            "tittel": "Gruppeoppgave 3",            "kategori": "G"},
    {"nr": 23, "slug": "gruppeoppgave_3_resultater", "tittel": "Resultater Gruppeoppgave 3", "kategori": "G"},
    {"nr": 24, "slug": "context_engineering",        "tittel": "Context engineering",        "kategori": "K"},
    {"nr": 25, "slug": "individuell_oppgave_kohort", "tittel": "Individuell oppgave: Kohortanalyse", "kategori": "P"},
    {"nr": 26, "slug": "individuell_oppgave_konkurrent", "tittel": "Gruppeoppgave: Konkurrent-signaler", "kategori": "G"},
    {"nr": 27, "slug": "avslutning",                 "tittel": "Avslutning",                 "kategori": "F"},
]

KATEGORI_NAVN = {
    "I": "Innføring",
    "K": "Konfigurasjon",
    "P": "Praksis",
    "G": "Gruppe",
    "F": "Fordypning",
}

KATEGORI_FARGE = {
    "I": "#1F6FC4",  # Azur    (Innføring)
    "K": "#6B5BD2",  # Violett (Konfigurasjon)
    "P": "#1E9E6A",  # Grønn   (Praksis)
    "G": "#E08A3C",  # Oransje (Gruppe)
    "F": "#8A93A6",  # Grå     (Fordypning)
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
# `modules` lister `page_id()`-strenger, ikke nr - så stabil over om-
# nummerering av modul-listen.
SECTIONS = [
    {
        "id": "introduksjon",
        "label": "Introduksjon",
        "modules": [
            "m01_evolusjon",
            "m02_cortex_code",
            "m03_cortex_interaction",
            "m04_arkitektur",
        ],
    },
    {
        "id": "komme_i_gang",
        "label": "Komme i gang",
        "modules": [
            "m05_demo_1",
            "m06_individuell_oppgave_1",
        ],
    },
    {
        "id": "at_mentions",
        "label": "@-mentions",
        "modules": [
            "m07_at_mentions",
            "m08_individuell_oppgave_at_mentions",
        ],
    },
    {
        "id": "plan_mode",
        "label": "Plan Mode",
        "modules": [
            "m09_plan_mode",
            "m10_individuell_oppgave_plan_mode",
        ],
    },
    {
        "id": "kostnader",
        "label": "Kostnader",
        "modules": [
            "m11_kostnader",
        ],
    },
    {
        "id": "agents_md",
        "label": "AGENTS.md",
        "modules": [
            "m12_agents_md",
            "m13_gruppeoppgave_1",
            "m14_gruppeoppgave_1_resultater",
        ],
    },
    {
        "id": "modellvalg",
        "label": "Modellvalg",
        "modules": [
            "m15_tilgjengelige_modeller",
            "m16_individuell_oppgave_modellvalg",
        ],
    },
    {
        "id": "skills_md",
        "label": "skills.md",
        "modules": [
            "m17_skills_md",
            "m18_demo_bundled_skill",
            "m19_individuell_oppgave_bundled_skill",
            "m20_gruppeoppgave_2",
        ],
    },
    {
        "id": "memory_md",
        "label": "memory.md",
        "modules": [
            "m21_memory_md",
            "m22_gruppeoppgave_3",
            "m23_gruppeoppgave_3_resultater",
        ],
    },
    {
        "id": "context_engineering",
        "label": "Context engineering",
        "modules": [
            "m24_context_engineering",
        ],
    },
    {
        "id": "kurs_data",
        "label": "Anvendt praksis: KURS-data",
        "modules": [
            "m25_individuell_oppgave_kohort",
            "m26_individuell_oppgave_konkurrent",
        ],
    },
    {
        "id": "avslutning",
        "label": "Avslutning",
        "modules": [
            "m27_avslutning",
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
