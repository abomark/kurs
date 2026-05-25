"""Wrapper for modul 1: Cortex Code.

Tynn pass-through til `modules.cortex_code.app_logic.main` slik at
all eksisterende logikk (content/*.md, callouts, db-koblinger) bevares.
"""
from modules.cortex_code.app_logic import main as render

__all__ = ["render"]
