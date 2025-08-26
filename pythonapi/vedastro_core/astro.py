"""Basic astronomical calculations used by the Python port.

The functions in this module rely on the :mod:`astral` package to obtain
sunrise and sunset times for a given location.  They are intentionally
minimal and aim only to mirror a tiny subset of the original C# logic.
"""

from __future__ import annotations

from datetime import datetime, timedelta, timezone
from functools import lru_cache
from typing import Mapping

from astral import Observer, moon
from astral.sun import sun

from .constellation import ConstellationName
from .planet import PlanetName
from .time import Time


@lru_cache(maxsize=128)
def sunrise_time(time: Time) -> datetime:
    """Return the sunrise time for ``time``.

    The calculation uses the *astral* library and therefore requires the
    ``Time`` instance to carry geographic coordinates and a timezone aware
    :class:`datetime`.
    """

    observer = Observer(
        latitude=time.location.latitude, longitude=time.location.longitude
    )
    tz = time.dt.tzinfo or timezone.utc
    solar: Mapping[str, datetime] = sun(observer, date=time.dt.date(), tzinfo=tz)
    return solar["sunrise"]


@lru_cache(maxsize=128)
def sunset_time(time: Time) -> datetime:
    """Return the sunset time for ``time`` using :mod:`astral`."""

    observer = Observer(
        latitude=time.location.latitude, longitude=time.location.longitude
    )
    tz = time.dt.tzinfo or timezone.utc
    solar: Mapping[str, datetime] = sun(observer, date=time.dt.date(), tzinfo=tz)
    return solar["sunset"]


def day_duration_hours(time: Time) -> float:
    """Duration from sunrise to sunset in hours."""

    sunrise = sunrise_time(time)
    sunset = sunset_time(time)
    return (sunset - sunrise).total_seconds() / 3600


def is_night_birth(time: Time) -> bool:
    """Return ``True`` if ``time`` falls between sunset and next sunrise."""

    sunset = sunset_time(time)
    next_day = Time(dt=time.dt + timedelta(hours=23), location=time.location)
    sunrise_next = sunrise_time(next_day)
    return sunset <= time.dt <= sunrise_next


def is_day_birth(time: Time) -> bool:
    """Return ``True`` if ``time`` falls between sunrise and sunset."""

    sunrise = sunrise_time(time)
    sunset = sunset_time(time)
    return sunrise <= time.dt <= sunset


@lru_cache(maxsize=128)
def moon_phase(time: Time) -> float:
    """Return the moon phase for ``time`` as days since new moon."""

    return float(moon.phase(time.dt))


def moon_phase_name(time: Time) -> str:
    """Return a human-readable phase classification for ``time``."""

    phase = moon_phase(time)
    if phase < 1 or phase > 29:
        return "New Moon"
    if phase < 7:
        return "Waxing Crescent"
    if phase < 8:
        return "First Quarter"
    if phase < 14:
        return "Waxing Gibbous"
    if phase < 15:
        return "Full Moon"
    if phase < 22:
        return "Waning Gibbous"
    if phase < 23:
        return "Last Quarter"
    return "Waning Crescent"


_CONSTELLATION_LORDS = {
    ConstellationName.ASWINI: PlanetName.KETU,
    ConstellationName.MAKHA: PlanetName.KETU,
    ConstellationName.MOOLA: PlanetName.KETU,
    ConstellationName.BHARANI: PlanetName.VENUS,
    ConstellationName.PUBBA: PlanetName.VENUS,
    ConstellationName.POORVASHADA: PlanetName.VENUS,
    ConstellationName.KRITHIKA: PlanetName.SUN,
    ConstellationName.UTTARA: PlanetName.SUN,
    ConstellationName.UTTARASHADA: PlanetName.SUN,
    ConstellationName.ROHINI: PlanetName.MOON,
    ConstellationName.HASTA: PlanetName.MOON,
    ConstellationName.SRAVANA: PlanetName.MOON,
    ConstellationName.MRIGASIRA: PlanetName.MARS,
    ConstellationName.CHITTA: PlanetName.MARS,
    ConstellationName.DHANISHTA: PlanetName.MARS,
    ConstellationName.ARIDRA: PlanetName.RAHU,
    ConstellationName.SWATHI: PlanetName.RAHU,
    ConstellationName.SATABHISHA: PlanetName.RAHU,
    ConstellationName.PUNARVASU: PlanetName.JUPITER,
    ConstellationName.VISHAKHA: PlanetName.JUPITER,
    ConstellationName.POORVABHADRA: PlanetName.JUPITER,
    ConstellationName.PUSHYAMI: PlanetName.SATURN,
    ConstellationName.ANURADHA: PlanetName.SATURN,
    ConstellationName.UTTARABHADRA: PlanetName.SATURN,
    ConstellationName.ASLESHA: PlanetName.MERCURY,
    ConstellationName.JYESTA: PlanetName.MERCURY,
    ConstellationName.REVATHI: PlanetName.MERCURY,
}


def lord_of_constellation(constellation: ConstellationName) -> PlanetName:
    """Return the ruling planet for ``constellation``.

    Mirrors the C# ``Calculate.LordOfConstellation`` switch statement.
    """

    return _CONSTELLATION_LORDS.get(constellation, PlanetName.EMPTY)
