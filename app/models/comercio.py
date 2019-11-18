#Importar libreria para sqlite3
import sqlite3
#Importar configuración
from config import Config
#Importar librería datetime par fechas
from datetime import datetime
#Importar módulo con funciones de ayuda
from app.helpers.helper import *

class Comercio(object):

    def __init__(self, id: int = None, nombre: str = None, direccion: str = None, ruc: str = None, logo_url: str = None, fecha_de_creacion: datetime = None, fecha_de_actualizacion: datetime = None, productos: list = None):
        self.__id = id
        self.__nombre = nombre
        self.__direccion = direccion
        self.__ruc = ruc
        self.__logo_url = logo_url
        self.__fecha_de_creacion = fecha_de_creacion
        self.__fecha_de_actualizacion = fecha_de_actualizacion
        self.__productos = productos

    def __str__(self):
        return '''id: {}, nombre: "{}", direccion: "{}", ruc: "{}"'''.format(self.__id, self.__nombre, self.__direccion, self.__ruc)

    def toJSON(self):
        """Devuelve un diccionario con los atributos del comercio"""
        return {"id": self.id, "nombre": self.nombre, "direccion": self.direccion, "ruc": self.ruc, "logo_url": self.logo_url}

    @property
    def id(self):
        return self.__id

    @property
    def nombre(self):
        return self.__nombre

    @property
    def direccion(self):
        return self.__direccion

    @property
    def ruc(self):
        return self.__ruc

    @property
    def logo_url(self):
        return self.__logo_url

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

    @direccion.setter
    def direccion(self, nueva_direccion):
        self.__direccion = nueva_direccion

    @ruc.setter
    def ruc(self, nuevo_ruc):
        self.__ruc = nuevo_ruc

    @logo_url.setter
    def logo_url(self, nuevo_logo_url):
        self.__logo_url = nuevo_logo_url

    @fecha_de_creacion.setter
    def fecha_de_creacion(self, nueva_fecha_de_creacion):
        self.__fecha_de_creacion = nueva_fecha_de_creacion

    @fecha_de_actualizacion.setter
    def fecha_de_actualizacion(self, nueva_fecha_de_actualizacion):
        self.__fecha_de_actualizacion = nueva_fecha_de_actualizacion

    @productos.setter
    def productos(self, nuevos_productos):
        self.__productos = nuevos_productos

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
            query = """INSERT INTO comercios (nombre, direccion, ruc)
                VALUES('{}', '{}', '{}')""".format(self.nombre, self.direccion, self.ruc)
            #Imprimir query a ejecutar
            print('\u001b[32m' + '\033[1m' + query + '\033[0m')
            #Ejecutar query
            cursor.execute(query)
            #Confirmar cambios a base de datos
            db.commit()
            #Cambiar estado a True
            estado = True
            #Query para hallar el id de la instancia recién creada
            query = """SELECT MAX(id) FROM comercios;"""
            #Ejecutar query
            cursor.execute(query)
            #Extraer resultado del query ejecutado
            id_nueva_comercio = cursor.fetchone()
            #Asignar id a objeto
            self.id = int(id_nueva_comercio[0])
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
            query = """UPDATE comercios SET nombre = '{}', direccion = '{}', ruc = '{}'
                WHERE id = {}""".format(self.nombre, self.direccion, self.ruc, self.id)
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
    def obtener(id: int, database_filepath: str):
        """Recibe un id como integer que es el Primary Key y una ruta de base datos. Devuelve un objeto Comercio."""
        resultado = None
        try:
            #Conexión a la base de datos usando database_filepath como ruta
            database = sqlite3.connect(database_filepath)
            #Objeto cursor
            cursor = database.cursor()
            query = """SELECT * FROM comercios WHERE id = {}""".format(id)
            #Imprimir query a ejecutar
            print("\033[38;5;57m" + "\033[1m" + query + "\033[0m")
            cursor.execute(query)
            resultado = cursor.fetchone()
        except Exception as e:
            print("Error: {}".format(e))
        finally:
            #Cerrar conexión de db
            database.close()
        if resultado == None:
            print("No se pudo encontrar un Comercio con el id:", id)
        else:
            return Comercio(id = resultado[0], nombre = resultado[1], direccion = resultado[2], ruc = resultado[3], logo_url = resultado[4], fecha_de_creacion = resultado[5], fecha_de_actualizacion = resultado[6])
