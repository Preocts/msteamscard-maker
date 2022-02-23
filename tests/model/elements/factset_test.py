import json

from cardmaker.model.elements.factset import FactSet

FACTS = [
    ("Fact 1", "Value 1"),
    ("Fact 2", "Value 2"),
    ("Fact 3", "Value 3"),
    ("Fact 4", "Value 5"),
]

EXPECTED = {
    "type": "FactSet",
    "facts": [
        {
            "title": "Fact 1",
            "value": "Value 1",
        },
        {
            "title": "Fact 2",
            "value": "Value 2",
        },
        {
            "title": "Fact 3",
            "value": "Value 3",
        },
        {
            "title": "Fact 4",
            "value": "Value 5",
        },
    ],
}
EXPECTED_EMPTY = {"type": "FactSet", "facts": []}


def test_empty_object() -> None:
    result = FactSet()
    assert result.type == "FactSet"
    assert result.facts == []


def test_empty_repr() -> None:
    result = FactSet()
    assert str(result) == json.dumps(EXPECTED_EMPTY)


def test_empty_asdict() -> None:
    result = FactSet()
    assert result.asdict() == EXPECTED_EMPTY


def test_empty_render() -> None:
    result = FactSet()
    assert result.render() == json.dumps(EXPECTED_EMPTY)


def test_add_fact_method() -> None:
    facts = FactSet()
    facts.add_fact("Fact 1", "Value 1")

    assert len(facts.facts) == 1
    assert facts.facts[0]["title"] == "Fact 1"
    assert facts.facts[0]["value"] == "Value 1"


def test_add_facts() -> None:
    facts = FactSet()
    for fact in FACTS:
        facts.add_fact(*fact)

    assert len(facts.facts) == 4


def test_render_with_facts_by_init() -> None:
    facts = FactSet(FACTS)

    assert facts.render() == json.dumps(EXPECTED)


def test_asdict_with_facts() -> None:
    facts = FactSet()
    for fact in FACTS:
        facts.add_fact(*fact)

    assert facts.asdict() == EXPECTED
