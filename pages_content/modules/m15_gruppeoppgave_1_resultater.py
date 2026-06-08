"""Wrapper for modul 10: Resultater Gruppeoppgave 1.

Tynn pass-through til `modules.gruppeoppgave_1_resultater.app_logic.main` slik at
all eksisterende logikk (content/*.md, callouts, db-koblinger) bevares.
"""
from modules.gruppeoppgave_1_resultater.app_logic import main as render

__all__ = ["render"]
