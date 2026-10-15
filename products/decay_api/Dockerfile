FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY model.py api.py ./

ENV THERMOLEO_TLE_DIR=/data/tle
ENV THERMOLEO_INDEX=50

EXPOSE 8000

CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000"]
