from .categoria import Categoria
from .comercio import Comercio
#Importar libreria para sqlite3
import sqlite3

class Producto(object):

    def __init__(self, id: int = None, nombre: str = None, descripcion: str = None, precio: float = None,
        stock: int = None, categoria = None, comercio = None, pedidos: list = None, canastas: list = None):
        self.__id = id
        self.__nombre = nombre
        self.__descripcion = descripcion
        self.__precio = precio
        self.__stock = stock
        #Array de objetos Canasta
        self.__canastas = canastas
        #Array de objetos Pedido
        self.__pedidos = pedidos
        self.__categoria = categoria
        self.__comercio = comercio

    def __str__(self):
        return "id = {}, nombre = '{}', descripcion = '{}', precio = {}, stock = {}, id_categoria = {}, id_comercio = {}".format(self.id, self.nombre, self.descripcion, self.precio, self.stock, self.categoria.id, self.comercio.id)

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
    def precio(self):
        return self.__precio

    @property
    def stock(self):
        return self.__stock

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

    @precio.setter
    def precio(self, nuevo_precio):
        self.__precio = nuevo_precio

    @stock.setter
    def stock(self, nuevo_stock):
        self.__stock = nuevo_stock

    @stock.setter
    def stock(self, nuevo_stock):
        self.__stock = nuevo_stock

    @categoria.setter
    def categoria(self, nueva_categoria):
        self.__categoria = nueva_categoria

    @comercio.setter
    def comercio(self, nuevo_comercio):
        self.__comercio = nuevo_comercio

    def crear(self, database_filepath: str):
        """Recibe una ruta de base datos. Guarda el objeto en la db.
            Devuelve True si se logra guardar en la db, caso contrario devuelve False."""
        estado = False
        try:
            #Conexión a la base de datos usando database_filepath como ruta
            database = sqlite3.connect(database_filepath)
            #Objeto cursor
            cursor = database.cursor()
            query = """INSERT INTO productos (nombre, descripcion, precio, stock, id_categoria, id_comercio)
                VALUES('{}', '{}', {}, {}, {}, {})""".format(self.nombre, self.descripcion, self.precio,
                self.stock, self.categoria.id, self.comercio.id)
            cursor.execute(query)
            database.commit()
            estado = True
        except Exception as e:
            database.rollback()  # RESTAURAR ANTES DE CAMBIOS POR ERROR
            print("Error: {}".format(e))
        finally:
            #Cerrar conexión de db
            database.close()
            print(estado)

    def actualizar(self, database_filepath: str):
        """Recibe una ruta de base datos. Actualiza el objeto en la db.
            Devuelve True si se logra actualizar en la db, caso contrario devuelve False."""
        estado = False
        try:
            #Conexión a la base de datos usando database_filepath como ruta
            database = sqlite3.connect(database_filepath)
            #Objeto cursor
            cursor = database.cursor()
            query = """UPDATE productos SET nombre = '{}', descripcion = '{}', precio = {}, stock = {}, id_categoria = {},
                id_comercio = {} WHERE id = {}""".format(self.nombre, self.descripcion, self.precio, self.stock,
                self.categoria.id, self.comercio.id, self.id)
            cursor.execute(query)
            database.commit()
            estado = True
        except Exception as e:
            database.rollback()  # RESTAURAR ANTES DE CAMBIOS POR ERROR
            print("Error: {}".format(e))
        finally:
            #Cerrar conexión de db
            database.close()
            print(estado)

    @staticmethod
    def obtener(id: int, database_filepath: str):
        """Recibe un id como integer que es el Primary Key y una ruta de base datos. Devuelve un objeto Comercio."""
        producto = None
        try:
            #Conexión a la base de datos usando database_filepath como ruta
            database = sqlite3.connect(database_filepath)
            #Objeto cursor
            cursor = database.cursor()
            query = """SELECT * FROM productos WHERE id = '{}'""".format(id)
            cursor.execute(query)
            producto = cursor.fetchone()
            query = """SELECT categorias.* FROM categorias JOIN productos ON
                categorias.id = productos.id_categoria WHERE productos.id = {}""".format(id)
            cursor.execute(query)
            categoria = cursor.fetchone()
            query = """SELECT comercios.* FROM comercios JOIN productos ON comercios.id = productos.id_comercio WHERE productos.id = {}""".format(id)
            cursor.execute(query)
            comercio = cursor.fetchone()
        except Exception as e:
            print("Error: {}".format(e))
        finally:
            #Cerrar conexión de db
            database.close()
        if producto == None:
            print("No se pudo encontrar un Producto con el id:", id)
        else:
            return Producto(id = producto[0], nombre = producto[1], descripcion = producto[2], precio = producto[3],
                stock = producto[4], categoria = Categoria.obtener(producto[5], database_filepath),
                comercio = Comercio.obtener(producto[6],database_filepath))
