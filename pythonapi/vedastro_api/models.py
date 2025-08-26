from pydantic import BaseModel


class DayDurationRequest(BaseModel):
    year: int
    month: int
    day: int
    latitude: float
    longitude: float
    tz_offset: int = 0


class DayDurationResponse(BaseModel):
    duration_hours: float


class BirthPeriodRequest(BaseModel):
    year: int
    month: int
    day: int
    hour: int
    minute: int
    latitude: float
    longitude: float
    tz_offset: int = 0


class BirthPeriodResponse(BaseModel):
    is_day_birth: bool
    is_night_birth: bool


class MoonPhaseRequest(BaseModel):
    year: int
    month: int
    day: int
    tz_offset: int = 0


class MoonPhaseResponse(BaseModel):
    phase: float
