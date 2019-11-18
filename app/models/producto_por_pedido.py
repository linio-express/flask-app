from .producto import Producto
from .pedido import Pedido
#Importar libreria para sqlite3
import sqlite3
#Importar configuración
from config import Config
#Importar librería datetime par fechas
from datetime import datetime
#Importar módulo con funciones de ayuda
from app.helpers.helper import *

class ProductoPorPedido(object):

    def __init__(self, id: int = None, producto = None, pedido = None, cantidad: int = None, precio_unitario: float = None, fecha_de_creacion: datetime = None, fecha_de_actualizacion: datetime = None):
        self.__id = id
        self.__producto = producto
        self.__pedido = pedido
        self.__cantidad = cantidad
        self.__precio_unitario = precio_unitario
        self.__fecha_de_creacion = fecha_de_creacion
        self.__fecha_de_actualizacion = fecha_de_actualizacion

    def __str__(self):
        return "id:" + str(self.id)

    def toJSON(self):
        return {"id": self.id, "producto": self.producto.toJSON(), "pedido": self.pedido.toJSON(), "cantidad": self.cantidad, "precio_unitario": self.precio_unitario, "precio_unitario_str": formato_de_precio(self.precio_unitario)}

    @property
    def id(self):
        return self.__id

    @property
    def producto(self):
        return self.__producto

    @property
    def pedido(self):
        return self.__pedido

    @property
    def cantidad(self):
        return self.__cantidad

    @property
    def precio_unitario(self):
        return self.__precio_unitario

    @property
    def fecha_de_creacion(self):
        return self.__fecha_de_creacion

    @property
    def fecha_de_actualizacion(self):
        return self.__fecha_de_actualizacion

    @id.setter
    def id(self, nuevo_id):
        self.__id = nuevo_id

    @producto.setter
    def producto(self, nuevo_producto):
        self.__producto = nuevo_producto

    @pedido.setter
    def pedido(self, nuevo_pedido):
        self.__pedido = nuevo_pedido

    @cantidad.setter
    def cantidad(self, nueva_cantidad):
        self.__cantidad = nueva_cantidad

    @precio_unitario.setter
    def precio_unitario(self, nuevo_precio_unitario):
        self.__precio_unitario = nuevo_precio_unitario

    @fecha_de_creacion.setter
    def fecha_de_creacion(self, nueva_fecha_de_creacion):
        self.__fecha_de_creacion = nueva_fecha_de_creacion

    @fecha_de_actualizacion.setter
    def fecha_de_actualizacion(self, nueva_fecha_de_actualizacion):
        self.__fecha_de_actualizacion = nueva_fecha_de_actualizacion

    def crear(self):
        """Recibe una ruta de base datos. Guarda el objeto en la db.
            Devuelve True si se logra guardar en la db, caso contrario devuelve False."""
        estado = False
        try:
            #Conexión a la base de datos usando ruta de archivo de configuración
            db = sqlite3.connect(Config.get("DATABASE"), detect_types=sqlite3.PARSE_DECLTYPES)
            #Objeto cursor
            cursor = db.cursor()
            query = """INSERT INTO productos_por_pedido (id_producto, id_pedido, cantidad, precio_unitario) VALUES({}, {}, {}, {})""".format(self.producto.id, self.pedido.id, self.cantidad, self.producto.precio)
            #Imprimir query a ejecutar
            print('\u001b[32m' + '\033[1m' + query + '\033[0m')
            #Ejecutar query
            cursor.execute(query)
            #Confirmar cambios a base de datos
            db.commit()
            #Cambiar estado a True
            estado = True
            #Query para hallar el id de la instancia recién creada
            query = """SELECT MAX(id) FROM productos_por_pedido;"""
            #Ejecutar query
            cursor.execute(query)
            #Extraer resultado del query ejecutado
            id_nuevo_producto_por_pedido = cursor.fetchone()
            #Asignar id a objeto
            self.id = int(id_nuevo_producto_por_pedido[0])
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
            query = """UPDATE productos_por_pedido SET id_producto = {}, id_pedido = {}, cantidad = {}, precio_unitario = {}
                WHERE id = {}""".format(self.producto.id, self.pedido.id, self.cantidad, self.precio_unitario, self.id)
            cursor.execute(query)
            #Se imprime la confirmación de cambios en la consola
            print('\u001b[36m' + '\033[91m' + 'commit transaction' + '\033[0m')
            db.commit()
            estado = True
        except Exception as e:
            #Rollback en caso de error
            db.rollback()
            print("Error: {}".format(e))
        finally:
            #Cerrar conexión de db
            db.close()
            print(estado)

    @staticmethod
    def obtener(id: int):
        """Recibe un id como integer que es el Primary Key y una ruta de base datos. Devuelve un objeto Canasta."""
        producto_por_pedido = None
        try:
            #Conexión a la base de datos usando ruta de archivo de configuración
            db = sqlite3.connect(Config.get("DATABASE"), detect_types=sqlite3.PARSE_DECLTYPES)
            #Objeto cursor
            cursor = db.cursor()
            query = """SELECT * FROM productos_por_pedido WHERE id = '{}'""".format(id)
            #Imprimir query a ejecutar
            print("\033[38;5;57m" + "\033[1m" + query + "\033[0m")
            cursor.execute(query)
            producto_por_pedido = cursor.fetchone()
        except Exception as e:
            print("Error: {}".format(e))
        finally:
            #Cerrar conexión de db
            db.close()
        if producto_por_pedido == None:
            print("No se pudo encontrar un producto_por_pedido con el id:", id)
        else:
            return ProductoPorPedido(id = producto_por_pedido[0], producto = Producto.obtener(producto_por_pedido[1]), pedido = Pedido.obtener(producto_por_pedido[2]), cantidad = producto_por_pedido[3], precio_unitario = producto_por_pedido[4], fecha_de_creacion = producto_por_pedido[5], fecha_de_actualizacion = producto_por_pedido[6])
