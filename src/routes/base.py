from abc import abstractmethod, ABC

from flask.views import MethodView


class Route(MethodView, ABC):
    route_name: str = ""
    route_path: str = ""

    def __init__(self, *args, **kwargs):
        super(Route, self).__init__(*args, **kwargs)

    @abstractmethod
    def get(self, *args, **kwargs):
        pass

    @abstractmethod
    def post(self, *args, **kwargs):
        pass
