#Esta es la segunda señora

from flask.views import MethodView
from flask import render_template


class IndexController(MethodView):
    def get(self):
        return render_template('/segundoModulo/index.html')

class RecibomercanciaController(MethodView):
    def get(self):
        return render_template('/segundoModulo/recibo-mercancia.html')

class NuevoreciboController(MethodView):
    def get(self):
        return render_template('/segundoModulo/nuevo-recibo.html')

class ReportereciboController(MethodView):
    def get(self):
        return render_template('/segundoModulo/reporte-recibo.html')