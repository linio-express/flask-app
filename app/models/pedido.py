from datetime import datetime
#Importar libreria para sqlite3
import sqlite3
from .usuario import Usuario

class Pedido(object):

    def __init__(self, id: int = None, usuario = Usuario(), tarifa_de_envio: float = None, fecha_de_creacion: datetime = None,
        estado: str = None, repartidor: str = None, productos: list = None, metodo_de_pago: str = None,
        direccion_de_envio: str = None, fecha_de_envio: datetime = None, fecha_de_envio_programada: datetime = None,
        fecha_de_entrega: datetime = None):

        self.__id = id
        self.__usuario = usuario
        self.__tarifa_de_envio = tarifa_de_envio
        self.__fecha_de_creacion = fecha_de_creacion
        self.__estado = estado
        self.__repartidor = repartidor
        self.__productos = productos
        self.__metodo_de_pago = metodo_de_pago
        self.__direccion_de_envio = direccion_de_envio
        self.__fecha_de_envio = tarifa_de_envio
        self.__fecha_de_envio_programada = fecha_de_envio_programada
        self.__fecha_de_entrega = fecha_de_entrega

    def __str__(self):
        pass

    @property
    def id(self):
        return self.__id

    @property
    def usuario(self):
        return self.__usuario

    @property
    def tarifa_de_envio(self):
        return self.__tarifa_de_envio

    @property
    def fecha_de_creacion(self):
        return self.__fecha_de_creacion

    @property
    def estado(self):
        return self.__estado

    @property
    def repartidor(self):
        return self.__repartidor

    @property
    def productos(self):
        return self.__productos

    @property
    def metodo_de_pago(self):
        return self.__metodo_de_pago

    @property
    def direccion_de_envio(self):
        return self.__direccion_de_envio

    @property
    def fecha_de_envio(self):
        return self.__fecha_de_envio

    @usuario.setter
    def usuario(self, nuevo_usuario):
        self.__usuario = nuevo_usuario

    @tarifa_de_envio.setter
    def tarifa_de_envio(self, nueva_tarifa_de_envio):
        self.__tarifa_de_envio = nueva_tarifa_de_envio

    @fecha_de_creacion.setter
    def fecha_de_creacion(self, nueva_fecha_de_creacion):
        self.__fecha_de_creacion = nueva_fecha_de_creacion

    @estado.setter
    def estado(self, nuevo_estado):
        self.__estado = nuevo_estado

    @repartidor.setter
    def repartidor(self, nuevo_repartidor):
        self.__repartidor = nuevo_repartidor

    @productos.setter
    def productos(self, nuevos_productos):
        self.__productos = nuevos_productos

    @metodo_de_pago.setter
    def metodo_de_pago(self, nuevo_metodo_de_pago):
        self.__metodo_de_pago = nuevo_metodo_de_pago

    @direccion_de_envio.setter
    def direccion_de_envio(self, nueva_direccion_de_envio):
        self.__direccion_de_envio = nueva_direccion_de_envio

    @fecha_de_envio.setter
    def fecha_de_envio(self, nueva_fecha_de_envio):
        self.__fecha_de_envio = nueva_fecha_de_envio

    def se_puede_cancelar(self):
        if self.repartidor == None:
            return True
        else:
            return False

    def cancelar_pedido(self):
        self.estado = "Cancelado"

    def precio_total(self):
        precio_total = 0
        for producto in self.productos:
            precio_total += producto.precio_unitario * producto.cantidad
        return precio_total

    @staticmethod
    def obtener(id: int, database_filepath: str):
        """Recibe un id como integer que es el Primary Key y una ruta de base datos. Devuelve un objeto Pedido."""
        pedido = None
        try:
            #Conexión a la base de datos usando database_filepath como ruta
            database = sqlite3.connect(database_filepath)
            #Objeto cursor
            cursor = database.cursor()
            query = """SELECT * FROM productos WHERE id = '{}'""".format(id)
            cursor.execute(query)
            pedido = cursor.fetchone()
        except Exception as e:
            print("Error: {}".format(e))
        finally:
            #Cerrar conexión de db
            database.close()
        if pedido == None:
            print("No se pudo encontrar un Pedido con el id:", id)
        else:
            return Pedido(id = pedido[0], usuario = Usuario.obtener(pedido[1]), fecha_de_creacion = pedido[3],
                estado = pedido[4], repartidor = pedido[5], metodo_de_pago = pedido[6], tarifa_de_envio = pedido[7],
                fecha_de_envio = pedido[8], fecha_de_entrega_programada = pedido[9], fecha_de_entrega = pedido[10])
