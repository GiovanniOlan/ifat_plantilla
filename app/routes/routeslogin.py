from app.controllers.controllerlogin import *



routes = {
    "login_route": "/login", "login_controller": LoginController.as_view("login"),
}