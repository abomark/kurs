"""Wrapper for modul 16: Tilgjengelige modeller.

Tynn pass-through til `modules.tilgjengelige_modeller.app_logic.main` slik at
all eksisterende logikk (content/*.md, callouts, db-koblinger) bevares.
"""
from modules.tilgjengelige_modeller.app_logic import main as render

__all__ = ["render"]
