#Importar libreria para sqlite3
import sqlite3
#Importar configuración
from config import Config
#Importar librería datetime par fechas
from datetime import datetime
#Importar módulo con funciones de ayuda
from app.helpers.helper import *

class Canasta(object):

    def __init__(self, id: int = None, usuario = None, productos: list = None, fecha_de_creacion: datetime = None, fecha_de_actualizacion: datetime = None):
        self.__id = id
        self.__fecha_de_creacion = fecha_de_creacion
        self.__fecha_de_actualizacion = fecha_de_actualizacion
        self.__usuario = usuario
        self.__productos = productos

    def __str__(self):
        return "id = {}, id_usuario = {}".format(self.id, self.usuario.id)

    def toJSON(self):
        """Retorna un diccionario con los atributos del objeto."""
        return {"id": self.id, "subtotal": self.subtotal()}

    @property
    def id(self):
        return self.__id

    @property
    def fecha_de_creacion(self):
        return self.__fecha_de_creacion

    @property
    def fecha_de_actualizacion(self):
        return self.__fecha_de_actualizacion

    @property
    def usuario(self):
        return self.__usuario

    @property
    def productos(self):
        return self.__productos

    @id.setter
    def id(self, nuevo_id):
        self.__id = nuevo_id

    @fecha_de_creacion.setter
    def fecha_de_creacion(self, nueva_fecha_de_creacion):
        self.__fecha_de_creacion = nueva_fecha_de_creacion

    @fecha_de_actualizacion.setter
    def fecha_de_actualizacion(self, nueva_fecha_de_actualizacion):
        self.__fecha_de_actualizacion = nueva_fecha_de_actualizacion

    @usuario.setter
    def usuario(self, nuevo_usuario):
        self.__usuario = nuevo_usuario

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
            #Consulta de tipo insert
            query = """INSERT INTO canastas (id_usuario) VALUES({});""".format(self.usuario.id)
            #Imprimir query a ejecutar
            print('\u001b[32m' + '\033[1m' + query + '\033[0m')
            #Ejecutar query
            cursor.execute(query)
            #Confirmar cambios a base de datos
            db.commit()
            #Cambiar estado a True
            estado = True
            #Query para hallar el id de la instancia recién creada
            query = """SELECT MAX(id) FROM canastas;"""
            #Ejecutar query
            cursor.execute(query)
            #Extraer resultado del query ejecutado
            id_nueva_canasta = cursor.fetchone()
            #Asignar id a objeto
            self.id = int(id_nueva_canasta[0])
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

    def borrar_productos(self):
        """Borra todos los productos agregados a esta canasta. No retorna nada."""
        pass

    def verificar_stock(self):
        """Devuelve True si todos los productos en la canasta contienen stock. Devuelve False caso contrario."""
        pass

    def borrar_productos_sin_stock(self):
        """Borra los productos del carrito que no tienen stock. No retorna nada."""
        pass

    def subtotal(self):
        """Devuelve la suma de los precios unitarios por la cantidad de todos los productos en la canasta."""
        subtotal = 0
        from .producto_por_canasta import ProductoPorCanasta
        from .producto import Producto
        for producto_por_canasta in self.buscar_productos_por_canasta():
            producto_por_canasta = ProductoPorCanasta.obtener(producto_por_canasta.id)
            subtotal += producto_por_canasta.cantidad * producto_por_canasta.producto.precio
        return subtotal

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
            query = """UPDATE canastas SET id_usuario = {} WHERE id = {}""".format(self.usuario.id, self.id)
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

    def buscar_productos_por_canasta(self):
        """Devuelve un array con los productos por canasta que están dentro de la canasta."""
        productos_por_canasta = []
        try:
            #Conexión a la base de datos usando ruta de archivo de configuración
            db = sqlite3.connect(Config.get("DATABASE"), detect_types=sqlite3.PARSE_DECLTYPES)
            #Objeto cursor
            cursor = db.cursor()
            #Query de tipo SELECT
            query = """SELECT * FROM productos_por_canasta WHERE id_canasta = {}""".format(self.id)
            #Imprimir query a ejecutar
            print("\033[38;5;57m" + "\033[1m" + query + "\033[0m")
            cursor.execute(query)
            resultados = cursor.fetchall()
        except Exception as e:
            print("Error: {}".format(e))
        finally:
            #Cerrar conexión de db
            db.close()
            from .producto_por_canasta import ProductoPorCanasta
            for resultado in resultados:
                productos_por_canasta.append(ProductoPorCanasta.obtener(id = resultado[0]))
            return productos_por_canasta

    @staticmethod
    def obtener(id: int):
        """Recibe un id como integer que es el Primary Key. Devuelve un objeto Canasta."""
        resultado = None
        try:
            #Conexión a la base de datos usando ruta de archivo de configuración
            db = sqlite3.connect(Config.get("DATABASE"), detect_types=sqlite3.PARSE_DECLTYPES)
            #Objeto cursor
            cursor = db.cursor()
            query = """SELECT * FROM canastas WHERE id = {}""".format(id)
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
            print("No se pudo encontrar una Canasta con el id:", id)
        else:
            #from .usuario import Usuario
            return Canasta(id = resultado[0], fecha_de_creacion = resultado[1], fecha_de_actualizacion = resultado[2])
