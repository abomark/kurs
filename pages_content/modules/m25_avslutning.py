"""Wrapper for modul 24: Avslutning.

Tynn pass-through til `modules.avslutning.app_logic.main` slik at
all eksisterende logikk (content/*.md, callouts, db-koblinger) bevares.
"""
from modules.avslutning.app_logic import main as render

__all__ = ["render"]
