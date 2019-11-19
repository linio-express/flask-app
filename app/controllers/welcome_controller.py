#Importan
from flask import Blueprint, render_template
from flask import session, request
from app.models.producto import Producto
from app.models.categoria import Categoria
from app.models.usuario import Usuario
#Importar módulo con funciones de ayuda
from app.helpers.helper import *
import os

template_dir = os.path.abspath('app/views')
inicio_page = Blueprint('inicio_page', 'api', template_folder=template_dir)

def toJSON(lista):
    listaJSON = []
    for objeto in lista:
        listaJSON.append(objeto.toJSON())
    return listaJSON

@inicio_page.route('/', methods=['GET'])
def inicio():
    categorias = Categoria.todas()
    session["categorias"] = toJSON(categorias)
    if session.get('logged_in') == True:
        usuario = Usuario.obtener(session["current_user_id"])
        return render_template('welcome/index.html', logged_in = session["logged_in"], current_user_id = session["current_user_id"], usuario = usuario.toJSON())
    else:
        session["logged_in"] = False
        session["current_user_id"] = 0
        return render_template('welcome/index.html', logged_in = session["logged_in"], current_user_id = session["current_user_id"])

@inicio_page.route('/buscar', methods=['POST'])
def buscar_productos_por_palabra_clave():
    """Este método se encarga de la búsqueda por palabras claves"""

    #Texto a buscar extraído del formulario
    texto_a_buscar = request.form['texto_a_buscar']
    #id_categoria extraido del formulario, debe ser un número
    id_categoria = int(request.form['id_categoria'])

    #Si la búsqueda sea en blanco y la categoria también, se muestran todos los productos
    if (texto_a_buscar == None or texto_a_buscar == "") and (id_categoria == 0 or id_categoria == None):
        lista_productos = Producto.listar_productos_nombre()
    #Si la búsqueda es en blanco pero la categoría no, se muestran todos los productos dentro de esta categoría
    elif (texto_a_buscar == None or texto_a_buscar == "") and id_categoria > 0:
        lista_productos = Producto.listar_productos_nombre(id_categoria = id_categoria)
    #Si la búsqueda no es en blanco y no se seleccione una categoría, se muestran los productos que coinciden con la búsqueda en cualquier categoria.
    elif (texto_a_buscar != None and texto_a_buscar != "") and (id_categoria == None or id_categoria == 0):
        lista_productos = Producto.listar_productos_nombre(cadena_a_buscar = texto_a_buscar)
    #Si la búsqueda no es en blanco y se selecciona una categoría, se muestran los productos que coinciden con la búsqueda en la categoría seleccionada.
    elif (texto_a_buscar != None and texto_a_buscar != "") and id_categoria > 0:
        lista_productos = Producto.listar_productos_nombre(cadena_a_buscar = texto_a_buscar, id_categoria = id_categoria)


    #Finalmente, se retornan los resultados de la búsqueday el resultado de la búsqueda en el view index.html
    if session.get('logged_in') == True:
        usuario = Usuario.obtener(session['current_user_id'])
        return render_template('productos/index.html', logged_in = session["logged_in"], current_user_id = session["current_user_id"], resultados = toJSON(lista_productos), texto_a_buscar=texto_a_buscar, usuario=usuario.toJSON())
    else:
        session["current_user_id"] = 0
        session["logged_in"] = False
        return render_template('productos/index.html', logged_in = session["logged_in"], current_user_id = session["current_user_id"], resultados = toJSON(lista_productos), texto_a_buscar=texto_a_buscar)
