"""Time representation used across the core library."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Dict

from .geo import GeoLocation


@dataclass(frozen=True)
class Time:
    """A timezone-aware moment at a specific :class:`GeoLocation`."""

    dt: datetime
    location: GeoLocation

    def __post_init__(self) -> None:
        if self.dt.tzinfo is None:
            raise ValueError("dt must be timezone-aware")

    @property
    def utc_datetime(self) -> datetime:
        """Return the instant in UTC."""
        return self.dt.astimezone(timezone.utc)

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to a JSON-serialisable dictionary."""
        return {
            "dt": self.dt.isoformat(),
            "location": self.location.to_dict(),
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Time":
        """Deserialize a :class:`Time` from *data*."""
        return cls(
            dt=datetime.fromisoformat(data["dt"]),
            location=GeoLocation.from_dict(data["location"]),
        )
