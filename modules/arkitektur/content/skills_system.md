**Hva er Skills-systemet?**

Skills-systemet er en utvidelsesmekanisme som gir Cortex Code **spesialisert
domenekunnskap** utover det generelle system-promptet.

**To typer skills:**

**1. Server-side skills (`server_skill`)**
- Forhåndsbygde av Snowflake
- Dekker spesifikke domener: kostnadsanalyse, datastyring, maskinlæring,
  dbt, Streamlit, Iceberg, osv.
- Lastes inn _on-demand_ når en oppgave matcher domenet
- Utvider agentens instruksjoner med detaljerte arbeidsflyter

**2. Client-side skills (`.snowflake/cortex/skills/`)**
- Brukerdefinerte
- En mappe med en `SKILL.md`-fil som inneholder instruksjoner
- Kan inkludere støttescripts
- Lar brukere lage egne spesialiserte arbeidsflyter

**Slik fungerer det:**

1. Bruker stiller et spørsmål
2. Agenten gjenkjenner at det matcher et skill-domene
3. Skill-en lastes inn → agenten får nye, detaljerte instruksjoner
4. Agenten følger disse instruksjonene for å løse oppgaven

Skills er **"plug-in ekspertise"** - de gjør agenten til en spesialist på
et område uten at all den kunnskapen må ligge i system-promptet hele tiden.
