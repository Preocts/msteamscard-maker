"""
https://docs.microsoft.com/en-us/microsoftteams/platform/task-modules-and-cards/cards/cards-format?tabs=adaptive-md%2Cconnector-html#mention-support-within-adaptive-cards
"""
from __future__ import annotations

import dataclasses
import json
from typing import Any


@dataclasses.dataclass
class Mention:
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

    def __repr__(self) -> str:
        return json.dumps(self.asdict())

    def render(self, indent: int | None = None) -> str:
        """Render object as serialized string."""
        return json.dumps(self.asdict(), indent=indent)

    def asdict(self) -> dict[str, Any]:
        """Render object as dict."""
        obj = {
            "type": self.type,
            "text": self.text,
            "mentioned": {
                "id": self.id,
                "name": self.name,
            },
        }
        return obj
