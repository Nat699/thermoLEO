"""Quick start example."""
from thermoleo import ThermoSensor, fit_skew_vs_lower_tail

sensor = ThermoSensor(band=(823, 925))
sensor.load_tle('data/tle_sso_2014_2025.parquet')
result = sensor.fit()
print(result[['year', 'n_sats', 'skew', 'q10', 'q50', 'q90']])
print('Trend:', sensor.trend())
print('Skew vs lower tail:', fit_skew_vs_lower_tail(result))