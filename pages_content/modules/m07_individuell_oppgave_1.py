"""Wrapper for modul 6: Individuell oppgave 1.

Tynn pass-through til `modules.individuell_oppgave_1.app_logic.main` slik at
all eksisterende logikk (content/*.md, callouts, db-koblinger) bevares.
"""
from modules.individuell_oppgave_1.app_logic import main as render

__all__ = ["render"]
