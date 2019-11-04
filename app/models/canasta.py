#Importar libreria para sqlite3
import sqlite3
#Importar configuración
from config import Config

class Canasta(object):

    def __init__(self, id: int = None, usuario = None, productos: list = None):
        self.__id = id
        self.__usuario = usuario
        self.__productos = productos

    def __str__(self):
        return "id = {}, id_usuario = {}".format(self.id, self.usuario.id)

    @property
    def id(self):
        return self.__id

    @property
    def usuario(self):
        return self.__usuario

    @property
    def productos(self):
        return self.__productos

    @id.setter
    def id(self, nuevo_id):
        self.__id = nuevo_id

    @usuario.setter
    def usuario(self, nuevo_usuario):
        self.__usuario = nuevo_usuario

    @productos.setter
    def productos(self, nuevos_productos):
        self.__productos = nuevos_productos

    def crear(self):
        """Recibe una ruta de base datos. Guarda el objeto en la db.
            Devuelve True si se logra guardar en la db, caso contrario devuelve False."""
        estado = False
        try:
            #Conexión a la base de datos usando ruta de archivo de configuración
            db = sqlite3.connect(Config.get("DATABASE"))
            #Objeto cursor
            cursor = db.cursor()
            query = """INSERT INTO canastas (id_usuario) VALUES('{}')""".format(self.usuario.id)
            cursor.execute(query)
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

    def actualizar(self, database_filepath: str):
        """Recibe una ruta de base datos. Actualiza el objeto en la db.
            Devuelve True si se logra actualizar en la db, caso contrario devuelve False."""
        estado = False
        try:
            #Conexión a la base de datos usando database_filepath como ruta
            database = sqlite3.connect(database_filepath)
            #Objeto cursor
            cursor = database.cursor()
            query = """UPDATE canastas SET id_usuario = {} WHERE id = {}""".format(self.usuario.id, self.id)
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
        canasta = None
        try:
            #Conexión a la base de datos usando database_filepath como ruta
            database = sqlite3.connect(database_filepath)
            #Objeto cursor
            cursor = database.cursor()
            query = """SELECT * FROM canastas WHERE id = '{}'""".format(id)
            cursor.execute(query)
            canasta = cursor.fetchone()
        except Exception as e:
            print("Error: {}".format(e))
        finally:
            #Cerrar conexión de db
            database.close()
        if canasta == None:
            print("No se pudo encontrar un Producto con el id:", id)
        else:
            from .usuario import Usuario
            return Producto(id = canasta[0], usuario = Usuario.obtener(canasta[1]))
