# <h1 align=center> **PROYECTO INDIVIDUAL Nº1** </h1>

## Primer analisis

El dataset consiste en 3 tablas que contiene informacion de una pagina web de venta de videojuegos, informacion de los juegos y su caracteristicas, sobre los usuarios y sobre la relacion entre los usuario y los juegos.

los datos estan anidados en las 3 tablas de manera que en ciertos campos hay una tabla por registro, mi idea fue sacar cada tabla de cada registro y agregarle los campos de la tabla principal y colocar en todos los registros el mismo valor en cada campo que corresponde a la tabla principal, este procedimiento se hace con un codigo fuente de python para cada una de las tablas.

## esquema de directorios

<p align="center">
<img src="https://github.com/samuelchacon00/PI_PT05_1/blob/d1123f489f5fb086950b51c4a2f05bc4bdd05be6/src/arbol.png"  height=300></p>

En el directorio datasets_default estan los datasets descargados y descomprimidos manualmente para desanidarlos.
Una vez desanidados se guardan en csv en datasets para que se lleve a cabo el EDA y ETL de cada tabla.
Dentro de deploy estan los archivos necesarios para hacer el deploy.

se crearon 3 archivos fuente distintos para desanidar las tablas, dos utilizan multiprocesamiento para que el proceso no tarde demasiado, si se va a ejecutar tener en cuenta que los programas llevan el CPU al 100%.

## ETL - EDA

En este proceso se hizo en un jupyternotebook se eliminaron los duplicados, se hizo limpienza y normalizacion de columnas, se eliminaron columnas dependiendo de que es lo necesario para lo que se pide en el proyecto y las funciones de la api. Se realizaron algunos graficos para observar algunas curiosidades de las tablas dando lugar a una mejor comprension a los datos dados y tomando todas las acciones con una justificacion.

## Desarrolo de la API

Luego desarrolle las funciones de la api, y los modelos de aprendizaje automatico, este ultimo usando la similitud del conseno. En la mayoria de las funciones utilice el metodo .apply() en las tablas para optimizar el rendimiento del programa y tambien para hacer el codigo mas corto y sencillo. Al final del EDA antes de guardar los datos tome la descision de eliminar el 85% de los registros de forma aleatoria para que render me permitiera hacer el deploy, de todas formas en el archivo fuente se ecuentra un comentario en cada funcion de que input se debe utilizar para que devuelva una respuesta completa.

[Link del repositorio de render]("https://github.com/samuelchacon00/deploy_pt05")

[Link del enunciado](https://github.com/soyHenry/PI_ML_OPS/tree/PT)

[link del deploy en render](https://api-steam-games-fc4s.onrender.com/docs#/default)
