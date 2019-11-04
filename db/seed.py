#Importar libreria para sqlite3
import sqlite3

def insertar_datos(db: str, queries: list):
    """Recibe una conexión a una db en sqlite3 y un array con queries. Inserta datos a la tabla colaboradores"""
    #Cursor
    cursor = db.cursor()

    #Insertar datos a la tabla comercios
    for query in queries:
        cursor.execute(query)

    # Confirmar cambios
    db.commit()
    # Cerrar conexión
    cursor.close()

#Abrir db
db = sqlite3.connect("linio.db")

queries = []

comercios = """INSERT INTO comercios(nombre, direccion, ruc)
    VALUES ("iShop Perú", " Av. Ricardo Rivera Navarrete Nro. 475 Int. 1004, San Isidro.", "20600739477"),
    ("Samsung Perú", "Av. Rivera Navarrete Nro. 501 (Piso 6), San Isidro.", "20300263578"),
    ("LEGO Perú", "Av. Paseo de la Republica Nro. 3220, San Isidro", "20100128056")"""
queries.append(comercios)

categorias = """INSERT INTO categorias(nombre)
    VALUES ('Arte y artesanías'), ('Computadoras'), ('Moda'), ('Belleza y cuidado personal'),
    ('Salud y bienestar'), ('Deportes'), ('Juguetes'), ('Electrodomésticos')"""
queries.append(categorias)

productos = """INSERT INTO productos(nombre, descripcion, precio, stock, id_categoria, id_comercio)
    VALUES ('Apple iPhone 11 Pro 64GB', 'Un revolucio­nario sistema de triple cámara que multiplica las posibilidades de
    la forma más sencilla. Un salto sin precedentes en la autonomía. Un portento de chip que dobla la apuesta por
    el aprendizaje automático y redefine lo que es posible para un móvil. Ha habido otros iPhone, pero solo este
    se ha ganado el derecho a llamarse Pro.', 3500, 5, 2, 1),
    ('LEGO Technic Porsche 911 GT3 RS', 'Experimenta el emblemático Porsche 911 GT3 RS con esta auténtica réplica LEGO®
    Technic. Dentro de la caja encontrarás un libro especial para coleccionistas acerca de la historia de LEGO Technic y
    los modelos GT de Porsche, así como 4 llantas de diseño especial con el emblema de la gama RS. Los elementos se entregan
    en diferentes cajas y la construcción se lleva a cabo en el mismo orden en el que se ensamblan los vehículos en la vida
    real.', 700, 3, 7, 3)"""
queries.append(productos)

insertar_datos(db, queries)
