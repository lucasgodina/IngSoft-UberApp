from models.user import User


class Driver(User):
    def __init__(self, name, dni, email, number_phone, license_plate):
        super().__init__(name, dni, email, number_phone)
        self._license_plate = license_plate
        self._is_working = False
        self._work_area = None
        self.ratings = []

    @property
    def license_plate(self):
        return self._license_plate

    def set_license_plate(self, value):
        self._license_plate = value

    def set_working_status(self, status: bool):
        self._is_working = status

    def set_work_zone(self, zone: str):
        # defino la zona donde se encuentra trabajando
        print(f"Zona de trabajo establecida: {zone}")

    @property
    def is_working(self):
        return self._is_working

    def set_is_working(self, state: bool):
        self._is_working = state

    @property
    def work_area(self):
        return self._work_area

    def set_work_area(self, area: str):
        self._work_area = area

    def rate(self, rating):
        self.ratings.append(rating)
        print(f"El chofer {self.name} ha sido calificado con {rating} estrellas.")

    def get_driver_id(self):
        """Retorna un ID único para el conductor"""
        return f"driver_{self.dni}"

    @property
    def driver_id(self):
        """Propiedad para acceder al ID del conductor"""
        return self.get_driver_id()

    def update_location(self, location):
        """Actualiza la ubicación actual del conductor"""
        self._current_location = location
        print(f"🚗 {self.name}: Ubicación actualizada a {location}")

    @property
    def current_location(self):
        """Obtiene la ubicación actual del conductor"""
        return getattr(self, "_current_location", "Ubicación no disponible")
