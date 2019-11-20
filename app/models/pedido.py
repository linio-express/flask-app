#Importar librería datetime par fechas
from datetime import datetime
#Importar libreria para sqlite3
import sqlite3
from .usuario import Usuario
#Importar configuración
from config import Config
#Importar módulo con funciones de ayuda
from app.helpers.helper import *

class Pedido(object):

    #posibles_estados = ['Cancelado', 'En Progreso (Pago y dirección pendientes)', 'En Progreso (Pago pendiente)', 'En Progreso (Dirección pendiente)', 'En Progreso (Pago rechazado)', 'En Progreso (Pago rechazado y dirección pendiente)', 'En Progreso (Preparando paquete)'. 'Enviado', 'Entregado']

    def __init__(self, id: int = None, usuario = Usuario(), tarifa_de_envio: float = None, fecha_de_creacion: datetime = None, fecha_de_actualizacion: datetime = None, estado: str = None, repartidor: str = None, productos: list = None, metodo_de_pago: str = None, direccion_de_envio: str = None, fecha_de_envio: datetime = None, fecha_de_pago: datetime = None, fecha_de_entrega: datetime = None):
        self.__id = id
        self.__usuario = usuario
        self.__tarifa_de_envio = tarifa_de_envio
        self.__fecha_de_creacion = fecha_de_creacion
        self.__fecha_de_actualizacion = fecha_de_actualizacion
        self.__estado = estado
        self.__repartidor = repartidor
        self.__productos = productos
        self.__metodo_de_pago = metodo_de_pago
        self.__direccion_de_envio = direccion_de_envio
        self.__fecha_de_envio = fecha_de_envio
        self.__fecha_de_pago = fecha_de_pago
        self.__fecha_de_entrega = fecha_de_entrega

    def __str__(self):
        pass

    def toJSON(self):
        return {"id": self.__id, "tarifa_de_envio": self.__tarifa_de_envio, "estado": self.__estado, "repartidor": self.__repartidor, "metodo_de_pago": self.__metodo_de_pago, "direccion_de_envio": self.__direccion_de_envio, "fecha_de_creacion": self.fecha_de_creacion, "fecha_de_creacion_str": formato_corto(self.fecha_de_creacion), "precio_total": self.precio_total(), "precio_total_str": formato_de_precio(self.precio_total()), "cantidad_total": int(self.cantidad_total()), "productos_str": self.productos_str(), "subtotal_str": formato_de_precio(self.subtotal()), "tarifa_de_envio_str": formato_de_precio(self.tarifa_de_envio), "fecha_de_pago_str": formato_largo(self.fecha_de_pago)}

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
    def fecha_de_actualizacion(self):
        return self.__fecha_de_actualizacion

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

    @property
    def fecha_de_pago(self):
        return self.__fecha_de_pago

    @property
    def fecha_de_entrega(self):
        return self.__fecha_de_entrega

    @id.setter
    def id(self, nuevo_id):
        self.__id = nuevo_id

    @usuario.setter
    def usuario(self, nuevo_usuario):
        self.__usuario = nuevo_usuario

    @tarifa_de_envio.setter
    def tarifa_de_envio(self, nueva_tarifa_de_envio):
        self.__tarifa_de_envio = nueva_tarifa_de_envio

    @fecha_de_creacion.setter
    def fecha_de_creacion(self, nueva_fecha_de_creacion):
        self.__fecha_de_creacion = nueva_fecha_de_creacion

    @fecha_de_actualizacion.setter
    def fecha_de_actualizacion(self, nueva_fecha_de_actualizacion):
        self.__fecha_de_actualizacion = nueva_fecha_de_actualizacion

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

    @fecha_de_pago.setter
    def fecha_de_pago(self, nueva_fecha_de_pago):
        self.__fecha_de_pago = nueva_fecha_de_pago

    @fecha_de_envio.setter
    def fecha_de_entrega(self, nueva_fecha_de_entrega):
        self.__fecha_de_entrega = nueva_fecha_de_entrega

    def se_puede_cancelar(self):
        if self.repartidor == None:
            return True
        else:
            return False

    def cancelar_pedido(self):
        self.estado = "Cancelado"

    @staticmethod
    def generar_pedido(id_canasta: int):
        """Devuelve un nuevo pedido a partir de un id de canasta.
            Crea los productos_por_pedido necesarios."""
        #Importar clase Canasta
        from .canasta import Canasta
        #Importar clase ProductoPorCanasta
        from .producto_por_canasta import ProductoPorCanasta
        #Importar clase ProductoPorPedido
        from .producto_por_pedido import ProductoPorPedido
        #Creación de objeto Canasta
        canasta = Canasta.obtener(id_canasta)
        productos_por_canasta = canasta.buscar_productos_por_canasta()
        nuevo_pedido = Pedido()
        nuevo_pedido.usuario = Usuario.obtener(id_canasta)
        #Todo pedido recién creado tiene el estado "Nuevo"
        nuevo_pedido.estado = "En Progreso (Pago y dirección pendientes)"
        #La tarifa de envío es fija
        nuevo_pedido.tarifa_de_envio = 15
        #Valores por default
        nuevo_pedido.repartidor = ""
        nuevo_pedido.metodo_de_pago = ""
        nuevo_pedido.direccion_de_envio = ""
        nuevo_pedido.fecha_de_pago = datetime(1,1,1)
        nuevo_pedido.fecha_de_envio = datetime(1,1,1)
        nuevo_pedido.fecha_de_entrega = datetime(1,1,1)
        #Se crea un nuevo pedido
        nuevo_pedido.crear()
        for producto_por_canasta in productos_por_canasta:
            nuevo_producto_por_pedido = ProductoPorPedido()
            nuevo_producto_por_pedido.producto = producto_por_canasta.producto
            nuevo_producto_por_pedido.pedido = nuevo_pedido
            nuevo_producto_por_pedido.cantidad = producto_por_canasta.cantidad
            nuevo_producto_por_pedido.crear()
            producto = nuevo_producto_por_pedido.producto
            producto.stock -= 1
            producto_por_canasta.borrar()
            #producto.actualizar()
        return nuevo_pedido

    def subtotal(self) -> float:
        subtotal = 0
        for producto_por_pedido in self.buscar_productos_por_pedido():
            subtotal += producto_por_pedido.cantidad * producto_por_pedido.precio_unitario
        return subtotal

    def precio_total(self) -> float:
        precio_total = self.tarifa_de_envio + self.subtotal()
        return precio_total

    def cantidad_total(self) -> int:
        cantidad_total = 0
        for producto_por_pedido in self.buscar_productos_por_pedido():
            cantidad_total += producto_por_pedido.cantidad
        return cantidad_total

    def productos_str(self) -> str:
        """Devuelve una cadena de texto que es un resumen de los productos que hay en el carrito."""
        productos_por_pedido = self.buscar_productos_por_pedido()
        cadena_texto = productos_por_pedido[0].producto.nombre
        for i in range(1, len(productos_por_pedido)):
            cadena_texto += ", " + productos_por_pedido[i].producto.nombre
        return cadena_texto

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
            query = """INSERT INTO pedidos (id_usuario, estado, repartidor, metodo_de_pago, direccion_de_envio, tarifa_de_envio, fecha_de_pago, fecha_de_envio, fecha_de_entrega) VALUES ({}, '{}', '{}', '{}', '{}', {}, '{}', '{}', '{}');""".format(self.usuario.id, self.estado, self.repartidor, self.metodo_de_pago, self.direccion_de_envio, self.tarifa_de_envio, self.fecha_de_pago, self.fecha_de_envio, self.fecha_de_entrega)
            #Imprimir query a ejecutar
            print('\u001b[32m' + '\033[1m' + query + '\033[0m')
            #Ejecutar query
            cursor.execute(query)
            #Confirmar cambios a base de datos
            db.commit()
            #Cambiar estado a True
            estado = True
            #Query para hallar el id de la instancia recién creada
            query = """SELECT MAX(id) FROM pedidos;"""
            #Ejecutar query
            cursor.execute(query)
            #Extraer resultado del query ejecutado
            id_nuevo_pedido = cursor.fetchone()
            #Asignar id a objeto
            self.id = int(id_nuevo_pedido[0])
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
            query = """UPDATE pedidos SET id_usuario = {}, tarifa_de_envio = {}, fecha_de_actualizacion = '{}', estado = '{}', repartidor = '{}', metodo_de_pago = '{}', direccion_de_envio = '{}', tarifa_de_envio = '{}', fecha_de_pago = '{}' WHERE id = {}""".format(self.usuario.id, self.tarifa_de_envio, datetime.now(), self.estado, self.repartidor, self.metodo_de_pago, self.direccion_de_envio, self.tarifa_de_envio, self.fecha_de_pago, self.id)
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
        """Recibe un id como integer que es el Primary Key y una ruta de base datos. Devuelve un objeto Pedido."""
        pedido = None
        #Conexión a la base de datos usando ruta de archivo de configuración
        db = sqlite3.connect(Config.get("DATABASE"), detect_types=sqlite3.PARSE_DECLTYPES)
        try:
            #Objeto cursor
            cursor = db.cursor()
            query = """SELECT * FROM pedidos WHERE id = {}""".format(id)
            #Imprimir query a ejecutar
            print("\033[38;5;57m" + "\033[1m" + query + "\033[0m")
            #Ejecutar query
            cursor.execute(query)
            pedido = cursor.fetchone()
            print(pedido)
        except Exception as e:
            print("Error: {}".format(e))
        finally:
            #Cerrar conexión de db
            db.close()
            if pedido == None:
                print("No se pudo encontrar un Pedido con el id:", id)
            else:
                return Pedido(id = pedido[0], usuario = Usuario.obtener(pedido[1]), fecha_de_creacion = pedido[2], fecha_de_actualizacion = pedido[3], estado = pedido[4], repartidor = pedido[5], metodo_de_pago = pedido[6], direccion_de_envio = pedido[7], tarifa_de_envio = pedido[8], fecha_de_pago = pedido[9], fecha_de_envio = pedido[10], fecha_de_entrega = pedido[11])

    def buscar_productos_por_pedido(self):
        """Busca los productos para este pedido en la db. Devuelve una lista donde cada elemento es un objeto de tipo ProductoPorPedido."""
        productos_por_perdido = []
        try:
            #Conexión a la base de datos usando ruta de archivo de configuración
            db = sqlite3.connect(Config.get("DATABASE"), detect_types=sqlite3.PARSE_DECLTYPES)
            #Objeto cursor
            cursor = db.cursor()
            #Query de tipo SELECT
            query = """SELECT * FROM productos_por_pedido WHERE id_pedido = {}""".format(self.id)
            #Imprimir query a ejecutar
            print("\033[38;5;57m" + "\033[1m" + query + "\033[0m")
            cursor.execute(query)
            resultados = cursor.fetchall()
            print(resultados)
        except Exception as e:
            print("Error: {}".format(e))
        finally:
            #Cerrar conexión de db
            db.close()
            from .producto_por_pedido import ProductoPorPedido
            for resultado in resultados:
                productos_por_perdido.append(ProductoPorPedido.obtener(id = resultado[0]))
            return productos_por_perdido
