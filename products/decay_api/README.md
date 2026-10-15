# thermoLEO Decay Prediction API v3

Predicts time to reentry for LEO satellites using historical
TLE data and the thermoLEO Index.

## Model

For a given NORAD ID:

1. Load historical TLEs
2. Compute current altitude (from mean motion)
3. Estimate decay rate da/dt via linear fit of last 2 years
4. Amplify by thermoLEO Index:

       amplification = 0.7 + (TI / 100) * 0.8

5. Exponential projection to reentry altitude (200 km):

       t = (H / |v0|) * (1 - exp(-delta_h / H))

   where H = 50 km (atmospheric scale height)

## Status classification

| Status | eta_years | Meaning |
|--------|-----------|---------|
| stable_orbit | > 100 | Stable for centuries |
| long_term | 25-100 | Long-term decay |
| moderate | 5-25 | Moderate decay |
| approaching | 1-5 | Approaching reentry |
| imminent | < 1 | Imminent reentry |
| no_decay | - | No negative trend |

## Typical etas

| Altitude | da/dt (km/yr) | eta |
|----------|---------------|-----|
| 800 km | -0.02 | ~2500 years |
| 700 km | -0.05 | ~1000 years |
| 550 km | -0.5 | ~100 years |
| 400 km | -3.0 | ~16 years |
| 350 km | -15 | ~3 years |
| 280 km | -50 | ~10 months |

## Usage - offline (Jupyter)

```python
from model import predict_by_norad
r = predict_by_norad(25544, '/path/to/tle_dir', thermo_index=65)
print(r['eta_months'], 'months')
print(r['status'])
```

## Usage - API (local)

```bash
pip install -r requirements.txt
export THERMOLEO_TLE_DIR=/path/to/tle
uvicorn api:app --reload
```

## Response format

```json
{
  "norad_id": 25544,
  "current_altitude_km": 420.5,
  "decay_rate_km_per_year": -1.8,
  "thermo_index": 65,
  "eta_years": 12.5,
  "eta_months": 150,
  "confidence": 0.86,
  "status": "moderate"
}
```

## Limitations

- Linear da/dt assumption within the last 2-year window
- Exponential atmosphere with constant scale height (H = 50 km)
- Ignores solar cycle phase beyond thermoLEO Index
- Requires >= 2 TLEs per satellite
- Confidence capped at 0.9 (TLE precision limit)

## Related

- Index: thermoLEO_index
- Dataset: thermoLEO_tomography_v1
- GitHub: https://github.com/Nat699/thermoLEO

## License

MIT