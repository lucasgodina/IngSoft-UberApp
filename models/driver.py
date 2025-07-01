from models.user import User

class Driver(User):
    def __init__(self, name, dni, email, number_phone, patente):
        super().__init__(name, dni, email, number_phone)
        self._patente = patente
        self._esta_trabajando = False

    @property
    def patente(self):
        return self._patente

    @patente.setter
    def patente(self, valor):
        self._patente = valor

    @property
    def esta_trabajando(self):
        return self._esta_trabajando

    #  modificar estel estado si se encuentra trabajando o no, 
    
    def definir_esta_trabajando(self, estado: bool):
        self._esta_trabajando = estado

    def calificar(self):
        # hereda del metodo abstracto
        print("Calificando chofer...")

    def definir_zona_trabajo(self, zona: str):
        # defino la zona donde se encuentra trabajando
        print(f"Zona de trabajo establecida: {zona}")
