
"""Example queries — run these in a Jupyter cell."""
import sys
sys.path.insert(0, "..")

from model import predict_by_norad, predict_batch

TLE_DIR = "/home/jovyan/data/tle_hf"

print("Exemplo 1 — ISS (NORAD 25544):")
r = predict_by_norad(25544, TLE_DIR, thermo_index=65)
for k, v in r.items():
    print(f"  {k}: {v}")

print("\nExemplo 2 — lote de satélites:")
norads = [25544, 20580, 43013]
results = predict_batch(norads, TLE_DIR, thermo_index=65)
for r in results:
    if "error" in r:
        print(f"  {r['norad_id']}: {r['error']}")
    else:
        print(f"  {r['norad_id']}: eta={r['eta_years']:.2f}a "
              f"[{r['status']}]  conf={r['confidence']:.2f}")
