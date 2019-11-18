from flask import Blueprint, render_template
from flask import session, request
from datetime import datetime
from app.models.producto import Producto
#Importar módulo con funciones de ayuda
from app.helpers.helper import *
import os

template_dir = os.path.abspath('app/views')
producto_page = Blueprint('producto_page', 'api', template_folder=template_dir)

@producto_page.route('/producto/<int:id_producto>', methods=['GET'])
def show(id_producto):
    #Se obtiene el objeto Producto a partir del id
    producto = Producto.obtener(id_producto)

    if session.get('logged_in') != True:
        session["logged_in"] = False
        session["current_user_id"] = 0

    #Se pasan los atributos del producto como un JSON
    return render_template('/productos/show.html', producto=producto.toJSON(), logged_in=session["logged_in"], current_user_id = session["current_user_id"])

@producto_page.route('/producto/<int:id_producto>', methods=['POST'])
def nuevo_producto_en_canasta(id_producto):
    pass
