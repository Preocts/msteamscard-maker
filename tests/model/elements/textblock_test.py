from __future__ import annotations

import pytest
from cardmaker.model.elements.textblock import TextBlock


@pytest.fixture
def textblock() -> TextBlock:
    return TextBlock("")


def test_required_fields(textblock: TextBlock) -> None:
    assert textblock.type == "TextBlock"
    assert textblock.text == ""


def test_set_text(textblock: TextBlock) -> None:
    textblock.set_text("This is a test")
    assert textblock.text == "This is a test"


@pytest.mark.parametrize(
    ("attr", "value", "expected"),
    (
        ("color", "default", "default"),
        ("color", None, None),
        ("color", "invalid", None),
        ("fontType", "default", "default"),
        ("fontType", None, None),
        ("fontType", "invalid", None),
        ("horizontalAlignment", "left", "left"),
        ("horizontalAlignment", None, None),
        ("horizontalAlignment", "invalid", None),
        ("isSubtle", False, False),
        ("isSubtle", None, None),
        ("isSubtle", "invalid", True),
        ("maxLines", 1, 1),
        ("maxLines", None, None),
        ("maxLines", "invalid", None),
        ("maxLines", -10, None),
        ("size", "default", "default"),
        ("size", None, None),
        ("size", "invalid", None),
        ("weight", "default", "default"),
        ("weight", None, None),
        ("weight", "invalid", None),
        ("wrap", False, False),
        ("wrap", None, None),
        ("wrap", "invalid", True),
        ("style", "default", "default"),
        ("style", None, None),
        ("style", "invalid", None),
        ("height", "auto", "auto"),
        ("height", None, None),
        ("height", "invalid", None),
        ("separator", False, False),
        ("separator", None, None),
        ("separator", "invalid", True),
        ("spacing", "none", "none"),
        ("spacing", None, None),
        ("spacing", "invalid", None),
        ("id", "none", "none"),
        ("id", None, None),
        ("isVisible", False, False),
        ("isVisible", None, None),
        ("isVisible", "invalid", True),
    ),
)
def test_optional_setters(
    textblock: TextBlock,
    attr: str,
    value: str | bool | None,
    expected: str | None,
) -> None:
    assert getattr(textblock, attr) is None
    getattr(textblock, f"set_{attr}")(value)
    assert getattr(textblock, attr) == expected


@pytest.mark.parametrize(
    ("attr", "value"),
    (
        ("color", "dark"),
        ("fontType", "monospace"),
        ("horizontalAlignment", "right"),
        ("isSubtle", True),
        ("maxLines", 10),
        ("size", "small"),
        ("weight", "bolder"),
        ("wrap", True),
        ("style", "heading"),
        ("height", "stretch"),
        ("separator", True),
        ("id", "test"),
        ("isVisible", True),
    ),
)
def test_keyword_arguments(attr: str, value: str | bool | int) -> None:
    param = {attr: value}
    result = TextBlock("", **param)
    assert getattr(result, attr) == value


def test_text_positional() -> None:
    newobj = TextBlock("test")
    assert newobj.text == "test"


def test_invalid_keyword_raises() -> None:
    with pytest.raises(KeyError, match="Invalid keyword arguement"):
        TextBlock("", invalid="Test")
