# models/passenger.py
from models.user import User


class Passenger(User):
    def __init__(self, name, dni, email, number_phone):
        super().__init__(name, dni, email, number_phone)
        self.addresses = []
        self.ratings = []

    def rate(self, rating):
        self.ratings.append(rating)
        print(f"El pasajero {self.name} ha sido calificado con {rating} estrellas.")

    def add_address(self, address):
        self.addresses.append(address)

    def set_home_address(self, address):
        # Lógica para definir la dirección de casa
        print(f"Dirección de casa establecida: {address}")

    def get_passenger_id(self):
        """Retorna un ID único para el pasajero"""
        return f"passenger_{self.dni}"
