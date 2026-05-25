|  | `AGENTS.md` | `memory/` |
|---|---|---|
| **Hvor** | Prosjektrot | `~/.snowflake/cortex/memory/` |
| **Scope** | Per prosjekt | Per bruker (global) |
| **Skrives av** | Deg, manuelt | Agenten selv |
| **Lever** | Versjonskontrollert med koden | Lokalt på din maskin |
| **Egnet for** | Prosjektkonvensjoner, naming, tabell-katalog | Dine preferanser, gjenbrukte snippets, lærdom på tvers av oppdrag |

**Tommelfingerregel:** Hvis hele teamet bør se det → `AGENTS.md`. Hvis det er
ditt eget arbeidsverktøy → `memory`.

**Skal AGENTS.md referere til memory?** Som regel nei. AGENTS.md er felles
for teamet; memory er privat. Å referere til private filer i en delt
config bryter scope-skillet.
