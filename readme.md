# Super Simple ORM

Este pequeño ORM es un ejercicio de buenas prácticas y TDD, además de funcionalidades modernas de python.

## Objetivos

Crear una librería que maneje transparentemente diferentes conexiones a bases de datos para ser utilizada en las aplicaciones desarrolladas por mi. Un "create once, deploy everywhere". Las siguientes bases de datos están en el roadmap:

- SQLite (WIP)
- SQL
- Postgre

## Testing

El testing se ejecuta con pytest y coverage. Para correrlo, simplmente ejecutar:

coverage run -m pytest
coverage report