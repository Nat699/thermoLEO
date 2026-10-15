# thermoLEO Index v1

A single-number index (0–100) that summarizes the state of the
upper thermosphere (550–1550 km) derived from LEO satellite
altitude distributions.

## Interpretation

| Range | Class | Meaning |
|-------|-------|---------|
| 0–15 | calm | Stable thermosphere |
| 15–35 | normal | Typical conditions |
| 35–55 | active | Elevated activity |
| 55–75 | elevated | Degraded conditions |
| 75–100 | extreme | Severe drag environment |

## 2014–2025 evolution

| Year | TI | Class |
|------|----|----|| 2014 | 7.0 | calm |
| 2015 | 12.3 | calm |
| 2016 | 13.1 | calm |
| 2017 | 19.3 | normal |
| 2018 | 19.8 | normal |
| 2019 | 19.1 | normal |
| 2020 | 23.8 | normal |
| 2021 | 23.8 | normal |
| 2022 | 28.8 | normal |
| 2023 | 41.3 | active |
| 2024 | 66.3 | elevated |
| 2025 | 91.1 | extreme |

## Components

- **I1** (30%): mean skewness across bands, inverted
- **I2** (25%): skewness of 550 km band (saturation)
- **I3** (25%): fraction of band migration
- **I4** (20%): 3-year rolling slope of I1, inverted

## Files

- `thermoindex_annual.parquet` — main data
- `thermoindex_annual.csv` — same, CSV
- `thermoindex_annual.json` — same, JSON
- `metadata.json` — full specification
- `thermoindex.png/.pdf` — figures

## Usage

```python
import pandas as pd
df = pd.read_parquet('thermoindex_annual.parquet')
print(df[['year', 'thermoLEO_index', 'classification']])
```

## Related

- Dataset: thermoLEO_tomography_v1
- Software: https://github.com/Nat699/thermoLEO

## License

CC-BY-4.0