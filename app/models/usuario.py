#Importar librería datetime par fechas
from datetime import datetime
#Importar libreria para sqlite3
import sqlite3
#Importar configuración
from config import Config
#Importar librería de regex
import re
#Importar módulo con funciones de ayuda
from app.helpers.helper import *

class Usuario(object):

    def __init__(self, dni: str = None, fecha_nacimiento: datetime = None, nombre_completo: str = None, celular: str = None, numero_de_tarjeta: str = None, id: int = None, nombre_de_usuario: str = None, password: str = None, fecha_de_creacion: datetime = None, fecha_de_actualizacion: datetime = None, correo: str = None, canasta = None, pedidos: list = None):
        self.__id = id
        self.__dni = dni
        self.__fecha_nacimiento = fecha_nacimiento
        self.__nombre_completo = nombre_completo
        self.__celular = celular
        self.__numero_de_tarjeta = numero_de_tarjeta
        self.__nombre_de_usuario = nombre_de_usuario
        self.__password = password
        self.__fecha_de_creacion = fecha_de_creacion
        self.__fecha_de_actualizacion = fecha_de_actualizacion
        self.__correo = correo
        self.__canasta = canasta
        self.__pedidos = pedidos

    def __str__(self):
        return "id: " + self.id

    def toJSON(self):
        return {"id": self.id, "dni": self.dni, "nombre_completo": self.nombre_completo}

    @property
    def id(self):
        return self.__id

    @property
    def dni(self):
        return self.__dni

    @property
    def fecha_nacimiento(self):
        return self.__fecha_nacimiento

    @property
    def nombre_completo(self):
        return self.__nombre_completo

    @property
    def celular(self):
        return self.__celular

    @property
    def numero_de_tarjeta(self):
        return self.__numero_de_tarjeta

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
    def fecha_de_actualizacion(self):
        return self.__fecha_de_actualizacion

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

    @fecha_de_actualizacion.setter
    def fecha_de_actualizacion(self, nueva_fecha_de_actualizacion):
        self.__fecha_de_actualizacion = nueva_fecha_de_actualizacion

    @correo.setter
    def correo(self, nuevo_correo):
        self.__correo = nuevo_correo

    @canasta.setter
    def canasta(self, nueva_canasta):
        self.__canasta = nueva_canasta

    @pedidos.setter
    def pedidos(self, nuevos_pedidos):
        self.__pedidos = nuevos_pedidos

    @dni.setter
    def dni(self, nuevo_dni):
        self.__dni = nuevo_dni

    @fecha_nacimiento.setter
    def fecha_nacimiento(self, nueva_fecha_nacimiento):
        self.__fecha_nacimiento = nueva_fecha_nacimiento

    @nombre_completo.setter
    def nombre_completo(self, nuevo_nombre_completo):
        self.__nombre_completo = nuevo_nombre_completo

    @celular.setter
    def celular(self, nuevo_celular):
        self.__celular = nuevo_celular

    @numero_de_tarjeta.setter
    def numero_de_tarjeta(self, nuevo_numero_de_tarjeta):
        self.__numero_de_tarjeta = nuevo_numero_de_tarjeta

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
            query = """INSERT INTO usuarios (dni, fecha_nacimiento, nombre_completo, celular, numero_de_tarjeta, nombre_de_usuario, password, correo) VALUES('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')""".format(self.dni, str(self.fecha_nacimiento), self.nombre_completo, self.celular, self.numero_de_tarjeta, self.nombre_de_usuario, self.password, self.correo)
            #Imprimir query a ejecutar
            print('\u001b[32m' + '\033[1m' + query + '\033[0m')
            #Ejecutar query
            cursor.execute(query)
            #Confirmar cambios a base de datos
            db.commit()
            #Cambiar estado a True
            estado = True
            #Query para hallar el id de la instancia recién creada
            query = """SELECT MAX(id) FROM usuarios;"""
            #Ejecutar query
            cursor.execute(query)
            #Extraer resultado del query ejecutado
            id_nuevo_usuario = cursor.fetchone()
            #Asignar id a objeto
            self.id = int(id_nuevo_usuario[0])
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
    def obtener(id: int = None, correo: str = None):
        """Recibe un id como integer que es el Primary Key y el correo del usuario. Devuelve un objeto Usuario."""
        usuario = None
        try:
            #Conexión a la base de datos usando ruta de archivo de configuración
            db = sqlite3.connect(Config.get("DATABASE"), detect_types=sqlite3.PARSE_DECLTYPES)
            #Objeto cursor
            cursor = db.cursor()
            query = """SELECT * FROM usuarios"""
            if id != None:
                query += """ WHERE id = {}""".format(id)
            else:
                query += """ WHERE correo = '{}'""".format(correo)
            #Imprimir query a ejecutar
            print("\033[38;5;57m" + "\033[1m" + query + "\033[0m")
            #Ejecutar query
            cursor.execute(query)
            usuario = cursor.fetchone()
        except Exception as e:
            print("Error: {}".format(e))
        finally:
            #Cerrar conexión de db
            db.close()
        if usuario == None:
            print("No se pudo encontrar un Usuario con el id:", id)
        else:
            return Usuario(id = usuario[0], dni = usuario[1], nombre_completo = usuario[3],
                celular = usuario[4], numero_de_tarjeta = usuario[5], nombre_de_usuario = usuario[6], password = usuario[7],
                fecha_de_creacion = usuario[8], fecha_de_actualizacion = usuario[9], correo = usuario[11])

    def buscar_pedidos(self):
        """Busca todos los pedidos del usuario en la db.
            Devuelve una lista donde cada elemento es un objeto de tipo pedido"""
        pedidos = []
        resultados = []
        try:
            #Conexión a la base de datos usando ruta de archivo de configuración
            db = sqlite3.connect(Config.get("DATABASE"), detect_types=sqlite3.PARSE_DECLTYPES)
            #Objeto cursor
            cursor = db.cursor()
            #Query de tipo SELECT
            query = """SELECT * FROM pedidos WHERE id_usuario = {}""".format(self.id)
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
            #Se importa la clase Pedido para crear los objetos
            from .pedido import Pedido
            for resultado in resultados:
                pedidos.append(Pedido.obtener(id = resultado[0]))
            return pedidos

    def es_mayor_de_edad(self):
        """Devulve True si la diferencia de la fecha actual respecto a la fecha de nacimiento es mayor o igual a 18."""
        fecha_actual = datetime.now()
        edad = (fecha_actual - self.fecha_nacimiento).days / 365.0
        if edad >= 18:
            return True
        else:
            return False

    def nombre_completo_es_valido(self):
        """Devuelve true si el atributo nombre_completo no tiene caracteres especiales. Caso contrario devuelve False"""
        #Se comeinza asumiendo que el nombre es valido
        nombre_completo_es_valido = True
        #Se establece una lisrta con caracteres especiales
        caracteres_especiales = ['$', '@', '%', '/', '-', '_', '.', '*', '+', '']
        #Se busca cada caracter en la cadena de texto nombre_completo
        for caracter in caracteres_especiales:
            if caracter in self.nombre_completo:
                nombre_completo_es_valido = False
                #Basta con encontrar un caracter especial para que el nombre  deje de ser valido
                break
        return nombre_completo_es_valido

    def nombre_de_usuario_valido(self):
        """Devuelve True si nombre_de_usuario cumple con el formato.
            Caso contrario, devuelve False"""

        #Se usa Regex para establecer el formato de nombre de usuario.
        formato = re.compile("^(?!.*\.\.)(?!.*\.$)[^\W][\w.]{0,29}$")

        #Se pasa a revisar que nombre_de_usuario cumple con el anterior formato
        if formato.fullmatch(self.nombre_de_usuario) == None:
            return False
        else:
            return True

    def antes_de_guardar(self):
        """Normaliza algunos valores de atributos. No retornada nada."""
        #El correo electrónico debe estar en minusculas
        self.correo = self.correo.lower()
        #El nombre de usuario tambien debe estar en minúsculas
        self.nombre_de_usuario = self.nombre_de_usuario.lower()

    def nombre_de_usuario_es_unico(self):
        """Devuelve True si el nombre de usuario es único en la db.
            Caso contrario devuelve False"""

        #El nombre de usuario debe estar en minusculas
        self.nombre_de_usuario = self.nombre_de_usuario.lower()

        try:
            #Conexión a la base de datos usando ruta de archivo de configuración
            db = sqlite3.connect(Config.get("DATABASE"), detect_types=sqlite3.PARSE_DECLTYPES)
            #Objeto cursor
            cursor = db.cursor()
            query = """SELECT COUNT(*) FROM usuarios WHERE nombre_de_usuario = '{}';
                        """.format(self.nombre_de_usuario)
            #Imprimir query a ejecutar
            print("\033[38;5;57m" + "\033[1m" + query + "\033[0m")
            cursor.execute(query)
            #Si el resultado del query es 0, el nombre de usuario es unico
            if cursor.fetchone() == (0,):
                es_unico = True
            else:
                es_unico = False
        except Exception as e:
            print("Error: {}".format(e))
        finally:
            #Cerrar conexión de db
            db.close()
            return es_unico

    def inicio_de_sesion_valido(self):
        """Usa nombre_de_usuario, correo y password.
            Busca el  nombre de ususario, el correo y la contraseña en la db.
            Devuelve True si coincide; caso contrario, False"""
        estado = False
        try:
            #Conexión a la base de datos usando ruta de archivo de configuración
            db = sqlite3.connect(Config.get("DATABASE"), detect_types=sqlite3.PARSE_DECLTYPES)
            #Objeto cursor
            cursor = db.cursor()
            if self.correo == None and self.nombre_de_usuario != None:
                query = """SELECT COUNT(*) FROM usuarios WHERE nombre_de_usuario = '{}' AND password = '{}'
                        """.format(self.nombre_de_usuario.lower(), self.password)
            else:
                query = """SELECT COUNT(*) FROM usuarios WHERE correo = '{}' AND password = '{}';
                        """.format(self.correo.lower(), self.password)
            #Imprimir query a ejecutar
            print("\033[38;5;57m" + "\033[1m" + query + "\033[0m")
            cursor.execute(query)
            if cursor.fetchone() == (1,):
                estado = True
        except Exception as e:
            print("Error: {}".format(e))
        finally:
            #Cerrar conexión de db
            db.close()
            return True

    def actualizar(self):
        """Recibe una ruta de base datos. Guarda el objeto en la db.
            Devuelve True si se logra guardar en la db, caso contrario devuelve False."""
        estado = False
        try:
            #Conexión a la base de datos usando ruta de archivo de configuración
            db = sqlite3.connect(Config.get("DATABASE"), detect_types=sqlite3.PARSE_DECLTYPES)
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
    def todos():
        """Devuelve una lista con todos los usuarios en la db"""
        try:
            #Conexión a la base de datos usando ruta de archivo de configuración
            db = sqlite3.connect(Config.get("DATABASE"), detect_types=sqlite3.PARSE_DECLTYPES)
            #Objeto cursor
            cursor = db.cursor()
            query = """SELECT * FROM usuarios;""".format(id)
            #Imprimir query a ejecutar
            print("\033[38;5;57m" + "\033[1m" + query + "\033[0m")
            cursor.execute(query)
            resultado = cursor.fetchall()
        except Exception as e:
            print("Error: {}".format(e))
        finally:
            #Cerrar conexión de db
            db.close()
            print(resultado)
