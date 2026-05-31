<!-- De tre kjøremodusene. Splittes på "## " og rendres som tre kort. Tittelen
     som inneholder "Plan Mode" framheves automatisk i app_logic. -->

## Interaktiv
**Standard**

Foreslår endringer og ber om bekreftelse før den utfører operasjoner som kan ha stor påvirkning.

**Bruksområde** — daglig arbeid der du ønsker å se og godkjenne hvert steg.

**Aktivering** — standard, påskrudd som utgangspunkt.

## Plan Mode
**Read-only · planlegg først**

Holder seg read-only mens den tenker, og returnerer deretter en strukturert flertrinnsplan. Venter på godkjenning før den utfører noe.

**Bruksområde** — flerstegs- eller høyere risiko-oppgaver, som å opprette eller oppdatere kjernetabeller.

**Aktivering** — trykk `Ctrl + P` eller skriv `/plan`.

## Automatisert
**Betrodde miljøer**

Kjører en avtalt arbeidsflyt fra start til slutt med færre bekreftelser, når du er trygg på mønsteret.

**Bruksområde** — betrodde, ikke-produksjons eller strengt kontrollerte miljøer der arbeidsflyten er validert.

**Aktivering** — `Shift + Tab` for en mer automatisert modus godkjent av teamet.
