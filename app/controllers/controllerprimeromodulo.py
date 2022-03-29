# Esta es la primera señora

from flask.views import MethodView
from flask import render_template


class IndexController(MethodView):
    def get(self):
        return render_template('/primerModulo/index.html')

class ProveedoresController(MethodView):
    def get(self):
        return render_template('/primerModulo/proveedores.html')

class ProductosController(MethodView):
    def get(self):
        return render_template('/primerModulo/productos.html')
class AgregarproductoController(MethodView):
    def get(self):
        return render_template('/primerModulo/agregar-producto.html')

class NuevaordenController(MethodView):
    def get(self):
        return render_template('/primerModulo/nueva-orden.html')

class OrdencomprasController(MethodView):
    def get(self):
        return render_template('/primerModulo/orden-compras.html')

class ReporteordenController(MethodView):
    def get(self):
        return render_template('/primerModulo/reporte-orden.html')
