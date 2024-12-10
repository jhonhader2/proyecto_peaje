# Peaje Automatizado

Este proyecto es un sistema de peaje automatizado que gestiona vehículos, tarifas y transacciones. Permite crear y gestionar una base de datos para almacenar información relacionada con los vehículos y las tarifas de peaje.

## Requisitos

- Python 3.x
- MySQL Connector para Python

## Instalación

1. Clona el repositorio:
   ```bash
   git clone <URL_DEL_REPOSITORIO>
   cd peaje_automatizado
   ```

2. Instala las dependencias necesarias:
   ```bash
   pip install mysql-connector-python
   ```

## Uso

1. Configura la conexión a la base de datos en el archivo `Models/database.py`:
   ```python
   db = Database(host='localhost', user='tu_usuario', password='tu_contraseña', database='peaje_automatizado')
   ```

2. Ejecuta el script para inicializar la base de datos:
   ```python
   # Asegúrate de que el script que inicializa la base de datos se ejecute al iniciar tu aplicación.
   ```

3. Utiliza las funciones de la clase `Database` para interactuar con la base de datos.

## Estructura de la Base de Datos

El sistema crea automáticamente las siguientes tablas:

- **vehiculos**: Almacena información sobre los vehículos.
- **tarifas**: Almacena las tarifas asociadas a diferentes tipos de vehículos.
- **transacciones**: Registra las transacciones de peaje realizadas.

## Contribuciones

Las contribuciones son bienvenidas. Si deseas contribuir, por favor abre un issue o envía un pull request.

## Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.
