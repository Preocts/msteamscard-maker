from __future__ import annotations

import dataclasses
import json
from typing import Any


@dataclasses.dataclass(repr=False)
class BaseElement:
    def __repr__(self) -> str:
        return json.dumps(self.asdict())

    def render(self, indent: int | None = None) -> str:
        """Render object as serialized string. All None values are removed"""
        return json.dumps(self.asdict(), indent=indent)

    def asdict(self) -> dict[str, Any]:
        """All None values are removed from output"""
        return {k: v for k, v in dataclasses.asdict(self).items() if v is not None}
