"""Ordreduksjon for Gruppeoppgave 3 (memory.md).

Implementerer PRD §FR-3.5: pipeline lowercase → strip → fjern tegnsetting
→ splitt → drop stopwords/korte/non-answers. Duplikater beholdes (frekvens
styrer størrelse i ordskyen, jf. §FR-3.4).
"""

from __future__ import annotations

import re

from .config import NON_ANSWERS, STOPWORDS

_PUNCT_RE = re.compile(r"[^\w\sæøåÆØÅ-]", flags=re.UNICODE)
_SPLIT_RE = re.compile(r"[\s,;/]+")


def reduce_answer(raw: str) -> list[str]:
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
    out: list[str] = []
    for ans in answers:
        out.extend(reduce_answer(ans))
    return out
