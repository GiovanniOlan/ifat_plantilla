# Esta es la primera señora

from flask.views import MethodView
from flask import render_template


class IndexController(MethodView):
    def get(self):
        return render_template('/primerModulo/index.html')

class AgregarproductoController(MethodView):
    def get(self):
        return render_template('/primerModulo/agregar-producto.html')
