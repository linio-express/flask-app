from flask import Blueprint, render_template
from flask import session, request, redirect, url_for, flash
from datetime import datetime
from app.models.pedido import Pedido
from app.models.canasta import Canasta
from app.models.producto_por_canasta import ProductoPorCanasta
from app.models.usuario import Usuario
#Importar módulo con funciones de ayuda
from app.helpers.helper import *
import os

template_dir = os.path.abspath('app/views')
pedido_page = Blueprint('pedido_page', 'api', template_folder=template_dir)

@pedido_page.route('/nuevo_pedido', methods=['POST'])
def create():
    id_canasta = int(session["current_user_id"])
    nuevo_pedido = Pedido.generar_pedido(id_canasta)
    return redirect(url_for('pedido_page.index'))

@pedido_page.route('/mis_pedidos', methods=['GET'])
def index():
    if session.get('logged_in'):
        usuario = Usuario.obtener(int(session['current_user_id']))
        pedidos = usuario.buscar_pedidos()
        return render_template('pedidos/index.html', logged_in=session['logged_in'], pedidos = toJSON(pedidos))
    else:
        return redirect(url_for('inicio_page.inicio'))

@pedido_page.route('/pedido/<int:id_pedido>', methods=['GET'])
def show(id_pedido):
    #Si el usuario está logeado, se busca el pedido
    if session.get('logged_in') == True:
        #Se obtiene el objeto Pedido a partir del id
        pedido = Pedido.obtener(id_pedido)
        productos_por_pedido = pedido.buscar_productos_por_pedido()
        return render_template('pedidos/show.html', pedido=pedido.toJSON(), productos_por_pedido = toJSON(productos_por_pedido))
    else:
        session["logged_in"] = False
        session["current_user_id"] = 0
        return redirect(url_for('inicio_page.inicio'))

@pedido_page.route('/agregar_direccion', methods=['POST'])
def agregar_direccion(id_pedido):
    pedido = Pedido.obtener(id_pedido)
    distrito = request.form['distrito']
    direccion = request.form['direccion']
    pedido.direccion_de_envio = direccion + ", " + distrito
    pedido.actualizar()
    return redirect(url_for('pedido_page.show'))
