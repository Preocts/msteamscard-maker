"""
https://docs.microsoft.com/en-us/microsoftteams/platform/task-modules-and-cards/cards/cards-format?tabs=adaptive-md%2Cconnector-html#mention-support-within-adaptive-cards
"""
from __future__ import annotations

import dataclasses
from typing import Any

from cardmaker.model.base_element import BaseElement


@dataclasses.dataclass(repr=False)
class Mention(BaseElement):
    """
    Defines a mention object for Adaptive Card.

    Must be included in the `msteams.entities[]` block of the card.

    Args:
        text: Matches text from TextBlock objects. example: "<at>Name</at>"
        id: AzureAD UID of target or valid email of target
        name: Replaces `text` when mention is applied to card
        type: Required: "mention"
    """

    text: str
    id: str
    name: str
    type: str = "mention"

    def asdict(self) -> dict[str, Any]:
        """Render object as dict."""
        # Overwrites base class to format object's specific implementation
        obj = {
            "type": self.type,
            "text": self.text,
            "mentioned": {
                "id": self.id,
                "name": self.name,
            },
        }
        return obj
