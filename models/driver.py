from models.user import User

class Driver(User):
    def __init__(self, name, dni, email, number_phone, license_plate):
        super().__init__(name, dni, email, number_phone)
        self._license_plate = license_plate
        self._is_working = False

    @property
    def license_plate(self):
        return self._license_plate

    @license_plate.setter
    def license_plate(self, value):
        self._license_plate = value

    @property
    def is_working(self):
        return self._is_working

    #  modificar estel estado si se encuentra trabajando o no, 
    
    def set_working_status(self, status: bool):
        self._is_working = status

    def rate(self):
        # hereda del metodo abstracto
        rate = input("Calificar al chofer: ")
        print(f"Calificacion recibida: {rate}")

    def set_work_zone(self, zone: str):
        # defino la zona donde se encuentra trabajando
        print(f"Zona de trabajo establecida: {zone}")
