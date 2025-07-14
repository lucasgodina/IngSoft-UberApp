from models.ride import Ride
from services.backend_server import BackendServer
import random


class RideController:
    def __init__(self, view):
        self.view = view
        self.rides = []
        self.backend_server = BackendServer()

    def request_ride(self, passenger, origin, destination):
        ride = Ride(passenger, origin, destination)
        self.rides.append(ride)
        self.view.show_message(
            f"{passenger.name} quiere viajar desde {origin} hasta {destination}"
        )
        return ride

    def assign_driver(self, ride, driver):
        if not driver.is_working:  # Solo si NO está trabajando
            ride.driver = driver
            ride.status = "En camino"
            driver.set_working_status(True)
            self.view.show_message(f"{driver.name} aceptó tu viaje.")

            # Iniciar seguimiento de ubicación
            self.start_location_tracking(ride)

        else:
            self.view.show_message(f"{driver.name} no está disponible.")

    def start_location_tracking(self, ride):
        """Inicia el seguimiento de ubicación del conductor"""
        if ride.driver:
            passenger_id = ride.passenger.get_passenger_id()

            # Solicitar ubicación inicial del conductor
            driver_location = self.backend_server.request_driver_location(
                ride.driver.driver_id
            )

            # Notificar al pasajero la ubicación inicial
            self.view.show_message(
                f"🚗 {ride.driver.name} está en camino desde {driver_location}"
            )
            self.view.show_message(f"📍 Ubicación actual: {driver_location}")

            # Iniciar loop de seguimiento continuo
            self.backend_server.start_location_updates(
                ride.driver.driver_id, passenger_id
            )

            # Simular actualizaciones de ubicación
            self.simulate_location_updates(ride)

    def simulate_location_updates(self, ride):
        """Simula actualizaciones de ubicación en tiempo real"""
        if ride.driver:
            # Simular algunas actualizaciones de ubicación
            locations = [
                "Av. Corrientes 1234",
                "Av. Santa Fe 5678",
                "Av. Rivadavia 9101",
                "Cerca de tu ubicación",
            ]

            for location in locations:
                # Actualizar ubicación del conductor
                ride.driver.update_location(location)

                # Enviar al backend
                self.backend_server.update_driver_location(
                    ride.driver.driver_id, location
                )

                # Mostrar al pasajero
                self.view.show_message(
                    f"📍 {ride.driver.name} ahora está en: {location}"
                )

                # Calcular ETA estimado
                eta = self.calculate_eta(location, ride.destination)
                self.view.show_message(f"⏱️ Tiempo estimado de llegada: {eta} minutos")

    def calculate_eta(self, current_location, destination):
        """Calcula ETA estimado (simulado)"""
        # Simulación simple de cálculo de ETA
        import random

        return random.randint(5, 15)

    def stop_location_tracking(self, driver):
        """Detiene el seguimiento de ubicación del conductor"""
        self.backend_server.stop_location_updates(driver.driver_id)
        self.view.show_message(f"📍 Seguimiento de {driver.name} finalizado")

    def complete_ride(self, ride):
        # Detener seguimiento antes de completar
        if ride.driver:
            self.stop_location_tracking(ride.driver)

        ride.status = "CompletadO"
        ride.driver.available = True
        self.view.show_message(f"El viaje con {ride.passenger.name} se completo")

    # Validaciones Rocio
    def validate_passenger_data(self, name, dni, email, phone):
        if not self.is_valid_name(name):
            self.view.show_message("❌ El nombre no puede estar vacío.")
            return False
        if not self.is_valid_dni(dni):
            self.view.show_message(
                "❌ El DNI debe contener solo números y tener 7 u 8 dígitos."
            )
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
