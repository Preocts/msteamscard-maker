from __future__ import annotations

import dataclasses
from typing import Any

from cardmaker.model.base_element import BaseElement
from cardmaker.model.constants import HORIZONTALALIGNMENT
from cardmaker.model.constants import T_HORIZONTALALIGNMENT
from cardmaker.model.elements.textrun import TextRun


@dataclasses.dataclass(repr=False)
class RichTextBlock(BaseElement):
    type: str = "RichTextBlock"
    inlines: list[TextRun] = dataclasses.field(default_factory=list)
    horizontalAlignment: T_HORIZONTALALIGNMENT | None = None
    new_textrun = TextRun

    def asdict(self) -> dict[str, Any]:
        self_dict = super().asdict()
        self_dict["inlines"] = [tr.asdict() for tr in self.inlines]
        return self_dict

    def add_inline(self, textrun: TextRun) -> None:
        """Add a textrun to the element. Will appear in order added"""
        self.inlines.append(textrun)

    def set_horizontalAlignment(self, value: T_HORIZONTALALIGNMENT | None) -> None:
        """Control the horizontal text alignment"""
        if value is not None and value not in HORIZONTALALIGNMENT:
            value = None
        self.horizontalAlignment = value
