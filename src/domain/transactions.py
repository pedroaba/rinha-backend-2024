import datetime
from typing import Literal


class Transactions:
    def __init__(self, value: float, _type: Literal["c", "d"], description: str):
        self._value = value
        self._type = _type
        self._description = description
        self._created_at = str(datetime.datetime.now())

    def get_resume(self):
        return {
            "valor": self._value,
            "tipo": self._type,
            "descricao": self._description,
            "realizada_em": self._created_at
        }

    @property
    def value(self):
        return self._value

    @property
    def type(self):
        return self._type

    @property
    def description(self):
        return self._description

    @property
    def created_at(self):
        return self._created_at
