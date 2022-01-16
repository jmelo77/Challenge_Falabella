# Reto Falabella - API

## Introducción

+ [Python 3.10.1](https://www.python.org/downloads/release/python-3101/).
+ La API se creo con el framework [Flask](https://flask.palletsprojects.com/en/2.0.x/)
+ La conexion a la base de datos se logra 
    con la libreria [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/).
+ Para las pruebas unitarias se utilizo la libreria [Unitest](https://pypi.org/project/unittest2/) y la aplicacion Postman.    

## Prerequisitos

+ Instala [Python 3.10.1](https://www.python.org/downloads/release/python-3101/)

Habilitar entorno virtual de Python y luego instalar las dependencias del proyecto.

```commandline
python -m venv ./venv
venv/Scripts/activate
pip install -r requirements.txt
```
## Uso
El proyecto está configurado para ejecutarse en el puerto 5000 del localhost o 127.0.0.1:5000.

```commandline
python manage.py runserver
```

El endpoint para consumir el servicio es:

```commandline
GET http://127.0.0.1:5000/patent/id/<int:id>
```
Ejemplo:
```commandline
GET http://127.0.0.1:5000/patent/id/8
```
Respuesta del servicio:
```commandline
    {
        "patent": "AAAA007"
    }
```

El endpoint para consumir el servicio es:

```commandline
GET http://127.0.0.1:5000/patent/name/<name>
```
Ejemplo:
```commandline
GET http://127.0.0.1:5000/patent/name/AAAA007
```
Respuesta del servicio:
```commandline
    {
        "id": 8
    }
```

## Pruebas Unitarias

+ Postman.

![alt text](https://github.com/jmelo77/Challenge_Falabella/blob/main/doc/postman_1.png)
![alt text](https://github.com/jmelo77/Challenge_Falabella/blob/main/doc/postman_2.png)

+ Unittest.
```commandline
python -m unittest -v unittest_endpoints
```

![alt text](https://github.com/jmelo77/Challenge_Falabella/blob/main/doc/unittest.png)


## Diagrama Entidad Relación

Se propone el siguiente modelo de base de datos:

![alt text](https://github.com/jmelo77/Challenge_Falabella/blob/main/doc/Diagrama_ER_Falabella.png)

