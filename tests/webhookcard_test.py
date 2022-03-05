from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import pytest
from cardmaker.model.constants import EMPTY_WEBHOOK_CARD
from cardmaker.webhookcard import WebhookCard

EXPECTED_TEST_CARD = json.load(Path("tests/fixtures/webhook_card.json").open())
TEST_TEXTBLOCK = {
    "text": "<at>General Kenobi</at>",
    "weight": "bolder",
    "size": "large",
}
TEST_IMAGE = {
    "url": "https://127.0.0.1",
}
TEST_MENTION = [
    "<at>General Kenobi</at>",
    "24601",
    "Obiwan",
]
TEST_FACTSET = [
    ("fact 1", "value 1"),
    ("fact 2", "value 2"),
]
TEST_MEDIA = {
    "mime_type": "video/mp4",
    "media_url": "https://127.0.0.1",
    "altText": "Mock",
}
TEST_TEXTRUN: dict[str, Any] = {
    "text": "mock",
    "italic": True,
}


@pytest.fixture
def hookcard() -> WebhookCard:
    return WebhookCard()


# NOTE: As new componetes are added, include them in this test
def test_card_creation(hookcard: WebhookCard) -> None:
    hookcard.add_element(hookcard.new_textblock(**TEST_TEXTBLOCK))
    hookcard.add_element(hookcard.new_image(**TEST_IMAGE))
    hookcard.add_mention(hookcard.new_mention(*TEST_MENTION))
    hookcard.add_element(hookcard.new_factset(TEST_FACTSET))
    hookcard.add_element(hookcard.new_media.basic_setup(**TEST_MEDIA))
    rtb = hookcard.new_richtextblock()
    rtb.add_textrun(hookcard.new_textrun(**TEST_TEXTRUN))
    hookcard.add_element(rtb)
    assert hookcard.render() == json.dumps(EXPECTED_TEST_CARD)


def test_empty_card_repr(hookcard: WebhookCard) -> None:
    assert str(hookcard) == json.dumps(EMPTY_WEBHOOK_CARD)


def test_empty_card_render(hookcard: WebhookCard) -> None:
    assert hookcard.render() == json.dumps(EMPTY_WEBHOOK_CARD)


def test_empty_card_asdict(hookcard: WebhookCard) -> None:
    assert hookcard.asdict() == EMPTY_WEBHOOK_CARD


def test_add_mention(hookcard: WebhookCard) -> None:
    mention = hookcard.new_mention("mock", "123", "mock")

    hookcard.add_mention(mention)

    assert len(hookcard.entities) == 1
    assert hookcard.entities[0].render == mention.render
