from flask import request, abort, jsonify

from src.domain.app_state import app_state
from src.routes.base import Route


class ClientPostTransactions(Route):
    route_name = "post-transactions"
    route_path = "/clientes/<int:_id>/transacoes"

    methods = ["POST"]

    def post(self, _id: int):
        payload = request.get_json()
        account = app_state.get_by_id(_id)

        if account is None:
            return abort(404)

        result = account.make_transaction(payload)
        return jsonify(result)

    def get(self, *args, **kwargs):
        pass
