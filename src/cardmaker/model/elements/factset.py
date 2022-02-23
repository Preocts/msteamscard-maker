from __future__ import annotations

import dataclasses
import json
from typing import Any
from typing import TypedDict


class _Fact(TypedDict):
    title: str
    value: str


@dataclasses.dataclass(init=False)
class FactSet:
    type: str = "FactSet"
    facts: list[_Fact] = dataclasses.field(default_factory=list)

    def __init__(self, facts_: list[tuple[str, str]] | None = None) -> None:
        """
        Define a FactSet, Facts are rendered in the order added

        Args:
            facts: Iterable (title:value) collection of facts.
        """
        self.facts: list[_Fact] = []
        for fact in facts_ or []:
            self.add_fact(*fact)

    def __repr__(self) -> str:
        return json.dumps(dataclasses.asdict(self))

    def render(self, indent: int | None = None) -> str:
        """Render object as a string"""
        return json.dumps(dataclasses.asdict(self), indent=indent)

    def asdict(self) -> dict[str, Any]:
        """Object as a dict"""
        return dataclasses.asdict(self)

    def add_fact(self, title: str, value: str) -> None:
        """Add a fact to the FactSet. Facts are rendered in the order added"""
        self.facts.append({"title": title, "value": value})
