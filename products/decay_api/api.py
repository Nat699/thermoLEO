
"""FastAPI wrapper for thermoLEO decay prediction."""
import os
from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel

from model import predict_by_norad, predict_batch

app = FastAPI(
    title="thermoLEO Decay Prediction API",
    description=("Predicts time to reentry for LEO satellites using "
                 "historical TLE data and the thermoLEO Index."),
    version="3.0.0",
)

TLE_DIR = os.environ.get("THERMOLEO_TLE_DIR", "./data/tle_hf")
DEFAULT_TI = float(os.environ.get("THERMOLEO_INDEX", "50"))


class DecayPrediction(BaseModel):
    norad_id: int
    current_altitude_km: float
    decay_rate_km_per_year: float
    thermo_index: float
    eta_years: float | None
    eta_months: float | None
    confidence: float
    status: str
    reason: str | None = None


@app.get("/")
def root():
    return {
        "name": "thermoLEO Decay Prediction API",
        "version": "3.0.0",
        "docs": "/docs",
        "endpoints": ["/decay/{norad_id}", "/batch", "/health"],
    }


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/decay/{norad_id}", response_model=DecayPrediction)
def decay(norad_id: int,
          thermo_index: float = Query(DEFAULT_TI, ge=0.0, le=100.0)):
    result = predict_by_norad(norad_id, TLE_DIR, thermo_index)
    if "error" in result:
        raise HTTPException(status_code=404, detail=result["error"])
    return result


@app.get("/batch")
def batch(norads: str = Query(..., description="Comma-separated NORAD IDs"),
          thermo_index: float = Query(DEFAULT_TI, ge=0.0, le=100.0)):
    ids = [int(x.strip()) for x in norads.split(",") if x.strip()]
    results = predict_batch(ids, TLE_DIR, thermo_index)
    return {"count": len(results), "results": results}
