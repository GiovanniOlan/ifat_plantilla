#Esta es la segunda señora

from flask.views import MethodView
from flask import render_template


class IndexController(MethodView):
    def get(self):
        return "<h1>Esto es el index de la segunda señora</h1>"