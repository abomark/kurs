"""Claudes egne svar på spørsmål 1 og 2, tilpasset bank-/analysekontekst.

Implementerer PRD §FR-3.6: referansesvar for "Hva glemte vi?"-diff.
Hvert listeelement behandles som ett selvstendig svar (likt deltakersvar)
og gjennomgår samme reducer-pipeline (§FR-3.5).
"""

# Kontekst: analytikere i en bank som jobber med analyse, maskinlæring,
# Streamlit-applikasjoner og notebooks.

CLAUDE_ANSWERS_Q1 = [
    "Datakilder og hvilke tabeller, views og warehouse som brukes",
    "Datasensitivitet og klassifisering av PII og GDPR-hensyn",
    "Kodestil: PEP8, ruff, black, type hints",
    "Foretrukne biblioteker: pandas, polars, scikit-learn, plotly",
    "Notebook-konvensjoner: struktur, nbstripout, kjør-rekkefølge",
    "Streamlit-mønstre: st.cache_data, secrets, layout, sidemenyer",
    "Datavalidering med pydantic eller pandera",
    "Reproduserbarhet: random seeds, lockfile, miljø, requirements",
    "Hvor secrets hentes fra: Vault, environment variables, ikke i kode",
    "Test-konvensjoner: pytest, fixtures, mocking, kjørekommandoer",
    "Domeneord og forretningsbegrep: KPI-definisjoner og regulatoriske termer",
    "Modellevalueringsmetrikker: AUC, precision, recall, calibration",
    "Datakvalitet og valideringsregler",
    "Hvordan kjøre lokalt vs produksjon",
    "Bygge- og deploykommandoer",
    "Eksempler på god kode og prosjektstruktur",
    "Linter- og formatteringsoppsett",
    "Output-formater: parquet, csv, og hvor de lagres",
    "Logging-konvensjoner og log-nivåer",
    "Branch-strategi, commit-meldinger og PR-prosess",
    "Regulatoriske krav som påvirker koden",
    "Dokumentasjonsstandard for docstrings",
    "Python-versjon og avhengighetsstyring",
    "Hvilke modeller som er godkjent for produksjon",
    "Modellovervåking og driftsoppfølging",
    "Feilhåndtering og retry-strategier mot eksterne API",
    "Cache-strategi og invalidering",
    "Internasjonalisering og tegnsett",
    "Hvilke verktøy som brukes for orchestration: Airflow, Prefect, Dagster",
    "Kjente fallgruver og gotchas i prosjektet",
]

CLAUDE_ANSWERS_Q2 = [
    "Hemmeligheter, API-nøkler, passord og connection strings",
    "PII eller kundedata",
    "Eksempelrader fra produksjonsdatabase",
    "Lang endringshistorikk og changelog",
    "Møtenotater og beslutningsprotokoller",
    "Detaljert domenedokumentasjon - lenk heller til Confluence",
    "Personlige preferanser uten begrunnelse",
    "Modellvekter og hyperparametere som endres ofte",
    "Daglige TODOs og pågående oppgaver",
    "Generelle Python-tutorials og opplæringsmateriale",
    "Lange eksempler på modelloutput",
    "Reguleringstekst i sin helhet",
    "Interne telefonnumre og adressekataloger",
    "Pull request templates - bruk .github/-mappa",
    "Kommentarer rettet til en spesifikk kollega",
    "Spekulasjoner om fremtidig arkitektur",
    "Detaljerte SQL-spørringer som ofte endres",
    "Infrastrukturdetaljer og backup-strategi",
    "Brukernavn og personidentifikatorer",
    "Eksperimentelle modeller som ikke er i produksjon",
    "Konfigurasjon som hører hjemme i config-filer",
    "Stor mengde rådata eller eksempel-datasett",
    "Lisensavtaler og juridisk tekst",
    "Dårlig kode eller anti-mønstre uten kontekst",
    "Versjonsspesifikke detaljer som blir utdaterte raskt",
    "Datavekter, lookup-tabeller og store ordlister",
    "Marketing-tekst og produktbeskrivelser",
]
