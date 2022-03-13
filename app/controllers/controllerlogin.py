# Esta es la primera señora

from flask.views import MethodView
from flask import render_template


class LoginController(MethodView):
    def get(self):
        return render_template('login.html')
