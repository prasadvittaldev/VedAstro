"""Planet enumeration used throughout the core logic."""

from __future__ import annotations

from enum import Enum


class PlanetName(str, Enum):
    """Enumeration of planets and upagrahas.

    Values follow the C# ``PlanetName.PlanetNameEnum``.
    """

    EMPTY = "Empty"
    SUN = "Sun"
    MOON = "Moon"
    MARS = "Mars"
    MERCURY = "Mercury"
    JUPITER = "Jupiter"
    VENUS = "Venus"
    SATURN = "Saturn"
    RAHU = "Rahu"
    KETU = "Ketu"
    EARTH = "Earth"
    DHUMA = "Dhuma"
    VYATIPAATA = "Vyatipaata"
    PARIVESHA = "Parivesha"
    INDRACHAAPA = "Indrachaapa"
    UPAKETU = "Upaketu"
    KAALA = "Kaala"
    MRITYU = "Mrityu"
    ARTHAPRAHAARA = "Arthaprahaara"
    YAMAGHANTAKA = "Yamaghantaka"
    GULIKA = "Gulika"
    MAANDI = "Maandi"

    @classmethod
    def from_str(cls, name: str) -> "PlanetName":
        """Case-insensitive parser returning a :class:`PlanetName`.

        Raises ``ValueError`` if *name* does not match any member.
        """

        for member in cls:
            if member.value.lower() == name.lower():
                return member
        raise ValueError(f"Unknown planet name: {name}")

    def __str__(self) -> str:  # pragma: no cover - trivial
        return str(self.value)
