# API Endpoints

The Python FastAPI service exposes a small set of translated VedAstro
calculators. Each endpoint uses Pydantic models for request validation and
response serialization. Interactive documentation is available at
`/docs` when running the server.

## GET `/day-duration`

**Parameters**
- `year` – calendar year
- `month` – calendar month
- `day` – calendar day
- `latitude` – location latitude
- `longitude` – location longitude
- `tz_offset` – timezone offset from UTC in hours (default `0`)

**Response**
```json
{"duration_hours": 12.0}
```

## GET `/birth-period`

**Parameters**
- `year`, `month`, `day`, `hour`, `minute` – timestamp of the birth
- `latitude`, `longitude` – location coordinates
- `tz_offset` – timezone offset from UTC in hours (default `0`)

**Response**
```json
{"is_day_birth": true, "is_night_birth": false}
```

## GET `/moon-phase`

**Parameters**
- `year`, `month`, `day` – date to evaluate
- `tz_offset` – timezone offset from UTC in hours (default `0`)

**Response**
```json
{"phase": 14.8}
```
