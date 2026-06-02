Forskjellen er viktig fordi:

- **Inferens kan feile** - særlig på lange katalog-stier eller når
  navnet er tvetydig. Du får raskere og mer presis hjelp med eksplisitt
  binding.
- **Sample-statistikk** hjelper agenten å foreslå realistiske filter
  og join-prediketer.
- **Masking policies og PII-tags** kommer kun automatisk med
  `@`-mention. Uten tagger agenten ikke vet at en kolonne er sensitiv.

Tommelfingerregel: hvis du _vet_ hvilken ressurs du sikter til,
bruk `@`.
