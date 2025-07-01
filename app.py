from models.passenger import Passenger
from models.driver import Driver
from views.console_view import ConsoleView
from controllers.ride_controller import RideController

def main():
    view = ConsoleView()
    controller = RideController(view)

    passenger = Passenger("Rocio")
    driver = Driver("Fulano")

    origin, destination = view.get_ride_data()
    ride = controller.request_ride(passenger, origin, destination)
    controller.assign_driver(ride, driver)

    input("Presionar enter...")
    controller.complete_ride(ride)

if __name__ == "__main__":
    main()
