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
<<<<<<< HEAD
        patente = input("Patente: ")
        return name, dni, email, phone, patente
    
    def pedir_kilometros(self):
        while True:
            try:
                millage = float(input("Ingrese la cantidad de kilómetros recorridos: "))
                if millage > 0:
                    return millage
                else:
                    print("Por favor, ingrese un valor positivo.")
            except ValueError:
                print("Por favor, ingrese un número válido.")
        
           
=======
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
>>>>>>> main
