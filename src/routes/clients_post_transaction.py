from src.routes.base import Route


class ClientPostTransactions(Route):
    route_name = "post-transactions"
    route_path = "/clientes/[id]/transacoes"

    methods = ["POST"]

    def dispatch_request(self):
        pass
