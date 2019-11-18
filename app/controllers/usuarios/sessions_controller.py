from flask import Blueprint, render_template
from flask import session, request, redirect, url_for, flash
from datetime import datetime
from app.models.producto import Producto
from app.models.canasta import Canasta
from app.models.usuario import Usuario
from app.models.producto_por_canasta import ProductoPorCanasta
import os

template_dir = os.path.abspath('app/views')
session_page = Blueprint('session_page', 'api', template_folder=template_dir)

@session_page.route('/login', methods=['GET'])
def new():
    """Esta función muestra una página para iniciar sesión"""
    #Si el usuario entra a este enlace y ya inicio sesíon, lo mandamos al home
    if session.get('logged_in'):
        return redirect(url_for('inicio_page.inicio'))
    #Si el usuario no ha iniciado sesión, le mostramos el formulario de inico de sesión.
    else:
        return render_template('usuarios/sessions/new.html')

@session_page.route('/login', methods=['POST'])
def create():
    """Esta función crea una sesión"""
    #Creacion de nuevo objeto usuario sin atributos
    usuario = Usuario()
    #Extrer datos del formulario y asignarlo a atributos del objeto creado
    usuario.correo = request.form['correo']
    #Se pone el correo en minúsculas
    usuario.correo = usuario.correo.lower()
    usuario.password = request.form['password']
    #Se verifican las credenciales del usuario
    if usuario.inicio_de_sesion_valido():
        #Se establece que hay una sesión iniciada
        session['logged_in'] = True
        #Se busca al usuario actual
        current_user = Usuario.obtener(correo = "paolobejs@gmail.com")
        #Se establece que el id del usuario que inició sesión
        session['current_user_id'] = current_user.id
        flash('Inicio de sesión exitoso.')
        #Se redirecciona la página de inicio
        return redirect(url_for('inicio_page.inicio'))
    #Si las credenciales no coinciden, no se inicia la sesión
    else:
        session['logged_in'] = False
        flash('Correo electrónico o contraseña incorrectos.')
        return render_template('login.html')

@session_page.route('/logout', methods=['POST'])
def destroy():
    """Esta función cierra una sesión"""
    #Se establece que no hay una sesión iniciada
    session['logged_in'] = False
    #Se establece que no hay ningún id de usuario que inició sesión
    session['current_user_id'] = None
    return redirect(url_for('inicio_page.inicio'))
