from __future__ import annotations

import json
from typing import Any
from typing import Union

from cardmaker.model.constants import EMPTY_WEBHOOK_CARD
from cardmaker.model.elements.factset import FactSet
from cardmaker.model.elements.image import Image
from cardmaker.model.elements.media import Media
from cardmaker.model.elements.mention import Mention
from cardmaker.model.elements.richtextblock import RichTextBlock
from cardmaker.model.elements.textblock import TextBlock
from cardmaker.model.elements.textrun import TextRun

T_ELEMENTS = Union[
    TextBlock,
    FactSet,
    Image,
    Media,
    RichTextBlock,
]
T_ENTITIES = Mention


class WebhookCard:
    # Helper attributes allowing creation of elements without imports
    new_textblock = TextBlock
    new_image = Image
    new_media = Media
    new_factset = FactSet
    new_mention = Mention
    new_richtextblock = RichTextBlock
    new_textrun = TextRun

    def __init__(self) -> None:
        self._empty_card = json.dumps(EMPTY_WEBHOOK_CARD)
        self.body: list[T_ELEMENTS] = []
        self.entities: list[T_ENTITIES] = []

    def __repr__(self) -> str:
        return json.dumps(self.asdict())

    def render(self, indent: int | None = None) -> str:
        """Render webhook card as serialized JSON format"""
        return json.dumps(self.asdict(), indent=indent)

    def asdict(self) -> dict[str, Any]:
        """Translate object to webhook structure as dictionary"""
        card = json.loads(self._empty_card)
        for element in self.body:
            card["attachments"][0]["content"]["body"].append(element.asdict())

        for entity in self.entities:
            card["attachments"][0]["content"]["msteams"]["entities"].append(
                entity.asdict()
            )
        return card

    def add_element(self, element: T_ELEMENTS) -> None:
        """Add any valid body element to card. Will appear in order added."""
        self.body.append(element)

    def add_mention(self, mention: Mention) -> None:
        """Include a mention in the card."""
        is_referenced = False
        for element in self.body:
            if hasattr(element, "text") and mention.text in element.text:  # type: ignore # noqa: E501
                is_referenced = True
                break
        if not is_referenced:
            raise ValueError(
                f"Mention text '{mention.text}' referenced before defined in "
                "an element. Elements containing the mention text must be added first."
            )
        self.entities.append(mention)
