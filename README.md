# Basic Flask API

Prueba para Merqueo sobre la realizacion de un API REST.

- [Prueba Backend](prueba/PruebaBackend.pdf)
- [Metodos del API](prueba/RespuestaPruebaBackend.pdf)

## Ejecutar entorno

  - Iniciar entorno de desarrollo: `docker-compose up -d`
  - Importar base de datos: `docker exec -i $(docker-compose ps -q mysql-db) mysql -uroot -pm3rqu30! --database=merqueo < merqueo.sql`

## Adminer

  Se tiene un contenedor con Adminer sobre el cual se puede acceder a la base de datos

  `http://192.168.55.3:8080`

## MySQL

  - *Host:* 192.168.55.2
  - *User:* dbuser
  - *Password:* m3rqu30!

## Ejecutar Pruebas

### Requisitos

  - pytest
  - mock
  - mysql-connector-python
  - flask

### Ejecucion
  
  - `python3 -m pytest tests/* -v`
