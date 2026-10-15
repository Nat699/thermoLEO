
"""Offline tests for the decay model."""
import numpy as np
from model import (
    alt_from_mm, predict_reentry, classify_status,
)


def test_alt_from_mm():
    h = alt_from_mm(14.6)
    assert 650 < h < 750
    print(f"  [1] alt_from_mm(14.6) = {h:.1f} km  OK")


def test_status_classification():
    assert classify_status(200) == "stable_orbit"
    assert classify_status(50) == "long_term"
    assert classify_status(10) == "moderate"
    assert classify_status(3) == "approaching"
    assert classify_status(0.5) == "imminent"
    print(f"  [2] classify_status  OK")


def test_realistic_cases():
    casos = [
        (800, -0.02),
        (700, -0.05),
        (550, -0.5),
        (400, -3.0),
        (350, -15.0),
        (280, -50.0),
    ]
    print(f"  [3] casos realistas:")
    for alt, rate in casos:
        r = predict_reentry(alt, rate, thermo_index=65)
        print(f"       alt={alt:3.0f}, da/dt={rate:6.2f}: "
              f"eta={r['eta_years']:8.1f} a  [{r['status']}]")
    print(f"  [3] OK")


def test_ti_effect():
    r_low = predict_reentry(700, -2.0, thermo_index=10)
    r_high = predict_reentry(700, -2.0, thermo_index=90)
    assert r_high["eta_years"] < r_low["eta_years"]
    print(f"  [4] TI=10 → {r_low['eta_years']:.2f}a  |  "
          f"TI=90 → {r_high['eta_years']:.2f}a  OK")


def test_no_decay():
    r = predict_reentry(700, +0.5, thermo_index=50)
    assert r["eta_years"] is None
    print(f"  [5] sem decaimento → status={r['status']}  OK")


if __name__ == "__main__":
    print("Testes offline do modelo:")
    test_alt_from_mm()
    test_status_classification()
    test_realistic_cases()
    test_ti_effect()
    test_no_decay()
    print("\nTodos os testes passaram.")
