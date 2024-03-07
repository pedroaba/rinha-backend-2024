from src.domain.account import Account


class _AppState:
    def __init__(self):
        self._state = []

        self._populate_db()

    def _populate_db(self):
        account_one = Account(limit=100_000, balance=0, _id=1)
        account_two = Account(limit=80_000, balance=0, _id=2)
        account_three = Account(limit=1_000_000, balance=0, _id=3)
        account_four = Account(limit=10_000_000, balance=0, _id=4)
        account_five = Account(limit=500_000, balance=0, _id=5)

        self._state.append(account_one)
        self._state.append(account_two)
        self._state.append(account_three)
        self._state.append(account_four)
        self._state.append(account_five)


app_state = _AppState()
