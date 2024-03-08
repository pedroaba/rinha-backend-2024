import datetime

from src.domain.transactions import Transactions


class Account:
    def __init__(self, limit: int, balance: float, _id: int):
        self._limit = limit
        self._balance = balance
        self._id = _id

        self._transactions: list[Transactions] = []

    def get_statement(self):
        return {
            "saldo": {
                "total": self._balance,
                "data_extrato": str(datetime.datetime.now()),
                "limit": self._limit
            },
            "ultimas_transacoes": list(
                map(
                    lambda x: x.get_resume(),
                    self._transactions
                )
            )
        }

    @property
    def limit(self):
        return self._limit

    @property
    def balance(self):
        return self._balance

    @property
    def id(self):
        return self._id
