#!/usr/bin/env python3
"""Export gruppeoppgave_1 responses from Supabase.

Usage:
    python scripts/export_gruppeoppgave_1_data.py

Requires:
    - SUPABASE_URL and SUPABASE_SERVICE_KEY in .streamlit/secrets.toml
"""

import json
import sys
from pathlib import Path

# Add repo root to path so we can import modules
repo_root = Path(__file__).parent.parent
sys.path.insert(0, str(repo_root))

from modules.gruppeoppgave_1.db import fetch_all_responses, fetch_text_answers, fetch_choice_counts


def load_secrets():
    """Load secrets from .streamlit/secrets.toml"""
    try:
        import tomllib
    except ImportError:
        import tomli as tomllib

    secrets_path = repo_root / ".streamlit" / "secrets.toml"
    if not secrets_path.exists():
        raise FileNotFoundError(f"Secrets file not found: {secrets_path}")

    with open(secrets_path, "rb") as f:
        return tomllib.load(f)


def setup_secrets():
    """Set environment variables from secrets for Supabase client."""
    import os
    secrets = load_secrets()
    os.environ["SUPABASE_URL"] = secrets.get("SUPABASE_URL", "")
    os.environ["SUPABASE_SERVICE_KEY"] = secrets.get("SUPABASE_SERVICE_KEY", "")


def export_all_responses(output_file: str = "gruppeoppgave_1_responses.json"):
    """Export all responses to JSON."""
    print(f"Fetching all responses...")
    data = fetch_all_responses()

    output_path = repo_root / output_file
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2, default=str)

    print(f"✓ Exported {len(data)} responses to {output_path}")
    return data


def export_to_csv(output_file: str = "gruppeoppgave_1_responses.csv"):
    """Export all responses to CSV."""
    import csv

    print(f"Fetching all responses...")
    data = fetch_all_responses()

    if not data:
        print("No responses found.")
        return

    output_path = repo_root / output_file
    keys = data[0].keys()

    with open(output_path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        writer.writerows(data)

    print(f"✓ Exported {len(data)} responses to {output_path}")


def get_question_responses(question_id: int):
    """Get and print all responses for a specific question."""
    print(f"Fetching responses for question {question_id}...")
    answers = fetch_text_answers(question_id=question_id)

    print(f"\n{'='*60}")
    print(f"Question {question_id}: {len(answers)} responses")
    print(f"{'='*60}\n")

    for i, answer in enumerate(answers, 1):
        print(f"[{i}] {answer}\n")


def print_summary():
    """Print a summary of responses."""
    print("Fetching all responses...")
    data = fetch_all_responses()

    print(f"\n{'='*60}")
    print(f"Total responses: {len(data)}")
    print(f"{'='*60}\n")

    # Group by question_id
    by_question = {}
    for row in data:
        qid = row.get("question_id")
        if qid not in by_question:
            by_question[qid] = []
        by_question[qid].append(row)

    for qid in sorted(by_question.keys()):
        responses = by_question[qid]
        print(f"Question {qid}: {len(responses)} responses")

        # Show first few responses
        for i, resp in enumerate(responses[:3], 1):
            answer_text = resp.get("answer_text")
            answer_choice = resp.get("answer_choice")
            answer = answer_text or answer_choice or "(empty)"
            print(f"  [{i}] {answer[:80]}")

        if len(responses) > 3:
            print(f"  ... and {len(responses) - 3} more")
        print()


if __name__ == "__main__":
    try:
        setup_secrets()

        # Uncomment whichever you want to run:
        # get_question_responses(question_id=1)
        print_summary()
        # export_all_responses()
        # export_to_csv()

    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
