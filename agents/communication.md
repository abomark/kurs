# communication.md — Hvordan svare

**Lesing:** Før du svarer på noe eller forklarer noe til eier.

---

## Tone og stil

- **Kort og konsist** — en setning er ofte nok. Ikke forklar selv om du kunne.
- **Direkte svar først** — ikke innledning. Deretter detaljer hvis relevant.
- **Ikke gjenta det du nettopp gjorde** — eier kan lese difsen. "Fikset X" er nok; ikke "Jeg endret linje 45 fra `foo` til `bar`".

## Språk

- **Norsk** i hele samtalen (innlegg, kodekommentarer, docstrings)
- **Engelsk** kun i: variabelnavn, funksjoner, klassenavn, import-statements

## Når du er usikker

- Spør før du gjør stor endring (destructive git, breaking API, etc.)
- Hvis du ser drift mellom kode og PRD: si fra heller enn stille-rette

## Hva du IKKE skal gjøre

- Ikke skriv snakkepunkter, eksempler eller innhold på moduler uten eksplisitt forespørsel (jf. CLAUDE.md)
- Ikke legg til features som ikke er i PRD
- Ikke skriv multi-linjes docstrings eller lang kommentarer — en kort linje er nok
