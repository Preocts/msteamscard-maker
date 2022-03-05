from __future__ import annotations

from unittest.mock import patch

import pytest
from cardmaker.model.elements.richtextblock import RichTextBlock
from cardmaker.model.elements.textrun import TextRun

BASE_ELEMENT = {
    "type": "RichTextBlock",
    "inlines": [],
}

MOCK_TEXTRUN = TextRun("mock", italic=True)


@pytest.fixture
def rtb() -> RichTextBlock:
    return RichTextBlock()


def test_init_attrs(rtb: RichTextBlock) -> None:
    assert rtb.type == "RichTextBlock"
    assert rtb.inlines == []


def test_add_inline_from_asdict(rtb: RichTextBlock) -> None:
    with patch.dict(BASE_ELEMENT, {"inlines": []}) as expected:
        for _ in range(10):
            rtb.add_inline(MOCK_TEXTRUN)
            expected["inlines"].append(MOCK_TEXTRUN.asdict())

        assert rtb.asdict() == expected


def test_add_line_from_helper_attr(rtb: RichTextBlock) -> None:
    with patch.dict(BASE_ELEMENT, {"inlines": []}) as expected:
        new_tr = rtb.new_textrun("mock", size="small")
        rtb.add_inline(new_tr)
        expected["inlines"].append(new_tr.asdict())

        assert rtb.asdict() == expected


@pytest.mark.parametrize(
    ("value", "expected"),
    (
        ("right", "right"),
        ("invalid", None),
        (None, None),
    ),
)
def test_set_horizontal_alignment(
    rtb: RichTextBlock,
    value: str | None,
    expected: str | None,
) -> None:
    rtb.set_horizontalAlignment(value)  # type: ignore

    assert rtb.horizontalAlignment == expected
