#Importar libreria para sqlite3
import sqlite3

class Comercio(object):

    def __init__(self, id: int = None, nombre: str = None, direccion: str = None, ruc: str = None, productos: list = None):
        self.__id = id
        self.__nombre = nombre
        self.__direccion = direccion
        self.__ruc = ruc
        self.__productos = productos

    def __str__(self):
        return '''id: {}, nombre: "{}", direccion: "{}", ruc: "{}"'''.format(self.__id, self.__nombre, self.__direccion, self.__ruc)

    @property
    def id(self):
        return self.__id

    @property
    def nombre(self):
        return self.__nombre

    @property
    def direccion(self):
        return self.__direccion

    @property
    def ruc(self):
        return self.__ruc

    @property
    def productos(self):
        return self.__productos

    @nombre.setter
    def nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre

    @direccion.setter
    def direccion(self, nueva_direccion):
        self.__direccion = nueva_direccion

    @ruc.setter
    def ruc(self, nuevo_ruc):
        self.__ruc = nuevo_ruc

    @productos.setter
    def productos(self, nuevos_productos):
        self.__productos = nuevos_productos

    def crear(self, database_filepath: str):
        """Recibe una ruta de base datos. Guarda el objeto en la db.
            Devuelve True si se logra guardar en la db, caso contrario devuelve False."""
        estado = False
        try:
            #Conexión a la base de datos usando database_filepath como ruta
            database = sqlite3.connect(database_filepath)
            #Objeto cursor
            cursor = database.cursor()
            query = """INSERT INTO comercios (nombre, direccion, ruc)
                VALUES('{}', '{}', '{}')""".format(self.nombre, self.direccion, self.ruc)
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
            query = """UPDATE comercios SET nombre = '{}', direccion = '{}', ruc = '{}'
                WHERE id = {}""".format(self.nombre, self.direccion, self.ruc, self.id)
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
        comercio = None
        try:
            #Conexión a la base de datos usando database_filepath como ruta
            database = sqlite3.connect(database_filepath)
            #Objeto cursor
            cursor = database.cursor()
            query = """SELECT * FROM comercios WHERE id = {}""".format(id)
            cursor.execute(query)
            comercio = cursor.fetchone()
        except Exception as e:
            print("Error: {}".format(e))
        finally:
            #Cerrar conexión de db
            database.close()
        if comercio == None:
            print("No se pudo encontrar un Comercio con el id:", id)
        else:
            return Comercio(id = comercio[0], nombre = comercio[1], direccion = comercio[2], ruc = comercio[3])
