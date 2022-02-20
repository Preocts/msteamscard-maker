from __future__ import annotations

import dataclasses
import json

from cardmaker.model.constants import COLORS
from cardmaker.model.constants import FONTTYPES
from cardmaker.model.constants import HORIZONTALALIGNMENT
from cardmaker.model.constants import T_COLORS
from cardmaker.model.constants import T_FONTTYPES
from cardmaker.model.constants import T_HORIZONTALALIGNMENT


@dataclasses.dataclass
class TextBlock:
    type: str = "TextBlock"
    text: str = ""
    color: str | None = None
    fontType: str | None = None
    horizontalAlignment: str | None = None
    isSubtle: bool | None = None

    def __repr__(self) -> str:
        # Remove all None values
        cleaned = {k: v for k, v in dataclasses.asdict(self).items() if v is not None}
        return json.dumps(cleaned)

    @property
    def render(self) -> str:
        return str(self)

    def set_color(self, color: T_COLORS | None) -> None:
        """`default`, `dark`, `light`, `accent`, `good`, `warning`, `attention`"""
        if color is not None and color not in COLORS:
            color = None
        self.color = color

    def set_fontType(self, fonttype: T_FONTTYPES | None) -> None:
        """`default`, `monospace`"""
        if fonttype is not None and fonttype not in FONTTYPES:
            fonttype = None
        self.fontType = fonttype

    def set_horizontalAlignment(self, alignment: T_HORIZONTALALIGNMENT | None) -> None:
        """`left`, `center`, `right`"""
        if alignment is not None and alignment not in HORIZONTALALIGNMENT:
            alignment = None
        self.horizontalAlignment = alignment

    def set_isSubtle(self, flag: bool | None) -> None:
        self.isSubtle = bool(flag) if flag is not None else None
