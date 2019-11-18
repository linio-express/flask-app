from .categoria import Categoria
from .comercio import Comercio
#Importar libreria para sqlite3
import sqlite3
#Importar configuración
from config import Config
#Importar librería datetime par fechas
from datetime import datetime
#Importar módulo con funciones de ayuda
from app.helpers.helper import *

class Producto(object):

    def __init__(self, id: int = None, nombre: str = None, descripcion: str = None, fotos_url: list = None, precio: float = None, stock: int = None, fecha_de_creacion: datetime = None, fecha_de_actualizacion: datetime = None, categoria = None, comercio = None, pedidos: list = None, canastas: list = None):
        self.__id = id
        self.__nombre = nombre
        self.__descripcion = descripcion
        self.__fotos_url = fotos_url
        self.__precio = precio
        self.__stock = stock
        self.__fecha_de_creacion = fecha_de_creacion
        self.__fecha_de_actualizacion = fecha_de_actualizacion
        #Array de objetos Canasta
        self.__canastas = canastas
        #Array de objetos Pedido
        self.__pedidos = pedidos
        self.__categoria = categoria
        self.__comercio = comercio

    def __str__(self):
        return "id = {}, nombre = '{}', descripcion = '{}', precio = {}, stock = {}, id_categoria = {}, id_comercio = {}".format(self.id, self.nombre, self.descripcion, self.precio, self.stock, self.categoria.id, self.comercio.id)

    def toJSON(self):
        return {"id": self.id, "nombre": self.nombre, "descripcion": self.descripcion,
        "fotos_url": self.fotos_url, "precio": self.precio,"stock": self.stock, "precio_str": formato_de_precio(self.precio)}

    @property
    def id(self):
        return self.__id

    @property
    def nombre(self):
        return self.__nombre

    @property
    def descripcion(self):
        return self.__descripcion

    @property
    def fotos_url(self):
        return self.__fotos_url

    @property
    def precio(self):
        return self.__precio

    @property
    def stock(self):
        return self.__stock

    @property
    def fecha_de_creacion(self):
        return self.__fecha_de_creacion

    @property
    def fecha_de_actualizacion(self):
        return self.__fecha_de_actualizacion

    @property
    def canastas(self):
        return self.__canastas

    @property
    def pedidos(self):
        return self.__pedidos

    @property
    def categoria(self):
        return self.__categoria

    @property
    def comercio(self):
        return self.__comercio

    @nombre.setter
    def nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre

    @descripcion.setter
    def descripcion(self, nueva_descripcion):
        self.__descripcion = nueva_descripcion

    @fotos_url.setter
    def fotos_url(self, nuevas_fotos_url):
        self.__fotos_url = nuevas_fotos_url

    @precio.setter
    def precio(self, nuevo_precio):
        self.__precio = nuevo_precio

    @stock.setter
    def stock(self, nuevo_stock):
        self.__stock = nuevo_stock

    @stock.setter
    def stock(self, nuevo_stock):
        self.__stock = nuevo_stock

    @fecha_de_creacion.setter
    def fecha_de_creacion(self, nueva_fecha_de_creacion):
        self.__fecha_de_creacion = nueva_fecha_de_creacion

    @fecha_de_actualizacion.setter
    def fecha_de_actualizacion(self, nueva_fecha_de_actualizacion):
        self.__fecha_de_actualizacion = nueva_fecha_de_actualizacion

    @categoria.setter
    def categoria(self, nueva_categoria):
        self.__categoria = nueva_categoria

    @comercio.setter
    def comercio(self, nuevo_comercio):
        self.__comercio = nuevo_comercio

    @staticmethod
    def todos():
        productos = []
        try:
            #Conexión a la base de datos usando ruta de archivo de configuración
            db = sqlite3.connect(Config.get("DATABASE"), detect_types=sqlite3.PARSE_DECLTYPES)
            #Objeto cursor
            cursor = db.cursor()
            query = """SELECT * FROM productos;""".format(id)
            cursor.execute(query)
            resultados = cursor.fetchall()
            for resultado in resultados:
                productos.append({"id": resultado[0], "nombre": resultado[1], "descripcion": resultado[2],
                    "foto_url": resultado[3], "precio": resultado[4], "stock": resultado[5]})
        except Exception as e:
            print("Error: {}".format(e))
        finally:
            #Cerrar conexión de db
            db.close()
            return productos

    @staticmethod
    def listar_productos_nombre(cadena_a_buscar = None, id_categoria = None):
        """Recibe una cadena_a_buscar como str y un id_categoria como int.
            Devuelve un listado con el resultado de la búsqueda"""
        productos = []
        try:
            #Conexión a la base de datos usando ruta de archivo de configuración
            db = sqlite3.connect(Config.get("DATABASE"), detect_types=sqlite3.PARSE_DECLTYPES)
            #Objeto cursor
            cursor = db.cursor()
            query = """SELECT * FROM productos""".format(cadena_a_buscar)
            if cadena_a_buscar != None:
                query += """ WHERE nombre LIKE '%{}%'""".format(cadena_a_buscar)
                if id_categoria != None:
                    query += """ AND id_categoria = {}""".format(id_categoria)
            elif id_categoria != None:
                query += """ WHERE id_categoria = {}""".format(id_categoria)
            print(query)
            cursor.execute(query)
            resultados = cursor.fetchall()
            for resultado in resultados:
                productos.append(Producto(id= resultado[0], nombre = resultado[1], descripcion = resultado[2],
                    fotos_url = resultado[3].split(","), precio = resultado[4], stock = resultado[5]))
        except Exception as e:
            print("Error: {}".format(e))
        finally:
            #Cerrar conexión de db
            db.close()
            return productos

    @staticmethod
    def filtrar_productos(lista_de_productos, limite_inferior: float = None, limite_superior: float = None):
        """Recibe una lista donde cada elemento es un objeto de tipo Producto. Recibe dos parámetros opcionales como float que indican los límites del filtro. Devuelve una lista donde cada elemento es un objeto tipo Producto."""
        pass

    @staticmethod
    def ordernar_productos(lista_de_productos, ascendiente: bool):
        """Recibe una lista donde cada elemento es un objeto de tipo Producto. Recibe como segundo parámetro un boolean que indica si el orden es ascendiente o descendiente. Devuelve una lista donde cada elemento es un objeto tipo Producto."""
        pass

    @staticmethod
    def ultimos_productos(numero_de_productos: int):
        """Busca los últimos productos en la base de datos y los ordena de más recientes a más antiguos. Devuelve una lista donde cada elemento es un objeto de tipo Producto."""

    def crear(self):
        """Esta función agrega una nueva instancia en la base de datos con los atributos del objeto.
        Devuelve True si se logra guardar en la db, caso contrario devuelve False."""
        estado = False
        try:
            #Conexión a la base de datos usando ruta de archivo de configuración
            db = sqlite3.connect(Config.get("DATABASE"), detect_types=sqlite3.PARSE_DECLTYPES)
            #Objeto cursor
            cursor = db.cursor()
            #Consulta de tipo INSERT
            query = """INSERT INTO productos (nombre, descripcion, precio, stock, id_categoria, id_comercio) VALUES('{}', '{}', {}, {}, {}, {})""".format(self.nombre, self.descripcion, self.precio, self.stock, self.categoria.id, self.comercio.id)
            #Imprimir query a ejecutar
            print('\u001b[32m' + '\033[1m' + query + '\033[0m')
            #Ejecutar query
            cursor.execute(query)
            #Confirmar cambios a base de datos
            db.commit()
            #Cambiar estado a True
            estado = True
            #Query para hallar el id de la instancia recién creada
            query = """SELECT MAX(id) FROM productos;"""
            #Ejecutar query
            cursor.execute(query)
            #Extraer resultado del query ejecutado
            id_nuevo_producto = cursor.fetchone()
            #Asignar id a objeto
            self.id = int(id_nuevo_producto[0])
        except Exception as e:
            #Restaurar cambios en caso de error
            db.rollback()
            #Imprimir errores
            print("Error: {}".format(e))
        finally:
            #Cerrar conexión de db
            db.close()
            #Retornar estado
            return estado

    def actualizar(self):
        """Recibe una ruta de base datos. Actualiza el objeto en la db.
            Devuelve True si se logra actualizar en la db, caso contrario devuelve False."""
        estado = False
        try:
            #Conexión a la base de datos usando ruta de archivo de configuración
            db = sqlite3.connect(Config.get("DATABASE"), detect_types=sqlite3.PARSE_DECLTYPES)
            #Objeto cursor
            cursor = db.cursor()
            query = """UPDATE productos SET nombre = '{}', descripcion = '{}', precio = {}, stock = {}, id_categoria = {},
                id_comercio = {} WHERE id = {}""".format(self.nombre, self.descripcion, self.precio, self.stock,
                self.categoria.id, self.comercio.id, self.id)
            cursor.execute(query)
            db.commit()
            estado = True
        except Exception as e:
            db.rollback()  # RESTAURAR ANTES DE CAMBIOS POR ERROR
            print("Error: {}".format(e))
        finally:
            #Cerrar conexión de db
            db.close()
            print(estado)

    @staticmethod
    def obtener(id: int):
        """Recibe un id como integer que es el Primary Key y una ruta de base datos. Devuelve un objeto Producto."""
        producto = None
        try:
            #Conexión a la base de datos usando ruta de archivo de configuración
            db = sqlite3.connect(Config.get("DATABASE"), detect_types=sqlite3.PARSE_DECLTYPES)
            #Objeto cursor
            cursor = db.cursor()
            query = """SELECT * FROM productos WHERE id = '{}'""".format(id)
            #Imprimir query a ejecutar
            print("\033[38;5;57m" + "\033[1m" + query + "\033[0m")
            cursor.execute(query)
            producto = cursor.fetchone()
            #query = """SELECT categorias.* FROM categorias JOIN productos ON
            #    categorias.id = productos.id_categoria WHERE productos.id = {}""".format(id)
            #cursor.execute(query)
            #categoria = cursor.fetchone()
            #query = """SELECT comercios.* FROM comercios JOIN productos ON comercios.id = productos.id_comercio WHERE productos.id = {}""".format(id)
            #cursor.execute(query)
            #comercio = cursor.fetchone()
        except Exception as e:
            print("Error: {}".format(e))
        finally:
            #Cerrar conexión de db
            db.close()
        if producto == None:
            print("No se pudo encontrar un Producto con el id:", id)
        else:
            return Producto(id = producto[0], nombre = producto[1], descripcion = producto[2], fotos_url = producto[3].split(","), precio = producto[4], stock = producto[5], fecha_de_creacion = producto[6], fecha_de_actualizacion = producto[7])

    @staticmethod
    def lista_de_productos_por_default():
        """Devuelve una lista con los productos más recientes"""
        pass
