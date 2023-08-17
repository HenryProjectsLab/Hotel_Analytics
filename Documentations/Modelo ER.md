# Modelo entidad-relación sobre negocios de hotelería y sus reviews en Google Maps y Yelp

## Introducción

Este documento describe el diseño y la estructura de un modelo entidad-relación (ER) que representa los datos de los negocios de hotelería y sus reseñas en las plataformas de Google Maps y Yelp. El objetivo de este modelo es facilitar el análisis y la comparación de los hoteles que se encuentran en ambas plataformas, así como obtener información sobre las opiniones y preferencias de los usuarios.

## Diagrama del modelo ER

El diagrama del modelo ER se muestra a continuación:

![Diagrama ER](/Image/Modelo_er_copia.jpg)

El diagrama utiliza la notación de Chen, que consiste en representar las entidades con rectángulos, las relaciones con rombos y los atributos con óvalos. Las líneas que conectan las entidades y las relaciones indican las cardinalidades, que pueden ser uno a uno (1:1), uno a muchos (1:N), muchos a uno (N:1) o muchos a muchos (N:M).

## Descripción de las tablas

Para obtener más información donde se detallan las tablas que componen el modelo ER, así como sus atributos y restricciones visita el [Diccionario de datos](https://github.com/HenryProjectsLab/Hotel_Analytics/blob/a8049c47dcd2a55e6293f1b8f80839423f640079/Documentations/Diccionario%20de%20datos.md)

## Relaciones

Las relaciones que existen entre las entidades son las siguientes:

- La relación **pertenece** entre business_google y google_hotels indica que un negocio registrado en Google Maps puede pertenecer o no a la categoría de hotelería. Esta relación tiene una cardinalidad uno a uno (1:1), ya que cada negocio tiene un solo gmap_id y cada gmap_id corresponde a un solo negocio.

- La relación **reseña** entre google_hotels y google_hotels_review indica que un hotel puede tener una o más reseñas de los usuarios, y que una reseña pertenece a un solo hotel. Esta relación tiene una cardinalidad uno a muchos (1:N), ya que cada hotel tiene un solo gmap_id y cada gmap_id puede estar asociado a varias reseñas.

- La relación **pertenece** entre business_yelp y yelp_hotels indica que un negocio registrado en Yelp puede pertenecer o no a la categoría de hotelería. Esta relación tiene una cardinalidad uno a uno (1:1), ya que cada negocio tiene un solo business_id y cada business_id corresponde a un solo negocio.

- La relación **reseña** entre yelp_hotels y yelp_hotels_review indica que un hotel puede tener una o más reseñas de los usuarios, y que una reseña pertenece a un solo hotel. Esta relación tiene una cardinalidad uno a muchos (1:N), ya que cada hotel tiene un solo business_id y cada business_id puede estar asociado a varias reseñas.

- La relación **coincide** entre google_hotels y yelp_hotels indica que un hotel puede coincidir o no con otro hotel en ambas plataformas, según las dos primeras palabras del nombre y el código postal. Esta relación tiene una cardinalidad muchos a muchos (N:M), ya que un hotel puede coincidir con varios hoteles en la otra plataforma, y viceversa.

## Referencias

Chen, P.P. (1976). The entity-relationship model—toward a unified view of data. ACM Transactions on Database Systems (TODS), 1(1), 9–36. ²: Modelo de entidad relación
