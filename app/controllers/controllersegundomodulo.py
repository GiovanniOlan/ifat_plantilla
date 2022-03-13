#Esta es la segunda señora

from flask.views import MethodView
from flask import render_template


class IndexController(MethodView):
    def get(self):
        return render_template('/segundoModulo/index.html')

class RecepcionController(MethodView):
    def get(self):
        return render_template('/segundoModulo/recepcion.html')

class NuevarecepcionController(MethodView):
    def get(self):
        return render_template('/segundoModulo/nueva-recepcion.html')

class ReporterecepcionController(MethodView):
    def get(self):
        return render_template('/segundoModulo/reporte-recepcion.html')