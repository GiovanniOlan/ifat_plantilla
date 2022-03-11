from flask import *
from app.routes.routesprimermodulo import routes as primerModuloRoutes
from app.routes.routessegundomodulo import routes as segundoModuloRoutes

app=Flask(__name__)

# app.config['SQlALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost/tanquesoxigenos_database'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# SQLAlchemy(app)


#PRIMER SEÑORA - Si vas a trabajar en la primera señora, descomenta esto estas rutas y comentas las de la segunda señora
app.add_url_rule(primerModuloRoutes["index_route"], view_func=primerModuloRoutes['index_controller'])
app.add_url_rule(primerModuloRoutes["productos_route"], view_func=primerModuloRoutes['productos_controller'])
app.add_url_rule(primerModuloRoutes["agregarproducto_route"], view_func=primerModuloRoutes['agregarproducto_controller'])
app.add_url_rule(primerModuloRoutes["nuevaorden_route"], view_func=primerModuloRoutes['nuevaorden_controller'])
app.add_url_rule(primerModuloRoutes["ordencompras_route"], view_func=primerModuloRoutes['ordencompras_controller'])
app.add_url_rule(primerModuloRoutes["reporteorden_route"], view_func=primerModuloRoutes['reporteorden_controller'])


#SEGUNDA SEÑORA - Si vas a trabajar en la segunda señora, descomenta estas rutas y comenta las de la primera señora
#app.add_url_rule(segundoModuloRoutes["index_route"], view_func=segundoModuloRoutes['index_controller'])


