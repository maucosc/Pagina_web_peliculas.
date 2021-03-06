DROP DATABASE IF EXISTS descargar_peliculas;
CREATE DATABASE descargar_peliculas;
USE descargar_peliculas;

CREATE TABLE categoria(
	id INT AUTO_INCREMENT,
	nombre VARCHAR (100),
	PRIMARY KEY (id),
	UNIQUE (nombre)
);

INSERT INTO categoria VALUES(NULL, 'Accion'),
							(NULL, 'Ciencia Ficcion'),
							(NULL, 'Animacion'),
							(NULL, 'Artes Marciales'),
							(NULL, 'Comedia'),
							(NULL, 'Romance'),
							(NULL, 'Terror'),
							(NULL, 'Aventura'),
							(NULL, 'Deporte'),
							(NULL, 'Fantasia'),
							(NULL, 'Series TV'),
							(NULL, 'Triller');
						
CREATE TABLE formato(
	id INT AUTO_INCREMENT,
	nombre VARCHAR (50),
	descripcion TEXT,
	PRIMARY KEY (id),
	UNIQUE (nombre)
);

INSERT INTO formato VALUES(NULL, 'SCR', 'Obtebido de un DVD o de Blu-ray DE USO promocional'),
						   (NULL, 'VHS-Screener', 'Lo mismo de un SCR, pero obtenida de una cinta VHS'),
						   (NULL, 'TC(telecine)', 'Se obtiene por la transferencia del rollo analógico destinado a cines a un medio digital a través de una máquina destinada a este fin'),
						   (NULL, 'WP(Workprint)', 'Son copias obtenidas de películas no terminadas.'),
						   (NULL, 'DVDFull', 'Es una copia exacta del DVD original'),
						   (NULL, 'DVDRip', 'Son copias donde se extrae la película y uno o dos audios y a veces también uno o dos pistas de subtítulos'),
						   (NULL, 'BRRip', 'Son HDRip obtenidos de un Blu-ray comercial. '),
						   (NULL, 'HDTV', 'Son capturas realizadas desde emisiones digitales de Alta Definición.'),
						   (NULL, 'HD', 'son señales digitales que ofrecen una calidad superior a la ofrecida por el SD o ED.'),
						   (NULL, '720p y 1080p', 'hacen referencia al número de líneas verticales que muestra cada fotograma.');




CREATE TABLE cuenta (
	id INT AUTO_INCREMENT,
	nickname VARCHAR(50) UNIQUE,
	email VARCHAR(50) UNIQUE,
	passwd VARCHAR(64),
	PRIMARY KEY (id)
);

INSERT INTO cuenta VALUES(NULL, 'mrT', 'marc.sc@outlook.es', SHA2('63568', 0)),
						  (NULL, 'juan', 'juan@hotmail.com', SHA2('31231', 0)),
						  (null,'hola', 'hola@gmail.com', SHA2('hola',0)),
						  (null,'mauco', 'mauco@gmail.com', SHA2('mauco',0));
						   
CREATE TABLE servidor (
	id INT AUTO_INCREMENT,
	nombre VARCHAR(50) UNIQUE,
	id_cuenta_fk INT,
	
	PRIMARY KEY (id)
);

INSERT INTO servidor VALUES(NULL, 'Usercloud', 1),
						   (NULL, 'Openload', 3),
						   (NULL, 'Uptobox', 2),
						   (NULL, '1Fichier', 3),
						   (NULL, '4Shared', 1),
						   (NULL, 'Uploaded', 2),
						   (NULL, 'Mega', 3),
						   (NULL, 'GoogleDrive', 1);


CREATE TABLE pelicula (
	id INT AUTO_INCREMENT,
	nombre VARCHAR (100)UNIQUE,
	resolucion VARCHAR (15),
	idioma VARCHAR (50),
	tamano VARCHAR (10),
	sinopsis TEXT,
	
	PRIMARY KEY (id)
);

INSERT INTO pelicula VALUES(NULL, 'el jefe de la mafia', '1920x808', 'Español Latino', '3.75 GB', 'Biopic del famoso mafioso estadounidense John Gotti (1940-2002), jefe de la familia Gambino, una de las más importantes del crimen organizado en la Norteamérica del siglo XX.'),
							(NULL, 'el legado', '1920x1080', 'Español Latino', '3.96 GB ', 'Perseguidos por un criminal vengativo (James Franco) y una banda de soldados sobrenaturales,​ un exconvicto recién liberado (Jack Reynor) y su hermano adolescente adoptado (Myles Truitt) se ven obligados a escapar con un arma de origen misterioso que es su única protección.'),
							(NULL, 'star Wars: Episodio VI - El Retorno del jedi', '1920x1080', 'Inglés AC', '4.71 GB', 'Para ir a Tatooine y liberar a Han Solo, Luke Skywalker y la princesa Leia deben infiltrarse en la peligrosa guarida de Jabba the Hutt, el gángster más temido de la galaxia. Una vez reunidos, el equipo recluta a tribus de Ewoks para combatir a las fuerzas imperiales en los bosques de la luna de Endor. Mientras tanto, el Emperador y Darth Vader conspiran para atraer a Luke al lado oscuro, pero el joven está decidido a reavivar el espíritu del Jedi en su padre. La guerra civil galáctica termina con un último enfrentamiento entre las fuerzas rebeldes unificadas y una segunda Estrella de la Muerte, indefensa e incompleta, en una batalla que decidirá el destino de la galaxia.'),
                            (NULL, 'scarface', '1920x1080', 'Español', '2 GB', 'Un imigrande cubano de las carceles de fidel castro provoca un camino de destruccion en su ascenso en el mundo de las drogras de miami');

CREATE TABLE pelicula_servidor (
	id INT AUTO_INCREMENT,
	id_pelicula_fk INT,
	id_servidor_fk INT,
	url TEXT,
	
	PRIMARY KEY (id)
);

INSERT INTO pelicula_servidor VALUES(NULL, 3, 7, "http://paste.pelismegahd.pe/?v=52725"),
									 (NULL, 3, 8, "http://paste.pelismegahd.pe/?v=52726"),
									 (NULL, 2, 5, "http://paste.pelismegahd.pe/?v=53858"),
									 (NULL, 2, 2, "http://paste.pelismegahd.pe/?v=53858"),
									 (NULL, 1, 2, "http://paste.pelismegahd.pe/?v=53858"),
									 (NULL, 1, 3, "http://paste.pelismegahd.pe/?v=53858");

CREATE TABLE pelicula_formato (
	id INT AUTO_INCREMENT,
	id_pelicula_fk INT, 
	id_formato_fk INT, 
	
	PRIMARY KEY (id)
);

INSERT INTO pelicula_formato VALUES(NULL, 1, 7),
									(NULL, 2, 7);


CREATE TABLE categoria_pelicula (
	id INT AUTO_INCREMENT,
	id_pelicula_fk INT,
	id_categoria_fk INT,

	PRIMARY KEY (id)
);


INSERT INTO categoria_pelicula VALUES(NULL, 2, 1),
									  (NULL, 3, 2),
									  (NULL, 1, 1),
									  (NULL, 2, 2);

-- inner_join_Visualizar

SELECT pelicula.id AS 'N', 
	pelicula.nombre, 
	pelicula.resolucion, 
	pelicula.idioma, 
	pelicula.tamano, 
	categoria.nombre AS 'Categoria'
FROM categoria_pelicula
INNER JOIN categoria ON categoria_pelicula.id_categoria_fk = categoria.id
INNER JOIN pelicula ON categoria_pelicula.id_pelicula_fk = pelicula.id;

SELECT pelicula.nombre, 
	servidor.nombre, AS 'Servidor'
	pelicula_servidor.url
FROM
	pelicula_servidor
INNER JOIN pelicula ON pelicula_servidor.id_pelicula_fk = pelicula.id
INNER JOIN servidor ON pelicula_servidor.id_pelicula_fk = servidor.id;



-- Update_Usuario

UPDATE cuenta SET nickname = "mauco" WHERE nickname = 'hola';


