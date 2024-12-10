class Vehiculo:
    def __init__(self, db):
        self.db = db

    def registrar(self, matricula, tipo, saldo):
        query = "INSERT INTO vehiculos (matricula, tipo, saldo) VALUES (%s, %s, %s)"
        self.db.execute_query(query, (matricula, tipo, saldo))

    def obtener_saldo(self, matricula):
        query = "SELECT saldo FROM vehiculos WHERE matricula = %s"
        return self.db.fetch_one(query, (matricula,))

    def actualizar_saldo(self, matricula, nuevo_saldo):
        query = "UPDATE vehiculos SET saldo = %s WHERE matricula = %s"
        self.db.execute_query(query, (nuevo_saldo, matricula))
