import mysql.connector

class Database:
    def __init__(self, host, user, password, database):
        self.connection = mysql.connector.connect(
            host=host, 
            user=user, 
            password=password
        )
        self.cursor = self.connection.cursor(dictionary=True)
        self.create_database(database)
        self.connection.database = database  # Conectar a la base de datos creada

    def create_database(self, database):
        self.cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database};")
        self.cursor.execute(f"USE {database};")
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS vehiculos (
                id INT AUTO_INCREMENT PRIMARY KEY,
                matricula VARCHAR(20) UNIQUE NOT NULL,
                tipo VARCHAR(20) NOT NULL,
                saldo DECIMAL(10, 2) NOT NULL
            );
        """)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS tarifas (
                id INT AUTO_INCREMENT PRIMARY KEY,
                tipo_vehiculo VARCHAR(20) UNIQUE NOT NULL,
                tarifa DECIMAL(10, 2) NOT NULL
            );
        """)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS transacciones (
                id INT AUTO_INCREMENT PRIMARY KEY,
                vehiculo_id INT NOT NULL,
                fecha DATETIME NOT NULL,
                tarifa DECIMAL(10, 2) NOT NULL,
                FOREIGN KEY (vehiculo_id) REFERENCES vehiculos(id)
            );
        """)
        self.connection.commit()

    def execute_query(self, query, params=None):
        self.cursor.execute(query, params or ())
        self.connection.commit()

    def fetch_all(self, query, params=None):
        self.cursor.execute(query, params or ())
        return self.cursor.fetchall()

    def fetch_one(self, query, params=None):
        self.cursor.execute(query, params or ())
        return self.cursor.fetchone()
