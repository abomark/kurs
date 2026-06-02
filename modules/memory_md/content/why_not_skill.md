En **skill** er en invokerbar atferd - agenten _kaller_ den når en oppgave
matcher (f.eks. "kjør datakvalitets-sjekk"). Skill-filer er statiske
oppskrifter som lastes inn ved behov.

**Memory er passiv kontekst, ikke aktiv atferd.** Den lastes inn ved
sesjon-start og hjelper agenten forstå hvem _du_ er - preferanser,
historikk, beslutninger fra forrige uke.

Skiller du dem ikke, blir verktøykassen rotete: en "husk preferanser"-skill
blander abstraksjonsnivåer (data + atferd), og du må kalle den manuelt
hver sesjon. Memory løser nettopp dette - agenten henter selv inn det
som er relevant.
