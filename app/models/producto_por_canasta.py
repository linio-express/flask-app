from .producto import Producto
from .canasta import Canasta
#Importar libreria para sqlite3
import sqlite3

class ProductoPorCanasta(object):

    def __init__(self, id: int = None, canasta = Canasta(), producto = Producto(), cantidad: int = None):
        self.__id = id
        self.__canasta = canasta
        self.__producto = producto
        self.__cantidad = cantidad

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

    @canasta.setter
    def canasta(self, nueva_canasta):
        self.__canasta = nueva_canasta

    @producto.setter
    def producto(self, nuevo_producto):
        self.__producto = nuevo_producto

    @cantidad.setter
    def cantidad(self, cantidad):
        self.__cantidad = cantidad

    def crear(self, database_filepath: str):
        """Recibe una ruta de base datos. Guarda el objeto en la db.
            Devuelve True si se logra guardar en la db, caso contrario devuelve False."""
        estado = False
        try:
            #Conexión a la base de datos usando database_filepath como ruta
            database = sqlite3.connect(database_filepath)
            #Objeto cursor
            cursor = database.cursor()
            query = """INSERT INTO productos_por_canasta (id_producto, id_canasta, cantidad)
                VALUES({}, {}, {}, {})""".format(self.producto.id, self.canasta.id, self.cantidad)
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

    def actualizar(self, database_filepath: str):
        """Recibe una ruta de base datos. Actualiza el objeto en la db.
            Devuelve True si se logra actualizar en la db, caso contrario devuelve False."""
        estado = False
        try:
            #Conexión a la base de datos usando database_filepath como ruta
            database = sqlite3.connect(database_filepath)
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
    def obtener(id: int, database_filepath: str):
        """Recibe un id como integer que es el Primary Key y una ruta de base datos. Devuelve un objeto Canasta."""
        producto_por_canasta = None
        try:
            #Conexión a la base de datos usando database_filepath como ruta
            database = sqlite3.connect(database_filepath)
            #Objeto cursor
            cursor = database.cursor()
            query = """SELECT * FROM productos_por_canasta WHERE id = '{}'""".format(id)
            cursor.execute(query)
            producto_por_canasta = cursor.fetchone()
        except Exception as e:
            print("Error: {}".format(e))
        finally:
            #Cerrar conexión de db
            database.close()
        if producto_por_pedido == None:
            print("No se pudo encontrar un producto_por_pedido con el id:", id)
        else:
            return ProductoPorPedido(id = producto_por_canasta[0], producto = Producto.obtener(producto_por_canasta[1]),
                canasta = Canasta.obtener(producto_por_canasta[2]), cantidad = producto_por_canasta[3], precio_unitario = producto_por_canasta[4])
