from abc import ABC

from src.routes.base import Route
from flask import request, Response, abort
from flask.json import jsonify

from src.domain.app_state import app_state


class ClientGetBalance(Route):
    route_name = "get-balance"
    route_path = "/clientes/<int:_id>/extrato"

    methods = ["GET"]

    def get(self, _id: int):
        account = app_state.get_by_id(_id)

        if account is None:
            return abort(404)

        return jsonify(account.get_statement())

    def post(self):
        raise NotImplementedError()
