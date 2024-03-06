from flask.views import View


class Route(View):
    route_name: str = ""
    route_path: str = ""

    def __init__(self):
        super(Route, self).__init__()
