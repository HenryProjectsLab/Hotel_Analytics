#Diccionario de datos

Este conjunto de datos proporciona información valiosa sobre negocios registrados en Google Maps, incluyendo detalles como el nombre, dirección, descripción, calificaciones y más. Estos datos son de gran utilidad para realizar análisis y estudios relacionados con la industria de servicios y comercios en las distintas ciudades y estados de Estados Unidos.

Aquí está el diccionario de datos para la tabla business_google:

- `gmap_id`: Identificación única del negocio en Google Maps.
- `name`: Nombre del negocio.
- `address`: Dirección del negocio.
- `description`: Descripción del negocio.
- `num_of_reviews`: Número de reseñas del negocio.
- `avg_rating`: Calificación promedio del negocio.
- `latitude`: Latitud geográfica del negocio.
- `longitude`: Longitud geográfica del negocio.
- `price`: Precio del negocio.
- `state`: Estado donde se encuentra el negocio.
- `url`: URL de Google Maps para el negocio.
- `category`: Categoría(s) del negocio.
- `relative_results`: Resultados relacionados.
- `Etiqueta`: Etiqueta del negocio.
- `ciudad`: Ciudad donde se encuentra el negocio.
- `estado`: Estado donde se encuentra el negocio.
- `codigo_postal`: Código postal donde se encuentra el negocio.


Estos datos proporcionan información sobre varios hoteles registrados en Google Maps, incluyendo detalles como el nombre, número de reseñas, calificación promedio, dirección y categoría del hotel. Esta información es valiosa para realizar análisis y estudios relacionados con la industria hotelera en diferentes ciudades y estados.:

- `gmap_id`: Identificación única del hotel en Google Maps.
- `name`: Nombre del hotel.
- `num_of_reviews`: Número de reseñas del hotel.
- `avg_rating`: Calificación promedio del hotel.
- `address`: Dirección del hotel.
- `ciudad`: Ciudad donde se encuentra el hotel.
- `estado`: Estado donde se encuentra el hotel.
- `codigo_postal`: Código postal donde se encuentra el hotel.
- `category`: Categoría(s) del hotel.

Estos datos proporcionan información sobre varios restaurantes registrados en Google Maps, incluyendo detalles como el nombre, número de reseñas, calificación promedio y dirección del restaurante. Esta información es útil para realizar análisis y estudios relacionados con la industria de restaurantes en diferentes ciudades y estados.

Diccionario de datos para la tabla "google_restaurant" que contiene información sobre restaurantes en Google Maps:

- `gmap_id`: Identificación única del restaurante en Google Maps.
- `name`: Nombre del restaurante.
- `num_of_reviews`: Número de reseñas del restaurante.
- `avg_rating`: Calificación promedio del restaurante.
- `address`: Dirección del restaurante.
- `ciudad`: Ciudad donde se encuentra el restaurante.
- `estado`: Estado donde se encuentra el restaurante.
- `codigo_postal`: Código postal donde se encuentra el restaurante.

Estos datos proporcionan información sobre las reseñas dejadas por los usuarios sobre diferentes hoteles en Google Maps. Cada entrada incluye detalles como el nombre del usuario, la calificación, el comentario, la fecha de la reseña, la ubicación del hotel y la identificación única del hotel. Estos datos son útiles para analizar la satisfacción del cliente y obtener información sobre la calidad y el servicio de diferentes hoteles.

Diccionario de datos para la tabla "google_hotels_reviews" que contiene información sobre las reseñas de hoteles en Google Maps:

- `user_id`: Identificación única del usuario que dejó la reseña.
- `name`: Nombre del usuario que dejó la reseña.
- `rating`: Calificación otorgada en la reseña.
- `comentario`: Comentario del usuario sobre su experiencia en el hotel.
- `fecha`: Fecha en que se dejó la reseña.
- `estado`: Estado donde se encuentra el hotel.
- `ciudad`: Ciudad donde se encuentra el hotel.
- `codigo_postal`: Código postal donde se encuentra el hotel.
- `business_id`: Identificación única del negocio del hotel en Google Maps.

Estos datos proporcionan información sobre las reseñas dejadas por los usuarios sobre diferentes restaurantes en Google Maps. 
Diccionario de datos para la tabla "google_restaurant_reviews" que contiene información sobre las reseñas de restaurantes en Google Maps:

- `user_id`: Identificación única del usuario que dejó la reseña.
- `user_name`: Nombre del usuario que dejó la reseña.
- `rating`: Calificación otorgada en la reseña.
- `comentario`: Comentario del usuario sobre su experiencia en el restaurante.
- `fecha`: Fecha en que se dejó la reseña.
- `estado`: Estado donde se encuentra el restaurante.
- `ciudad`: Ciudad donde se encuentra el restaurante.
- `codigo_postal`: Código postal donde se encuentra el restaurante.
- `gmap_id`: Identificación única del negocio del restaurante en Google Maps.

Estos datos proporcionan información sobre diferentes negocios registrados en Yelp. Cada entrada incluye detalles como la identificación única del negocio, el nombre, la dirección, la ubicación geográfica, la calificación promedio, el número de reseñas y si el negocio está abierto o cerrado. Estos datos son útiles para analizar y comprender la distribución geográfica de los negocios, sus calificaciones y su popularidad en función de las reseñas.

Diccionario de datos que contiene información sobre negocios registrados en Yelp:

- `business_id`: Identificación única del negocio en Yelp.
- `name`: Nombre del negocio.
- `address`: Dirección del negocio.
- `city`: Ciudad donde se encuentra el negocio.
- `state`: Estado donde se encuentra el negocio.
- `postal_code`: Código postal donde se encuentra el negocio.
- `latitude`: Latitud geográfica del negocio.
- `longitude`: Longitud geográfica del negocio.
- `stars`: Calificación promedio del negocio en Yelp.
- `review_count`: Número de reseñas recibidas por el negocio.
- `is_open`: Indicador de si el negocio está abierto (1) o cerrado (0).

Estos datos proporcionan información sobre diferentes hoteles registrados en Yelp. Cada entrada incluye detalles como la identificación única del negocio, el nombre del hotel, la ubicación geográfica, la calificación promedio, el número de reseñas y la dirección del hotel. 

Diccionario de datos para el archivo "yelp_hotels" que contiene información sobre hoteles en Yelp:

- `business_id`: Identificación única del negocio en Yelp.
- `name`: Nombre del hotel.
- `city`: Ciudad donde se encuentra el hotel.
- `stars`: Calificación promedio del hotel en Yelp.
- `review_count`: Número de reseñas recibidas por el hotel.
- `address`: Dirección del hotel.
- `postal_code`: Código postal donde se encuentra el hotel.

Estos datos proporcionan información sobre las reseñas realizadas por usuarios en diferentes hoteles registrados en Yelp. Cada entrada incluye detalles como la identificación única del negocio, el nombre del hotel, las categorías del negocio, la fecha de la reseña, el texto de la reseña, la calificación, el número de votos útiles, cool y chistosos recibidos, la identificación única del usuario que hizo la reseña, la ciudad, el estado y el código postal del negocio (hotel). Estos datos son útiles para analizar y comprender las opiniones y experiencias de los usuarios con respecto a diferentes hoteles.

Diccionario de datos para el archivo "yelp_hotels_review" que contiene información sobre las reseñas de hoteles en Yelp:

- `business_id`: Identificación única del negocio en Yelp.
- `name`: Nombre del negocio (hotel).
- `categories`: Categorías del negocio.
- `fecha`: Fecha de la reseña.
- `review_id`: Identificación única de la reseña.
- `comentario`: Texto de la reseña.
- `rating`: Calificación de la reseña.
- `c_util`: Número de votos útiles para la reseña.
- `c_cool`: Número de votos cool para la reseña.
- `c_chistoso`: Número de votos chistosos para la reseña.
- `user_id`: Identificación única del usuario que hizo la reseña.
- `ciudad`: Ciudad del negocio (hotel).
- `estado`: Estado del negocio (hotel).
- `codigo_postal`: Código postal donde se encuentra el negocio (hotel).

Estos datos proporcionan información sobre hoteles que tienen reseñas y calificaciones tanto en Google como en Yelp. Cada entrada incluye detalles como el nombre del hotel, las calificaciones promedio en Google y Yelp, el número de reseñas en Yelp y Google, la dirección del hotel, la ciudad, el estado y el código postal donde se encuentra el hotel, así como las identificaciones únicas de Google Maps y Yelp. Estos datos son útiles para comparar las calificaciones y reseñas de hoteles en ambas plataformas.

El archivo "hotels_cruzado" que contiene información sobre los hoteles que comparten datos en Yelp y Google:

- `nombre`: Nombre del hotel.
- `avg_rating_google`: Calificación promedio en Google.
- `stars_yelp`: Calificación en Yelp.
- `num_reviews_yelp`: Número de reseñas en Yelp.
- `num_reviews_google`: Número de reseñas en Google.
- `address`: Dirección del hotel.
- `ciudad`: Ciudad donde se encuentra el hotel.
- `estado`: Estado donde se encuentra el hotel.
- `codigo_postal`: Código postal donde se encuentra el hotel.
- `gmap_id`: Identificación única de Google Maps para el hotel.
- `yelp_business_id`: Identificación única de Yelp para el hotel.


















