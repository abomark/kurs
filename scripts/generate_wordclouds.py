#!/usr/bin/env python3
"""Generate word clouds for gruppeoppgave_1 question 1 responses."""

from wordcloud import WordCloud
import matplotlib.pyplot as plt
from pathlib import Path

responses = [
    """Språkkonvensjoner som dere allerede har norsk i markdown engelsk i kode
    Kodestil og formatering font farger navnekonvensjoner
    Bygge test lint kommandoer dbt build dbt test
    Prosjektstruktur og filorganisering
    Guardrails og regler for AI oppførsel
    Domenespesifikke termer glossar referanser
    Hvilke roller warehouses som brukes""",

    """formattering preferanser kommunikasjon preferanser bullet points
    samhandlings retningslinjer utfordre meg når jeg tar feil""",

    """farger preferanser for språk instruks om å være skeptisk til det jeg sier
    Fortell meg hvis jeg er dum preferanser for navngivning av tabeller og kolonner
    Kort og godt ting du ellers ville gjenta ofte""",

    """Farger stil språk""",

    """Hvordan agenten skal gi svar korte og konsise svar med mindre noe annet er beskrevet
    At den skal kommentere kodelinjene
    Foretrukne datakilder skjema og exporttabeller med mindre annet er beskrevet
    Om mulig kvalitetssjekk av data men det må gjøres generelt""",

    """Kontekst""",

    """Kvalitetskrav"""
]

labels = [
    "Resp 1: Språk, kode, byggkommandoer",
    "Resp 2: Kommunikasjon og samhandling",
    "Resp 3: Design og navngivning",
    "Resp 4: Stil (kort)",
    "Resp 5: Agentens oppførsel",
    "Resp 6: Kontekst",
    "Resp 7: Kvalitet"
]

output_dir = Path("scripts/wordclouds")
output_dir.mkdir(exist_ok=True)

# Norwegian stopwords (add more as needed)
stopwords = {
    "og", "som", "for", "at", "med", "den", "de", "jeg", "du", "han", "hun",
    "det", "en", "et", "er", "var", "ikke", "ville", "skal", "kan", "om",
    "på", "til", "fra", "av", "i", "eller", "ellers", "mer", "det", "hvis",
    "men", "må", "gjøres", "annet", "beskrevet", "mindre"
}

for idx, (response, label) in enumerate(zip(responses, labels), 1):
    print(f"Genererer: {label}")

    # Generate word cloud
    wordcloud = WordCloud(
        width=800,
        height=600,
        background_color='white',
        stopwords=stopwords,
        collocations=False,
        prefer_horizontal=0.7,
        relative_scaling=0.5,
        min_font_size=10,
        colormap='viridis',
        font_path='/System/Library/Fonts/Arial.ttf'  # macOS Arial
    ).generate(response)

    # Create figure
    fig, ax = plt.subplots(figsize=(10, 7))
    ax.imshow(wordcloud, interpolation='bilinear')
    ax.axis('off')
    plt.title(label, fontsize=14, fontweight='bold', pad=20)
    plt.tight_layout()

    # Save
    filename = f"wordcloud_{idx}.png"
    filepath = output_dir / filename
    plt.savefig(filepath, dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()

    print(f"  → Lagret: {filepath}")

print(f"\n✓ Alle ordskyer lagret i {output_dir}/")
