# thermoLEO

**A TLE-based thermospheric density probe.**

thermoLEO estimates thermospheric density in the 800-1000 km range
using only public Two-Line Element (TLE) data. The method analyzes
the lower tail of the LEO satellite altitude distribution.

## Method

12 years (2014-2025) of TLE data, fixed population of 1,369
Sun-synchronous satellites at 823-925 km.

Key results:

- Skewness collapsed from +0.12 (2014) to -1.85 (2025)
- Lower tail (q05) decayed 6.6x faster than upper tail (q95)
- r(skew, lower tail) = -0.98 (bootstrap 95% CI [-0.999, -0.787])
- Multiple regression R2 = 0.986

## Installation

    pip install git+https://github.com/SEU-USUARIO/thermoLEO.git

## Quick start

    from thermoleo import ThermoSensor
    sensor = ThermoSensor(band=(823, 925))
    sensor.load_tle('data/tle_sso.parquet')
    result = sensor.fit()
    print(result[['year', 'skew', 'q10', 'q50', 'q90']])

## Data

This repository does not include TLE data.

- Space-Track: https://www.space-track.org
- Hugging Face: https://huggingface.co/datasets/juliensimon/space-track-tle-history

Place files in `data/` as `tle_YYYY.parquet`.

## License

MIT