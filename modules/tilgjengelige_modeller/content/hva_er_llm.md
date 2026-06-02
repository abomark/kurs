**LLM** står for *Large Language Model* (stor språkmodell).

- Den grunnleggende oppgaven er å forutsi neste «token» (en liten bit av et ord) gitt teksten som kommer før.
- «Large» viser til både antall parametere (milliarder) og datamengden modellen er trent på.
- Opus og Sonnet er LLM-er, laget av Anthropic. Haiku er raskest og minst, Sonnet er balansert, og Opus er den mest kapable.
- Nyanse: modellene er multimodale (de kan også tolke bilder), men i kjernen er de LLM-er.
- LLM-en er modellen som «tenker». En agent som Cortex Code er den modellen pluss verktøy og en loop rundt.
- Det er **tokens** modellen fakturerer for - lengre prompt og flere svar-runder gir flere tokens og dermed høyere kostnad.
- **Kontekstvinduet** er hvor mye modellen har plass til å holde i hodet i en samtale (alt den har lest og skrevet så langt); blir samtalen lang nok, faller det eldste ut av vinduet.
