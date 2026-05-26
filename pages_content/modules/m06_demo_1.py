"""Wrapper for modul 4: Første demo.

Tynn pass-through til `modules.demo_1.app_logic.main` slik at
all eksisterende logikk (content/*.md, callouts, db-koblinger) bevares.
"""
from modules.demo_1.app_logic import main as render

__all__ = ["render"]
