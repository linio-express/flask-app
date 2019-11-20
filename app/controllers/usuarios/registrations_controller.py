from flask import Blueprint, render_template
from flask import session, request, redirect, url_for
from datetime import datetime
from app.models.usuario import Usuario
from app.models.canasta import Canasta
import os

template_dir = os.path.abspath('app/views')
registration_page = Blueprint('registration_page', 'api', template_folder=template_dir)

@registration_page.route('/register', methods=['GET'])
def new():
    if session.get('logged_in'):
        #Si el usuario entra a este enlace y ya inicio sesíon, lo mandamos al home
        return redirect(url_for('inicio_page.inicio'))
    else:
        return render_template('usuarios/registrations/new.html')

@registration_page.route('/register', methods=['POST'])
def create():
    #Array de errores
    errores = []
    #Creación de nuevo objeto
    usuario = Usuario()
    #Datos introducidos por el usuario
    usuario.correo = request.form['correo']
    usuario.nombre_de_usuario = request.form['nombre_de_usuario']
    usuario.password = request.form['password']
    usuario.nombre_completo = request.form['nombre_completo']
    usuario.celular = request.form['celular']
    usuario.dni = request.form['dni']
    dia = int(request.form['fecha_de_nacimiento_dia'])
    mes = int(request.form['fecha_de_nacimiento_mes'])
    anho = int(request.form['fecha_de_nacimiento_anho'])
    usuario.fecha_nacimiento = datetime(anho, mes, dia)
    usuario.numero_de_tarjeta = request.form['numero_de_tarjeta']
    if usuario.es_mayor_de_edad() and usuario.nombre_completo_es_valido():
        if usuario.crear():
            #Se logea al usuario automaticamente
            session['logged_in'] = True
            session['current_user_id'] = usuario.id
            #Se crea una nueva canasta si el usuario logra registrarse
            canasta = Canasta()
            #El usuario de esta canasta será el usuario que se acaba de registrar
            canasta.usuario = usuario
            #Se crea la canasta
            if canasta.crear():
                print("Canasta registrada")
            return redirect(url_for('inicio_page.inicio'))
        else:
            errores.append('Hubo un error al crear tu cuenta.')
            return render_template('usuarios/registrations/new.html', errores = errores)
    else:
        if not usuario.es_mayor_de_edad():
            errores.append("Debes ser mayor de edad para registrarte")
        if not usuario.nombre_completo_es_valido():
            errores.append("Tu nombre no debe contener caracteres especiales.")
        return render_template('usuarios/registrations/new.html', errores = errores)
