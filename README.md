//proyecto individual parte 1

El dataset consiste en 3 tablas que contiene informacion de una pagina web de venta de videojuegos, informacion de los juegos y su caracteristicas, sobre los usuarios y sobre la relacion entre los usuario y los juegos.

los datos esta anidados en las 3 tablas de manera que en ciertos campos hay una tabla por registro, mi idea fue sacar cada tabla de cada registro y agregarle los campos de la tabla principal y colocar en todos los registros el mismo valor en cada campo que corresponde a la tabla principal, este procedimiento se hace con un codigo fuente de python para cada una de las tablas.

una vez desanidados, se ha hecho EDA y un ETL de cada tabla con respecto a sus campos, que estaba bien o mal, si
habian campos que normalizar o eliminar dependiendo de era necesario para lo que se pide en el proyecto y las funciones de la api. Se realizaron algunos graficos para observar algunas curiosidades de las tablas dando lugar a una mejor comprension a los datos dados.

Luego desarrolle las funciones de la api, y los modelos de aprnedisaje automatico este ultimo usando la similitud del conseno