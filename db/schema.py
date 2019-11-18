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

def crear_tabla_comercios(db):
    """Recibe una conexión a una db en sqlite3. Crea la tabla comercios."""

    #Cursor
    cursor = db.cursor()

    #Creacion de tabla comercios
    cursor.execute("""CREATE TABLE IF NOT EXISTS comercios(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre VARCHAR(50) NOT NULL,
        direccion VARCHAR(200) NOT NULL,
        ruc VARCHAR(11) NOT NULL,
        logo_url VARCHAR(200) NOT NULL,
        fecha_de_creacion timestamp DEFAULT (datetime(current_timestamp)),
        fecha_de_actualizacion timestamp DEFAULT (datetime(current_timestamp)));""")

    # Confirmar cambios
    db.commit()

    # Cerrar conexión
    cursor.close()

def crear_tabla_categorias(db):
    """Recibe una conexión a una db en sqlite3. Crea la tabla categorias."""

    #Cursor
    cursor = db.cursor()

    #Creacion de tabla categorias
    cursor.execute("""CREATE TABLE IF NOT EXISTS categorias(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre VARCHAR(30) NOT NULL,
        icono_url VARCHAR(200) NOT NULL,
        fecha_de_creacion timestamp DEFAULT (datetime(current_timestamp)),
        fecha_de_actualizacion timestamp DEFAULT (datetime(current_timestamp)));""")

    # Confirmar cambios
    db.commit()

    # Cerrar conexión
    cursor.close()

def crear_tabla_productos(db):
    """Recibe una conexión a una db en sqlite3. Crea la tabla productos."""

    #Cursor
    cursor = db.cursor()

    #Creacion de tabla productos
    cursor.execute("""CREATE TABLE IF NOT EXISTS productos(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre VARCHAR(30) NOT NULL,
        descripcion VARCHAR(200) NOT NULL,
        fotos_url TEXT,
        precio FLOAT NOT NULL,
        stock INTEGER NOT NULL,
        fecha_de_creacion timestamp DEFAULT (datetime(current_timestamp)),
        fecha_de_actualizacion timestamp DEFAULT (datetime(current_timestamp)),
        id_categoria INTEGER NOT NULL,
        id_comercio INTEGER NOT NULL,
        FOREIGN KEY(id_categoria) REFERENCES categorias(id),
        FOREIGN KEY(id_comercio) REFERENCES comercios(id))""")

    # Confirmar cambios
    db.commit()

    # Cerrar conexión
    cursor.close()

def crear_tabla_usuarios(db):
    """Recibe una conexión a una db en sqlite3. Crea la tabla usuarios."""

    #Cursor
    cursor = db.cursor()

    #Creacion de tabla usuarios
    cursor.execute("""CREATE TABLE IF NOT EXISTS usuarios(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        dni VARCHAR(8) UNIQUE,
        fecha_nacimiento timestamp,
        nombre_completo VARCHAR(100) NOT NULL,
        celular VARCHAR(15) NOT NULL,
        numero_de_tarjeta VARCHAR(16),
        nombre_de_usuario VARCHAR(32) UNIQUE,
        password VARCHAR(60) NULL,
        fecha_de_creacion timestamp DEFAULT (datetime(current_timestamp)),
        fecha_de_actualizacion timestamp DEFAULT (datetime(current_timestamp)),
        id_canasta INTEGER,
        correo VARCHAR(128) NOT NULL,
        FOREIGN KEY (id_canasta) REFERENCES canastas(id));""")

    # Confirmar cambios
    db.commit()

    # Cerrar conexión
    cursor.close()

def crear_tabla_canastas(db):
    """Recibe una conexión a una db en sqlite3. Crea la tabla canastas."""

    #Cursor
    cursor = db.cursor()

    #Creacion de tabla canastas
    cursor.execute("""CREATE TABLE IF NOT EXISTS canastas(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        fecha_de_creacion timestamp DEFAULT (datetime(current_timestamp)),
        fecha_de_actualizacion timestamp DEFAULT (datetime(current_timestamp)),
        id_usuario INTEGER NOT NULL,
        FOREIGN KEY (id_usuario) REFERENCES usuarios(id));""")

    # Confirmar cambios
    db.commit()

    # Cerrar conexión
    cursor.close()

def crear_tabla_pedidos(db):
    """Recibe una conexión a una db en sqlite3. Crea la tabla pedidos."""

    #Cursor
    cursor = db.cursor()

    #Creacion de tabla pedidos
    cursor.execute("""CREATE TABLE IF NOT EXISTS pedidos(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        id_usuario INTEGER NOT NULL,
        fecha_de_creacion timestamp DEFAULT (datetime(current_timestamp)),
        fecha_de_actualizacion timestamp DEFAULT (datetime(current_timestamp)),
        estado VARCHAR(30) NOT NULL,
        repartidor VARCHAR(100),
        metodo_de_pago VARCHAR(100),
        direccion_de_envio VARCHAR(200),
        tarifa_de_envio NUMERIC(10,2),
        fecha_de_pago timestamp,
        fecha_de_envio timestamp,
        fecha_de_entrega timestamp,
        FOREIGN KEY(id_usuario) REFERENCES usuarios(id));""")

    # Confirmar cambios
    db.commit()

    # Cerrar conexión
    cursor.close()

def crear_tabla_productos_por_pedido(db):
    """Recibe una conexión a una db en sqlite3. Crea la tabla productos_por_pedido."""

    #Cursor
    cursor = db.cursor()

    #Creacion de tabla productos_por_pedido
    cursor.execute("""CREATE TABLE IF NOT EXISTS productos_por_pedido(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        id_producto INTEGER NOT NULL,
        id_pedido INTEGER NOT NULL,
        cantidad INTEGER NOT NULL,
        precio_unitario FLOAT NOT NULL,
        fecha_de_creacion timestamp DEFAULT (datetime(current_timestamp)),
        fecha_de_actualizacion timestamp DEFAULT (datetime(current_timestamp)),
        FOREIGN KEY(id_producto) REFERENCES productos(id),
        FOREIGN KEY(id_pedido) REFERENCES pedidos(id));""")

    # Confirmar cambios
    db.commit()

    # Cerrar conexión
    cursor.close()

def crear_tabla_productos_por_canasta(db):
    """Recibe una conexión a una db en sqlite3. Crea la tabla productos_por_canasta."""

    #Cursor
    cursor = db.cursor()

    #Creacion de tabla productos_por_canasta
    cursor.execute("""CREATE TABLE IF NOT EXISTS productos_por_canasta(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        id_producto INTEGER NOT NULL,
        id_canasta INTEGER NOT NULL,
        cantidad INTEGER NOT NULL,
        fecha_de_creacion timestamp DEFAULT (datetime(current_timestamp)),
        fecha_de_actualizacion timestamp DEFAULT (datetime(current_timestamp)),
        FOREIGN KEY(id_producto) REFERENCES productos(id),
        FOREIGN KEY(id_canasta) REFERENCES canastas(id));""")

    # Confirmar cambios
    db.commit()

    # Cerrar conexión
    cursor.close()

#Abrir db
db = sqlite3.connect("linio.db")

drop(db)
crear_tabla_comercios(db)
crear_tabla_categorias(db)
crear_tabla_usuarios(db)
crear_tabla_canastas(db)
crear_tabla_pedidos(db)
crear_tabla_productos(db)
crear_tabla_productos_por_pedido(db)
crear_tabla_productos_por_canasta(db)
