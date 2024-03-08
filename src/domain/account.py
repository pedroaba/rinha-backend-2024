import datetime

from flask import abort, jsonify

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

    def make_transaction(self, payload):
        value = payload["valor"]
        transaction_type = payload["tipo"]
        description = payload["descricao"]

        transaction = Transactions(
            float(value),
            transaction_type,
            description
        )

        match transaction_type:
            case "c":
                if abs(self._balance - transaction.value) <= self._limit:
                    self._balance -= transaction.value
                    self._transactions.append(transaction)
                else:
                    abort(422)
            case "d":
                self._balance += transaction.value
                self._transactions.append(transaction)
            case _:
                abort(300)

        return {
            "limit": self._limit,
            "saldo": self._balance
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
