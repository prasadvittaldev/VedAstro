from fastapi.testclient import TestClient

from vedastro_api import app


def test_birth_period_endpoint_day():
    client = TestClient(app)
    resp = client.get(
        "/birth-period",
        params={
            "year": 2024,
            "month": 6,
            "day": 1,
            "hour": 12,
            "minute": 0,
            "latitude": 0.0,
            "longitude": 0.0,
            "tz_offset": 0,
        },
    )
    assert resp.status_code == 200
    data = resp.json()
    assert data["is_day_birth"] is True
    assert data["is_night_birth"] is False


def test_birth_period_endpoint_night():
    client = TestClient(app)
    resp = client.get(
        "/birth-period",
        params={
            "year": 2024,
            "month": 6,
            "day": 1,
            "hour": 23,
            "minute": 0,
            "latitude": 0.0,
            "longitude": 0.0,
            "tz_offset": 0,
        },
    )
    assert resp.status_code == 200
    data = resp.json()
    assert data["is_day_birth"] is False
    assert data["is_night_birth"] is True


def test_moon_phase_endpoint():
    client = TestClient(app)
    resp = client.get(
        "/moon-phase",
        params={"year": 2024, "month": 1, "day": 26, "tz_offset": 0},
    )
    assert resp.status_code == 200
    data = resp.json()
    assert 14 < data["phase"] < 15


def test_day_duration_endpoint():
    client = TestClient(app)
    resp = client.get(
        "/day-duration",
        params={
            "year": 2024,
            "month": 1,
            "day": 1,
            "latitude": 0.0,
            "longitude": 0.0,
            "tz_offset": 0,
        },
    )
    assert resp.status_code == 200
    data = resp.json()
    assert 11 < data["duration_hours"] < 13
