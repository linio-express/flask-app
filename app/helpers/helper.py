#Importar librería datetime par fechas
from datetime import datetime

def toJSON(lista):
    """Esta función convierte todos los elementos de una lista en JSON. Asume que los elementos de la lista son objetos con un método toJSON() ya definido."""
    listaJSON = []
    for objeto in lista:
        listaJSON.append(objeto.toJSON())
    return listaJSON

def formato_largo(fecha: datetime):
    """Recibe una fecha que es un objeto de tipo datetime.
        Devuelve una cadena de texto con el siguiente formato: {día de la semana} {día del mes}" de {mes}, {año}"""
    anio=fecha.year
    mes=fecha.month
    dia=fecha.day
    ds = fecha.weekday()
    dia_sem={0:'lunes',1:'martes', 2:'miércoles', 3:'jueves',4:'viernes',5:'sábado',6:'domingo'}
    meses = {1:'enero', 2:'febrero', 3:'marzo',4:'abril',5:'mayo',6:'junio',7:'julio', 8:'agosto', 9:'setiembre',10:'octubre',11:'noviembre',12:'diciembre'}
    return dia_sem[ds] + ' ' + str(dia) + ' de ' + meses[mes] + ', ' + str(anio)

def formato_corto(fecha: datetime):
    """Recibe una fecha que es un objeto de tipo datetime.
        Devuelve una cadena de texto con el siguiente formato: {día de la semana} {día del mes}" de {mes}, {año}"""
    anio=fecha.year
    mes=fecha.month
    dia=fecha.day
    if len(str(mes))==1:
        mes='0'+str(fecha.month)
    if len(str(dia))==1:
        dia='0'+str(fecha.day)
    return str(dia) + '/' + str(mes) + '/' + str(anio)

def formato_de_precio(precio: float):
    precion=precio//1000
    preciov = int(precio) % 1000
    decimal=str(round(precio%1,2))
    decimalu=decimal[1:]
    if decimal=='1.0':
        decimalu = '.99'
    if preciov==0:
        preciov='000'
    if precion==0:
        if len(decimalu) == 0:
            print(str(preciov) + '.00')
            return str(preciov) + '.00'
        elif len(decimalu) == 2:
            print(str(preciov) + decimalu + '0')
            return str(preciov) + decimalu + '0'
        else:
            print(str(preciov) + decimalu)
            return str(preciov) + decimalu

    else:
        if len(decimalu)==0:
            if len(str(preciov)) != 3:
                preciov = str(0) * (3 - len(str(preciov))) + str(preciov)
                print(str(int(precion))+' '+preciov + '.00')
                return str(int(precion)) + ' ' + preciov + '.00'
            else:
                print(str(int(precion)) + ' ' + str(preciov) + '.00')
                return str(int(precion)) + ' ' + str(preciov) + '.00'
        elif len(decimalu)==2:
            if len(str(preciov))!=3:
                preciov = str(0)*(3-len(str(preciov)))+str(preciov)
                print(str(int(precion)) + ' ' + preciov + decimalu + '0')
                return str(int(precion)) + ' ' + preciov + decimalu + '0'
            else:
                print(str(int(precion)) + ' ' + str(preciov) + decimalu +'0')
                return str(int(precion)) + ' ' + str(preciov) + decimalu +'0'
        else:
            if len(str(preciov))!=3:
                preciov = str(0)*(3-len(str(preciov)))+str(preciov)
                print(str(int(precion)) + ' ' + preciov + decimalu)
                return str(int(precion)) + ' ' + preciov + decimalu
            else:
                print(str(int(precion)) + ' ' + str(preciov) + decimalu)
                return str(int(precion)) + ' ' + str(preciov) + decimalu
