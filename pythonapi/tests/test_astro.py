from datetime import datetime, timezone

import pytest

from vedastro_core import (
    GeoLocation,
    Time,
    day_duration_hours,
    is_day_birth,
    is_night_birth,
    moon_phase,
    moon_phase_name,
    sunrise_time,
)


def test_day_duration_hours_equator():
    dt = datetime(2024, 1, 1, tzinfo=timezone.utc)
    loc = GeoLocation(name="equator", longitude=0.0, latitude=0.0)
    t = Time(dt=dt, location=loc)
    assert day_duration_hours(t) == pytest.approx(12, abs=0.2)


def test_day_and_night_birth():
    loc = GeoLocation(name="equator", longitude=0.0, latitude=0.0)
    day_dt = datetime(2024, 6, 1, 12, tzinfo=timezone.utc)
    night_dt = datetime(2024, 6, 1, 23, tzinfo=timezone.utc)

    day_time = Time(dt=day_dt, location=loc)
    night_time = Time(dt=night_dt, location=loc)

    assert is_day_birth(day_time)
    assert not is_night_birth(day_time)

    assert is_night_birth(night_time)
    assert not is_day_birth(night_time)


def test_sunrise_caching():
    loc = GeoLocation(name="equator", longitude=0.0, latitude=0.0)
    dt = datetime(2024, 1, 1, tzinfo=timezone.utc)
    t = Time(dt=dt, location=loc)

    sunrise_time.cache_clear()
    sunrise_time(t)
    first = sunrise_time.cache_info()
    sunrise_time(t)
    second = sunrise_time.cache_info()
    assert second.hits == first.hits + 1


def test_moon_phase_new_and_full():
    loc = GeoLocation(name="equator", longitude=0.0, latitude=0.0)

    new_time = Time(dt=datetime(2024, 1, 12, tzinfo=timezone.utc), location=loc)
    full_time = Time(dt=datetime(2024, 1, 26, tzinfo=timezone.utc), location=loc)

    assert moon_phase_name(new_time) == "New Moon"
    assert moon_phase(new_time) == pytest.approx(0, abs=1)

    assert moon_phase_name(full_time) == "Full Moon"
    assert 14 < moon_phase(full_time) < 15
