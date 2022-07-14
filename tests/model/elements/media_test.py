from __future__ import annotations

from unittest.mock import patch

from cardmaker.model.base_element import BaseElement
from cardmaker.model.elements.media import Media

EXPECTED_EMPTY = {
    "type": "Media",
    "sources": [],
}

EXPECTED_SOURCES = {
    "mimeType": "video/mp4",
    "url": "https://127.0.0.1",
}


def test_ensure_superclass() -> None:
    assert issubclass(Media, BaseElement)


def test_add_source_against_asdict_result() -> None:
    media = Media()
    with patch.dict(EXPECTED_EMPTY, {"sources": []}) as expected_full:
        for _ in range(10):
            expected_full["sources"].append(EXPECTED_SOURCES)
            media.add_source(EXPECTED_SOURCES["mimeType"], EXPECTED_SOURCES["url"])

        assert media.asdict() == expected_full


def test_set_poster() -> None:
    media = Media()
    media.set_poster("https://127.0.0.1")

    result = media.asdict()

    assert result["poster"] == "https://127.0.0.1"


def test_set_altText() -> None:
    media = Media()
    media.set_altText("Mock")

    result = media.asdict()

    assert result["altText"] == "Mock"


def test_build_from_basic_setup() -> None:
    with patch.dict(EXPECTED_EMPTY, {"sources": []}) as expected:
        media = Media.basic_setup(
            EXPECTED_SOURCES["mimeType"],
            EXPECTED_SOURCES["url"],
            "mock",
            "mock",
        )
        expected["sources"].append(EXPECTED_SOURCES)
        expected["poster"], expected["altText"] = ("mock", "mock")

        result = media.asdict()

        assert result == expected
