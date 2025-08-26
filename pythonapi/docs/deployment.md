# Deployment

This workspace includes tooling for containerizing and deploying the
FastAPI service.

## Docker

The `Dockerfile` builds a minimal image containing the translated
core library and API.  It exposes the service on port `8000` and
runs `uvicorn` as the entry point.

## Continuous delivery

The workflow `.github/workflows/docker.yml` builds the image and
publishes it to the GitHub Container Registry whenever changes are
pushed to the `pythonapi` directory.

## Integration tests

`tests/test_integration.py` calls the live C# service at
`https://api.vedastro.org` to verify that Python endpoints produce
matching results.  The same test suite also issues repeated requests
to confirm basic performance under load.
