import os
from typing import Union, List, Type

from flask import Flask
from flask_cors import CORS

from src.routes.base import Route
from src.routes.hello_world import HelloWorld
from src.routes.clients_post_transaction import ClientPostTransactions
from src.routes.clients_get_balance import ClientGetBalance


class Server:
    def __init__(self):
        self.app = Flask(__name__)

        CORS(self.app)

    def run(self):
        self.app.run(
            host="0.0.0.0",
            port=os.getenv("PORT", 5000)
        )

    def register_route(self, route: Union[Type[Route], List[Type[Route]]]):
        if isinstance(route, list):
            for r in route:
                self._register_single_route(r)
        else:
            self._register_single_route(route)

    def _register_single_route(self, route: Type[Route]) -> None:
        self.app.add_url_rule(
            route.route_path,
            view_func=route.as_view(route.route_name)
        )


server = Server()

server.register_route([HelloWorld, ClientGetBalance, ClientPostTransactions])
