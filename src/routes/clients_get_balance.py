from src.routes.base import Route


class ClientGetBalance(Route):
    route_name = "get-balance"
    route_path = "/clientes/[id]/extrato"

    methods = ["GET"]

    def dispatch_request(self):
        pass
