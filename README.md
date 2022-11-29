# Python - Pytest - Flask - Poetry - Postgresql - Docker / Microservicios

TEAM:

- Kevin Galindo 
- Maria Emily parra

# RUN PROJECT

- Git clone https://github.com/Ksgalo/microservice
- cd <nombre_carpeta> && docker-compose up -d

# Tests

- _Los test se deben realizar mientras la aplicacion se esta ejecutando en docker_
- cd <nombre_carpeta>
- cd tests/
- source env/Scripts/activate
- pytest -v

# Services

### Postgresql

http://localhost:5432

### Faker

- Visualizar registros: http://localhost:3000/select
- Crear registros: http://localhost:3000/insert
- Eliminar registros: http://localhost:3000/delete

### API

- Visualizar registros: http://localhost:3001
- Crear registros: http://localhost:3001/admin/insert
- Eliminar registros: http://localhost:3001/admin/delete

### WEB

- Panel de admin: http://localhost:3002/admin
- Visualizar registros: http://localhost:3002
- Crear registros: http://localhost:3002/admin/insert
- Eliminar registros: http://localhost:3002/admin/delete
