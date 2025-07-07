class ConsoleView:
    def show_message(self, message):
        print(message)

    def get_ride_data(self):
        origin = input("Origen: ")
        destination = input("Destino: ")
        return origin, destination

    def get_passenger_data(self):
        name = input("Nombre del pasajero: ")
        dni = input("DNI: ")
        email = input("Email: ")
        phone = input("Teléfono: ")
        return name, dni, email, phone

    def get_driver_data(self):
        name = input("Nombre del chofer: ")
        dni = input("DNI: ")
        email = input("Email: ")
        phone = input("Teléfono: ")
        patente = input("Patente: ")
        return name, dni, email, phone, patente