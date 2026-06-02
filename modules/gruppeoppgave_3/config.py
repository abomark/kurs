"""Sentral konfigurasjon for Gruppeoppgave 3 - memory.md.

Implementerer PRD §FR-3.1 (spørsmål) og §FR-3.5 (stopwords/ikke-svar).
"""

# Fire spørsmål: Q1/Q2 fritekst (hva skal/skal-ikke lagres), Q3 valg
# (bank-spesifikk risiko), Q4 fritekst (konkret eksempel fra eget arbeid).
QUESTIONS = {
    1: {
        "type": "text",
        "text": "Hva BØR lagres i persistent memory?",
        "placeholder": "Tenk på info som er stabil og verdt å huske på tvers av sesjoner...",
    },
    2: {
        "type": "text",
        "text": "Hva bør IKKE lagres i memory?",
        "placeholder": "Tenk på det som er for sensitivt, for kortvarig, eller bedre andre steder...",
    },
    3: {
        "type": "choice",
        "text": "Hvilken risiko er størst når en bank-analytiker slår på persistent memory?",
        "options": [
            "PII-lekkasje til lokal disk",
            "Modell-bias over tid",
            "Compliance-godkjenning mangler",
            "Kostnader",
        ],
    },
    4: {
        "type": "text",
        "text": "Skriv en linje du faktisk ville lagt i din egen memory etter denne uken.",
        "placeholder": "Konkret - ikke abstrakt prinsipp.",
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

# Norske + engelske stopwords. Bevisst kort liste - vi vil heller beholde
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
