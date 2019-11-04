from datetime import datetime
#Importar libreria para sqlite3
import sqlite3

class Persona(object):

    def __init__(self, dni: str = None, fecha_nacimiento = None, nombre_completo: str = None, celular: str = None, numero_de_tarjeta: str = None):
        self.__dni = dni
        self.__fecha_nacimiento = fecha_nacimiento
        self.__nombre_completo = nombre_completo
        self.__celular = celular
        self.__numero_de_tarjeta = numero_de_tarjeta

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

    def es_mayor_de_edad(self):
        fecha_actual = datetime.now()
        fecha_nacimiento = self.fecha_nacimiento
        edad = (fecha_actual - fecha_nacimiento).days / 365.0
        if edad > 18:
            return True
        else:
            return False
