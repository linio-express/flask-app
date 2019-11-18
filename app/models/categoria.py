#Importar libreria para sqlite3
import sqlite3
#Importar configuración
from config import Config
#Importar librería datetime par fechas
from datetime import datetime
#Importar módulo con funciones de ayuda
from app.helpers.helper import *

class Categoria(object):

    def __init__(self, id: int = None, nombre: str = None, icono_url:str = None, fecha_de_creacion: datetime = None, fecha_de_actualizacion: datetime = None):
        self.__id = id
        self.__nombre = nombre
        self.__icono_url = icono_url
        self.__fecha_de_creacion = fecha_de_creacion
        self.__fecha_de_actualizacion = fecha_de_actualizacion
        #Array con objetos Producto
        self.__productos = []

    def __str__(self):
        return "id = {}, nombre = {}".format(self.id, self.nombre)

    def toJSON(self):
        return {"id": self.id, "nombre": self.nombre, "icono_url": self.icono_url}

    @property
    def id(self):
        return self.__id

    @property
    def nombre(self):
        return self.__nombre

    @property
    def icono_url(self):
        return self.__icono_url

    @property
    def fecha_de_creacion(self):
        return self.__fecha_de_creacion

    @property
    def fecha_de_actualizacion(self):
        return self.__fecha_de_actualizacion

    @property
    def productos(self):
        return self.__productos

    @nombre.setter
    def nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre

    @icono_url.setter
    def icono_url(self, nuevo_icono_url):
        self.__icono_url = nuevo_icono_url

    @fecha_de_creacion.setter
    def fecha_de_creacion(self, nueva_fecha_de_creacion):
        self.__fecha_de_creacion = nueva_fecha_de_creacion

    @fecha_de_actualizacion.setter
    def fecha_de_actualizacion(self, nueva_fecha_de_actualizacion):
        self.__fecha_de_actualizacion = nueva_fecha_de_actualizacion

    @productos.setter
    def productos(self, nuevos_productos):
        self.__productos = nuevos_productos

    @staticmethod
    def todas():
        """Devuelve una lista con todas las categorías. Cada elemento de la lista es un objeto"""
        categorias = []
        try:
            #Conexión a la base de datos usando ruta de archivo de configuración
            db = sqlite3.connect(Config.get("DATABASE"), detect_types=sqlite3.PARSE_DECLTYPES)
            #Objeto cursor
            cursor = db.cursor()
            query = """SELECT * FROM categorias;"""
            cursor.execute(query)
            resultados = cursor.fetchall()
        except Exception as e:
            print("Error: {}".format(e))
        finally:
            #Cerrar conexión de db
            db.close()
            for resultado in resultados:
                categorias.append(Categoria(id = resultado[0], nombre = resultado[1], icono_url = resultado[2]))
            return categorias

    def buscar_productos(self):
        """Devuelve una lista con todos los productos de esta categoría en la db. Cada elemento de la lista es un objeto de tipo Producto"""
        productos = []
        try:
            #Conexión a la base de datos usando ruta de archivo de configuración
            db = sqlite3.connect(Config.get("DATABASE"), detect_types=sqlite3.PARSE_DECLTYPES)
            #Objeto cursor
            cursor = db.cursor()
            #Query de tipo SELECT
            query = """SELECT * FROM productos WHERE id_categoria = {}""".format(self.id)
            #Imprimir query a ejecutar
            print("\033[38;5;57m" + "\033[1m" + query + "\033[0m")
            #Ejecutar query
            cursor.execute(query)
            #Extraer resultados y asignar a variable resultados
            resultados = cursor.fetchall()
        except Exception as e:
            #En caso de error, imprimir errores.
            print("Error: {}".format(e))
        finally:
            #Cerrar conexión de db
            db.close()
            #Importar clase Producto
            from .producto import Producto
            for resultado in resultados:
                productos.append(Producto.obtener(id = resultado[0]))
            return productos

    def tiene_stock(self):
        """Devuelve True si en esta categoría hay al menos un producto con stock mayor a cero.
            Caso contrario, devuelve cero."""
        pass

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
            query = """INSERT INTO categorias (nombre, icono_url) VALUES('{}')""".format(self.nombre, self.icono_url)
            #Imprimir query a ejecutar
            print('\u001b[32m' + '\033[1m' + query + '\033[0m')
            #Ejecutar query
            cursor.execute(query)
            #Confirmar cambios a base de datos
            db.commit()
            #Cambiar estado a True
            estado = True
            #Query para hallar el id de la instancia recién     creada
            query = """SELECT MAX(id) FROM categorias;"""
            #Ejecutar query
            cursor.execute(query)
            #Extraer resultado del query ejecutado
            id_nueva_categoria = cursor.fetchone()
            #Asignar id a objeto
            self.id = int(id_nueva_categoria[0])
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
        """Actualiza los valores de la instancia en la db según los atributos del objeto.
            Devuelve True si se logra actualizar en la db, caso contrario devuelve False."""
        estado = False
        try:
            #Conexión a la base de datos usando ruta de archivo de configuración
            db = sqlite3.connect(Config.get("DATABASE"), detect_types=sqlite3.PARSE_DECLTYPES)
            #Objeto cursor
            cursor = db.cursor()
            #Consulta de tipo UPDATE
            query = """UPDATE categorias SET nombre = '{}', icono_url = '{}' WHERE id = {}""".format(self.nombre, self.icono_url, self.id)
            #Imprimir query a ejecutar
            print('\u001b[33m' + '\033[1m' + query + '\033[0m')
            #Ejecutar query
            cursor.execute(query)
            #Confirmar cambios a base de datos
            db.commit()
            #Cambiar estado a True
            estado = True
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

    @staticmethod
    def obtener(id: int):
        """Recibe un id como integer que es el Primary Key y una ruta de base datos. Devuelve un objeto Categoria."""
        resultado = None
        try:
            #Conexión a la base de datos usando ruta de archivo de configuración
            db = sqlite3.connect(Config.get("DATABASE"), detect_types=sqlite3.PARSE_DECLTYPES)
            #Objeto cursor
            cursor = db.cursor()
            query = """SELECT * FROM categorias WHERE id = {}""".format(id)
            #Imprimir query a ejecutar
            print("\033[38;5;57m" + "\033[1m" + query + "\033[0m")
            cursor.execute(query)
            resultado = cursor.fetchone()
        except Exception as e:
            print("Error: {}".format(e))
        finally:
            #Cerrar conexión de db
            db.close()
        if resultado == None:
            print("No se pudo encontrar una Categoria con el id:", id)
        else:
            return Categoria(id = resultado[0], nombre = resultado[1], icono_url = resultado[2], fecha_de_creacion = resultado[3], fecha_de_actualizacion = resultado[4])
