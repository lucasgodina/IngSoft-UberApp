import time
import threading
from services.location_service import LocationService


class BackendServer:
    """Servidor backend simulado que maneja el seguimiento de ubicación"""

    def __init__(self):
        self.location_service = LocationService()
        self.tracking_active = {}  # Control de seguimiento por conductor

    def request_driver_location(self, driver_id):
        """Solicita la ubicación del conductor al GPS"""
        print(f"🔄 ServidorBackend: Solicitando ubicación del conductor {driver_id}")
        location = self.location_service.get_gps_location(driver_id)
        return location

    def send_location_to_driver_app(self, driver_id, location):
        """Simula envío de ubicación a la AppConductor"""
        print(f"📱 Enviando ubicación actual a AppConductor {driver_id}")
        formatted = self.location_service.format_location(location)
        print(f"   → {formatted}")
        return True

    def store_and_confirm_location(self, driver_id, location):
        """Almacena la ubicación y simula confirmación"""
        self.location_service.store_driver_location(driver_id, location)
        print(f"✅ Confirmación: Ubicación recibida del conductor {driver_id}")
        return True

    def notify_new_location_available(self, passenger_id, driver_id):
        """Notifica al pasajero que hay nueva ubicación disponible"""
        print(f"📢 Notificando nueva ubicación disponible a pasajero {passenger_id}")
        return True

    def send_location_to_passenger_app(self, passenger_id, driver_id):
        """Envía la ubicación del conductor a la AppPasajero"""
        stored_location = self.location_service.get_stored_location(driver_id)
        if stored_location:
            print(f"📱 Enviando ubicación del conductor a AppPasajero {passenger_id}")
            formatted = self.location_service.format_location(stored_location)
            print(f"   → {formatted}")
            return True
        return False

    def start_tracking_session(self, driver_id, passenger_id):
        """Inicia una sesión de seguimiento"""
        print(
            f"🎯 Iniciando seguimiento: Conductor {driver_id} → Pasajero {passenger_id}"
        )
        self.tracking_active[driver_id] = {"passenger_id": passenger_id, "active": True}

        # Simula el primer ciclo del diagrama
        self._simulate_tracking_cycle(driver_id, passenger_id)
        return True

    def stop_tracking_session(self, driver_id):
        """Detiene la sesión de seguimiento"""
        if driver_id in self.tracking_active:
            self.tracking_active[driver_id]["active"] = False
            print(f"⏹️ Seguimiento detenido para conductor {driver_id}")

    def start_location_updates(self, driver_id, passenger_id):
        """Inicia las actualizaciones de ubicación continuas"""
        print(f"🎯 Iniciando actualizaciones de ubicación para conductor {driver_id}")
        self.tracking_active[driver_id] = {"passenger_id": passenger_id, "active": True}
        return True

    def update_driver_location(self, driver_id, location):
        """Actualiza la ubicación del conductor en el sistema"""
        print(f"📍 Actualizando ubicación del conductor {driver_id}: {location}")
        # Simular almacenamiento de ubicación
        location_data = {
            "location": location,
            "timestamp": time.time(),
            "driver_id": driver_id,
        }
        self.location_service.store_driver_location(driver_id, location_data)
        return True

    def stop_location_updates(self, driver_id):
        """Detiene las actualizaciones de ubicación"""
        if driver_id in self.tracking_active:
            self.tracking_active[driver_id]["active"] = False
            print(
                f"⏹️ Actualizaciones de ubicación detenidas para conductor {driver_id}"
            )
        return True

    def _simulate_tracking_cycle(self, driver_id, passenger_id):
        """Simula el ciclo de seguimiento del diagrama de secuencia"""
        if (
            driver_id not in self.tracking_active
            or not self.tracking_active[driver_id]["active"]
        ):
            return

        print("\n" + "=" * 50)
        print("🔄 CICLO DE ACTUALIZACIÓN DE UBICACIÓN")
        print("=" * 50)

        # 1. Solicitar ubicación actual del GPS
        location = self.request_driver_location(driver_id)

        # 2. Enviar ubicación actual del conductor a AppConductor
        self.send_location_to_driver_app(driver_id, location)

        # 3. Enviar ubicación del conductor al servidor
        print(f"📤 Conductor {driver_id}: Enviando ubicación al servidor")

        # 4. Almacenar/actualizar ubicación + confirmar
        self.store_and_confirm_location(driver_id, location)

        # 5. Notificar nueva ubicación disponible al pasajero
        self.notify_new_location_available(passenger_id, driver_id)

        # 6. Solicitar ubicación del conductor para el pasajero
        print(f"🔄 ServidorBackend: Solicitando ubicación del conductor para pasajero")

        # 7. Enviar última ubicación conocida al pasajero
        self.send_location_to_passenger_app(passenger_id, driver_id)

        print("=" * 50)
        print("✅ CICLO COMPLETADO")
        print("=" * 50 + "\n")
