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
        license_plate = input("Patente: ")
        return name, dni, email, phone, license_plate
    

    def get_passenger_name(self):
        return input("Nombre del pasajero: ")

    def get_passenger_dni(self):
        return input("DNI: ")

    def get_passenger_email(self):
        return input("Email: ")

    def get_passenger_phone(self):
        return input("Teléfono: ")

    def get_driver_name(self):
        return input("Nombre del chofer: ")

    def get_driver_dni(self):
        return input("DNI: ")

    def get_driver_email(self):
        return input("Email: ")

    def get_driver_phone(self):
        return input("Teléfono: ")

    def get_driver_license_plate(self):
        return input("Patente: ")
    def pedir_kilometros(self):
        return int(input("Ingrese la cantidad de kilómetros del viaje: "))
    
    def get_valid_driver_rating(self, driver_name):
        while True:
            try:
                rating = int(input(f"¿Con cuántas estrellas calificás al chofer {driver_name}? (1-5): "))
                if 1 <= rating <= 5:
                    return rating
                else:
                    self.show_message("Por favor, ingresá un número entre 1 y 5.")
            except ValueError:
                self.show_message("Entrada inválida. Ingresá un número.")

    def get_valid_passenger_rating(self, passenger_name):
        while True:
            try:
                rating = int(input(f"¿Con cuántas estrellas calificás al pasajero {passenger_name}? (1-5): "))
                if 1 <= rating <= 5:
                    return rating
                else:
                    self.show_message("Por favor, ingresá un número entre 1 y 5.")
            except ValueError:
                self.show_message("Entrada inválida. Ingresá un número.")