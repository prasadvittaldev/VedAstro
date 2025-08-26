"""FastAPI application exposing a small subset of VedAstro logic."""

from datetime import datetime, timedelta, timezone

from fastapi import Depends, FastAPI

from vedastro_core import (
    GeoLocation,
    Time,
    day_duration_hours,
    is_day_birth,
    is_night_birth,
    moon_phase,
)

from .models import (
    BirthPeriodRequest,
    BirthPeriodResponse,
    DayDurationRequest,
    DayDurationResponse,
    MoonPhaseRequest,
    MoonPhaseResponse,
)

app = FastAPI(title="VedAstro Python API")


@app.get("/day-duration", response_model=DayDurationResponse)
def read_day_duration(
    params: DayDurationRequest = Depends(),  # noqa: B008
) -> DayDurationResponse:
    """Return length of the day in hours for the provided date and location."""

    dt = datetime(
        params.year,
        params.month,
        params.day,
        tzinfo=timezone(timedelta(hours=params.tz_offset)),
    )
    location = GeoLocation(
        name="location", longitude=params.longitude, latitude=params.latitude
    )
    t = Time(dt=dt, location=location)
    return DayDurationResponse(duration_hours=day_duration_hours(t))


@app.get("/birth-period", response_model=BirthPeriodResponse)
def read_birth_period(
    params: BirthPeriodRequest = Depends(),  # noqa: B008
) -> BirthPeriodResponse:
    """Return whether the provided moment is a day or night birth."""

    dt = datetime(
        params.year,
        params.month,
        params.day,
        params.hour,
        params.minute,
        tzinfo=timezone(timedelta(hours=params.tz_offset)),
    )
    location = GeoLocation(
        name="location", longitude=params.longitude, latitude=params.latitude
    )
    t = Time(dt=dt, location=location)
    return BirthPeriodResponse(
        is_day_birth=is_day_birth(t),
        is_night_birth=is_night_birth(t),
    )


@app.get("/moon-phase", response_model=MoonPhaseResponse)
def read_moon_phase(
    params: MoonPhaseRequest = Depends(),  # noqa: B008
) -> MoonPhaseResponse:
    """Return the moon phase (days since new moon) for the given date."""

    dt = datetime(
        params.year,
        params.month,
        params.day,
        tzinfo=timezone(timedelta(hours=params.tz_offset)),
    )
    location = GeoLocation(name="location", longitude=0.0, latitude=0.0)
    t = Time(dt=dt, location=location)
    return MoonPhaseResponse(phase=moon_phase(t))
