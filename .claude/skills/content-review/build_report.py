#!/usr/bin/env python3
"""Bygg CONTENT_REVIEW.md fra content-quality-eval-workflowens output-fil.

Bruk:  python .claude/skills/content-review/build_report.py <workflow-output-fil>
Kjøres fra repo-rot. Skriver CONTENT_REVIEW.md i CWD.

Output-fila (…/tasks/<taskid>.output) er JSON med selve workflow-returen under
nøkkelen "result" = {results, verifications, highRiskCount}.
"""
import sys, json
from collections import Counter


def main() -> None:
    if len(sys.argv) < 2:
        sys.exit("Bruk: build_report.py <workflow-output-fil>")
    d = json.loads(open(sys.argv[1]).read())
    R = d.get("result", d)
    if isinstance(R, str):
        R = json.loads(R)
    results, verifs = R["results"], R["verifications"]

    try:
        from data.moduler import MODULER
        NR = {m["slug"]: m["nr"] for m in MODULER}
    except Exception:
        NR = {}

    def nr(s):
        return NR.get(s, 0 if s == "oppvarming" else 990)

    def fnum(x):
        return "-" if x is None else str(x)

    def f_disp(fl):
        s = fnum(fl.get("F"))
        return s + ("?" if fl.get("F_unverified") and fl.get("F") is not None else "")

    allfiles = [(r["module"], fl) for r in results for fl in r["files"]]
    fullc = Counter(fl["Full"] for _, fl in allfiles)
    nunver = sum(1 for _, fl in allfiles if fl.get("F_unverified"))
    nR4 = sum(1 for _, fl in allfiles if (fl.get("R") or 0) >= 4)
    vc = Counter(v["verdict"] for v in verifs)
    claims_total = sum(len(r["product_claims"]) for r in results)

    o = []
    o.append("# CONTENT_REVIEW - innholdsevaluering av kurset\n")
    o.append("> Generert av content-review-skillen (multi-agent: 1 score-agent per modul + "
             "web-verifikasjon av høyrisiko-påstander). Vurdering, ikke omskriving. "
             "**Faktuell score på produktpåstander er begrenset** - `F?` = Cortex Code/Snowflake-"
             "produktpåstand som må verifiseres mot Snowflakes egen dokumentasjon.\n")
    o.append("## Skala\n")
    o.append("- **F** faktuell (1-5, `?`=uverifisert) · **R** kilde-/fabrikasjonsrisiko (1-5, **høy=dårlig**) · "
             "**Rel** relevans · **P** pedagogisk verdi · **Full** modenhet · **T** tone (1-5/n-a)\n")
    o.append("## Sammendrag (aggregat)\n")
    o.append(f"- Moduler vurdert: **{len(results)}** · content-enheter: **{len(allfiles)}**\n")
    o.append(f"- Fullføring: ferdig **{fullc.get('ferdig', 0)}**, UTKAST **{fullc.get('UTKAST', 0)}**, "
             f"placeholder **{fullc.get('placeholder', 0)}**, tom **{fullc.get('tom', 0)}**\n")
    o.append(f"- Uverifiserte produktpåstander (F?): **{nunver}** · enheter med R>=4: **{nR4}**\n")
    o.append(f"- Produktpåstander ekstrahert: **{claims_total}** (hvorav {R.get('highRiskCount', '?')} høyrisiko)\n")
    o.append(f"- Web-verifikasjon: støttet **{vc.get('støttet', 0)}**, delvis **{vc.get('delvis støttet', 0)}**, "
             f"motsagt **{vc.get('motsagt', 0)}**, ingen kilde **{vc.get('ingen kilde funnet', 0)}**\n")

    o.append("\n## 1. Modul-heatmap\n")
    o.append("| Nr | Modul | F | R | Rel | P | Full | T | #filer | #høyrisiko |")
    o.append("|---:|---|--:|--:|--:|--:|---|--:|--:|--:|")
    for r in sorted(results, key=lambda r: nr(r["module"])):
        ms = r["module_scores"]
        hi = sum(1 for c in r["product_claims"] if c["risk"] >= 4)
        o.append(f"| {nr(r['module'])} | {r['module']} | {ms['F']} | {ms['R']} | {ms['Rel']} | "
                 f"{ms['P']} | {ms['Full']} | {ms['T']} | {len(r['files'])} | {hi} |")

    flagged = sorted([(m, fl) for m, fl in allfiles if (fl.get("R") or 0) >= 4],
                     key=lambda x: -(x[1].get("R") or 0))
    o.append("\n## 2. Må verifiseres før kurs (R>=4)\n")
    o.append("| R | Modul | Fil | F | Rel | P | Note |")
    o.append("|--:|---|---|--:|--:|--:|---|")
    for m, fl in flagged:
        o.append(f"| {fl['R']} | {m} | {fl['file'].split('/')[-1]} | {f_disp(fl)} | "
                 f"{fnum(fl.get('Rel'))} | {fnum(fl.get('P'))} | {fl['note'].replace(chr(10), ' ')[:160]} |")

    empt = [(m, fl) for m, fl in allfiles if fl["Full"] in ("placeholder", "tom")]
    o.append(f"\n## 3. Tomt / placeholder ({len(empt)} - må fylles)\n")
    o.append("| Modul | Fil | Status |")
    o.append("|---|---|---|")
    for m, fl in sorted(empt, key=lambda x: nr(x[0])):
        o.append(f"| {m} | {fl['file'].split('/')[-1]} | {fl['Full']} |")

    low = [(m, fl) for m, fl in allfiles
           if fl["Full"] not in ("placeholder", "tom")
           and ((fl.get("Rel") is not None and fl["Rel"] <= 2) or (fl.get("P") is not None and fl["P"] <= 2))]
    o.append("\n## 4. Lav relevans/verdi (Rel<=2 eller P<=2)\n")
    if low:
        o.append("| Modul | Fil | Rel | P | Note |")
        o.append("|---|---|--:|--:|---|")
        for m, fl in low:
            o.append(f"| {m} | {fl['file'].split('/')[-1]} | {fnum(fl.get('Rel'))} | "
                     f"{fnum(fl.get('P'))} | {fl['note'].replace(chr(10), ' ')[:140]} |")
    else:
        o.append("_Ingen ferdige enheter scoret Rel<=2 eller P<=2._")

    o.append("\n## 5. Web-verifikasjon av høyrisiko-påstander\n")
    o.append("| Verdikt | Modul | Påstand | Kilde | Note |")
    o.append("|---|---|---|---|---|")
    order = {"motsagt": 0, "delvis støttet": 1, "ingen kilde funnet": 2, "støttet": 3}
    for v in sorted(verifs, key=lambda v: order.get(v["verdict"], 9)):
        src = v["source"] or "-"
        if src.startswith("http"):
            src = f"[lenke]({src})"
        o.append(f"| {v['verdict']} | {v.get('module', '')} | {v['claim'][:80].replace(chr(10), ' ')} | "
                 f"{src} | {v['note'].replace(chr(10), ' ')[:120]} |")

    open("CONTENT_REVIEW.md", "w").write("\n".join(o) + "\n")
    print(f"CONTENT_REVIEW.md skrevet ({len(chr(10).join(o))} tegn). "
          f"Moduler={len(results)} F?={nunver} R>=4={nR4} verdikt={dict(vc)}")


if __name__ == "__main__":
    main()
