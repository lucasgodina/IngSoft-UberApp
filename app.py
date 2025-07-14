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
        passenger_name = view.get_passenger_name()
        passenger_name = passenger_name.title()
        if controller.is_valid_name(passenger_name):
            break
        view.show_message("❌ El nombre no puede estar vacío.")

    # Pedir DNI del pasajero
    while True:
        passenger_dni = view.get_passenger_dni()
        if controller.is_valid_dni(passenger_dni):
            break
        view.show_message("❌ El DNI debe contener solo números y tener 7 u 8 dígitos.")

    # Pedir email del pasajero
    while True:
        passenger_email = view.get_passenger_email()
        if controller.is_valid_email(passenger_email):
            break
        view.show_message("❌ El email no es válido.")

    # Pedir teléfono del pasajero
    while True:
        passenger_phone = view.get_passenger_phone()
        if controller.is_valid_phone(passenger_phone):
            break
        view.show_message("❌ El teléfono debe tener al menos 10 dígitos.")

    view.show_message("✅ Datos del pasajero válidos.")
    passenger = Passenger(
        passenger_name, passenger_dni, passenger_email, passenger_phone
    )

    # 2. Pedir datos del chofer
    view.show_message("------ Pantalla del Chofer ------")
    view.show_message("Ingresá tus datos: ")

    # Pedir nombre del chofer
    while True:
        driver_name = view.get_driver_name()
        driver_name = driver_name.title()
        if controller.is_valid_name(driver_name):
            break
        view.show_message("❌ El nombre no puede estar vacío.")

    # Pedir DNI del chofer
    while True:
        driver_dni = view.get_driver_dni()
        if controller.is_valid_dni(driver_dni):
            break
        view.show_message("❌ El DNI debe contener solo números y tener 7 u 8 dígitos.")

    # Pedir email del chofer
    while True:
        driver_email = view.get_driver_email()
        if controller.is_valid_email(driver_email):
            break
        view.show_message("❌ El email no es válido.")

    # Pedir teléfono del chofer
    while True:
        driver_phone = view.get_driver_phone()
        if controller.is_valid_phone(driver_phone):
            break
        view.show_message("❌ El teléfono debe tener al menos 10 dígitos.")

    # Pedir patente del chofer
    while True:
        license_plate = view.get_driver_license_plate()
        if license_plate.strip():
            break
        view.show_message("❌ La patente no puede estar vacía.")

    view.show_message("✅ Datos del chofer válidos.")
    driver = Driver(driver_name, driver_dni, driver_email, driver_phone, license_plate)

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
        approved = input(f"¿Querés realizar el viaje a {destination}? (s/n): ").lower()
        if approved in ["s", "n"]:
            break
        view.show_message("❌ Por favor ingresá 's' para sí o 'n' para no.")

    if approved == "s":
        view.show_message(
            "¡Gracias por tomar el viaje y llevar a nuestro pasajero! 🚗💨"
        )
        # Crear viaje y asignar chofer
        ride = controller.request_ride(passenger, origin, destination)
        view.show_message("------ Pantalla del Pasajero ------")
        controller.assign_driver(ride, driver)
        view.show_message(
            f"El viaje ha sido asignado a {driver.name} con patente {driver.license_plate}."
        )

        # Calcular precio del viaje
        view.show_message("Vamos a calcular el precio del viaje...")
        cantidad_millage = view.pedir_kilometros()
        precio_viaje = controller.calcular_viaje(cantidad_millage)
        view.show_message(f"💰 El precio del viaje es: ${precio_viaje}")

        # Finalizar viaje
        # Demostrar el seguimiento de ubicación
        view.show_message("\n" + "=" * 60)
        view.show_message("🎯 DEMOSTRACIÓN DE SEGUIMIENTO DE UBICACIÓN")
        view.show_message("=" * 60)

        input("Presiona Enter para ver las actualizaciones de ubicación...")

        # El seguimiento ya se inició automáticamente en assign_driver
        # Ahora simulamos ver las actualizaciones
        controller.simulate_location_updates(ride)

        view.show_message("\n" + "=" * 60)
        view.show_message("🏁 FIN DEL SEGUIMIENTO - LLEGASTE AL DESTINO")
        view.show_message("=" * 60)

        # Demostrar el seguimiento de ubicación
        view.show_message("\n" + "=" * 60)
        view.show_message("🎯 DEMOSTRACIÓN DE SEGUIMIENTO DE UBICACIÓN")
        view.show_message("=" * 60)

        input("Presiona Enter para ver las actualizaciones de ubicación...")

        # El seguimiento ya se inició automáticamente en assign_driver
        # Ahora simulamos ver las actualizaciones
        controller.simulate_location_updates(ride)

        view.show_message("\n" + "=" * 60)
        view.show_message("🏁 FIN DEL SEGUIMIENTO - LLEGASTE AL DESTINO")
        view.show_message("=" * 60)

        input("Presioná enter para finalizar el viaje...")
        view.show_message("------ Pantalla del Chofer ------")
        controller.complete_ride(ride)

        # Calificar al chofer
        view.show_message("------ Pantalla del Pasajero ------")
        driver_rating = view.get_valid_driver_rating(driver.name)
        driver.rate(driver_rating)
        view.show_message("Gracias por calificar al chofer. ¡Hasta la próxima! 👋")

        # Calificar al pasajero
        view.show_message("------ Pantalla del Chofer ------")
        passenger_rating = view.get_valid_passenger_rating(passenger.name)
        passenger.rate(passenger_rating)
        view.show_message("Gracias por calificar al pasajero. ¡Hasta la próxima! 👋")

    else:
        # Si el chofer no acepta el viaje
        view.show_message(
            f"Es una lástima que no puedas llevar a {passenger.name}. ¡Hasta luego! 👋"
        )
        view.show_message("------ Pantalla del Pasajero ------")
        view.show_message("No hay vehículos disponibles.")


if __name__ == "__main__":
    main()
