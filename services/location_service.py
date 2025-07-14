import random
import time


class LocationService:
    """Servicio simulado de ubicación GPS"""

    def __init__(self):
        # Simulamos una base de datos en memoria para ubicaciones
        self.driver_locations = {}

    def get_gps_location(self, driver_id):
        """Simula obtener ubicación del GPS del dispositivo del conductor"""
        # Generamos coordenadas aleatorias (simulando Buenos Aires)
        lat = round(random.uniform(-34.7, -34.5), 6)
        lng = round(random.uniform(-58.5, -58.3), 6)

        location = {
            "latitude": lat,
            "longitude": lng,
            "timestamp": time.time(),
            "driver_id": driver_id,
        }

        print(f"📍 GPS - Ubicación obtenida: Lat {lat}, Lng {lng}")
        return location

    def store_driver_location(self, driver_id, location_data):
        """Almacena/actualiza la ubicación del conductor"""
        self.driver_locations[driver_id] = location_data
        print(f"💾 Ubicación almacenada para conductor {driver_id}")

    def get_stored_location(self, driver_id):
        """Obtiene la última ubicación almacenada del conductor"""
        return self.driver_locations.get(driver_id, None)

    def format_location(self, location_data):
        """Formatea la ubicación para mostrar"""
        if not location_data:
            return "Ubicación no disponible"

        # Si location_data es un string simple, devolverlo directamente
        if isinstance(location_data, str):
            return location_data

        # Si es un diccionario con coordenadas
        if isinstance(location_data, dict):
            if "latitude" in location_data and "longitude" in location_data:
                return f"📍 Lat: {location_data['latitude']}, Lng: {location_data['longitude']}"
            elif "location" in location_data:
                return location_data["location"]

        return str(location_data)
