# Domain model

Foundational data types used by the Python port of VedAstro.

## GeoLocation

Represents a named position on Earth.

```python
GeoLocation(name="Tokyo", longitude=139.83, latitude=35.65)
```

- Validates that longitude is within ``-180..180`` and latitude within ``-90..90``.
- ``to_dict()`` and ``from_dict()`` round-trip the instance for JSON serialisation.

## Time

Combines a timezone-aware ``datetime`` with a ``GeoLocation``.

```python
dt = datetime(2024, 1, 1, 12, tzinfo=timezone.utc)
loc = GeoLocation("Greenwich", 0.0, 51.48)
Time(dt=dt, location=loc)
```

- ``utc_datetime`` returns the instant in UTC.
- ``to_dict()``/``from_dict()`` serialise the structure.

## PlanetName

Enum listing planets and upagrahas.

```python
PlanetName.MARS
PlanetName.from_str("sun")
```

The ``from_str`` classmethod parses names in a case-insensitive manner.

## ConstellationName

Enum of the 27 lunar mansions (nakshatras).

```python
ConstellationName.ASWINI
ConstellationName.from_str("revathi")
```
