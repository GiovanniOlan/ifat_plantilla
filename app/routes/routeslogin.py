from app.controllers.controllerlogin import *



routes = {
    "login_route": "/login", "login_controller": LoginController.as_view("login"),
    "registrar_route": "/registrar", "registrar_controller": RegistrarController.as_view("registrar-usuario"),#Esto es para registrar un usuario
}