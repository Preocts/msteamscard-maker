from __future__ import annotations

import pytest
from cardmaker.model.elements.textrun import TextRun


@pytest.fixture
def textrun() -> TextRun:
    return TextRun("mock")


def test_init_setup(textrun: TextRun) -> None:
    assert textrun.type == "TextRun"
    assert textrun.text == "mock"


def test_empty_asdict(textrun: TextRun) -> None:
    assert textrun.asdict() == {"type": "TextRun", "text": "mock"}


@pytest.mark.parametrize(
    ("attr", "value", "expected"),
    (
        ("color", "default", "default"),
        ("color", None, None),
        ("color", "invalid", None),
        ("fontType", "monospace", "monospace"),
        ("fontType", None, None),
        ("fontType", "invalid", None),
        ("highlight", False, False),
        ("highlight", None, None),
        ("highlight", "invalid", True),
        ("isSubtle", False, False),
        ("isSubtle", None, None),
        ("isSubtle", "invalid", True),
        ("italic", False, False),
        ("italic", None, None),
        ("italic", "invalid", True),
        ("size", "small", "small"),
        ("size", None, None),
        ("size", "invalid", None),
        ("strikethrough", False, False),
        ("strikethrough", None, None),
        ("strikethrough", "invalid", True),
        ("underline", False, False),
        ("underline", None, None),
        ("underline", "invalid", True),
        ("weight", "bolder", "bolder"),
        ("weight", None, None),
        ("weight", "invalid", None),
    ),
)
def test_optional_setters(
    textrun: TextRun,
    attr: str,
    value: str | bool | None,
    expected: str | None,
) -> None:
    assert getattr(textrun, attr) is None
    getattr(textrun, f"set_{attr}")(value)
    assert getattr(textrun, attr) == expected


@pytest.mark.parametrize(
    ("attr", "value"),
    (
        ("color", "dark"),
        ("fontType", "monospace"),
        ("highlight", True),
        ("isSubtle", True),
        ("italic", True),
        ("size", "small"),
        ("strikethrough", True),
        ("underline", True),
        ("weight", "bolder"),
    ),
)
def test_keyword_arguments(attr: str, value: str | bool | int) -> None:
    param = {attr: value}
    result = TextRun("mock", **param)
    assert getattr(result, attr) == value


def test_text_positional() -> None:
    newobj = TextRun("test")
    assert newobj.text == "test"


def test_text_positional_requires_truthy() -> None:
    with pytest.raises(ValueError, match="'text' is required"):
        _ = TextRun("")


def test_invalid_keyword_raises() -> None:
    with pytest.raises(KeyError, match="Invalid keyword arguement"):
        TextRun("mock", invalid="Test")
