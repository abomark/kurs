"""Wrapper for modul 3: Cortex Code i Snowsight.

Tynn pass-through til `modules.cortex_in_snowsight.app_logic.main` slik at
all eksisterende logikk (content/*.md, callouts, db-koblinger) bevares.
"""
from modules.cortex_in_snowsight.app_logic import main as render

__all__ = ["render"]
