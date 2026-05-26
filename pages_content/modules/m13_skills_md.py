"""Wrapper for modul 7: skills.md.

Tynn pass-through til `modules.skills_md.app_logic.main` slik at
all eksisterende logikk (content/*.md, callouts, db-koblinger) bevares.
"""
from modules.skills_md.app_logic import main as render

__all__ = ["render"]
