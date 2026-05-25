"""Wrapper for Bli kjent (Oppvarming, modul 0).

Tynn pass-through til `modules.oppvarming.app_logic.main`.
"""
from modules.oppvarming.app_logic import main as render

__all__ = ["render"]
