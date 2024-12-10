class Vista:
    def __init__(self, controlador):
        self.controlador = controlador

    def menu(self):
        while True:
            print("\n--- Sistema de Peaje ---")
            print("1. Registrar vehículo")
            print("2. Consultar saldo")
            print("3. Procesar peaje")
            print("4. Recargar saldo")
            print("5. Salir")
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.registrar_vehiculo()
            elif opcion == "2":
                self.consultar_saldo()
            elif opcion == "3":
                self.procesar_peaje()
            elif opcion == "4":
                self.recargar_saldo()
            elif opcion == "5":
                print("Saliendo del sistema.")
                break
            else:
                print("Opción inválida.")

    def registrar_vehiculo(self):
        matricula = input("Ingrese la matrícula: ")
        tipo = input("Ingrese el tipo de vehículo: ")
        try:
            saldo = float(input("Ingrese el saldo inicial: "))
        except ValueError:
            print("Saldo inválido.")
            return
        self.controlador.vehiculo.registrar(matricula, tipo, saldo)
        print("Vehículo registrado con éxito.")

    def consultar_saldo(self):
        matricula = input("Ingrese la matrícula del vehículo: ")
        saldo_info = self.controlador.vehiculo.obtener_saldo(matricula)
        if saldo_info:
            print(f"El saldo actual es: {saldo_info['saldo']}")
        else:
            print("Vehículo no encontrado.")

    def procesar_peaje(self):
        matricula = input("Ingrese la matrícula del vehículo: ")
        try:
            tarifa = float(input("Ingrese la tarifa de peaje: "))
        except ValueError:
            print("Tarifa inválida.")
            return
        mensaje = self.controlador.procesar_peaje(matricula, tarifa)
        print(mensaje)

    def recargar_saldo(self):
        matricula = input("Ingrese la matrícula del vehículo: ")
        try:
            monto = float(input("Ingrese el monto a recargar: "))
        except ValueError:
            print("Monto inválido.")
            return
        mensaje = self.controlador.recargar_saldo_vehiculo(matricula, monto)
        print(mensaje)
