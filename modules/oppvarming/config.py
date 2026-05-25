"""Konfigurasjon for Oppvarming-modulen (Bli kjent).

PRD §FR-3.1 (variant for Likert-skala): fem påstander som hver vurderes
på en 1–5-skala (1 = uenig, 5 = enig). Alle besvares samtidig i én form
og lagres som heltall i `kurs.oppvarming_responses.answer_value`.

Brukes til å kalibrere kursleders forventninger til deltakergruppen.
"""

# Stabile ID-er 1–10. Endre ordlyd, men ikke flytt rundt på ID-ene
# (de er lagret i databasen for tidligere svar).
# Q1–5: generell teknisk bakgrunn. Q6–10: Cortex Code-modenhet.
STATEMENTS = {
    1: "Jeg bruker Snowflake regelmessig",
    2: "Jeg er erfaren med AI-assistenter i koding (Copilot, Claude, Cursor, ChatGPT, etc.)",
    3: "Jeg er komfortabel i terminalen / med CLI",
    4: "Jeg har solid programmeringsbakgrunn utover SQL",
    5: "Jeg er positivt innstilt til AI-agenter som tar avgjørelser på egen hånd",
    6: "Jeg bruker Cortex Code regelmessig",
    7: "Jeg kjenner anbefalt praksis for bruk av Cortex Code",
    8: "Jeg forstår sentrale begreper som agent, modell og prompt",
    9: "Jeg forstår hva som driver kostnader ved bruk av Cortex Code",
    10: "Jeg vet hvordan jeg optimaliserer bruken av Cortex Code",
}

# Skala-anker. 1 = lav enighet, 5 = høy enighet.
SCALE_MIN = 1
SCALE_MAX = 5
SCALE_LABELS = {
    1: "1 — uenig",
    5: "5 — enig",
}

# PRD §FR-3.4 / §NFR-4.1: skjul resultater til minst N svar er inne.
# Oppvarming bruker 1 (ikke 3) fordi dataene ikke er sensitive på samme måte
# som ord-svar i gruppeoppgaver, og fordi kursleder vil se trender umiddelbart.
MIN_RESPONSES_BEFORE_REVEAL = 1

# PRD §NFR-4.3: auto-refresh-intervall for resultat-siden (ms).
REFRESH_INTERVAL_MS = 10_000
