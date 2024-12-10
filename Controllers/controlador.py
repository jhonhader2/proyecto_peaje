from Models.vehiculo import Vehiculo

class Controlador:
    def __init__(self, db):
        self.db = db
        self.vehiculo = Vehiculo(db)

    def procesar_peaje(self, matricula, tarifa):
        info_saldo = self.vehiculo.obtener_saldo(matricula)
        if not info_saldo:
            return "Vehículo no encontrado."

        saldo_actual = info_saldo["saldo"]
        if saldo_actual >= tarifa:
            nuevo_saldo = saldo_actual - tarifa
            self.vehiculo.actualizar_saldo(matricula, nuevo_saldo)
            query = """INSERT INTO transacciones (vehiculo_id, fecha, tarifa) 
                       VALUES ((SELECT id FROM vehiculos WHERE matricula = %s), NOW(), %s)"""
            self.db.execute_query(query, (matricula, tarifa))
            return f"Peaje procesado. Nuevo saldo: {nuevo_saldo}"
        else:
            return "Saldo insuficiente."

    def recargar_saldo_vehiculo(self, matricula, monto):
        # Funcionalidad adicional opcional
        query = "UPDATE vehiculos SET saldo = saldo + %s WHERE matricula = %s"
        self.db.execute_query(query, (monto, matricula))
        return f"Se recargaron {monto} unidades al vehículo {matricula}."
