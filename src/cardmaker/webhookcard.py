from __future__ import annotations

import json
from typing import Union

from cardmaker.model.constants import EMPTY_WEBHOOK_CARD
from cardmaker.model.elements.factset import FactSet
from cardmaker.model.elements.textblock import TextBlock
from cardmaker.model.entities.mention import Mention

T_ELEMENTS = Union[TextBlock, FactSet]
T_ENTITIES = Mention


class WebhookCard:
    def __init__(self) -> None:
        self._empty_card = json.dumps(EMPTY_WEBHOOK_CARD)
        self.body: list[T_ELEMENTS] = []
        self.entities: list[T_ENTITIES] = []

    def __repr__(self) -> str:
        card = json.loads(self._empty_card)
        for element in self.body:
            card["attachments"][0]["content"]["body"].append(element.asdict())

        for entity in self.entities:
            card["attachments"][0]["content"]["msteams"]["entities"].append(
                entity.asdict()
            )
        return json.dumps(card)

    @property
    def render(self) -> str:
        """Renders a serialized string of the webhook payload"""
        return str(self)

    def add_element(self, element: T_ELEMENTS) -> None:
        """Add any valid body element to card. Will appear in order added."""
        self.body.append(element)

    def add_mention(self, mention: Mention) -> None:
        """Include a mention in the card. Does not check if `text` is referenced."""
        self.entities.append(mention)
