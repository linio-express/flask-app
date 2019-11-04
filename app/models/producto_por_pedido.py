from .producto import Producto
from .pedido import Pedido
#Importar libreria para sqlite3
import sqlite3

class ProductoPorPedido(object):

    def __init__(self, id: int = None, producto = Producto(), pedido = Pedido(), cantidad: int = None, precio_unitario: float = None):
        self.__id = id
        self.__producto = producto
        self.__pedido = pedido
        self.__cantidad = cantidad
        self.__precio_unitario = precio_unitario

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

    def crear(self, database_filepath: str):
        """Recibe una ruta de base datos. Guarda el objeto en la db.
            Devuelve True si se logra guardar en la db, caso contrario devuelve False."""
        estado = False
        try:
            #Conexión a la base de datos usando database_filepath como ruta
            database = sqlite3.connect(database_filepath)
            #Objeto cursor
            cursor = database.cursor()
            query = """INSERT INTO productos_por_pedido (id_producto, id_pedido, cantidad, precio_unitario)
                VALUES({}, {}, {}, {})""".format(self.producto.id, self.pedido.id, self.cantidad, self.precio_unitario)
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
            query = """UPDATE productos_por_pedido SET id_producto = {}, id_pedido = {}, cantidad = {}, precio_unitario = {}
                WHERE id = {}""".format(self.producto.id, self.pedido.id, self.cantidad, self.precio_unitario, self.id)
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
        producto_por_pedido = None
        try:
            #Conexión a la base de datos usando database_filepath como ruta
            database = sqlite3.connect(database_filepath)
            #Objeto cursor
            cursor = database.cursor()
            query = """SELECT * FROM productos_por_pedido WHERE id = '{}'""".format(id)
            cursor.execute(query)
            producto_por_pedido = cursor.fetchone()
        except Exception as e:
            print("Error: {}".format(e))
        finally:
            #Cerrar conexión de db
            database.close()
        if producto_por_pedido == None:
            print("No se pudo encontrar un producto_por_pedido con el id:", id)
        else:
            return ProductoPorPedido(id = producto_por_pedido[0], producto = Producto.obtener(producto_por_pedido[1]),
                pedido = Pedido.obtener(producto_por_pedido[2]), cantidad = producto_por_pedido[3], precio_unitario = producto_por_pedido[4])
