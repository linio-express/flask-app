from flask import Blueprint, render_template
from flask import session, request, redirect, url_for, flash
from datetime import datetime
from app.models.producto import Producto
from app.models.canasta import Canasta
from app.models.producto_por_canasta import ProductoPorCanasta
#Importar módulo con funciones de ayuda
from app.helpers.helper import *
import os

template_dir = os.path.abspath('app/views')
producto_por_canasta_page = Blueprint('producto_por_canasta_page', 'api', template_folder=template_dir)

@producto_por_canasta_page.route('/agregar', methods=['POST'])
def create():
    if session['logged_in']:
        producto_por_canasta = ProductoPorCanasta()
        id_producto = int(request.form['id_producto'])
        id_canasta = int(request.form['id_canasta'])
        producto_por_canasta.producto = Producto.obtener(id_producto)
        producto_por_canasta.canasta = Producto.obtener(id_canasta)
        producto_por_canasta.cantidad = int(request.form['cantidad'])
        print(producto_por_canasta.producto.id)
        print(producto_por_canasta.canasta.id)
        print(producto_por_canasta.cantidad)
        if producto_por_canasta.crear():
            return redirect(url_for('canasta_page.show'))
        else:
            return redirect(url_for('canasta_page.show'))
    else:
        return redirect(url_for('canasta_page.show'))

@producto_por_canasta_page.route('/borrar', methods=['POST'])
def destroy():
    id_producto_por_canasta = int(request.form['id_producto_por_canasta'])
    producto_por_canasta = ProductoPorCanasta.obtener(id_producto_por_canasta)
    producto_por_canasta.borrar()
    return redirect(url_for('canasta_page.show'))
