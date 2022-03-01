from __future__ import annotations

import dataclasses
import re

from cardmaker.model.base_element import BaseElement
from cardmaker.model.constants import HEIGHT
from cardmaker.model.constants import HORIZONTALALIGNMENT
from cardmaker.model.constants import IMAGE_STYLE
from cardmaker.model.constants import SIZE
from cardmaker.model.constants import T_HORIZONTALALIGNMENT
from cardmaker.model.constants import T_IMAGE_STYLE
from cardmaker.model.constants import T_SIZE


@dataclasses.dataclass(init=False, repr=False)
class Image(BaseElement):
    type: str = "Image"
    url: str = ""
    altText: str | None = None
    backgroundColor: str | None = None
    height: str | None = None
    horizontalAlignment: T_HORIZONTALALIGNMENT | None = None
    size: T_SIZE | None = None
    style: T_IMAGE_STYLE | None = None
    width: str | None = None

    def __init__(self, url: str, **kwargs: str) -> None:
        """
        Display an image. Accepts PNG, JPEG, and GIF

        Attributes can be set with keyword arguments, directly thought assigment
        or use `set_[attrname]()` methods. All `None` assigned attributes are
        excluded from final `.render()` of model.

        Invalid values will default to `None` when set through keywords or setters.

        Arguments:
            url : [required] URL/URI to the image (png, jpeg, or gif)

        Keyword Arguments:
            altText: [str] Alternate text describing the image
            backgroundColor: [str] Apply a background to a transparent image
            height: [str] The desired height of the image. Default behavior: `auto`
            horizontalAlignment: [str] Control horizontal position within parent
            size: [str] Control the approximate size of image
            style: [str] Control how Image is displayed
            width: [str] The desired width of the image, ending in 'px'. E.g., 50px

        """
        if not url:
            raise ValueError("url is required when defining an Image")
        self.url = url

        for key, value in kwargs.items():
            if not hasattr(self, f"set_{key}"):
                raise KeyError(f"Invalid keyword arguement: '{key}'")
            getattr(self, f"set_{key}")(value)

    def set_altText(self, text: str | None) -> None:
        """Alternate text describing the image"""
        self.altText = text

    def set_backgroundColor(self, color_code: str | None) -> None:
        """Applies a background to a transparent image"""
        self.backgroundColor = color_code

    def set_height(self, height: str | None) -> None:
        """
        The desired height of the image. Default behavior: `auto`
            `auto`, `stretch`, `[N]px`

        If specified as a pixel value, ending in 'px', E.g., 50px, the image
        will distort to fit that exact height. This overrides the size property.
        """
        # Allow 50px, 150px, etc
        match = re.match(r"^[0-9]*px$", str(height))
        if height is not None and height not in HEIGHT and not match:
            height = None
        self.height = height

    def set_horizontalAlignment(self, alignment: T_HORIZONTALALIGNMENT | None) -> None:
        """
        Controls how this element is horizontally positioned within its parent
            `left`, `center`, `right`
        """
        if alignment is not None and alignment not in HORIZONTALALIGNMENT:
            alignment = None
        self.horizontalAlignment = alignment

    def set_size(self, size: T_SIZE | None) -> None:
        """
        Control the approximate size of image. Physical dimensions vary per host
            `auto`, `stretch`, `small`, `medium`, `large`
        """
        if size is not None and size not in SIZE:
            size = None
        self.size = size

    def set_style(self, style: T_IMAGE_STYLE | None) -> None:
        """
        Control how Image is displayed
            `default`, `person`
        """
        if style is not None and style not in IMAGE_STYLE:
            style = None
        self.style = style

    def set_width(self, width: str | None) -> None:
        """The desired width of the image, ending in 'px'. E.g., 50px"""
        # Allow 50px, 150px, etc
        match = re.match(r"^[0-9]*px$", str(width))
        if width is not None and not match:
            width = None
        self.width = width
