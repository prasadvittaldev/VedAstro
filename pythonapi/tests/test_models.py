from __future__ import annotations

from datetime import datetime, timezone

import pytest

from vedastro_core import GeoLocation, PlanetName, Time


def test_geolocation_roundtrip() -> None:
    loc = GeoLocation(name="Tokyo", longitude=139.83, latitude=35.65)
    data = loc.to_dict()
    assert GeoLocation.from_dict(data) == loc


def test_geolocation_validation() -> None:
    with pytest.raises(ValueError):
        GeoLocation(name="Bad", longitude=200.0, latitude=0.0)


def test_time_roundtrip() -> None:
    dt = datetime(2024, 1, 1, 12, tzinfo=timezone.utc)
    loc = GeoLocation(name="Greenwich", longitude=0.0, latitude=51.48)
    t = Time(dt=dt, location=loc)
    restored = Time.from_dict(t.to_dict())
    assert restored == t
    assert restored.utc_datetime == dt


def test_planetname_parsing() -> None:
    assert PlanetName.from_str("sun") is PlanetName.SUN
    assert str(PlanetName.MARS) == "Mars"
