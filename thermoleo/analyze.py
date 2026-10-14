"""Core analysis for thermoLEO."""
import numpy as np
import pandas as pd
from scipy.stats import skew, linregress


def compute_quantiles(altitudes, qs=(0.05, 0.10, 0.25, 0.50, 0.75, 0.90, 0.95)):
    """Return quantiles of the altitude distribution."""
    return {f"q{int(q * 100):02d}": float(np.quantile(altitudes, q)) for q in qs}


def compute_skewness(altitudes):
    """Return third standardized moment."""
    return float(skew(altitudes))


def analyze_band(df, band=(823, 925), min_sats=100):
    """Compute yearly skew and quantiles for a given altitude band."""
    rows = []
    for year, g in df.groupby(df["epoch"].dt.year):
        g_band = g[g["alt_calc"].between(*band)]
        if g_band["norad_id"].nunique() < min_sats:
            continue
        alt = g_band["alt_calc"].dropna().values
        qs = compute_quantiles(alt)
        rows.append({
            "year": int(year),
            "n_sats": int(g_band["norad_id"].nunique()),
            "n_regs": len(alt),
            "skew": compute_skewness(alt),
            **qs,
        })
    return pd.DataFrame(rows)


def fit_skew_trend(df_year):
    """Fit linear trend of skew vs year."""
    slope, intercept, r, p, se = linregress(df_year["year"], df_year["skew"])
    return {"slope": float(slope), "r": float(r), "p": float(p), "se": float(se)}


def fit_skew_vs_lower_tail(df_year):
    """Fit skew vs lower-tail extent (q50 - q10)."""
    lower = df_year["q50"] - df_year["q10"]
    slope, intercept, r, p, se = linregress(lower, df_year["skew"])
    return {"slope": float(slope), "r": float(r), "p": float(p), "se": float(se)}