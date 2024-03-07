from src.routes.base import Route
from flask import request, Response


class ClientGetBalance(Route):
    route_name = "get-balance"
    route_path = "/clientes/<int:_id>/extrato"

    methods = ["GET"]

    def dispatch_request(self, _id: int):
        pass
