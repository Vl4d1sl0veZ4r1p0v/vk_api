from dataclasses import dataclass


@dataclass
class User:
    id: int
    first_name: str
    last_name: str
    count: int

    @classmethod
    def from_dict(cls, data):
        return cls(
            data.get("id", -1),
            data.get("first_name", ""),
            data.get("last_name", ""),
            data.get("count", -1),
        )

    def __str__(self):
        return f"{self.id} {self.first_name} {self.last_name} {self.count}"
