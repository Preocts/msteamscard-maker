from typing import Literal

EMPTY_WEBHOOK_CARD = {
    "type": "message",
    "attachments": [
        {
            "contentType": "application/vnd.microsoft.card.adaptive",
            "content": {
                "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
                "version": "1.2",
                "type": "AdaptiveCard",
                "body": [],
                "actions": [],
                "msteams": {
                    "width": "Full",
                    "entities": [],
                },
            },
        }
    ],
}

T_COLORS = Literal[
    "default",
    "dark",
    "light",
    "accent",
    "good",
    "warning",
    "attention",
]

COLORS = [
    "default",
    "dark",
    "light",
    "accent",
    "good",
    "warning",
    "attention",
]

T_FONTTYPES = Literal[
    "default",
    "monospace",
]

FONTTYPES = [
    "default",
    "monospace",
]

T_HORIZONTALALIGNMENT = Literal[
    "left",
    "center",
    "right",
]
HORIZONTALALIGNMENT = [
    "left",
    "center",
    "right",
]

T_FONTSIZE = Literal[
    "default",
    "small",
    "medium",
    "large",
    "extraLarge",
]

FONTSIZE = [
    "default",
    "small",
    "medium",
    "large",
    "extraLarge",
]

T_WEIGHT = Literal[
    "default",
    "lighter",
    "bolder",
]

WEIGHT = [
    "default",
    "lighter",
    "bolder",
]

T_STYLE = Literal[
    "default",
    "heading",
]

STYLE = [
    "default",
    "heading",
]

T_IMAGE_STYLE = Literal[
    "default",
    "person",
]

IMAGE_STYLE = [
    "default",
    "person",
]

T_HEIGHT = Literal[
    "auto",
    "stretch",
]

HEIGHT = [
    "auto",
    "stretch",
]

T_SPACING = Literal[
    "default",
    "none",
    "small",
    "medium",
    "large",
    "extraLarge",
    "padding",
]

SPACING = [
    "default",
    "none",
    "small",
    "medium",
    "large",
    "extraLarge",
    "padding",
]

T_SIZE = Literal[
    "auto",
    "stretch",
    "small",
    "medium",
    "large",
]

SIZE = [
    "auto",
    "stretch",
    "small",
    "medium",
    "large",
]
