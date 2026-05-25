"""Sentral konfigurasjon for AGENTS.md-modulen.

Implementerer PRD §FR-3.1 (spørsmål) og §FR-3.5 (stopwords/ikke-svar).
"""

# PRD §FR-3.1: fire spørsmål, Q1/Q2 fritekst, Q3/Q4 valg med tre alternativer.
QUESTIONS = {
    1: {
        "type": "text",
        "text": "Hva bør være i AGENTS.md?",
        "placeholder": "F.eks. kodestil, byggekommandoer, eksempler...",
    },
    2: {
        "type": "text",
        "text": "Hva bør IKKE være i AGENTS.md?",
        "placeholder": "F.eks. hemmeligheter, lange historikker, ...",
    },
    3: {
        "type": "choice",
        "text": "Bør AGENTS.md være personlig eller felles?",
        "options": ["Personlig", "Felles", "Begge deler"],
    },
    4: {
        "type": "choice",
        "text": "Vil AGENTS.md øke eller redusere kostnader?",
        "options": ["Øker", "Reduserer", "Ingen endring"],
    },
}

# PRD §FR-3.4 / §NFR-4.1: skjul resultater til minst N svar er inne.
MIN_RESPONSES_BEFORE_REVEAL = 3

# PRD §NFR-4.3: auto-refresh-intervall for resultat-siden (ms).
REFRESH_INTERVAL_MS = 10_000

# Tokens som filtreres bort fra ordskyen.
NON_ANSWERS = {
    "",
    "-",
    "n/a",
    "na",
    "vet ikke",
    "ingen",
    "ingenting",
    "vet ei",
    "?",
    "??",
    "???",
}

# Norske + engelske stopwords. Bevisst kort liste — vi vil heller beholde
# litt støy enn å filtrere bort meningsbærende ord.
STOPWORDS = {
    # Norsk
    "og", "i", "på", "av", "for", "til", "med", "som", "er", "et", "en",
    "den", "det", "de", "har", "ikke", "ha", "være", "bli", "blir",
    "skal", "vil", "kan", "må", "bør", "om", "at", "så", "men", "også",
    "eller", "hvis", "når", "der", "her", "du", "jeg", "vi", "han", "hun",
    "min", "din", "sin", "vår", "deres", "fra", "etter", "før", "noe",
    "noen", "alle", "alt", "annet", "andre", "samme", "hele", "veldig",
    "bare", "kun", "lite", "mye", "ganske", "litt", "mer", "mest",
    "f.eks", "feks", "eks", "osv", "etc",
    # Engelsk
    "the", "and", "or", "but", "if", "of", "to", "in", "on", "at", "for",
    "with", "by", "as", "is", "are", "was", "were", "be", "been", "being",
    "have", "has", "had", "do", "does", "did", "will", "would", "should",
    "could", "may", "might", "must", "a", "an", "this", "that", "these",
    "those", "it", "its", "from", "about",
}
