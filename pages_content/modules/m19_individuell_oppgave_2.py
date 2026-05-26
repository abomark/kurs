"""Wrapper for modul 8: Individuell oppgave 2.

Tynn pass-through til `modules.individuell_oppgave_2.app_logic.main` slik at
all eksisterende logikk (content/*.md, callouts, db-koblinger) bevares.
"""
from modules.individuell_oppgave_2.app_logic import main as render

__all__ = ["render"]
