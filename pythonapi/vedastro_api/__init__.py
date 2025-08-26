"""FastAPI application exposing a subset of VedAstro logic."""

import os
from datetime import datetime, timedelta, timezone
from typing import Awaitable, Callable

from fastapi import Depends, FastAPI, Request, Response

from vedastro_core import (
    GeoLocation,
    Time,
    day_duration_hours,
    is_day_birth,
    is_night_birth,
    moon_phase,
)

from .api_logger import log_request
from .general import router as general_router
from .models import (
    BirthPeriodRequest,
    BirthPeriodResponse,
    DayDurationRequest,
    DayDurationResponse,
    MoonPhaseRequest,
    MoonPhaseResponse,
)
from .throttle_manager import is_allowed

app = FastAPI(title="VedAstro Python API")
app.include_router(general_router)

THROTTLE_LIMIT = int(os.getenv("VEDASTRO_THROTTLE_LIMIT", "1000"))
THROTTLE_WINDOW = int(os.getenv("VEDASTRO_THROTTLE_WINDOW", "60"))


@app.middleware("http")
async def log_and_throttle(
    request: Request, call_next: Callable[[Request], Awaitable[Response]]
) -> Response:
    """Log all requests and throttle by IP."""
    client_ip = request.client.host if request.client else "unknown"
    if not is_allowed(client_ip, THROTTLE_LIMIT, THROTTLE_WINDOW):
        return Response(status_code=429)
    response = await call_next(request)
    log_request(request.url.path, response.status_code)
    return response


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
