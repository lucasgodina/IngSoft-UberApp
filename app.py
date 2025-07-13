from models.passenger import Passenger
from models.driver import Driver
from views.console_view import ConsoleView
from controllers.ride_controller import RideController

def main():
    # Crear vista y controlador
    view = ConsoleView()
    controller = RideController(view)

    # 1. Pedir datos del pasajero desde consola
    view.show_message("📥 Ingresá los datos del pasajero:")
    name, dni, email, phone = view.get_passenger_data()
    passenger = Passenger(name, dni, email, phone)

    # 2. Pedir datos del chofer desde consola
    view.show_message("Ingresá los datos del chofer:")
    name, dni, email, phone, patente = view.get_driver_data()
    driver = Driver(name, dni, email, phone, patente)

    zona = input("Definir zona de trabajo del chofer: ")
   
    print(f"Zona de trabajo del chofer {driver.name} establecida: {zona}")
   
    # 3. Pedir origen y destino
    view.show_message(f"Hola {passenger.name}, ¿desde dónde querés viajar?")
    origin, destination = view.get_ride_data()

    aproved = input(f"¿Querés realizar el viaje a {destination}? (s/n): ")
    if aproved.lower() == 's': 
        view.show_message("¡Gracias por tomar el viaje y llevar a nuestro pasajero! 🚗💨")
    else:
        view.show_message(f"Es una lastima que no puedas que no puedas llva a {passenger.name}  ¡Hasta luego! 👋")
    # 4. Crear viaje, asignar chofer y completarlo
    ride = controller.request_ride(passenger, origin, destination)
    controller.assign_driver(ride, driver)
         
    count_millage = view.pedir_kilometros()
    total_millage = controller.calcular_viaje(count_millage)
    view.show_message(f"El costo del viaje es: {total_millage} pesos")
    
    input("Presioná enter para finalizar el viaje...")
    controller.complete_ride(ride)



    



if __name__ == "__main__":
    main()
