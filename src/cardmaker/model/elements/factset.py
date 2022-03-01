from __future__ import annotations

import dataclasses
from typing import TypedDict

from cardmaker.model.base_element import BaseElement


class _Fact(TypedDict):
    title: str
    value: str


@dataclasses.dataclass(init=False, repr=False)
class FactSet(BaseElement):
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

    def add_fact(self, title: str, value: str) -> None:
        """Add a fact to the FactSet. Facts are rendered in the order added"""
        self.facts.append({"title": title, "value": value})
