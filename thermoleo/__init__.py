"""thermoLEO - TLE-based thermospheric density probe."""
__version__ = "0.1.0"

from .io import load_tle_parquet, load_hf_year, filter_sso_leo
from .analyze import (
    compute_quantiles, compute_skewness, analyze_band,
    fit_skew_trend, fit_skew_vs_lower_tail,
)

__all__ = [
    "load_tle_parquet", "load_hf_year", "filter_sso_leo",
    "compute_quantiles", "compute_skewness", "analyze_band",
    "fit_skew_trend", "fit_skew_vs_lower_tail",
    "ThermoSensor",
]


class ThermoSensor:
    """High-level interface for thermospheric density estimation."""

    def __init__(self, band=(823, 925)):
        self.band = band
        self.df = None
        self.result = None

    def load_tle(self, path):
        self.df = load_tle_parquet(path)
        return self

    def fit(self):
        self.result = analyze_band(self.df, band=self.band)
        return self.result

    def density_signal(self):
        return self.result[["year", "skew", "q10", "q50"]].copy()

    def trend(self):
        return fit_skew_trend(self.result)