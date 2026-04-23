"""Test the add function."""

from template_python_library import add


def test_add() -> None:
    """Test the add function."""
    assert add(2, 3) == 5  # noqa: PLR2004
