"""Wrapper for modul 12: Demo 2.

Tynn pass-through til `modules.demo_2.app_logic.main` slik at
all eksisterende logikk (content/*.md, callouts, db-koblinger) bevares.
"""
from modules.demo_2.app_logic import main as render

__all__ = ["render"]
