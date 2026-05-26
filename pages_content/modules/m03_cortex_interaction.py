"""Wrapper for modul 2: Snowsight vs CLI.

Tynn pass-through til `modules.cortex_interaction.app_logic.main` slik at
all eksisterende logikk (content/*.md, callouts, db-koblinger) bevares.
"""
from modules.cortex_interaction.app_logic import main as render

__all__ = ["render"]
