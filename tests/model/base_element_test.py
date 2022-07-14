from __future__ import annotations

import json
from dataclasses import dataclass

from cardmaker.model.base_element import BaseElement


@dataclass(repr=False)
class MockClass(BaseElement):
    value01: str = "test01"
    value02: int = 0
    value03 = None


EXPECTED_DICT = {"value01": "test01", "value02": 0}
EXPECTED_REPR = json.dumps(EXPECTED_DICT)


def test_repr() -> None:
    testclass = MockClass()

    assert str(testclass) == EXPECTED_REPR


def test_render() -> None:
    testclass = MockClass()

    assert testclass.render() == EXPECTED_REPR


def test_asdict() -> None:
    testclass = MockClass()

    assert testclass.asdict() == EXPECTED_DICT
