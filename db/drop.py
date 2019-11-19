#Importar libreria para sqlite3
import sqlite3

def drop(db):
    """Recibe una conexión a una db en sqlite3. Borra las tablas."""

    #Cursor
    cursor = db.cursor()

    cursor.execute("DROP TABLE IF EXISTS comercios")
    cursor.execute("DROP TABLE IF EXISTS categorias")
    cursor.execute("DROP TABLE IF EXISTS productos")
    cursor.execute("DROP TABLE IF EXISTS canastas")
    cursor.execute("DROP TABLE IF EXISTS usuarios")
    cursor.execute("DROP TABLE IF EXISTS pedidos")
    cursor.execute("DROP TABLE IF EXISTS productos_por_pedido")
    cursor.execute("DROP TABLE IF EXISTS productos_por_canasta")

    #Confirmar cambios
    db.commit()

    #Cerrar conexión
    cursor.close()

#Abrir db
db = sqlite3.connect("linio.db")

drop(db)
