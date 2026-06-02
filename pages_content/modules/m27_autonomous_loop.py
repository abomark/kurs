"""Wrapper for modul 14: Autonomous loop.

Tynn pass-through til `modules.autonomous_loop.app_logic.main` slik at
all eksisterende logikk (content/*.md, callouts, db-koblinger) bevares.
"""
from modules.autonomous_loop.app_logic import main as render

__all__ = ["render"]
