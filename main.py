from Models.database import Database
from Controllers.controlador import Controlador
from Views.vista import Vista

if __name__ == "__main__":
    # Ajustar credenciales y base de datos según entorno
    db = Database(host="localhost", user="root", password="", database="peaje_automatizado")
    controlador = Controlador(db)
    vista = Vista(controlador)
    vista.menu()
