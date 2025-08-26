# Core algorithms

Initial translations of routines from the C# `Calculate.Core` module.  The
functions documented here rely on the domain types defined in
[`docs/domain-model.md`](domain-model.md).

## Solar calculations

The module `vedastro_core.astro` uses the [`astral`](https://astral.readthedocs.io/)
package to obtain sunrise and sunset for a given [`Time`](../vedastro_core/time.py)
instance.  Results are cached with an in-memory LRU to avoid repeating heavy
solar computations for identical inputs:

- `sunrise_time(time)` – moment of sunrise at the location in ``time``.
- `sunset_time(time)` – sunset for the same location and date.
- `day_duration_hours(time)` – hours between sunrise and sunset.
- `moon_phase(time)` – days since the last new moon.
- `moon_phase_name(time)` – textual classification (e.g. "Full Moon").

## Day/night classification

Two helpers mirror the C# methods `IsDayBirth` and `IsNightBirth`:

- `is_day_birth(time)` returns ``True`` when ``time`` lies between sunrise and
  sunset on that day.
- `is_night_birth(time)` returns ``True`` when ``time`` is after sunset and
  before the next day's sunrise.

These utilities form the basis for many later calculations in the original
project, so verifying their behaviour early helps ensure parity with the .NET
implementation.

## Constellation lords

`lord_of_constellation(constellation)` returns the ruling
[`PlanetName`](../vedastro_core/planet.py) for a given
[`ConstellationName`](../vedastro_core/constellation.py).  The mapping mirrors
the switch statement in the C# `Calculate.LordOfConstellation` method.
