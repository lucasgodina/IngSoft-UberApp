from models.ride import Ride
from services.backend_server import BackendServer
import random


class RideController:
    def __init__(self, view):
        self.view = view
        self.rides = []
        self.backend_server = BackendServer()
        self.ride_etas = {}  # Almacena ETA inicial para cada viaje

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

            # Establecer ETA inicial para este viaje (entre 15-25 minutos)
            initial_eta = random.randint(15, 25)
            self.ride_etas[ride] = {
                "initial_eta": initial_eta,
                "current_eta": initial_eta,
                "updates_count": 0,
            }

            # Solicitar ubicación inicial del conductor
            driver_location = self.backend_server.request_driver_location(
                ride.driver.driver_id
            )

            # Notificar al pasajero la ubicación inicial
            self.view.show_message(
                f"🚗 {ride.driver.name} está en camino desde {driver_location}"
            )
            self.view.show_message(f"📍 Ubicación actual: {driver_location}")
            self.view.show_message(f"⏱️ Tiempo estimado inicial: {initial_eta} minutos")

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

            for i, location in enumerate(locations):
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

                # Calcular ETA estimado que se reduce progresivamente
                eta = self.calculate_eta_progressive(ride, i)
                self.view.show_message(f"⏱️ Tiempo estimado de llegada: {eta} minutos")

    def calculate_eta_progressive(self, ride, update_index):
        """Calcula ETA que se reduce progresivamente con cada actualización"""
        if ride not in self.ride_etas:
            return 5  # Fallback si no hay datos

        eta_data = self.ride_etas[ride]
        initial_eta = eta_data["initial_eta"]
        updates_count = eta_data["updates_count"]

        # Reducir el ETA basado en el número de actualizaciones
        # Cada actualización reduce el tiempo entre 2-5 minutos
        reduction_per_update = random.randint(2, 5)
        total_reduction = (updates_count + update_index + 1) * reduction_per_update

        new_eta = max(1, initial_eta - total_reduction)  # Mínimo 1 minuto

        # Actualizar el contador de actualizaciones
        eta_data["updates_count"] += 1
        eta_data["current_eta"] = new_eta

        return new_eta

    def calculate_eta(self, current_location, destination):
        """Calcula ETA estimado (método legacy, mantenido por compatibilidad)"""
        # Simulación simple de cálculo de ETA
        return random.randint(5, 15)

    def stop_location_tracking(self, driver):
        """Detiene el seguimiento de ubicación del conductor"""
        self.backend_server.stop_location_updates(driver.driver_id)
        self.view.show_message(f"📍 Seguimiento de {driver.name} finalizado")

    def complete_ride(self, ride):
        # Detener seguimiento antes de completar
        if ride.driver:
            self.stop_location_tracking(ride.driver)

        # Limpiar datos de ETA para este viaje
        if ride in self.ride_etas:
            del self.ride_etas[ride]

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
