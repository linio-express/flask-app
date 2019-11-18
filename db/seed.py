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

comercios = """INSERT INTO comercios(nombre, direccion, ruc, logo_url)
    VALUES ("iShop Perú", " Av. Ricardo Rivera Navarrete Nro. 475 Int. 1004, San Isidro.", "20600739477", "https://linio-express.s3-sa-east-1.amazonaws.com/comercios/ishop.jpg"),
    ("Samsung Perú", "Av. Rivera Navarrete Nro. 501 (Piso 6), San Isidro.", "20300263578", "https://linio-express.s3-sa-east-1.amazonaws.com/comercios/samsung.png"),
    ("LEGO Perú", "Av. Paseo de la Republica Nro. 3220, San Isidro", "20100128056", "https://linio-express.s3-sa-east-1.amazonaws.com/comercios/lego.png")"""
queries.append(comercios)

categorias = """INSERT INTO categorias(nombre, icono_url)
    VALUES ('Arte y artesanías', 'https://linio-express.s3-sa-east-1.amazonaws.com/iconos/arte.svg'), ('Computadoras', 'https://linio-express.s3-sa-east-1.amazonaws.com/iconos/computadoras.svg'), ('Moda', 'https://linio-express.s3-sa-east-1.amazonaws.com/iconos/moda.svg'), ('Belleza y cuidado personal', 'https://linio-express.s3-sa-east-1.amazonaws.com/iconos/belleza.svg'), ('Salud y bienestar', 'https://linio-express.s3-sa-east-1.amazonaws.com/iconos/salud.svg'), ('Deportes', 'https://linio-express.s3-sa-east-1.amazonaws.com/iconos/deportes.svg'), ('Juguetes', 'https://linio-express.s3-sa-east-1.amazonaws.com/iconos/juguetes.svg'), ('Electrodomésticos', 'https://linio-express.s3-sa-east-1.amazonaws.com/iconos/electrodomesticos.svg')"""
queries.append(categorias)

productos = """INSERT INTO productos(nombre, descripcion, fotos_url, precio, stock, id_categoria, id_comercio)
    VALUES ('Apple iPhone 11 Pro 64GB', 'Un revolucio­nario sistema de triple cámara que multiplica las posibilidades de
    la forma más sencilla. Un salto sin precedentes en la autonomía. Un portento de chip que dobla la apuesta por
    el aprendizaje automático y redefine lo que es posible para un móvil. Ha habido otros iPhone, pero solo este
    se ha ganado el derecho a llamarse Pro.', 'https://linio-express.s3-sa-east-1.amazonaws.com/productos/iphone11pro/iphone-11-pro-midnight-green-select-2019.png', 3500, 5, 2, 1),
    ('Apple Airpods Pro', 'Descripcion', 'https://linio-express.s3-sa-east-1.amazonaws.com/productos/airpods_pro/MWP22.jpeg, https://linio-express.s3-sa-east-1.amazonaws.com/productos/airpods_pro/MWP22_AV1.jpeg,
    https://linio-express.s3-sa-east-1.amazonaws.com/productos/airpods_pro/MWP22_AV2.jpeg, https://linio-express.s3-sa-east-1.amazonaws.com/productos/airpods_pro/MWP22_AV3.jpeg, https://linio-express.s3-sa-east-1.amazonaws.com/productos/airpods_pro/MWP22_AV4.jpeg',
    890, 10, 2, 1),
    ('Apple Airpods con cargador inalámbrico', 'descripcion', 'https://linio-express.s3-sa-east-1.amazonaws.com/productos/airpods_con_cargador_inalambrico/MRXJ2.jpeg, https://linio-express.s3-sa-east-1.amazonaws.com/productos/airpods_con_cargador_inalambrico/MRXJ2_AV1.jpeg,
    https://linio-express.s3-sa-east-1.amazonaws.com/productos/airpods_con_cargador_inalambrico/MRXJ2_AV2.jpeg, https://linio-express.s3-sa-east-1.amazonaws.com/productos/airpods_con_cargador_inalambrico/MRXJ2_AV3.jpeg', 690, 5, 2, 1),
    ('Apple Airpods con cargador', 'descripcion', 'https://linio-express.s3-sa-east-1.amazonaws.com/productos/airpods_con_cargador/MV7N2.jpeg, https://linio-express.s3-sa-east-1.amazonaws.com/productos/airpods_con_cargador/MV7N2_AV1.jpeg,
    https://linio-express.s3-sa-east-1.amazonaws.com/productos/airpods_con_cargador/MV7N2_AV2.jpeg, https://linio-express.s3-sa-east-1.amazonaws.com/productos/airpods_con_cargador/MV7N2_AV3.jpeg', 590, 10, 2, 1),
    ('Apple Airpods cargador inalámbrico', 'descripcion', 'https://linio-express.s3-sa-east-1.amazonaws.com/productos/cargador_inalambrico_airpods/MR8U2.jpeg, https://linio-express.s3-sa-east-1.amazonaws.com/productos/cargador_inalambrico_airpods/MR8U2_AV1.jpeg,
    https://linio-express.s3-sa-east-1.amazonaws.com/productos/cargador_inalambrico_airpods/MR8U2_AV2.jpeg, https://linio-express.s3-sa-east-1.amazonaws.com/productos/cargador_inalambrico_airpods/MR8U2_AV3.jpeg', 390, 11, 2, 1),
    ('Apple iPhone 11 64GB Verde', 'descripcion', 'https://linio-express.s3-sa-east-1.amazonaws.com/productos/iphone11/iphone11-green-select-2019.png', 1700, 5, 2, 1),
    ('Apple iPhone 11 64GB Amarillo', 'descripcion', 'https://linio-express.s3-sa-east-1.amazonaws.com/productos/iphone11/iphone11-yellow-select-2019.png', 1700, 10, 2, 1),
    ('Apple iPhone 11 64GB Negro', 'descripcion', 'https://linio-express.s3-sa-east-1.amazonaws.com/productos/iphone11/iphone11-black-select-2019.png', 1700, 10, 3, 1),
    ('Apple iPhone 11 64FB Rojo', 'descripcion', 'https://linio-express.s3-sa-east-1.amazonaws.com/productos/iphone11/iphone11-red-select-2019.png', 1700, 15, 2, 1),
    ('LEGO Technic Porsche 911 GT3 RS', 'Experimenta el emblemático Porsche 911 GT3 RS con esta auténtica réplica LEGO®
    Technic. Dentro de la caja encontrarás un libro especial para coleccionistas acerca de la historia de LEGO Technic y
    los modelos GT de Porsche, así como 4 llantas de diseño especial con el emblema de la gama RS. Los elementos se entregan
    en diferentes cajas y la construcción se lleva a cabo en el mismo orden en el que se ensamblan los vehículos en la vida
    real.', 'https://linio-express.s3-sa-east-1.amazonaws.com/productos/Juguetes/LegoTechnic911GT3RS/91eOW8yziNL._AC_SL1500_.jpg,
    https://linio-express.s3-sa-east-1.amazonaws.com/productos/Juguetes/LegoTechnic911GT3RS/611lLgb6TLL._AC_SL1000_.jpg, https://linio-express.s3-sa-east-1.amazonaws.com/productos/Juguetes/LegoTechnic911GT3RS/9151mHylI3L._AC_SL1500_.jpg,
    https://linio-express.s3-sa-east-1.amazonaws.com/productos/Juguetes/LegoTechnic911GT3RS/91pDCHxZK7L._AC_SL1500_.jpg', 700, 3, 7, 3)"""
queries.append(productos)

insertar_datos(db, queries)
