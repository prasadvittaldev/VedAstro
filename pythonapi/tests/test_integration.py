from time import perf_counter

import httpx
import pytest
from fastapi.testclient import TestClient

from vedastro_api import app

client = TestClient(app)


def test_day_duration_matches_csharp():
    params = {
        "year": 2020,
        "month": 6,
        "day": 1,
        "latitude": 1.28967,
        "longitude": 103.85007,
        "tz_offset": 8,
    }
    py_hours = client.get("/day-duration", params=params).json()["duration_hours"]
    cs_url = (
        "https://api.vedastro.org/api/Calculate/DayDurationHours/"
        "Location/Singapore/Time/12:00/01/06/2020/+08:00"
    )
    cs_hours = float(
        httpx.get(cs_url, timeout=10).json()["Payload"]["DayDurationHours"]
    )
    assert py_hours == pytest.approx(cs_hours, rel=0.02)


def test_day_duration_under_load():
    params = {
        "year": 2020,
        "month": 6,
        "day": 1,
        "latitude": 1.28967,
        "longitude": 103.85007,
        "tz_offset": 8,
    }
    start = perf_counter()
    for _ in range(100):
        resp = client.get("/day-duration", params=params)
        assert resp.status_code == 200
    assert perf_counter() - start < 5
