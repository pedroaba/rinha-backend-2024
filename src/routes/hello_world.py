import json

from flask import Response


from src.routes.base import Route


class HelloWorld(Route):
    route_name = "hello-world"
    route_path = "/hello_world"

    def __init__(self):
        super(HelloWorld, self).__init__()

    def dispatch_request(self):
        return Response(
            response=json.dumps({
                "message": "hello-world"
            })
        )
