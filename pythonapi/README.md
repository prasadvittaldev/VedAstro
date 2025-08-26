# VedAstro Python Workspace

This directory hosts the experimental Python port of VedAstro.  Phase 0
sets up tooling and documents the existing C# project so later phases can
focus on translating the library and API.

## Layout

```
pythonapi/
├─ vedastro_core/   # translated core logic (in progress)
├─ vedastro_api/    # FastAPI app exposing the core logic
├─ tests/           # pytest suite
├─ pyproject.toml   # dependencies and tool configuration
├─ requirements.txt
└─ requirements-dev.txt
```

## Installing

```bash
pip install -r requirements.txt
pip install -r requirements-dev.txt
```

## Running the API

```bash
uvicorn vedastro_api:app --reload
```

The API currently exposes:

- `/day-duration` – length of the day in hours for a given date and location.
- `/birth-period` – whether a moment is a day or night birth.
- `/moon-phase` – days since new moon for the supplied date.

All routes use Pydantic request and response models and are documented via the
auto-generated OpenAPI schema available at `http://localhost:8000/docs`.

Endpoint details are summarized in [`docs/api.md`](docs/api.md).

## Docker image

The service can be containerized using the provided `Dockerfile`:

```bash
docker build -t vedastro-api .
docker run -p 8000:8000 vedastro-api
```

GitHub Actions builds and publishes this image to the GitHub
Container Registry on every push.

## Domain model

Foundational types translated from the C# project are documented in
[`docs/domain-model.md`](docs/domain-model.md).  These include:

- `GeoLocation` — a named longitude/latitude pair with validation.
- `Time` — a timezone-aware `datetime` paired with a location.
- `PlanetName` — enumeration of planets and upagrahas with parsing helper.
- `ConstellationName` — enumeration of the 27 lunar mansions.

## Core algorithms

Early translations from the C# `Calculate.Core` module are documented in
[`docs/core-algorithms.md`](docs/core-algorithms.md).  They cover sunrise and
sunset times, day duration, helpers for classifying a moment as a day or
night birth, and the ruling planet for each constellation.

## Development tasks

```bash
ruff .
black --check .
mypy vedastro_core vedastro_api
pytest
```

The `tests/test_integration.py` module exercises the Python
service against the live C# API and performs a simple load test
to ensure endpoints remain responsive under repeated calls.

## C# inventory

A brief overview of the original C# solutions and their NuGet
dependencies is recorded in [`docs/inventory.md`](docs/inventory.md).
This serves as a reference during the porting effort.

Deployment notes are captured in [`docs/deployment.md`](docs/deployment.md).
