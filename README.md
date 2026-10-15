# thermoLEO

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.23376365.svg)](https://doi.org/10.5281/zenodo.23376365)

**A TLE-based probe of thermospheric density and geomagnetic coupling.**

thermoLEO analyzes the altitude distribution of LEO satellites using
only public TLE data. The skewness of this distribution serves as a
sensitive proxy for thermospheric density and correlates with the
radial component of the geomagnetic field.

## Key findings

- **Orbital-class fingerprint:** skewness is a property of the orbital
  class (SSO +1.37, polar −0.55, inclined −0.34, equatorial +0.35)

- **Geomagnetic coupling:** skewness correlates with the RADIAL
  component of the geomagnetic field (B_C), validated independently:
  - Swarm in-situ: r = −0.67 (p = 0.0003)
  - CHAOS-7 model: r = −0.61 (p = 0.0015)
  - Cross-validation: r = +0.81

- **Magnitude does NOT correlate:** |B| gives r = −0.21 (n.s.),
  isolating the vertical magnetosphere-ionosphere-thermosphere
  coupling as the physical driver

- **Multi-band tomography:** 11 altitude bands (550–1550 km) show
  an oscillating collapse pattern, with the strongest signal at
  1150 km (−2.34) and an inversion at 550 km (+0.88)

- **Lower-tail saturation at 550 km:** skewness goes from −2.43
  (2014) to −0.05 (2025)

- **Band migration accelerates:** 0.85% (2019) → 14.9% (2025)

## Method

12 years (2014–2025) of public TLE data are analyzed for a fixed
population of 4,108 Sun-synchronous satellites. Each satellite is
assigned to its initial altitude band and tracked over time.
Skewness, quantiles, and band migration are computed annually.
External validation uses Swarm in-situ measurements and the
CHAOS-7 geomagnetic field model.

## Installation

    pip install git+https://github.com/Nat699/thermoLEO.git

## Quick start

    from thermoleo import ThermoSensor

    sensor = ThermoSensor(band=(823, 925))
    sensor.load_tle("data/tle_sso.parquet")
    result = sensor.fit()
    print(result[["year", "skew", "q10", "q50", "q90"]])

## Data

This repository does not include TLE data. To download:

- Space-Track: https://www.space-track.org
- Hugging Face: https://huggingface.co/datasets/juliensimon/space-track-tle-history

Place files in `data/` as `tle_YYYY.parquet`.

## Revision

See [REVISION_NOTES.md](REVISION_NOTES.md) for the full history
of hypotheses tested, refuted, and consolidated.

## License

MIT
