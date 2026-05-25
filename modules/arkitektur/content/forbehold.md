Beskrivelsen over er korrekt for det **observerbare agent-laget** — det
agenten selv kan se av egne instruksjoner og verktøy.

**Det dekker ikke:**

- Den underliggende infrastrukturen (hvordan Snowflake orkestrerer
  API-kall til Claude, håndterer autentisering, session-styring)
- Eventuelle mellomvare-lag mellom Snowsight-frontend og LLM-en
  (f.eks. prompt-injeksjon av kontekst, routing-logikk)

Med andre ord: arkitekturen rundt Cortex Code (Snowflakes plattform-side)
ligger bakenfor det vi kan utlede fra agenten selv.
