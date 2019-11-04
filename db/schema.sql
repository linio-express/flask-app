DROP TABLE IF EXISTS comercios;
DROP TABLE IF EXISTS categorias;
DROP TABLE IF EXISTS productos;
DROP TABLE IF EXISTS canastas;
DROP TABLE IF EXISTS usuarios;
DROP TABLE IF EXISTS pedidos;
DROP TABLE IF EXISTS productos_por_pedido;
DROP TABLE IF EXISTS productos_por_canasta;

CREATE TABLE IF NOT EXISTS comercios(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  nombre VARCHAR(50) NOT NULL,
  direccion VARCHAR(200) NOT NULL,
  ruc VARCHAR(11) NOT NULL,
  fecha_de_creacion DateTime DEFAULT (datetime(current_timestamp)));

CREATE TABLE IF NOT EXISTS categorias(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  nombre VARCHAR(30) UNIQUE);

CREATE TABLE IF NOT EXISTS productos(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  nombre VARCHAR(30) NOT NULL,
  descripcion VARCHAR(200) NOT NULL,
  precio FLOAT NOT NULL,
  stock INTEGER NOT NULL,
  id_categoria INTEGER NOT NULL,
  id_comercio INTEGER NOT NULL,
  FOREIGN KEY(id_categoria) REFERENCES categorias(id),
  FOREIGN KEY(id_comercio) REFERENCES comercios(id));

CREATE TABLE IF NOT EXISTS usuarios(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  dni VARCHAR(8) UNIQUE,
  fecha_nacimiento DATETIME,
  nombre_completo VARCHAR(100) NOT NULL,
  celular VARCHAR(15) NOT NULL,
  numero_de_tarjeta VARCHAR(16) NOT NULL,
  nombre_de_usuario VARCHAR(32) UNIQUE,
  password VARCHAR(60) NULL,
  fecha_de_creacion DateTime DEFAULT (datetime(current_timestamp)),
  id_canasta INTEGER,
  correo VARCHAR(128) NOT NULL,
  FOREIGN KEY (id_canasta) REFERENCES canastas(id));

CREATE TABLE IF NOT EXISTS canastas(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  id_usuario INTEGER NOT NULL,
  FOREIGN KEY (id_usuario) REFERENCES usuarios(id));

CREATE TABLE IF NOT EXISTS pedidos(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  id_usuario INTEGER NOT NULL,
  fecha_de_creacion DateTime DEFAULT (datetime(current_timestamp)),
  estado VARCHAR(30) NOT NULL,
  repartidor VARCHAR(100) NOT NULL,
  metodo_de_pago VARCHAR(100),
  direccion_de_envio VARCHAR(200),
  tarifa_de_envio NUMERIC(10,2),
  fecha_de_envio DATETIME,
  fecha_de_entrega_programada DATETIME,
  fecha_de_entrega DATETIME,
  FOREIGN KEY(id_usuario) REFERENCES usuarios(id));

CREATE TABLE IF NOT EXISTS productos_por_pedido(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  id_producto INTEGER NOT NULL,
  id_pedido INTEGER NOT NULL,
  cantidad INTEGER NOT NULL,
  precio_unitario FLOAT NOT NULL,
  FOREIGN KEY(id_producto) REFERENCES productos(id),
  FOREIGN KEY(id_pedido) REFERENCES pedidos(id));

CREATE TABLE IF NOT EXISTS productos_por_canasta(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  id_producto INTEGER NOT NULL,
  id_canasta INTEGER NOT NULL,
  cantidad INTEGER NOT NULL,
  FOREIGN KEY(id_producto) REFERENCES productos(id),
  FOREIGN KEY(id_canasta) REFERENCES canastas(id));
