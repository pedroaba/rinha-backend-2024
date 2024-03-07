from src.domain.transactions import Transactions


class Account:
    def __init__(self, limit: int, balance: float, _id: int):
        self._limit = limit
        self._balance = balance
        self._id = _id

        self._transactions: list[Transactions] = []

    @property
    def limit(self):
        return self._limit

    @property
    def balance(self):
        return self._balance

    @property
    def id(self):
        return self._id
