from app.controllers.controllerprimeromodulo import *



routes = {
    "index_route": "/", "index_controller": IndexController.as_view("index"),
    "agregarproducto_route": "/agregar-producto", "agregarproducto_controller": AgregarproductoController.as_view("agregar-producto"),
}