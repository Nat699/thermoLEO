"""Plotting utilities for thermoLEO."""
import matplotlib.pyplot as plt


def plot_skew_trend(df_year, ax=None, save=None):
    """Plot skewness vs year."""
    if ax is None:
        fig, ax = plt.subplots(figsize=(6, 4))
    ax.plot(df_year["year"], df_year["skew"], "o-")
    ax.set_xlabel("Year")
    ax.set_ylabel("Skewness")
    ax.set_title("Altitude skewness (823-925 km)")
    ax.grid(alpha=0.3)
    if save:
        plt.savefig(save, dpi=150, bbox_inches='tight')
    return ax


def plot_quantile_evolution(df_year, ax=None, save=None):
    """Plot q10, q50, q90 evolution."""
    if ax is None:
        fig, ax = plt.subplots(figsize=(6, 4))
    for q in ["q10", "q50", "q90"]:
        ax.plot(df_year["year"], df_year[q], "o-", label=q)
    ax.set_xlabel("Year")
    ax.set_ylabel("Altitude (km)")
    ax.legend()
    ax.grid(alpha=0.3)
    if save:
        plt.savefig(save, dpi=150, bbox_inches='tight')
    return ax