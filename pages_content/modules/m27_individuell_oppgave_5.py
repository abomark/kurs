"""Wrapper for modul 15: Individuell oppgave 5.

Tynn pass-through til `modules.individuell_oppgave_5.app_logic.main` slik at
all eksisterende logikk (content/*.md, callouts, db-koblinger) bevares.
"""
from modules.individuell_oppgave_5.app_logic import main as render

__all__ = ["render"]
