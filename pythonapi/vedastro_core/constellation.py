"""Constellation enumeration used across the core logic."""

from __future__ import annotations

from enum import Enum


class ConstellationName(str, Enum):
    """Enumeration of the 27 nakshatras.

    Values mirror the C# ``ConstellationName`` enum.
    """

    EMPTY = "Empty"
    ASWINI = "Aswini"
    BHARANI = "Bharani"
    KRITHIKA = "Krithika"
    ROHINI = "Rohini"
    MRIGASIRA = "Mrigasira"
    ARIDRA = "Aridra"
    PUNARVASU = "Punarvasu"
    PUSHYAMI = "Pushyami"
    ASLESHA = "Aslesha"
    MAKHA = "Makha"
    PUBBA = "Pubba"
    UTTARA = "Uttara"  # Uttara Phalguni
    HASTA = "Hasta"
    CHITTA = "Chitta"
    SWATHI = "Swathi"
    VISHAKHA = "Vishhaka"
    ANURADHA = "Anuradha"
    JYESTA = "Jyesta"
    MOOLA = "Moola"
    POORVASHADA = "Poorvashada"
    UTTARASHADA = "Uttarashada"
    SRAVANA = "Sravana"
    DHANISHTA = "Dhanishta"
    SATABHISHA = "Satabhisha"
    POORVABHADRA = "Poorvabhadra"
    UTTARABHADRA = "Uttarabhadra"
    REVATHI = "Revathi"

    @classmethod
    def from_str(cls, name: str) -> "ConstellationName":
        """Case-insensitive parser returning a :class:`ConstellationName`."""

        for member in cls:
            if member.value.lower() == name.lower():
                return member
        raise ValueError(f"Unknown constellation name: {name}")

    def __str__(self) -> str:  # pragma: no cover - trivial
        return str(self.value)
