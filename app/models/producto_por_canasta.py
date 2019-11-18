from .producto import Producto
from .canasta import Canasta
#Importar libreria para sqlite3
import sqlite3
#Importar librería datetime par fechas
from datetime import datetime
#Importar configuración
from config import Config
#Importar módulo con funciones de ayuda
from app.helpers.helper import *

class ProductoPorCanasta(object):

    def __init__(self, id: int = None, canasta = Canasta(), producto = Producto(), cantidad: int = None, fecha_de_creacion: datetime = None, fecha_de_actualizacion: datetime = None):
        self.__id = id
        self.__canasta = canasta
        self.__producto = producto
        self.__cantidad = cantidad
        self.__fecha_de_creacion = fecha_de_creacion
        self.__fecha_de_actualizacion = fecha_de_actualizacion

    def __srt__(self):
        return "id = {}, id_canasta = {}, id_producto = {}, cantidad = {}".format(self.id, self.canasta.id, self.producto.id, self.cantidad)

    def toJSON(self):
        return {"id": self.id, "producto": self.producto.toJSON(), "cantidad": self.cantidad}

    @property
    def id(self):
        return self.__id

    @property
    def canasta(self):
        return self.__canasta

    @property
    def producto(self):
        return self.__producto

    @property
    def cantidad(self):
        return self.__cantidad

    @property
    def fecha_de_creacion(self):
        return self.__fecha_de_creacion

    @property
    def fecha_de_actualizacion(self):
        return self.__fecha_de_actualizacion

    @canasta.setter
    def canasta(self, nueva_canasta):
        self.__canasta = nueva_canasta

    @producto.setter
    def producto(self, nuevo_producto):
        self.__producto = nuevo_producto

    @cantidad.setter
    def cantidad(self, cantidad):
        self.__cantidad = cantidad

    @fecha_de_creacion.setter
    def fecha_de_creacion(self, nueva_fecha_de_creacion):
        self.__fecha_de_creacion = nueva_fecha_de_creacion

    @fecha_de_actualizacion.setter
    def fecha_de_actualizacion(self, nueva_fecha_de_actualizacion):
        self.__fecha_de_actualizacion = nueva_fecha_de_actualizacion

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
            query = """INSERT INTO productos_por_canasta (id_producto, id_canasta, cantidad) VALUES({}, {}, {})""".format(self.producto.id, self.canasta.id, self.cantidad)
            #Imprimir query a ejecutar
            print('\u001b[32m' + '\033[1m' + query + '\033[0m')
            #Ejecutar query
            cursor.execute(query)
            #Confirmar cambios a base de datos
            db.commit()
            #Cambiar estado a True
            estado = True
            #Query para hallar el id de la instancia recién creada
            query = """SELECT MAX(id) FROM productos_por_canasta;"""
            #Ejecutar query
            cursor.execute(query)
            #Extraer resultado del query ejecutado
            id_nuevo_producto_por_canasta = cursor.fetchone()
            #Asignar id a objeto
            self.id = int(id_nuevo_producto_por_canasta[0])
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

    def borrar(self):
        """Devuelve True si se logra borrar en la db, caso contrario devuelve False."""
        estado = False
        try:
            #Conexión a la base de datos usando ruta de archivo de configuración
            db = sqlite3.connect(Config.get("DATABASE"), detect_types=sqlite3.PARSE_DECLTYPES)
            #Objeto cursor
            cursor = db.cursor()
            #Query de tipo DELETE
            query = "DELETE FROM productos_por_canasta WHERE id = {}".format(self.id)
            #Se imprime el query a ejecutar
            print('\033[1m' + '\u001b[31m' + query + '\033[0m')
            #Se ejecuta el query
            cursor.execute(query)
            #Se confirma los cabios a la db
            db.commit()
            #Se imprime la confirmación de cambios en la consola
            print('\u001b[36m' + '\033[91m' + 'commit transaction' + '\033[0m')
            estado = True
        except Exception as e:
            #Rollback en caso de error
            db.rollback()
            print("Error: {}".format(e))
        finally:
            #Cerrar conexión de db
            db.close()
            return estado

    def actualizar(self):
        """Recibe una ruta de base datos. Actualiza el objeto en la db.
            Devuelve True si se logra actualizar en la db, caso contrario devuelve False."""
        estado = False
        try:
            #Conexión a la base de datos usando ruta de archivo de configuración
            db = sqlite3.connect(Config.get("DATABASE"), detect_types=sqlite3.PARSE_DECLTYPES)
            #Objeto cursor
            cursor = database.cursor()
            query = """UPDATE productos_por_canasta SET id_producto = {}, id_canasta = {}, cantidad = {}
                WHERE id = {}""".format(self.producto.id, self.canasta.id, self.cantidad, self.id)
            cursor.execute(query)
            database.commit()
            estado = True
        except Exception as e:
            #Rollback en caso de error
            database.rollback()
            print("Error: {}".format(e))
        finally:
            #Cerrar conexión de db
            database.close()
            print(estado)

    @staticmethod
    def obtener(id: int):
        """Recibe un id como integer que es el Primary Key y una ruta de base datos. Devuelve un objeto Canasta."""
        producto_por_canasta = None
        try:
            #Conexión a la base de datos usando ruta de archivo de configuración
            db = sqlite3.connect(Config.get("DATABASE"), detect_types=sqlite3.PARSE_DECLTYPES)
            #Objeto cursor
            cursor = db.cursor()
            query = """SELECT * FROM productos_por_canasta WHERE id = '{}'""".format(id)
            #Imprimir query a ejecutar
            print("\033[38;5;57m" + "\033[1m" + query + "\033[0m")
            cursor.execute(query)
            producto_por_canasta = cursor.fetchone()
        except Exception as e:
            print("Error: {}".format(e))
        finally:
            #Cerrar conexión de db
            db.close()
        if producto_por_canasta == None:
            print("No se pudo encontrar un producto_por_pedido con el id:", id)
        else:
            return ProductoPorCanasta(id = producto_por_canasta[0], producto = Producto.obtener(producto_por_canasta[1]), canasta = Canasta.obtener(producto_por_canasta[2]), cantidad = producto_por_canasta[3], fecha_de_creacion = producto_por_canasta[4], fecha_de_actualizacion = producto_por_canasta[5])
