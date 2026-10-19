# thermoLEO

A TLE-based probe of thermospheric density and geomagnetic coupling.

## Key findings

### Bimodal orbital skewness collapse (Q1 vs Q4)
The altitude distribution of 4,124 Sun-synchronous satellites (2014-2025) shows a bimodal collapse:
- Q1 (fast decayers, 264 sats): skewness collapses from +2.36 (2014) to -4.43 (2025)
- Q4 (slow decayers, 264 sats): skewness remains stable (+0.52 to +0.60)
- Output B (sub-bands 823-850, 850-880, 880-925): slopes -0.6088 / -0.4053 / -0.0361 (reproduced exactly)

### 3 skews coupled in Q1
- r(alt, v) = -0.9999
- r(alt, rho) = -0.9784
- r(v, rho) = +0.9792

### Driver is the radial component of the geomagnetic field (B_C)
- Swarm in-situ: r = -0.67 (p = 0.0003)
- CHAOS-7: r = -0.61 (p = 0.0015)
- Magnitude |B| does not correlate: r = -0.21 (n.s.)

## What was refuted

The linear skewness collapse (+0.12 to -1.85, slope -0.125/yr) does not reproduce.
The correct finding is the bimodal collapse: 25% of satellites (Q1) drive the entire
skewness trend, while 75% remain stable.

## Installation

    pip install git+https://github.com/Nat699/thermoLEO.git

## License
MIT