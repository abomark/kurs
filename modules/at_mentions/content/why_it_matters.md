For bank-analytikere er forskjellen særlig viktig fordi:

- **Masking policies og PII-tags** kommer kun automatisk med
  `@`-mention. Uten tagger agenten ikke vet at en kolonne er sensitiv.
- **Inferens kan feile** — særlig på lange katalog-stier eller når
  navnet er tvetydig. Du får raskere og mer presis hjelp med eksplisitt
  binding.
- **Sample-statistikk** hjelper agenten å foreslå realistiske filter
  og join-prediketer.

Tommelfingerregel: hvis du _vet_ hvilken ressurs du sikter til,
bruk `@`. Det er gratis og forhindrer at agenten må gjette.
