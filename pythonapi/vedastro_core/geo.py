"""Geographic location utilities."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict


@dataclass(frozen=True)
class GeoLocation:
    """A named location with longitude and latitude."""

    name: str
    longitude: float
    latitude: float

    def __post_init__(self) -> None:
        if not (-180.0 <= self.longitude <= 180.0):
            raise ValueError("Longitude must be between -180 and 180 degrees")
        if not (-90.0 <= self.latitude <= 90.0):
            raise ValueError("Latitude must be between -90 and 90 degrees")

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to a JSON-serialisable dictionary."""
        return {
            "name": self.name,
            "longitude": self.longitude,
            "latitude": self.latitude,
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "GeoLocation":
        """Deserialize a :class:`GeoLocation` from *data*."""
        return cls(
            name=data["name"],
            longitude=float(data["longitude"]),
            latitude=float(data["latitude"]),
        )
