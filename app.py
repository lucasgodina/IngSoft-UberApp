from models.passenger import Passenger
from models.driver import Driver
from views.console_view import ConsoleView
from controllers.ride_controller import RideController

def main():
    # Crear vista y controlador
    view = ConsoleView()
    controller = RideController(view)
    
    # 0. Mostrar mensaje de bienvenida
    view.show_message("******Bienvenido a la App de Viajes 🚗******")
    
    # 1. Pedir datos del pasajero
    view.show_message("------ Pantalla del Pasajero ------")
    view.show_message("📥 Ingresá tus datos: ")
    
    # Pedir nombre del pasajero
    while True:
        name = view.get_passenger_name()
        name = name.title() 
        if controller.is_valid_name(name):
            break
        view.show_message("❌ El nombre no puede estar vacío.")
    
    # Pedir DNI del pasajero
    while True:
        dni = view.get_passenger_dni()
        if controller.is_valid_dni(dni):
            break
        view.show_message("❌ El DNI debe contener solo números y tener 7 u 8 dígitos.")
    
    # Pedir email del pasajero
    while True:
        email = view.get_passenger_email()
        if controller.is_valid_email(email):
            break
        view.show_message("❌ El email no es válido.")
    
    # Pedir teléfono del pasajero
    while True:
        phone = view.get_passenger_phone()
        if controller.is_valid_phone(phone):
            break
        view.show_message("❌ El teléfono debe tener al menos 10 dígitos.")
    
    view.show_message("✅ Datos del pasajero válidos.")
    passenger = Passenger(name, dni, email, phone)
    


    # 2. Pedir datos del chofer
    view.show_message("------ Pantalla del Chofer ------")
    view.show_message("Ingresá tus datos: ")
    
    # Pedir nombre del chofer
    while True:
        name = view.get_driver_name()
        name = name.title()  
        if controller.is_valid_name(name):
            break
        view.show_message("❌ El nombre no puede estar vacío.")
    
    # Pedir DNI del chofer
    while True:
        dni = view.get_driver_dni()
        if controller.is_valid_dni(dni):
            break
        view.show_message("❌ El DNI debe contener solo números y tener 7 u 8 dígitos.")
    
    # Pedir email del chofer
    while True:
        email = view.get_driver_email()
        if controller.is_valid_email(email):
            break
        view.show_message("❌ El email no es válido.")
    
    # Pedir teléfono del chofer
    while True:
        phone = view.get_driver_phone()
        if controller.is_valid_phone(phone):
            break
        view.show_message("❌ El teléfono debe tener al menos 10 dígitos.")
    
    # Pedir patente del chofer
    while True:

        license_plate = view.get_driver_license_plate()
        if license_plate.strip():
            break
        view.show_message("❌ La patente no puede estar vacía.")
    
    view.show_message("✅ Datos del chofer válidos.")
    driver = Driver(name, dni, email, phone, license_plate)

    # 3. Definir zona de trabajo
    while True:
        zone = input("Definir zona de trabajo del chofer: ")
        if zone.strip():
            driver.set_work_zone(zone)
            break
        else:
            view.show_message("❌ La zona de trabajo no puede estar vacía.")

    # 4. Pedir origen y destino
    view.show_message("------ Pantalla del Pasajero ------")
    view.show_message(f"Hola {passenger.name}, ¿desde dónde querés viajar?")
    while True:
        origin, destination = view.get_ride_data()
        if origin.strip() and destination.strip():
            break
        view.show_message("❌ El origen y el destino no pueden estar vacíos.")

    # 5. Confirmar viaje
    view.show_message("------ Pantalla del Chofer ------")
    while True:
        approved = input("¿Querés realizar el viaje? (s/n): ").lower()
        if approved in ['s', 'n']:
            break
        view.show_message("❌ Por favor ingresá 's' para sí o 'n' para no.")
    
    if approved == 's':
        view.show_message("¡Gracias por tomar el viaje y llevar a nuestro pasajero! 🚗💨")
        # 4. Crear viaje, asignar chofer y completarlo
        ride = controller.request_ride(passenger, origin, destination)
        view.show_message("------ Pantalla del Pasajero ------")
        controller.assign_driver(ride, driver)
        view.show_message(f"El viaje ha sido asignado a {driver.name} con patente {driver.license_plate}.")
        input("Presioná enter para finalizar el viaje...")
        view.show_message("------ Pantalla del Chofer ------")
        controller.complete_ride(ride)
        # Calificar al chofer
        view.show_message("------ Pantalla del Pasajero ------")
        driver_rating = view.get_valid_driver_rating(driver.name)
        driver.rate(driver_rating)
        view.show_message("Gracias por calificar al chofer del viaje. ¡Hasta la próxima! 👋")
        view.show_message("Se ha finalizado el viaje exitosamente. 🚗💨")
        # Calificar al pasajero
        view.show_message("------ Pantalla del Chofer ------")
        passenger_rating = view.get_valid_passenger_rating(passenger.name)
        passenger.rate(passenger_rating)
        view.show_message("Gracias por calificar al pasajero del viaje. ¡Hasta la próxima! 👋")
        view.show_message("Se ha finalizado el viaje exitosamente. 🚗💨")
    else:
        # Si el chofer no puede llevar al pasajero
        view.show_message(f"Es una lástima que no puedas llevar a {passenger.name}  ¡Hasta luego! 👋")
        view.show_message("------ Pantalla del Pasajero ------")
        view.show_message("No hay vehiculos disponibles.")
        
if __name__ == "__main__":
    main()