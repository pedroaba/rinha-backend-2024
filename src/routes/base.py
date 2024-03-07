from flask.views import View


class Route(View):
    route_name: str = ""
    route_path: str = ""

    def __init__(self, *args, **kwargs):
        super(Route, self).__init__(*args, **kwargs)
