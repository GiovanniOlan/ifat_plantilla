#Esta es la segunda señora

from flask.views import MethodView
from flask import render_template


class IndexController(MethodView):
    def get(self):
        return render_template('/segundoModulo/index.html')