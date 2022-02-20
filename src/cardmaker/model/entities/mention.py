import dataclasses
import json


@dataclasses.dataclass
class Mention:
    text: str
    id: str
    name: str
    type: str = "mention"

    def __repr__(self) -> str:
        obj = {
            "type": self.type,
            "text": self.text,
            "mentioned": {
                "id": self.id,
                "name": self.name,
            },
        }
        return json.dumps(obj)

    @property
    def render(self) -> str:
        return str(self)
