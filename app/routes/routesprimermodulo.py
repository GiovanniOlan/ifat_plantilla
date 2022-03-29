from app.controllers.controllerprimeromodulo import *



routes = {
    "index_route": "/", "index_controller": IndexController.as_view("index"),
    "proveedores_route": "/proveedores", "proveedores_controller": ProveedoresController.as_view("proveedores"),
    "productos_route": "/productos", "productos_controller": ProductosController.as_view("productos"),
    "agregarproducto_route": "/agregar-producto", "agregarproducto_controller": AgregarproductoController.as_view("agregar-producto"),
    "nuevaorden_route": "/nueva-orden", "nuevaorden_controller": NuevaordenController.as_view("nueva-orden"),
    "ordencompras_route": "/orden-compras", "ordencompras_controller": OrdencomprasController.as_view("orden-compras"),
    "reporteorden_route": "/reporte-orden", "reporteorden_controller": ReporteordenController.as_view("reporte-orden"),
}