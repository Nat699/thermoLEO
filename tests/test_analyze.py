"""Basic tests."""
import numpy as np
from thermoleo import compute_quantiles, compute_skewness


def test_quantiles():
    x = np.arange(100)
    qs = compute_quantiles(x, qs=(0.5,))
    assert 49 < qs['q50'] < 51


def test_skewness():
    x = np.random.normal(0, 1, 10000)
    assert abs(compute_skewness(x)) < 0.1