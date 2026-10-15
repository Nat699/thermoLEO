# thermoLEO Tomography Dataset v1

**Multi-band altitude skewness of LEO satellites (2014-2025)**

## Overview

This dataset contains the altitude skewness of LEO satellite
populations across 11 altitude bands (550-1550 km), computed
annually from public TLE data.

- **Period:** 2014-2025 (12 years)
- **Population:** 4,108 Sun-synchronous satellites (fixed)
- **Bands:** 11 bands of 100 km each
- **Cells:** 132 (12 years x 11 bands)
- **License:** CC-BY-4.0

## Files

| File | Description |
|------|-------------|
| `thermoLEO_tomography_v1.parquet` | Main dataset (recommended) |
| `thermoLEO_tomography_v1.csv` | Same data, CSV format |
| `thermoLEO_tomography_v1.json` | Same data, JSON format |
| `metadata.json` | Full metadata in JSON-LD style |
| `CITATION.cff` | Citation information |

## Columns

| Column | Type | Units | Description |
|--------|------|-------|-------------|
| year | int | - | Calendar year (2014-2025) |
| band_km | float | km | Center of altitude band |
| band_lo_km | float | km | Lower edge of band |
| band_hi_km | float | km | Upper edge of band |
| n_satellites | int | - | Satellites in the band that year |
| n_observations | int | - | TLE observations used |
| skewness | float | - | Third standardized moment |
| q10_km | float | km | 10th percentile altitude |
| q50_km | float | km | Median altitude |
| q90_km | float | km | 90th percentile altitude |

## Method

Satellites are assigned to altitude bands based on their **initial
altitude in 2014**, and tracked over time (so they stay in the same
band even if they decay). For each (year, band) cell:

1. Filter satellites in the band
2. Collect all altitude observations that year
3. Compute skewness and quantiles

This approach avoids population bias from new satellites entering
lower bands.

## Key findings

- **Maximum collapse:** band 1150 km, delta skewness = -2.34 (2014 to 2025)
- **Saturation:** band 550 km, delta skewness = **+0.88** (inverted)
- **Oscillatory structure:** the collapse is not uniform in altitude
- **Post-2020 acceleration:** 10 of 11 bands show positive slope after 2020

## How to load

    import pandas as pd
    df = pd.read_parquet('thermoLEO_tomography_v1.parquet')
    print(df.head())

    pivot = df.pivot(index='year', columns='band_km', values='skewness')
    print(pivot)

## Citation

    Junior, N. A. (2026). thermoLEO Tomography Dataset v1 [Data set].
    Zenodo. https://doi.org/10.5281/zenodo.XXXXXXX

## Related

- Software: https://github.com/Nat699/thermoLEO
- Paper: in preparation

## License

This dataset is licensed under CC-BY-4.0. You are free to share
and adapt, with attribution.
