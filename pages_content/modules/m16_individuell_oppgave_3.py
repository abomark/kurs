"""Wrapper for modul 11: Individuell oppgave 3.

Tynn pass-through til `modules.individuell_oppgave_3.app_logic.main` slik at
all eksisterende logikk (content/*.md, callouts, db-koblinger) bevares.
"""
from modules.individuell_oppgave_3.app_logic import main as render

__all__ = ["render"]
