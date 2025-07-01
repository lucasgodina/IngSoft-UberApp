# models/passenger.py
from models.user import User

class Passenger(User):
    def __init__(self, name, dni, email, number_phone):
        super().__init__(name, dni, email, number_phone)
        self.direcciones = []

    def calificar(self):
        # Lógica para calificar al pasajero
        print("Calificando pasajero...")

    def agregar_direccion(self, direccion):
        self.direcciones.append(direccion)

    def definir_direccion_casa(self, direccion):
        # Lógica para definir la dirección de casa
        print(f"Dirección de casa establecida: {direccion}")
