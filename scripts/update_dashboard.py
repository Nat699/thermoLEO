#!/usr/bin/env python3
"""Atualiza o dashboard thermoLEO com TLE mais recente."""
import json, urllib.request, re
from datetime import datetime, timezone
from pathlib import Path
import numpy as np
import pandas as pd
from scipy.stats import skew

ROOT = Path(__file__).resolve().parent.parent
HISTORY = ROOT / "history.json"
TLE_FILE = ROOT / "tle_latest.txt"
INDEX = ROOT / "index.html"
TEMPLATE = ROOT / "scripts" / "template.html"

BAND = (823, 925)
MIN_SATS = 100
MU = 398600.4418


def baixar():
    url = "https://celestrak.org/NORAD/elements/gp.php?GROUP=active&FORMAT=tle"
    print("Baixando TLE...")
    urllib.request.urlretrieve(url, TLE_FILE)
    print("  ", TLE_FILE.stat().st_size, "B")


def parse():
    rows = []
    with open(TLE_FILE) as f:
        lines = [l.rstrip() for l in f if l.strip()]
    for i in range(0, len(lines) - 2, 3):
        l1, l2 = lines[i+1], lines[i+2]
        if not l1.startswith("1 ") or not l2.startswith("2 "):
            continue
        try:
            rows.append({"incl": float(l2[8:16]),
                         "mm": float(l2[52:63])})
        except Exception:
            pass
    return pd.DataFrame(rows)


def ponto(df):
    df = df[(df.incl > 95) & (df.incl < 105)].copy()
    T = 86400 / df.mm
    a = (MU * (T / (2 * np.pi)) ** 2) ** (1/3)
    df["alt"] = a - 6371.0
    b = df[(df.alt > BAND[0]) & (df.alt < BAND[1])]
    if len(b) < MIN_SATS:
        return None
    return {"n_sats": int(len(b)), "skew": float(skew(b.alt)),
            "q10": float(b.alt.quantile(0.10)),
            "q50": float(b.alt.quantile(0.50)),
            "q90": float(b.alt.quantile(0.90))}


def main():
    baixar()
    df = parse()
    print("TLEs:", len(df))
    p = ponto(df)
    if p is None:
        print("Poucos sats na banda")
        return
    hoje = datetime.now(timezone.utc).strftime("%Y-%m-01")
    p["data"] = hoje
    print("Novo ponto:", p)

    hist = json.loads(HISTORY.read_text()) if HISTORY.exists() else []
    hist = [x for x in hist if x["data"][:7] != hoje[:7]]
    hist.append(p)
    hist.sort(key=lambda x: x["data"])
    HISTORY.write_text(json.dumps(hist, indent=2))

    # regenera index.html a partir do template
    tpl = TEMPLATE.read_text(encoding="utf-8")
    stamp = datetime.now(timezone.utc).strftime("%d/%m/%Y %H:%M UTC")

    # substitui os arrays embutidos no HTML
    anos = [x["data"][:4] for x in hist]
    skew_v = [round(x["skew"], 4) for x in hist]
    q10_v = [round(x["q10"], 2) for x in hist]
    q50_v = [round(x["q50"], 2) for x in hist]
    q90_v = [round(x["q90"], 2) for x in hist]

    tpl = re.sub(r'const ANOS = \[[^\]]*\]',
                 "const ANOS = " + json.dumps(anos), tpl)
    tpl = re.sub(r'const SKEW = \[[^\]]*\]',
                 "const SKEW = " + json.dumps(skew_v), tpl)
    tpl = re.sub(r'const Q10  = \[[^\]]*\]',
                 "const Q10  = " + json.dumps(q10_v), tpl)
    tpl = re.sub(r'const Q50  = \[[^\]]*\]',
                 "const Q50  = " + json.dumps(q50_v), tpl)
    tpl = re.sub(r'const Q90  = \[[^\]]*\]',
                 "const Q90  = " + json.dumps(q90_v), tpl)

    INDEX.write_text(tpl, encoding="utf-8")
    print("index.html regenerado:", INDEX.stat().st_size, "B")


if __name__ == "__main__":
    main()
