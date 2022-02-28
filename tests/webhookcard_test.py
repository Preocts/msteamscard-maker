import json
from pathlib import Path

import pytest
from cardmaker.model.constants import EMPTY_WEBHOOK_CARD
from cardmaker.model.elements.factset import FactSet
from cardmaker.model.elements.image import Image
from cardmaker.model.elements.textblock import TextBlock
from cardmaker.model.entities.mention import Mention
from cardmaker.webhookcard import WebhookCard

EXPECTED_TEST_CARD = json.load(Path("tests/fixtures/webhook_card.json").open())
TEST_TEXTBLOCK = TextBlock(
    text="<at>General Kenobi</at>",
    weight="bolder",
    size="large",
)
TEST_IMAGE = Image("https://127.0.0.1")
TEST_MENTION = Mention("<at>General Kenobi</at>", "24601", "Obiwan")
TEST_FACTSET = FactSet([("fact 1", "value 1"), ("fact 2", "value 2")])


@pytest.fixture
def hookcard() -> WebhookCard:
    return WebhookCard()


# NOTE: As new componetes are added, include them in this test
def test_card_creation(hookcard: WebhookCard) -> None:
    hookcard.add_element(TEST_TEXTBLOCK)
    hookcard.add_element(TEST_IMAGE)
    hookcard.add_mention(TEST_MENTION)
    hookcard.add_element(TEST_FACTSET)

    assert hookcard.render == json.dumps(EXPECTED_TEST_CARD)


def test_empty_card_repr(hookcard: WebhookCard) -> None:
    assert str(hookcard) == json.dumps(EMPTY_WEBHOOK_CARD)


def test_empty_card_render(hookcard: WebhookCard) -> None:
    assert hookcard.render == json.dumps(EMPTY_WEBHOOK_CARD)


def test_add_textblock(hookcard: WebhookCard) -> None:
    tblock = TextBlock(text="mocking test", wrap=True)

    hookcard.add_element(tblock)

    assert len(hookcard.body) == 1
    assert hookcard.body[0].render == tblock.render


def test_add_mention(hookcard: WebhookCard) -> None:
    mention = Mention("mock", "123", "mock")

    hookcard.add_mention(mention)

    assert len(hookcard.entities) == 1
    assert hookcard.entities[0].render == mention.render
