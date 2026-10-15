
"""Decay prediction model for LEO satellites.

Uses historical TLE-derived altitude trends and the thermoLEO Index
to estimate time until reentry.
"""
import numpy as np
import pandas as pd
from pathlib import Path


MU = 398600.4418       # km^3/s^2
R_EARTH = 6371.0       # km
REENTRY_ALT = 200.0    # km
H_SCALE = 50.0         # km — atmospheric scale height


def load_tle_cache(tle_dir):
    """Load cached TLE parquets into a single DataFrame."""
    tle_dir = Path(tle_dir)
    files = sorted(tle_dir.glob("tle_*.parquet"))
    if not files:
        raise FileNotFoundError(f"no parquets in {tle_dir}")
    frames = []
    for f in files:
        d = pd.read_parquet(f)
        d["epoch"] = pd.to_datetime(d["epoch"], utc=True)
        frames.append(d)
    return pd.concat(frames, ignore_index=True)


def alt_from_mm(mm):
    """Altitude from mean motion (rev/day) via Kepler."""
    T = 86400.0 / mm
    a = (MU * (T / (2 * np.pi)) ** 2) ** (1.0 / 3.0)
    return a - R_EARTH


def estimate_decay_rate(df_sat, window_years=2):
    """Estimate da/dt (km/year) from historical TLEs."""
    df = df_sat.sort_values("epoch").copy()
    df["alt"] = alt_from_mm(df["mean_motion"])
    df["year_frac"] = (
        (df["epoch"] - df["epoch"].min()).dt.total_seconds() / 86400.0 / 365.25
    )
    if len(df) < 2:
        return np.nan
    cutoff = df["year_frac"].max() - window_years
    recent = df[df["year_frac"] >= cutoff]
    if len(recent) < 2:
        recent = df.tail(max(2, len(df) // 4))
    slope = np.polyfit(recent["year_frac"], recent["alt"], 1)[0]
    return float(slope)


def classify_status(eta_years):
    """Classify orbital status from eta."""
    if eta_years is None:
        return "unknown"
    if eta_years > 100:
        return "stable_orbit"
    if eta_years > 25:
        return "long_term"
    if eta_years > 5:
        return "moderate"
    if eta_years > 1:
        return "approaching"
    return "imminent"


def predict_reentry(alt_km, da_dt_km_per_year, thermo_index=50.0):
    """Predict reentry time using exponential atmosphere model.

    Model:
        dh/dt = -|v0| * exp((h0 - h) / H)
        t_reentry = (H / |v0|) * (1 - exp(-delta_h / H))
    """
    if da_dt_km_per_year >= 0 or np.isnan(da_dt_km_per_year):
        return {
            "eta_years": None,
            "eta_months": None,
            "confidence": 0.0,
            "status": "no_decay",
            "reason": "no negative decay trend",
        }

    # amplificação pelo thermoLEO Index
    amplification = 0.7 + (thermo_index / 100.0) * 0.8
    effective_rate = da_dt_km_per_year * amplification

    delta_alt = alt_km - REENTRY_ALT
    if delta_alt <= 0:
        return {
            "eta_years": 0.0,
            "eta_months": 0.0,
            "confidence": 1.0,
            "status": "imminent",
            "reason": "already at reentry altitude",
        }

    # FÓRMULA CORRIGIDA
    eta_years = (H_SCALE / abs(effective_rate)) * (
        1.0 - np.exp(-delta_alt / H_SCALE)
    )

    confidence = min(0.9, 0.5 + abs(da_dt_km_per_year) * 2.0)
    status = classify_status(eta_years)

    return {
        "eta_years": float(eta_years),
        "eta_months": float(eta_years * 12.0),
        "confidence": float(confidence),
        "status": status,
        "effective_rate_km_per_year": float(effective_rate),
    }


def predict_by_norad(norad_id, tle_dir, thermo_index=50.0):
    """End-to-end prediction for a given satellite."""
    df = load_tle_cache(tle_dir)
    df_sat = df[df["norad_id"] == int(norad_id)]
    if len(df_sat) < 2:
        return {
            "norad_id": int(norad_id),
            "error": "satellite not found or insufficient data",
        }
    df_sat["alt"] = alt_from_mm(df_sat["mean_motion"])
    current_alt = float(df_sat.sort_values("epoch").iloc[-1]["alt"])
    rate = estimate_decay_rate(df_sat)
    pred = predict_reentry(current_alt, rate, thermo_index)

    return {
        "norad_id": int(norad_id),
        "current_altitude_km": current_alt,
        "decay_rate_km_per_year": rate,
        "thermo_index": thermo_index,
        **pred,
    }


def predict_batch(norad_ids, tle_dir, thermo_index=50.0):
    """Predict for a list of NORAD IDs."""
    return [predict_by_norad(n, tle_dir, thermo_index) for n in norad_ids]
