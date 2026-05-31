Dette ser ut som en repeterbar arbeidsflyt jeg vil ha for mange PRD-er.
Bruk [Skill Attached: skill-development] til å bygge en project skill som
tar PRD-lignende filer og gjør dem om til en plan for å legge dem inn i en
mål-Dynamic Table (her: SILVER_AP_INVOICES).

Definer:
  • Når skill-en skal brukes
  • Hvilke inputs den forventer (f.eks. prd_path og target_dynamic_table)
  • De eksakte outputene den alltid skal returnere
  • Beste praksis for å løfte fram assumptions og åpne spørsmål i stedet for å gjette
  • Et eksempel på bruk for en AP-invoices pipeline-oppdatering

Krav:
  • Gjør den til en project skill
  • Legg den under .cortex/skills/ i dette repoet
  • Start med å støtte XLSX-filer
