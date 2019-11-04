from .persona import Persona
from datetime import datetime
#Importar libreria para sqlite3
import sqlite3
#Importar configuración
from config import Config

class Usuario(Persona):

    def __init__(self, dni: str = None, fecha_nacimiento: datetime = None, nombre_completo: str = None, celular: str = None,
        numero_de_tarjeta: str = None, id: int = None, nombre_de_usuario: str = None, password: str = None,
        fecha_de_creacion: datetime = None, correo: str = None, pedidos: list = None):
        #Uso de clase padre
        Persona.__init__(self, dni, fecha_nacimiento, nombre_completo, celular, numero_de_tarjeta)
        self.__id = id
        self.__nombre_de_usuario = nombre_de_usuario
        self.__password = password
        self.__fecha_de_creacion = fecha_de_creacion
        self.__correo = correo
        from .canasta import Canasta
        self.__canasta = Canasta()
        self.__pedidos = pedidos

    @property
    def id(self):
        return self.__id

    @property
    def nombre_de_usuario(self):
        return self.__nombre_de_usuario

    @property
    def password(self):
        return self.__password

    @property
    def fecha_de_creacion(self):
        return self.__fecha_de_creacion

    @property
    def correo(self):
        return self.__correo

    @property
    def canasta(self):
        return self.__canasta

    @property
    def pedidos(self):
        return self.__pedidos

    @id.setter
    def id(self, nuevo_id):
        self.__id = nuevo_id

    @nombre_de_usuario.setter
    def nombre_de_usuario(self, nuevo_nombre_de_usuario):
        self.__nombre_de_usuario = nuevo_nombre_de_usuario

    @password.setter
    def password(self, nuevo_password):
        self.__password = nuevo_password

    @fecha_de_creacion.setter
    def fecha_de_creacion(self, nueva_fecha_de_creacion):
        self.__fecha_de_creacion = nueva_fecha_de_creacion

    @correo.setter
    def correo(self, nuevo_correo):
        self.__correo = nuevo_correo

    @canasta.setter
    def canasta(self, nueva_canasta):
        self.__canasta = nueva_canasta

    @pedidos.setter
    def pedidos(self, nuevos_pedidos):
        self.__pedidos = nuevos_pedidos

    def inicio_de_sesion_valido(self):
        """Recibe el nombre de usuario, el correo electrónico y la contraseña.
            Busca el  nombre de ususario, el correo y la contraseña en la db.
            Devuelve True si coincide; caso contrario, False"""
        estado = False
        try:
            #Conexión a la base de datos usando ruta de archivo de configuración
            db = sqlite3.connect(Config.get("DATABASE"))
            #Objeto cursor
            cursor = db.cursor()
            if self.correo == None and self.nombre_de_usuario != None:
                query = """SELECT COUNT(*) FROM usuarios WHERE nombre_de_usuario = '{}' AND password = '{}'
                        """.format(self.nombre_de_usuario, self.password)
            else:
                query = """SELECT COUNT(*) FROM usuarios WHERE correo = '{}' AND password = '{}';
                        """.format(self.correo, self.password)
            cursor.execute(query)
            if cursor.fetchone() == (1,):
                estado = True
        except Exception as e:
            print("Error: {}".format(e))
        finally:
            #Cerrar conexión de db
            db.close()
            return estado

    def crear(self):
        """Recibe una ruta de base datos. Guarda el objeto en la db.
            Devuelve True si se logra guardar en la db, caso contrario devuelve False."""
        estado = False
        try:
            #Conexión a la base de datos usando ruta de archivo de configuración
            db = sqlite3.connect(Config.get("DATABASE"))
            #Objeto cursor
            cursor = db.cursor()
            query = """INSERT INTO usuarios (dni, fecha_nacimiento, nombre_completo, celular,
                    numero_de_tarjeta, nombre_de_usuario, password, correo)
                    VALUES('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')""".format(self.dni,
                    str(self.fecha_nacimiento), self.nombre_completo, self.celular, self.numero_de_tarjeta,
                    self.nombre_de_usuario, self.password, self.correo)
            cursor.execute(query)
            db.commit()
            estado = True
            query = """SELECT MAX(id) FROM usuarios;"""
            cursor.execute(query)
            self.id = cursor.fetchone()
        except Exception as e:
            db.rollback()  # RESTAURAR ANTES DE CAMBIOS POR ERROR
            print("Error: {}".format(e))
        finally:
            #Cerrar conexión de db
            db.close()
            return estado

    def actualizar(self):
        """Recibe una ruta de base datos. Guarda el objeto en la db.
            Devuelve True si se logra guardar en la db, caso contrario devuelve False."""
        estado = False
        try:
            #Conexión a la base de datos usando ruta de archivo de configuración
            db = sqlite3.connect(Config.get("DATABASE"))
            #Objeto cursor
            cursor = db.cursor()
            query = """UPDATE usuarios SET dni = {}, fecha_nacimiento = {}, nombre_completo = {}, celular = {},
                numero_de_tarjeta = {}, nombre_de_usuario = {}, password = {}, id_canasta = {}, correo = {} WHERE id = {}""".format(self.dni,
                str(self.fecha_nacimiento), self.nombre_completo, self.celular, self.numero_de_tarjeta,
                self.nombre_de_usuario, self.password, self.canasta.id, self.correo, self.id)
            cursor.execute(query)
            db.commit()
            estado = True
        except Exception as e:
            db.rollback()  # RESTAURAR ANTES DE CAMBIOS POR ERROR
            print("Error: {}".format(e))
        finally:
            #Cerrar conexión de db
            db.close()
            return estado

    @staticmethod
    def obtener(id: int):
        """Recibe un id como integer que es el Primary Key y una ruta de base datos. Devuelve un objeto Usuario."""
        usuario = None
        try:
            #Conexión a la base de datos usando ruta de archivo de configuración
            db = sqlite3.connect(Config.get("DATABASE"))
            #Objeto cursor
            cursor = db.cursor()
            query = """SELECT * FROM usuarios WHERE id = '{}'""".format(id)
            cursor.execute(query)
        except Exception as e:
            print("Error: {}".format(e))
        finally:
            #Cerrar conexión de db
            db.close()
        if usuario == None:
            print("No se pudo encontrar un Producto con el id:", id)
        else:
            return Usuario(id = usuario[0], dni = usuario[1], fecha_nacimiento = usuario[2], nombre_completo = usuario[3],
                celular = usuario[4], numero_de_tarjeta = usuario[5], nombre_de_usuario = usuario[6], password = usuario[7],
                fecha_de_creacion = usuario[8], id_canasta = usuario[9], correo = usuario[10])

    @staticmethod
    def todos():
        """Devuelve una lista con todos los usuarios en la db"""
        try:
            #Conexión a la base de datos usando ruta de archivo de configuración
            db = sqlite3.connect(Config.get("DATABASE"))
            #Objeto cursor
            cursor = db.cursor()
            query = """SELECT * FROM usuarios;""".format(id)
            cursor.execute(query)
            resultado = cursor.fetchall()
        except Exception as e:
            print("Error: {}".format(e))
        finally:
            #Cerrar conexión de db
            db.close()
            print(resultado)
