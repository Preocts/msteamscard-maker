from __future__ import annotations

import pytest
from cardmaker.model.elements.textblock import TextBlock


@pytest.fixture
def textblock() -> TextBlock:
    return TextBlock()


def test_required_fields(textblock: TextBlock) -> None:
    assert textblock.type == "TextBlock"
    assert textblock.text == ""


def test_repl(textblock: TextBlock) -> None:
    assert str(textblock) == '{"type": "TextBlock", "text": ""}'


def test_render(textblock: TextBlock) -> None:
    assert textblock.render == '{"type": "TextBlock", "text": ""}'


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
