from models.ride import Ride

class RideController:
    def __init__(self, view):
        self.view = view
        self.rides = []

    def request_ride(self, passenger, origin, destination):
        ride = Ride(passenger, origin, destination)
        self.rides.append(ride)
        self.view.show_message(f"{passenger.name} quiere viajar desde {origin} hasta {destination}")
        return ride

    def assign_driver(self, ride, driver):
        if not driver.is_working:  # Solo si NO está trabajando
            ride.driver = driver
            ride.status = "En camino"
            driver.set_working_status(True)
            driver.set_is_working(True)
            self.view.show_message(f"{driver.name} aceptó tu viaje.")
        else:
            self.view.show_message(f"{driver.name} no está disponible.")

    def complete_ride(self, ride):
        ride.status = "Completado"
        ride.driver.available = True
        self.view.show_message(f"El viaje con {ride.passenger.name} se completo")

#Validaciones Rocio
    def validate_passenger_data(self, name, dni, email, phone):
        if not self.is_valid_name(name):
            self.view.show_message("❌ El nombre no puede estar vacío.")
            return False
        if not self.is_valid_dni(dni):
            self.view.show_message("❌ El DNI debe contener solo números y tener 7 u 8 dígitos.")
            return False
        if not self.is_valid_email(email):
            self.view.show_message("❌ El email no es válido.")
            return False
        if not self.is_valid_phone(phone):
            self.view.show_message("❌ El teléfono debe tener al menos 10 dígitos.")
            return False
        return True

    def validate_driver_data(self, name, dni, email, phone, license_plate):
        if not self.validate_passenger_data(name, dni, email, phone):
            return False
        if not license_plate.strip():
            self.view.show_message("❌ La patente no puede estar vacía.")
            return False
        return True

    def is_valid_name(self, name):
        return bool(name.strip())

    def is_valid_dni(self, dni):
        return dni.isdigit() and 7 <= len(dni) <= 8

    def is_valid_email(self, email):
        return "@" in email and "." in email and len(email) >= 5

    def is_valid_phone(self, phone):
        return phone.isdigit() and len(phone) >= 10  
        self.view.show_message(f"El viaje con {ride.passenger.name} se completó")
        ride.driver.set_is_working(False)
