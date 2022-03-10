#Esta es la primera señora

from flask.views import MethodView
from flask import render_template


class IndexController(MethodView):
    def get(self):
        return render_template('/primerModulo/index.html')
    def post(self):
        return "Esto es un post"

    def put(self):
        return "Esto es un PUT"