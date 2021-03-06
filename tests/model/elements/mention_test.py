from __future__ import annotations

from cardmaker.model.elements.mention import Mention

TEST_DATA = {
    "text": "<at>General Kenobi</at>",
    "id": "24601",
    "name": "ObiWan",
}

EXPECTED = {
    "type": "mention",
    "text": "<at>General Kenobi</at>",
    "mentioned": {
        "id": "24601",
        "name": "ObiWan",
    },
}


def test_init_mention() -> None:
    result = Mention(**TEST_DATA)
    assert result.type == "mention"
    assert result.text == TEST_DATA["text"]
    assert result.id == TEST_DATA["id"]
    assert result.name == TEST_DATA["name"]


def test_asdict() -> None:
    result = Mention(**TEST_DATA)
    assert result.asdict() == EXPECTED
