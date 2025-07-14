from models.passenger import Passenger
from models.driver import Driver
from views.console_view import ConsoleView
from controllers.ride_controller import RideController


def main():
    # Crear vista y controlador
    view = ConsoleView()
    controller = RideController(view)

    # 1. Pedir datos del pasajero
    view.show_message("📥 Ingresá los datos del pasajero:")

    # Pedir nombre del pasajero
    while True:
        name = view.get_passenger_name()
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
    view.show_message("🚗 Ingresá los datos del chofer:")

    # Pedir nombre del chofer
    while True:
        name = view.get_driver_name()
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
        view.show_message("❌ La zona de trabajo no puede estar vacía.")

    # 4. Pedir origen y destino
    view.show_message(f"Hola {passenger.name}, ¿desde dónde querés viajar?")
    while True:
        origin, destination = view.get_ride_data()
        if origin.strip() and destination.strip():
            break
        view.show_message("❌ El origen y el destino no pueden estar vacíos.")

    # 5. Confirmar viaje
    while True:
        approved = input("¿Querés realizar el viaje? (s/n): ").lower()
        if approved in ["s", "n"]:
            break
        view.show_message("❌ Por favor ingresá 's' para sí o 'n' para no.")

    if approved == "s":
        view.show_message(
            "¡Gracias por tomar el viaje y llevar a nuestro pasajero! 🚗💨"
        )

        # 6. Crear, asignar y completar el viaje
        ride = controller.request_ride(passenger, origin, destination)
        controller.assign_driver(ride, driver)

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
        controller.complete_ride(ride)
        view.show_message("✅ ¡Viaje completado exitosamente!")
    else:
        view.show_message(
            f"Es una lástima que no puedas llevar a {passenger.name}. ¡Hasta luego! 👋"
        )


if __name__ == "__main__":
    main()
