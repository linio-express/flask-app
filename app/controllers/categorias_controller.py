from flask import Blueprint, render_template
from flask import session, request
from datetime import datetime
from app.models.producto import Producto
from app.models.usuario import Usuario
from app.models.categoria import Categoria
#Importar módulo con funciones de ayuda
from app.helpers.helper import *
import os

template_dir = os.path.abspath('app/views')
categoria_page = Blueprint('categoria_page', 'api', template_folder=template_dir)

@categoria_page.route('/canasta/<int:id_categoria>', methods=['GET'])
def show(id_categoria):
    #Se obtiene el objeto Canasta a partir del id
    categoria = Categoria.obtener(id_categoria)
    #Se obtienen los productos dentro de esta categoría
    productos = Producto.listar_productos_nombre(id_categoria = categoria.id)
    if session.get('logged_in') == True:
        usuario = Usuario.obtener(session['current_user_id'])
        return render_template('productos/index.html', resultados = toJSON(productos), usuario=usuario.toJSON(), categoria = categoria.toJSON())
    else:
        session["current_user_id"] = 0
        session["logged_in"] = False
        return render_template('productos/index.html', logged_in = session["logged_in"], current_user_id = session["current_user_id"], resultados = toJSON(productos), categoria = categoria.toJSON())
