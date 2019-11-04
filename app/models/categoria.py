#Importar libreria para sqlite3
import sqlite3
#Importar configuración
from config import Config

class Categoria(object):

    def __init__(self, id: int = None, nombre: str = None):
        self.__id = id
        self.__nombre = nombre
        #Array con objetos Producto
        self.__productos = []

    def __str__(self):
        return "id = {}, nombre = {}".format(self.id, self.nombre)

    @property
    def id(self):
        return self.__id

    @property
    def nombre(self):
        return self.__nombre

    @property
    def productos(self):
        return self.__productos

    @nombre.setter
    def nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre

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
            query = """INSERT INTO categorias (nombre) VALUES('{}')""".format(self.nombre)
            cursor.execute(query)
            db.commit()
            estado = True
        except Exception as e:
            db.rollback()  # RESTAURAR ANTES DE CAMBIOS POR ERROR
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
            query = """UPDATE categorias SET nombre = '{}' WHERE id = {}""".format(self.nombre, self.id)
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
        """Recibe un id como integer que es el Primary Key y una ruta de base datos. Devuelve un objeto Categoria."""
        categoria = None
        try:
            #Conexión a la base de datos usando database_filepath como ruta
            database = sqlite3.connect(database_filepath)
            #Objeto cursor
            cursor = database.cursor()
            query = """SELECT * FROM categorias WHERE id = {}""".format(id)
            cursor.execute(query)
            categoria = cursor.fetchone()
        except Exception as e:
            print("Error: {}".format(e))
        finally:
            #Cerrar conexión de db
            database.close()
        if categoria == None:
            print("No se pudo encontrar una Categoria con el id:", id)
        else:
            return Categoria(id = categoria[0], nombre = categoria[1])
