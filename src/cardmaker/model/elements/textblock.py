from __future__ import annotations

import dataclasses
import json
from typing import Any

from cardmaker.model.constants import COLORS
from cardmaker.model.constants import FONTSIZE
from cardmaker.model.constants import FONTTYPES
from cardmaker.model.constants import HEIGHT
from cardmaker.model.constants import HORIZONTALALIGNMENT
from cardmaker.model.constants import SPACING
from cardmaker.model.constants import STYLE
from cardmaker.model.constants import T_COLORS
from cardmaker.model.constants import T_FONTSIZE
from cardmaker.model.constants import T_FONTTYPES
from cardmaker.model.constants import T_HEIGHT
from cardmaker.model.constants import T_HORIZONTALALIGNMENT
from cardmaker.model.constants import T_SPACING
from cardmaker.model.constants import T_STYLE
from cardmaker.model.constants import T_WEIGHT
from cardmaker.model.constants import WEIGHT


@dataclasses.dataclass(init=False)
class TextBlock:
    """
    Defines a TextBlock Card Element used inside `content.body[]`

    Attributes can be set with keyword arguments, directly thought assigment
    or use `set_[attrname]()` methods. All `None` assigned attributes are
    excluded from final `.render()` of model.

    Invalid values will default to `None` when set through keywords or setters.

    Keyword Arguments:
        text: [str] Text to display. A subset of markdown is supported
        color: [str] Controls the color of TextBlock elements.
        fontType: [str] Type of font to use for rendering
        horizontalAlignment: [str] Controls the horizontal text alignment
        isSubtle: [bool] If true displays text slightly toned down
        maxLines: [int] Specify the maximum number of lines to display
        size: [str] Control size of text
        weight: [str] Controls the weight of TextBlock elements
        wrap: [bool] If true, allow text to wrap. Otherwise text is clipped
        style: [str] The style of this TextBlock for accessibility purposes
        height: [str] Specify the height of the element
        separator: [bool] When True, draw a sparating line at the top of the element
        spacing: [str] Controls spacing between this element and the preceding element
        id: [str] A unique indentifier associated with the item
        idVisible: [bool] If False, this item will be removed from the visual tree
    """

    type: str = "TextBlock"
    text: str = ""
    color: str | None = None
    fontType: str | None = None
    horizontalAlignment: str | None = None
    isSubtle: bool | None = None
    maxLines: int | None = None
    size: str | None = None
    weight: str | None = None
    wrap: bool | None = None
    style: str | None = None
    height: str | None = None
    separator: bool | None = None
    spacing: str | None = None
    id: str | None = None
    isVisible: bool | None = None
    fallback: str = "drop"

    def __init__(self, **kwargs: str | int | bool | None) -> None:
        for key, value in kwargs.items():
            if not hasattr(self, f"set_{key}"):
                raise KeyError(f"Invalid keyword arguement: '{key}'")
            getattr(self, f"set_{key}")(value)

    def __repr__(self) -> str:
        return json.dumps(self.asdict)

    @property
    def render(self) -> str:
        """Render object as serialized string. All None values are removed"""
        return str(self)

    @property
    def asdict(self) -> dict[str, Any]:
        """All None values are removed from output"""
        return {k: v for k, v in dataclasses.asdict(self).items() if v is not None}

    def set_text(self, text: str) -> None:
        """Text to display. A subset of markdown is supported"""
        self.text = text

    def set_color(self, color: T_COLORS | None) -> None:
        """
        Controls the color of TextBlock elements.
            `default`, `dark`, `light`, `accent`, `good`, `warning`, `attention`
        """
        if color is not None and color not in COLORS:
            color = None
        self.color = color

    def set_fontType(self, fonttype: T_FONTTYPES | None) -> None:
        """
        Type of font to use for rendering
            `default`, `monospace`
        """
        if fonttype is not None and fonttype not in FONTTYPES:
            fonttype = None
        self.fontType = fonttype

    def set_horizontalAlignment(self, alignment: T_HORIZONTALALIGNMENT | None) -> None:
        """
        Controls the horizontal text alignment. Default `left` or from parent container
            `left`, `center`, `right`
        """
        if alignment is not None and alignment not in HORIZONTALALIGNMENT:
            alignment = None
        self.horizontalAlignment = alignment

    def set_isSubtle(self, flag: bool | None) -> None:
        """If true displays text slightly toned down to appear less prominent"""
        self.isSubtle = bool(flag) if flag is not None else None

    def set_maxLines(self, lines: int | None) -> None:
        """Specify the maximum number of lines to display"""
        if not isinstance(lines, int) or lines < 1:
            lines = None
        self.maxLines = lines

    def set_size(self, fontsize: T_FONTSIZE | None) -> None:
        """
        Control size of text
            `default`, `small`, `medium`, `large`, `extraLarge`
        """
        if fontsize is not None and fontsize not in FONTSIZE:
            fontsize = None
        self.size = fontsize

    def set_weight(self, weight: T_WEIGHT | None) -> None:
        """
        Controls the weight of TextBlock elements
            `default`, `lighter`, `bolder`
        """
        if weight is not None and weight not in WEIGHT:
            weight = None
        self.weight = weight

    def set_wrap(self, wrap: bool | None) -> None:
        """If true, allow text to wrap. Otherwise text is clipped"""
        self.wrap = bool(wrap) if wrap is not None else None

    def set_style(self, style: T_STYLE | None) -> None:
        """
        The style of this TextBlock for accessibility purposes
            `default`, `heading`
        """
        if style is not None and style not in STYLE:
            style = None
        self.style = style

    def set_height(self, height: T_HEIGHT | None) -> None:
        """
        Specify the height of the element
            `auto`, `stretch`
        """
        if height is not None and height not in HEIGHT:
            height = None
        self.height = height

    def set_separator(self, flag: bool | None) -> None:
        """When True, draw a sparating line at the top of the element"""
        self.separator = bool(flag) if flag is not None else None

    def set_spacing(self, spacing: T_SPACING | None) -> None:
        """
        Controls the amount of spacing between this element and the preceding element
            'default', 'none', 'small', 'medium', 'large', 'extraLarge', 'padding'
        """
        if spacing is not None and spacing not in SPACING:
            spacing = None
        self.spacing = spacing

    def set_id(self, id_: str | None) -> None:
        """A unique indentifier associated with the item"""
        self.id = id_

    def set_isVisible(self, flag: bool | None) -> None:
        """If False, this item will be removed from the visual tree"""
        self.isVisible = bool(flag) if flag is not None else None
