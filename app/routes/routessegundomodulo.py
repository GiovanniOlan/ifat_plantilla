from app.controllers.controllersegundomodulo import *



routes = {
    "index_route": "/", "index_controller": IndexController.as_view("index"),
    "recepcion_route": "/recepcion", "recepcion_controller": RecepcionController.as_view("recepcion"),
    "nuevarecepcion_route": "/nueva-recepcion", "nuevarecepcion_controller": NuevarecepcionController.as_view("nueva-recepcion"),
    "reporterecepcion_route": "/reporte-recepcion", "reporterecepcion_controller": ReporterecepcionController.as_view("reporte-recepcion"),
}