from app.controllers.controllersegundomodulo import *



routes = {
    "index_route": "/", "index_controller": IndexController.as_view("index"),
    "recibomercancia_route": "/recibo-mercancia", "recibomercancia_controller": RecibomercanciaController.as_view("recibo-mercancia"),
    "nuevorecibo_route": "/nuevo-recibo", "nuevorecibo_controller": NuevoreciboController.as_view("nuevo-recibo"),
    "reporterecibo_route": "/reporte-recibo", "reporterecibo_controller": ReportereciboController.as_view("reporte-recibo"),
}