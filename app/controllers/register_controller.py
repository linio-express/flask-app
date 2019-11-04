from flask import Blueprint, render_template
from flask import session, request
from datetime import datetime
from app.models.usuario import Usuario
from app.models.canasta import Canasta
import os

template_dir = os.path.abspath('app/views')
register_page = Blueprint('register_page', 'api', template_folder=template_dir)


@register_page.route('/register', methods=['GET'])
def register():
    return render_template('register.html')

@register_page.route('/register', methods=['POST'])
def register_user():
    usuario = Usuario()
    usuario.correo = request.form['correo']
    usuario.nombre_de_usuario = request.form['nombre_de_usuario']
    usuario.password = request.form['password']
    usuario.nombre_completo = request.form['nombre_completo']
    usuario.celular = request.form['celular']
    usuario.dni = request.form['dni']
    dia = int(request.form['fecha_de_nacimiento_dia'])
    mes = int(request.form['fecha_de_nacimiento_mes'])
    anho = int(request.form['fecha_de_nacimiento_anho'])
    usuario.fecha_de_nacimiento = datetime(anho, mes, dia)
    usuario.numero_de_tarjeta = request.form['numero_de_tarjeta']
    if usuario.crear():
        #Se crea una nueva canasta si el usuario logra registrarse
        canasta = Canasta()
        #El usuario de esta canasta será el usuario que se acaba de registrar
        canasta.usuario = usuario
        #Se crea la canasta
        canasta.crear()
        print("Usuario registrado")
    return render_template('register.html')
