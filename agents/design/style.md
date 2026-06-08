# design/style.md — Visuell stil

**Lesing:** Før du endrer layout, farger, eller brukergrensesnitt.

---

**Single source of truth:** [DESIGN_GUIDE.md](../../DESIGN_GUIDE.md)

Du trenger **ikke** å lese hele DESIGN_GUIDE. Les heller bare relevante seksjoner:

- §2 — fargepalett (Bankbrief: Marine `#0A2C72`, Azur `#1F6FC4`, Fersken `#F8E6D5`)
- §1.7 — **ingen emojis**, men SVG-ikoner ok via `svg_icon()` helper
- §1.8 — **aldri en-dash eller em-dash** (`–` eller `—`), bruk bare `-`
- §1.10 — **aldri `é`/`É`**, skriv `e`/`E` (f.eks. "en" ikke "én")
- §5 — callout-typer: `info`, `tip`, `warn`, `subtle` (og hvordan de ser ut)
- §6 — tema i `.streamlit/config.toml`

## Når du legger til/endrer en modul

Gå gjennom DESIGN_GUIDE §10 — det er sjekklisten.

## Oppdatering

Når du endrer noe visuelt: oppdater også [`CHANGELOG.md`](../../CHANGELOG.md) med hva som endret seg.
