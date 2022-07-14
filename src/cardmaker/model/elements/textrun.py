from __future__ import annotations

import dataclasses

from cardmaker.model.base_element import BaseElement
from cardmaker.model.constants import COLORS
from cardmaker.model.constants import FONTTYPES
from cardmaker.model.constants import SIZE
from cardmaker.model.constants import T_COLORS
from cardmaker.model.constants import T_FONTTYPES
from cardmaker.model.constants import T_SIZE
from cardmaker.model.constants import T_WEIGHT
from cardmaker.model.constants import WEIGHT


@dataclasses.dataclass(repr=False)
class TextRun(BaseElement):
    """
    Defines a TextRun element

    Attributes can be set with keyword arguments, directly thought assigment
    or use `set_[attrname]()` methods. All `None` assigned attributes are
    excluded from final `.render()` of model.

    Invalid values will default to `None` when set through keywords or setters.

    Arguments:
        text: [str] Text to display. Markdown is not supported

    Keyword Arguments:
        color: [str] Control the color of TextBlock elements
        fontType: [str] Type of font to use for rendering
        highlight: [bool] If true, displays the text highlighted
        isSubtle: [bool] If true displays text slightly toned down
        italic: [bool] If true, displays the text using italic font
        size: [str] Control size of text
        strikethrough: [bool] If true, displays the text with strikethrough
        underline: [bool] If true, displays the text with an underline
        weight: [str] Control the weight of TextBlock elements
    """

    type: str = "TextRun"  # noqa: A003
    text: str = ""
    color: str | None = None
    fontType: str | None = None
    highlight: bool | None = None
    isSubtle: bool | None = None
    italic: bool | None = None
    size: str | None = None
    strikethrough: bool | None = None
    underline: bool | None = None
    weight: str | None = None

    def __init__(self, text: str, **kwargs: str | int | bool | None) -> None:
        if not text:
            raise ValueError("'text' is required when defining a TextRun")

        self.text = text
        for key, value in kwargs.items():
            if not hasattr(self, f"set_{key}"):
                raise KeyError(f"Invalid keyword arguement: '{key}'")
            getattr(self, f"set_{key}")(value)

    def set_color(self, color: T_COLORS | None) -> None:
        """
        Control the color of TextBlock elements
            `default`, `dark`, `light`, `accent`, `good`, `warning`, `attention`
        """
        if color is not None and color not in COLORS:
            color = None
        self.color = color

    def set_fontType(self, font_type: T_FONTTYPES | None) -> None:
        """
        Type of font to use for rendering
            `default`, `monospace`
        """
        if font_type is not None and font_type not in FONTTYPES:
            font_type = None
        self.fontType = font_type

    def set_highlight(self, flag: bool | None) -> None:
        """If true, displays the text highlighted"""
        self.highlight = bool(flag) if flag is not None else None

    def set_isSubtle(self, flag: bool | None) -> None:
        """If true, displays text slightly toned down to appear less prominent"""
        self.isSubtle = bool(flag) if flag is not None else None

    def set_italic(self, flag: bool | None) -> None:
        """If true, displays the text using italic font"""
        self.italic = bool(flag) if flag is not None else None

    def set_size(self, size: T_SIZE | None) -> None:
        """
        Control size of text
            `default`, `small`, `medium`, `large`, `extraLarge`
        """
        if size is not None and size not in SIZE:
            size = None
        self.size = size

    def set_strikethrough(self, flag: bool | None) -> None:
        """If true, displays the text with strikethrough"""
        self.strikethrough = bool(flag) if flag is not None else None

    def set_underline(self, flag: bool | None) -> None:
        """If true, displays the text with underline"""
        self.underline = bool(flag) if flag is not None else None

    def set_weight(self, weight: T_WEIGHT | None) -> None:
        """
        Control the weight of TextBlock elements
            `default`, `lighter`, `bolder`
        """
        if weight is not None and weight not in WEIGHT:
            weight = None
        self.weight = weight
