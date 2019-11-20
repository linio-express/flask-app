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
    return redirect(url_for('pedido_page.show(id_canasta)'))

@pedido_page.route('/mis_pedidos/<estado>', methods=['GET'])
def index(estado):
    if session.get('logged_in'):
        usuario = Usuario.obtener(int(session['current_user_id']))
        pedidos = usuario.buscar_pedidos(estado)
        return render_template('pedidos/index.html', logged_in=session['logged_in'], pedidos = toJSON(pedidos), usuario = usuario.toJSON(), estado=estado)
    else:
        return redirect(url_for('inicio_page.inicio'), estado=estado)

@pedido_page.route('/pedido/<int:id_pedido>', methods=['GET'])
def show(id_pedido):
    #Si el usuario está logeado, se busca el pedido
    if session.get('logged_in'):
        #Se obtiene el objeto Pedido a partir del id
        pedido = Pedido.obtener(id_pedido)
        usuario = Usuario.obtener(int(session['current_user_id']))
        productos_por_pedido = pedido.buscar_productos_por_pedido()
        return render_template('pedidos/show.html', pedido=pedido.toJSON(), productos_por_pedido = toJSON(productos_por_pedido), usuario = usuario.toJSON())
    else:
        session["logged_in"] = False
        session["current_user_id"] = 0
        return redirect(url_for('inicio_page.inicio'))

@pedido_page.route('/agregar_direccion', methods=['POST'])
def agregar_direccion():
    distrito = request.form['distrito']
    direccion = request.form['direccion']
    id_pedido = request.form['id_pedido']
    pedido = Pedido.obtener(id_pedido)
    pedido.direccion_de_envio = direccion + ", " + distrito
    if pedido.estado == "En Progreso (Dirección pendiente)":
        pedido.estado = "En Progreso (Preparando paquete)"
    if pedido.estado == "En Progreso (Pago y dirección pendientes)":
        pedido.estado = "En Progreso (Pago pendiente)"
    pedido.actualizar()
    return redirect(url_for('pedido_page.show', id_pedido = id_pedido))

@pedido_page.route('/cancelar_pedido', methods=['POST'])
def cancelar_pedido():
    id_pedido = request.form['id_pedido']
    pedido = Pedido.obtener(id_pedido)
    pedido.estado = "Cancelado"
    pedido.actualizar()
    return redirect(url_for('inicio_page.inicio'))

@pedido_page.route('/elegir_metodo_de_pago', methods=['POST'])
def elegir_metodo_de_pago():
    opcion = request.form['metodo_de_pago']
    id_pedido = request.form['id_pedido']
    pedido = Pedido.obtener(id_pedido)
    if opcion == "tarjeta":
        pedido.metodo_de_pago = "Tarjeta de crédito/débito"
    if opcion == "efectivo":
        pedido.metodo_de_pago = "Efectivo"
    pedido.actualizar()
    return redirect(url_for('pedido_page.show', id_pedido = id_pedido))
