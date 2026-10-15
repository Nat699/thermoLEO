# thermoLEO Regime Change Alert v1

Detects anomalous regimes in the upper thermosphere using three
independent signals from LEO satellite altitude distributions.

## Signals

| Signal | Description | Threshold |
|--------|-------------|-----------|
| S1 | thermoLEO Index | > 50 |
| S2 | Band migration rate | > 5% per year |
| S3 | 550 km saturation stalled | slope < 0.05 |

## Alert levels

| Level | Signals active | Action |
|-------|---------------|--------|
| none | 0 | normal monitoring |
| watch | 1 | increase frequency |
| alert | 2 | investigate |
| critical | 3 | immediate action |

## Results 2014–2025

| 2014 | 0 | 0 | 0 | 0 | none |
| 2015 | 0 | 0 | 0 | 0 | none |
| 2016 | 0 | 0 | 0 | 0 | none |
| 2017 | 0 | 0 | 0 | 0 | none |
| 2018 | 0 | 0 | 0 | 0 | none |
| 2019 | 0 | 0 | 1 | 1 | watch |
| 2020 | 0 | 0 | 0 | 0 | none |
| 2021 | 0 | 0 | 0 | 0 | none |
| 2022 | 0 | 0 | 1 | 1 | watch |
| 2023 | 0 | 1 | 0 | 1 | watch |
| 2024 | 1 | 1 | 1 | 3 | critical |
| 2025 | 1 | 1 | 1 | 3 | critical |

## Detected regime change

Anomalous regime detected starting: **2024**

Total years with alert: 2

## Files

- `regime_alert.parquet` — main data
- `regime_alert.csv` — same, CSV
- `regime_alert.json` — same, JSON
- `metadata.json` — specification
- `regime_alert.png/.pdf` — figures

## Related

- Index: thermoLEO_index
- Dataset: thermoLEO_tomography_v1
- Software: https://github.com/Nat699/thermoLEO

## License

CC-BY-4.0