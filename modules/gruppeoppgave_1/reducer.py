"""MVP-ordreduksjon i ren Python.

Implementerer PRD §FR-3.5: pipeline lowercase → strip → fjern tegnsetting
→ splitt → drop stopwords/korte/non-answers. Duplikater beholdes (frekvens
styrer størrelse i ordskyen, jf. §FR-3.4).

Senere v2: byttes til `reducer_ai.py` med samme signatur
`reduce_answers(list[str]) -> list[str]`.
"""

from __future__ import annotations

import re

from .config import NON_ANSWERS, STOPWORDS

# Behold bokstaver (inkl. norske), tall, mellomrom og bindestrek.
# Alt annet erstattes med mellomrom slik at sammensatte tegn ikke
# kleber seg til ordet.
_PUNCT_RE = re.compile(r"[^\w\sæøåÆØÅ-]", flags=re.UNICODE)
_SPLIT_RE = re.compile(r"[\s,;/]+")


def reduce_answer(raw: str) -> list[str]:
    """Reduser ett enkelt svar til en liste med tokens."""
    if raw is None:
        return []
    text = raw.strip().lower()
    if text in NON_ANSWERS:
        return []

    text = _PUNCT_RE.sub(" ", text)
    tokens = _SPLIT_RE.split(text)

    result = []
    for tok in tokens:
        tok = tok.strip("-_")
        if len(tok) < 3:
            continue
        if tok in STOPWORDS:
            continue
        if tok in NON_ANSWERS:
            continue
        result.append(tok)
    return result


def reduce_answers(answers: list[str]) -> list[str]:
    """Reduser en liste med svar til en flat token-liste (med duplikater)."""
    out: list[str] = []
    for ans in answers:
        out.extend(reduce_answer(ans))
    return out
