from __future__ import annotations

import pytest
from cardmaker.model.elements.image import Image


@pytest.fixture
def image() -> Image:
    return Image("https://127.0.0.1")


def test_url_required() -> None:
    with pytest.raises(ValueError, match="url is required"):
        Image("")


def test_required_values_set() -> None:
    obj = Image("mock")

    assert obj.type == "Image"
    assert obj.url == "mock"


@pytest.mark.parametrize(
    ("attr", "value", "expected"),
    (
        ("altText", "default", "default"),
        ("altText", None, None),
        ("backgroundColor", "default", "default"),
        ("backgroundColor", None, None),
        ("height", "stretch", "stretch"),
        ("height", "100px", "100px"),
        ("height", "invalid", None),
        ("height", None, None),
        ("horizontalAlignment", "center", "center"),
        ("horizontalAlignment", "invalid", None),
        ("horizontalAlignment", None, None),
        ("size", "large", "large"),
        ("size", "invalid", None),
        ("size", None, None),
        ("style", "person", "person"),
        ("style", "invalid", None),
        ("style", None, None),
        ("width", "100px", "100px"),
        ("width", "invalid", None),
        ("width", None, None),
    ),
)
def test_optional_setters(
    image: Image,
    attr: str,
    value: str | bool | None,
    expected: str | None,
) -> None:
    assert getattr(image, attr) is None
    getattr(image, f"set_{attr}")(value)
    assert getattr(image, attr) == expected


@pytest.mark.parametrize(
    ("attr", "value"),
    (
        ("altText", "default"),
        ("backgroundColor", "default"),
        ("height", "100px"),
        ("horizontalAlignment", "center"),
        ("size", "large"),
        ("style", "person"),
        ("width", "100px"),
    ),
)
def test_keyword_arguments(attr: str, value: str) -> None:
    param = {attr: value}
    result = Image("mock_url", **param)
    assert getattr(result, attr) == value


def test_invalid_keyword_raises() -> None:
    with pytest.raises(KeyError, match="Invalid keyword arguement"):
        Image("test", invalid="Test")
