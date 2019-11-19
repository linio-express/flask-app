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
    ("LEGO Perú", "Av. Paseo de la Republica Nro. 3220, San Isidro", "20100128056", "https://linio-express.s3-sa-east-1.amazonaws.com/comercios/lego.png"),
    ("TAG Heuer", "Av. Santa Cruz 301, Miraflores", "20897813911", "https://linio-express.s3-sa-east-1.amazonaws.com/comercios/TAG_Heuer_Logo.svg"), ("Galería Indigo", "Strip Mall El Bosque,  San Isidro", "20897867121", "https://linio-express.s3-sa-east-1.amazonaws.com/comercios/indigo.png")"""
queries.append(comercios)

categorias = """INSERT INTO categorias(nombre, icono_url)
    VALUES ('Arte y artesanías', 'https://linio-express.s3-sa-east-1.amazonaws.com/iconos/arte.svg'), ('Computadoras', 'https://linio-express.s3-sa-east-1.amazonaws.com/iconos/computadoras.svg'), ('Moda', 'https://linio-express.s3-sa-east-1.amazonaws.com/iconos/moda.svg'), ('Belleza y cuidado personal', 'https://linio-express.s3-sa-east-1.amazonaws.com/iconos/belleza.svg'), ('Salud y bienestar', 'https://linio-express.s3-sa-east-1.amazonaws.com/iconos/salud.svg'), ('Deportes', 'https://linio-express.s3-sa-east-1.amazonaws.com/iconos/deportes.svg'), ('Juguetes', 'https://linio-express.s3-sa-east-1.amazonaws.com/iconos/juguetes.svg'), ('Electrodomésticos', 'https://linio-express.s3-sa-east-1.amazonaws.com/iconos/electrodomesticos.svg')"""
queries.append(categorias)

productos = """INSERT INTO productos(nombre, descripcion, fotos_url, precio, stock, id_categoria, id_comercio)
    VALUES ('Apple iPhone 11 Pro 64gb', 'Un revolucio­nario sistema de triple cámara que multiplica las posibilidades de la forma más sencilla. Un salto sin precedentes en la autonomía. Un portento de chip que dobla la apuesta por el aprendizaje automático y redefine lo que es posible para un móvil. Ha habido otros iPhone, pero solo este se ha ganado el derecho a llamarse Pro.', 'https://linio-express.s3-sa-east-1.amazonaws.com/productos/iphone11pro/iphone-11-pro-midnight-green-select-2019.png', 3500, 5, 2, 1),
    ('Apple Airpods Pro', 'Descripcion', 'https://linio-express.s3-sa-east-1.amazonaws.com/productos/airpods_pro/MWP22.jpeg, https://linio-express.s3-sa-east-1.amazonaws.com/productos/airpods_pro/MWP22_AV1.jpeg,
    https://linio-express.s3-sa-east-1.amazonaws.com/productos/airpods_pro/MWP22_AV2.jpeg, https://linio-express.s3-sa-east-1.amazonaws.com/productos/airpods_pro/MWP22_AV3.jpeg, https://linio-express.s3-sa-east-1.amazonaws.com/productos/airpods_pro/MWP22_AV4.jpeg', 890, 10, 2, 1),
    ('Apple Airpods con cargador inalámbrico', 'descripcion', 'https://linio-express.s3-sa-east-1.amazonaws.com/productos/airpods_con_cargador_inalambrico/MRXJ2.jpeg, https://linio-express.s3-sa-east-1.amazonaws.com/productos/airpods_con_cargador_inalambrico/MRXJ2_AV1.jpeg,
    https://linio-express.s3-sa-east-1.amazonaws.com/productos/airpods_con_cargador_inalambrico/MRXJ2_AV2.jpeg, https://linio-express.s3-sa-east-1.amazonaws.com/productos/airpods_con_cargador_inalambrico/MRXJ2_AV3.jpeg', 690, 5, 2, 1),
    ('Apple Airpods con cargador', 'descripcion', 'https://linio-express.s3-sa-east-1.amazonaws.com/productos/airpods_con_cargador/MV7N2.jpeg, https://linio-express.s3-sa-east-1.amazonaws.com/productos/airpods_con_cargador/MV7N2_AV1.jpeg,
    https://linio-express.s3-sa-east-1.amazonaws.com/productos/airpods_con_cargador/MV7N2_AV2.jpeg, https://linio-express.s3-sa-east-1.amazonaws.com/productos/airpods_con_cargador/MV7N2_AV3.jpeg', 590, 10, 2, 1),
    ('Apple Airpods cargador inalámbrico', 'descripcion', 'https://linio-express.s3-sa-east-1.amazonaws.com/productos/cargador_inalambrico_airpods/MR8U2.jpeg, https://linio-express.s3-sa-east-1.amazonaws.com/productos/cargador_inalambrico_airpods/MR8U2_AV1.jpeg,
    https://linio-express.s3-sa-east-1.amazonaws.com/productos/cargador_inalambrico_airpods/MR8U2_AV2.jpeg, https://linio-express.s3-sa-east-1.amazonaws.com/productos/cargador_inalambrico_airpods/MR8U2_AV3.jpeg', 390, 11, 2, 1),
    ('Apple iPhone 11 64GB Verde', 'descripcion', 'https://linio-express.s3-sa-east-1.amazonaws.com/productos/iphone11/iphone11-green-select-2019.png', 1700, 5, 2, 1),
    ('Apple iPhone 11 64GB Amarillo', 'descripcion', 'https://linio-express.s3-sa-east-1.amazonaws.com/productos/iphone11/iphone11-yellow-select-2019.png', 1700, 10, 2, 1),
    ('Apple iPhone 11 64GB Negro', 'descripcion', 'https://linio-express.s3-sa-east-1.amazonaws.com/productos/iphone11/iphone11-black-select-2019.png', 1700, 10, 2, 1),
    ('Apple iPhone 11 64GB Rojo', 'descripcion', 'https://linio-express.s3-sa-east-1.amazonaws.com/productos/iphone11/iphone11-red-select-2019.png', 1700, 15, 2, 1),
    ('LEGO Technic Porsche 911 GT3 RS', 'Experimenta el emblemático Porsche 911 GT3 RS con esta auténtica réplica LEGO®
    Technic. Dentro de la caja encontrarás un libro especial para coleccionistas acerca de la historia de LEGO Technic y
    los modelos GT de Porsche, así como 4 llantas de diseño especial con el emblema de la gama RS. Los elementos se entregan
    en diferentes cajas y la construcción se lleva a cabo en el mismo orden en el que se ensamblan los vehículos en la vida
    real.', 'https://linio-express.s3-sa-east-1.amazonaws.com/productos/Juguetes/LegoTechnic911GT3RS/91eOW8yziNL._AC_SL1500_.jpg,
    https://linio-express.s3-sa-east-1.amazonaws.com/productos/Juguetes/LegoTechnic911GT3RS/611lLgb6TLL._AC_SL1000_.jpg, https://linio-express.s3-sa-east-1.amazonaws.com/productos/Juguetes/LegoTechnic911GT3RS/9151mHylI3L._AC_SL1500_.jpg,
    https://linio-express.s3-sa-east-1.amazonaws.com/productos/Juguetes/LegoTechnic911GT3RS/91pDCHxZK7L._AC_SL1500_.jpg', 700, 3, 7, 3),
    ('Apple MacBook Pro 16 Gris Espacial', 'descripcion', 'https://linio-express.s3-sa-east-1.amazonaws.com/productos/MacBookPro16Grey/mbp16touch-space-gallery1-201911.jpeg, https://linio-express.s3-sa-east-1.amazonaws.com/productos/MacBookPro16Grey/mbp16touch-space-gallery2-201911.jpeg, https://linio-express.s3-sa-east-1.amazonaws.com/productos/MacBookPro16Grey/mbp16touch-space-gallery3-201911.jpeg, https://linio-express.s3-sa-east-1.amazonaws.com/productos/MacBookPro16Grey/mbp16touch-space-gallery4-201911.jpeg', 5000, 10, 2, 1),
    ('Apple iPhone 11 Pro Max 64GB', 'descripcion', 'https://linio-express.s3-sa-east-1.amazonaws.com/productos/iphone11promax/iphone-11-pro-max-midnight-green-select-2019.png', 4000, 20, 2, 1),
    ('Apple MacBook Pro 15 Gris Espacial', 'descripcion', 'https://linio-express.s3-sa-east-1.amazonaws.com/productos/MacBookPro15TouchBarGrey/mbp15touch-space-gallery1-201807.jpeg, https://linio-express.s3-sa-east-1.amazonaws.com/productos/MacBookPro15TouchBarGrey/mbp15touch-space-gallery2-201807_GEO_US.jpeg, https://linio-express.s3-sa-east-1.amazonaws.com/productos/MacBookPro15TouchBarGrey/mbp15touch-space-gallery3-201610.jpeg, https://linio-express.s3-sa-east-1.amazonaws.com/productos/MacBookPro15TouchBarGrey/mbp15touch-space-gallery4-201610.jpeg', 4500, 20, 2, 1),
    ('Lego Technic Bugatti Chiron', 'descripcion', 'https://linio-express.s3-sa-east-1.amazonaws.com/productos/LegoTechnicBugattiChiron/91B2ftaRW7L._AC_SL1500_.jpg, https://linio-express.s3-sa-east-1.amazonaws.com/productos/LegoTechnicBugattiChiron/81In5bbt40L._AC_SL1500_.jpg, https://linio-express.s3-sa-east-1.amazonaws.com/productos/LegoTechnicBugattiChiron/81Tiy8Ww%2BxL._AC_SL1500_.jpg, https://linio-express.s3-sa-east-1.amazonaws.com/productos/LegoTechnicBugattiChiron/81nSVBZ8EUL._AC_SL1500_.jpg, https://linio-express.s3-sa-east-1.amazonaws.com/productos/LegoTechnicBugattiChiron/716AJ2jpgRL._AC_SL1500_.jpg, https://linio-express.s3-sa-east-1.amazonaws.com/productos/LegoTechnicBugattiChiron/71St4QL1z%2BL._AC_SL1000_.jpg, https://linio-express.s3-sa-east-1.amazonaws.com/productos/LegoTechnicBugattiChiron/8146hMBYeJL._AC_SL1500_.jpg', 700, 25, 7, 3),
    ('TAG Heuer Carrera Calibre Heuer 01', 'SIÉNTESE AL VOLANTE. Velocidad. Sudor. Fuerza. Jack Heuer creó el reloj Carrera en 1963 como homenaje a la famosa Carrera Panamericana, considerada por muchos la carrera automovilística más peligrosa el mundo. Este reloj, tan apasionante como la carrera que inspiró su creación, rompió las reglas de la fabricación de relojes y fue el primer cronógrafo especialmente diseñado para los pilotos profesionales, pero se convirtió también en el compañero ideal para salir a la carretera o para el día a día gracias a su diseño más sencillo, elegante y legible. Jack Heuer rompió las reglas de la fabricación de relojes, y desde entonces TAG Heuer no ha dejado de combinar forma y función. El Carrera rinde homenaje a los locos de la velocidad, los audaces y los soñadores que luchan contra en tiempo sin bajar jamás el ritmo.', 'https://linio-express.s3-sa-east-1.amazonaws.com/productos/Moda/TAGHeuerCarrera/CBG2A10.FT6168_resize.png, https://linio-express.s3-sa-east-1.amazonaws.com/productos/Moda/TAGHeuerCarrera/tag-heuer-CBG2A10.FT6168-caseback.jpg',5000, 2, 3, 4),
    ('Les Rayons n°9, 2019', 'Carbon, steel, epoxy paint 47 1/5 × 23 3/5 × 5 9/10 in 120 × 60 × 15 cm', 'https://linio-express.s3-sa-east-1.amazonaws.com/productos/Arte/Les_rayons/large-1.jpg', 1000, 2, 1, 5),
    ('Wild Kong Oil TAG, 2019', 'Hand painted resin sculpture 67 × 27 1/2 × 13 7/10 in 170.2 × 69.9 × 34.8 cm', 'https://linio-express.s3-sa-east-1.amazonaws.com/productos/Arte/Wild_kong/large-2.jpg, https://linio-express.s3-sa-east-1.amazonaws.com/productos/Arte/Wild_kong/large-3.jpg', 5000, 3, 1, 5),
    ('BEETLE, 2018', 'Aluminum 22 × 59 1/10 × 5 9/10 in 56 × 150 × 15 cm', 'https://linio-express.s3-sa-east-1.amazonaws.com/productos/Arte/beetle/large-10.jpg', 2000, 3, 1, 5),
    ('Happy Branding, 2019', 'Light installation, Mounted on black lacquered metal carrier, transparent plexiglass box, American electricity system 59 1/10 × 59 1/10 in 150 × 150 cm', 'https://linio-express.s3-sa-east-1.amazonaws.com/productos/Arte/happy_branding/large-8.jpg, https://linio-express.s3-sa-east-1.amazonaws.com/productos/Arte/happy_branding/large-9.jpg', 4000, 3, 1, 5),
    ('Responsibilities (orange), 2018', 'Neon 9 4/5 × 86 in 25 × 218.5 cm', 'https://linio-express.s3-sa-east-1.amazonaws.com/productos/Arte/responsabilities/large-4.jpg, https://linio-express.s3-sa-east-1.amazonaws.com/productos/Arte/responsabilities/large-5.jpg, https://linio-express.s3-sa-east-1.amazonaws.com/productos/Arte/responsabilities/large-6.jpg', 3500, 3, 1, 5);"""
queries.append(productos)

insertar_datos(db, queries)
