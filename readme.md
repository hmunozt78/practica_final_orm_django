<h1 align="center">Trabajo de Consolidacion Modulo 07</h1>

## Consideraciones Generales

Se asume que la persona tiene conocimientos basicos adecuados de Python, HTML y Django

## Pasos iniciales

Para comenzar este proyecto, debe tener instalado los siguientes elementos basicos:

* Visual Studio Code
* Python 3.12.3
* PostgreSQL 16

## Entorno Virtual y Modulos Requeridos

Una vez ya cumpla con los requisitos previamente indicados en el punto anterior, cree una carpeta y ejecute los siguientes pasos:

> Cree el entorno virtual

```
python -m venv venv
```


> Ejecute el entorno virtual

```
./venv/Scripts/activate
```

> Instale los modulos necesarios con las siguientes instrucciones

```
pip install Django==5.1.3
pip install psycopg2==2.9.10
```

> Para clonar el proyecto ejecute la siguiente instruccion:

```
git clone https://github.com/hmunozt78/practica_final_orm_django.git
```

## Creacion de la Base de datos y configuracion del proyecto:

para la creacion de la base de datos, debe ejecutar en la interfaz grafica de postgreSQL, llamada PGAdmin, las siguientes instrucciones:

```
CREATE DATABASE db_final_orm;
CREATE USER userdjango WITH PASSWORD 'userdjango';
GRANT ALL PRIVILEGES ON DATABASE db_final_orm TO userdjango;
```

El el archivo settings.py ubicado en la carpeta config, debe verificar los siguientes codigos:

> En seccion Databases

```
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "db_final_orm",
        "USER": "userdjango",
        "PASSWORD": "userdjango",
        "HOST": "127.0.0.1",
        "PORT": "5432",
    }
}
```