# Tema-patch — Designsystem v1 «Bankbrief» (lyst)

Dette er **drop-in-erstatninger** for kurs-appen, reskinnet fra det mørke
Snowflake-temaet til det lyse marine + fersken-uttrykket avledet fra
PowerPoint-malen. Se `Designsystem.html` for full spesifikasjon.

## Slik tar du det i bruk
Kopier hver fil under `theme-light/` til **samme relative sti** i `kurs/`:

| Fil | Hva som endret seg |
|-----|--------------------|
| `.streamlit/config.toml` | `base="light"`, marine primær, hvit canvas, azur lenker |
| `modules/shared/ui.py` | Fargekonstantene (`COLOR_*`, `TEXT_*`, `BORDER`) + callout-paletten. Alle komponenter (`callout`, `metric_card`, `card`, `numbered_steps`, `crumb`, `next_module_cta`) arver disse — ingen annen endring nødvendig. |
| `components/sidebar.py` | `SIDEBAR_CSS` reskinnet til lyst; aktiv modul får azur tint + strek |
| `pages_content/forside.py` | `_CARD_CSS` → hvite kort med azur venstrestrek + subtil skygge |
| `data/moduler.py` | `KATEGORI_FARGE` → mettede kategorifarger som leser på hvitt |
| `modules/oppvarming/app_logic.py` | Likert-grid + skala-pille reskinnet (eneste innholdsside med hardkodet mørk CSS) |

> Navnene på fargekonstantene (`COLOR_VANN`, `COLOR_FROST`, `COLOR_SAND` …)
> er **beholdt** for bakoverkompatibilitet — kun verdiene er endret. Ingen
> import-stier eller funksjonssignaturer er rørt.

## Token-mapping (mørk → lys)
| Konstant | Før | Etter | Rolle |
|----------|-----|-------|-------|
| `COLOR_VANN` | `#005AA4` | `#0A2C72` | Marine — primær, ikon-disker, knapper |
| `COLOR_FJELL` | `#002776` | `#071E50` | Marine dyp — hover |
| `COLOR_FROST` | `#7EB5D2` | `#1F6FC4` | Azur — lenker, aksent |
| `COLOR_SAND` | `#F8E9DD` | `#F8E6D5` | Fersken — signaturflate |
| `COLOR_CANVAS` | `#0A0F1F` | `#FFFFFF` | Canvas |
| `COLOR_SURFACE_1` | `#0F1729` | `#FFFFFF` | Kort / sidebar |
| `COLOR_SURFACE_2` | `#131C33` | `#F7F8FB` | Dempet flate |
| `COLOR_SURFACE_3` | `#1A2542` | `#EAF1FB` | Azur tint |
| `TEXT_PRIMARY` | `#F4F6FB` | `#16203A` | Blekk |
| `TEXT_SECONDARY` | `#A8B3C7` | `#3B4256` | Brødtekst |
| `TEXT_TERTIARY` | `#6B7691` | `#6B7280` | Dempet |
| `BORDER` | `rgba(126,181,210,.10)` | `#E3E8F1` | Kant |

## Kategorifarger
| Kode | Kategori | Før | Etter |
|------|----------|-----|-------|
| I | Innføring | `#7EB5D2` | `#1F6FC4` |
| K | Konfigurasjon | `#B197FC` | `#6B5BD2` |
| P | Praksis | `#66D9A8` | `#1E9E6A` |
| G | Gruppe | `#FFAD80` | `#E08A3C` |
| F | Fordypning | `#94A3B8` | `#8A93A6` |

## Ikke endret (verifisert)
Øvrige innholdssider (`bli_kjent`, `resultater`, `admin` og alle `mNN_*`
modul-wrappere) bruker `st`-native + delte helpers fra `ui.py`, så de
arver det lyse temaet automatisk uten egne endringer.
