from flask import Blueprint, render_template
from flask import session, request
from datetime import datetime
from app.models.producto import Producto
from app.models.canasta import Canasta
from app.models.producto_por_canasta import ProductoPorCanasta
#Importar módulo con funciones de ayuda
from app.helpers.helper import *
import os

template_dir = os.path.abspath('app/views/canastas')
canasta_page = Blueprint('canasta_page', 'api', template_folder=template_dir)

@canasta_page.route('/canasta', methods=['GET'])
def show():
    #Si el usuario está logeado, se busca su canasta
    if session.get('logged_in') == True:
        canasta = Canasta.obtener(session['current_user_id'])
        productos_por_canasta = canasta.buscar_productos_por_canasta()
        return render_template('show.html', productos_por_canasta=toJSON(productos_por_canasta), canasta=canasta.toJSON(), logged_in=session["logged_in"], current_user_id=session["current_user_id"])
    #Si el usuario no está logeado, no se buscará ninguna canasta
    else:
        session["logged_in"] = False
        session["current_user_id"] = 0
        return render_template('show.html', logged_in=session["logged_in"], current_user_id=session["current_user_id"])
