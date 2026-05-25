"""Deltakerflyt for Gruppeoppgave 3 (workshop om memory.md).

Implementerer PRD §FR-3.1 (spørsmål), §FR-3.2 (innsending, flere svar),
§FR-3.9 (valgfri deltakerkode), §NFR-4.1 (anonymitet, caption om secrets).

Eksponerer `main()` som driver hele deltakerskjermen. Kalt fra
`pages_content/modules/m09_gruppeoppgave_3.py`.
"""

from __future__ import annotations

import streamlit as st

from modules.shared.ui import callout, crumb, load_markdown, next_module_cta_for

from .config import QUESTIONS
from .db import insert_choice_response, insert_text_response


def _participant_gate() -> bool:
    """PRD §FR-3.9: valgfri soft-gate, deltakerkode oppgitt muntlig."""
    expected = st.secrets.get("PARTICIPANT_CODE")
    if not expected:
        return True
    if st.session_state.get("participant_ok"):
        return True

    st.title("🧑‍🤝‍🧑 Gruppeoppgave 3 — memory.md")
    st.write("Skriv inn deltakerkoden du fikk ved kursstart.")
    code = st.text_input("Deltakerkode", type="password")
    if st.button("Fortsett", type="primary"):
        if code == expected:
            st.session_state.participant_ok = True
            st.rerun()
        else:
            callout("Feil kode.", kind="warning", key="g3_gate_error")
    return False


def _render_question(qid: int, qcfg: dict) -> None:
    count_key = f"g3_count_{qid}"
    sent_count = st.session_state.get(count_key, 0)

    with st.container(border=True):
        st.markdown(f"**Spørsmål {qid}: {qcfg['text']}**")
        if sent_count:
            st.caption(f"Du har sendt inn {sent_count} svar på dette spørsmålet.")

        with st.form(key=f"g3_form_{qid}", clear_on_submit=True):
            if qcfg["type"] == "text":
                value = st.text_area(
                    "Ditt svar",
                    placeholder=qcfg.get("placeholder", ""),
                    label_visibility="collapsed",
                    height=100,
                )
                submitted = st.form_submit_button("Send inn", type="primary")
                if submitted:
                    if value and value.strip():
                        try:
                            insert_text_response(qid, value)
                            st.session_state[count_key] = sent_count + 1
                            st.toast(f"Takk! Svar lagret på spørsmål {qid}.")
                            st.rerun()
                        except Exception as exc:  # noqa: BLE001
                            callout(
                                f"Kunne ikke lagre svar: {exc}",
                                kind="warning",
                                key=f"g3_err_{qid}_{sent_count}",
                            )
                    else:
                        callout(
                            "Skriv noe før du sender inn.",
                            kind="warning",
                            key=f"g3_text_empty_{qid}",
                        )

            else:  # choice
                value = st.radio(
                    "Velg ett",
                    qcfg["options"],
                    index=None,
                    label_visibility="collapsed",
                )
                submitted = st.form_submit_button("Send inn", type="primary")
                if submitted:
                    if value:
                        try:
                            insert_choice_response(qid, value)
                            st.session_state[count_key] = sent_count + 1
                            st.toast(f"Takk! Svar lagret på spørsmål {qid}.")
                            st.rerun()
                        except Exception as exc:  # noqa: BLE001
                            callout(
                                f"Kunne ikke lagre svar: {exc}",
                                kind="warning",
                                key=f"g3_err_{qid}_{sent_count}",
                            )
                    else:
                        callout(
                            "Velg ett alternativ før du sender inn.",
                            kind="warning",
                            key=f"g3_choice_empty_{qid}",
                        )


def main() -> None:
    if not _participant_gate():
        return

    crumb(["Kursmoduler", "13 · Gruppeoppgave 3"])
    st.title("🧑‍🤝‍🧑 Gruppeoppgave 3 — memory.md")
    st.caption(
        "Gå sammen to og to. Diskuter åpent — svarene er anonyme. "
        "Ikke skriv navn, bedriftshemmeligheter eller PII."
    )

    st.markdown(load_markdown(__file__, "intro"))

    for qid, qcfg in QUESTIONS.items():
        _render_question(qid, qcfg)

    st.divider()
    total_sent = sum(st.session_state.get(f"g3_count_{qid}", 0) for qid in QUESTIONS)
    st.caption(f"Du har sendt inn totalt {total_sent} svar i denne sesjonen.")

    st.divider()
    next_module_cta_for("gruppeoppgave_3_resultater")
