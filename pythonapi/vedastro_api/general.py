"""Miscellaneous endpoints mirroring the C# GeneralAPI."""

from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def home() -> dict[str, str]:
    """Return a simple welcome message."""
    return {"message": "VedAstro Python API"}
