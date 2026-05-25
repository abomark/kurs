"""Wrapper for modul 5: AGENTS.md.

Tynn pass-through til `modules.agents_md.app_logic.main` slik at
all eksisterende logikk (content/*.md, callouts, db-koblinger) bevares.
"""
from modules.agents_md.app_logic import main as render

__all__ = ["render"]
