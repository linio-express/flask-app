from flask import Blueprint, render_template, session, request, redirect, url_for, flash
from app.models.usuario import Usuario
import os

template_dir = os.path.abspath('app/views')
login_page = Blueprint('login_page', 'api', template_folder=template_dir)


@login_page.route('/login', methods=['GET'])
def login():
    return render_template('login.html')

@login_page.route('/login', methods=['POST'])
def login_user():
    #Creacion de nuevo objeto usuario
    usuario = Usuario()
    usuario.correo = request.form['email']
    usuario.password = request.form['password']
    if usuario.inicio_de_sesion_valido():
        flash('Inicio de sesión exitoso.')
    else:
        flash('Correo electrónico o contraseña incorrectos.')
    return render_template('login.html')
