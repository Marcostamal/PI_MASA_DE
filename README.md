# <h1 align=center> PI_MASA_DE Proyecto Individual ML_ops <h/>

<h3 align=center>Hola mi nombre es Marcos y este es mi proyecto <h/>

<p align="center">
<img src="https://media.tenor.com/f_EOn4JhDZUAAAAC/anya-forger-smile.gif"  height=300>
</p>

## Primera Parte
En la primera parte del proyecto (ETL) conte con 4 archivos csv que contenia el nombre de las peliculas y algunas caracteristicas de estas identificadas por un id
cada archivo correspondia a una plataforma de steaming (Amazon, Netflix, Disney, Hulu)
### Transformaciones que se hicieron
+ Se genero un campo **`id`**: Cada id es la union del campo show_id con la primera inicial de la plataforma (ejemplo para títulos de Amazon = **`as123`**)
+ Se genero un campo llamado plataforma el cual contiene la inicial de cada plataforma ("a", "n", "d", "h")
+ Los valores nulos del campo rating se remplazaron por el string “**`G`**” (corresponde al maturity rating: “general for all audiences”)
+ Las fechas, se cambiaron al formato **`AAAA-mm-dd`**
+ Los campos de texto se pasaron a minusculas **minúsculas**, sin excepciones
+ El campo ***duration*** se convirtio en dos campos: **`duration_int`** y **`duration_type`**. 
El primero es un integer y el segundo un string indicando la unidad de medición de duración: min (minutos) o season (temporadas)
+ Los campos "show_id", "duration". y "description" fueron borrados.
+ Los campos de texto nullos se remplazaron por "sin dato"
+ se corrigieron datos sobreescritos en el campo rating

Puedes revisar los cambios hechos aqui:
[ETL a Datos de las Plataformas](https://github.com/Marcostamal/PI_MASA_DE/blob/main/Data_Cleaning_Plataformas.ipynb)

## Segunda Parte
En la segunda parte del proceso de ETL se hicieron transformaciones a la data de los usuarios, solo se usaron 7 archivos de todos los adquiridos, solo se hizo una transformacion.
+ Las fechas, se cambiaron al formato **`AAAA-mm-dd`** 
 
Puedes ver los cambios aqui: 
[ETL a Datos de los usuarios](https://github.com/Marcostamal/PI_MASA_DE/blob/main/Data_Cleaning_UserScore.ipynb)

## Tercera Parte
En la tercera parte del ETL hice 2 uniones:
 1. Union de los promedios de score y los datos limpios de las plataformas (Para API)
 2. Union de todos los datos de usuarios con plataformas (Para Modelo de Machine Learning)
 
Puedes ver lo realizado aqui:
[ETL union de data](https://github.com/Marcostamal/PI_MASA_DE/blob/main/Union_Data.ipynb)
 
Puedes revisar la fuente de datos Aqui: 
[Drive de datos](https://drive.google.com/drive/folders/1225oX7a5IgmPLOSO90WAVNcvo8zn1g1h?usp=share_link)
<p align="center">
<img src="https://cdn-icons-png.flaticon.com/512/2875/2875333.png"  height=300>
</p>
En la carpeta Data_util estan los archivos csv limpios y las uniones

## Cuarta Parte API 
He creado una API para que puedas consultar alguna info de los datos que he trabajado como por ejemplo la cantidad de peliculas que hay en una plataforma

Usa [Mi app en Deta Space](https://deta.space/discovery/r/lvlxbrwtm85idcym) para entrar en mi app y ver como funciona, una ves que la estes utilizando te aconsejo escribas /docs para que mires la documentacion y sepas que puedes introducir y como introducirlo.

Una de las funciones llamada get_max_duration para probarla tendras que remplazar los valores de string y para el anio el 0 esto solo si quieres filtrar por algun campo, pero si no quieres mover esto puedes no tocarlo y te devolvera una respuesta buscando en todos los datos

ejemplo:
~~~
{
  "platform": "amazon",
  "year": 2014,
  "duration_type": "min"
}
~~~
