import pytest

from vedastro_core import ConstellationName, PlanetName, lord_of_constellation

_CASES = {
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


@pytest.mark.parametrize("constellation, expected", list(_CASES.items()))
def test_lord_of_constellation(constellation, expected):
    assert lord_of_constellation(constellation) == expected
