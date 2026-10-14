"""IO utilities for thermoLEO."""
import pandas as pd
from pathlib import Path


def load_tle_parquet(path):
    """Load TLE parquet file."""
    df = pd.read_parquet(path)
    df["epoch"] = pd.to_datetime(df["epoch"], utc=True)
    return df


def load_hf_year(base_path, year):
    """Load one year from the Hugging Face dataset."""
    p = Path(base_path) / f'tle_{year}.parquet'
    return pd.read_parquet(p)


def filter_sso_leo(df, incl_range=(95, 105), ecc_max=0.05,
                   alt_range=(400, 2000), mu=398600.4418):
    """Apply standard SSO/LEO filters."""
    df = df[df["inclination"].between(*incl_range)]
    df = df[df["eccentricity"] < ecc_max]
    T = 86400 / df["mean_motion"]
    a = (mu * (T / (2 * 3.141592653589793)) ** 2) ** (1 / 3)
    df = df.assign(alt_calc=a - 6371.0)
    df = df[df["alt_calc"].between(*alt_range)]
    return df