from models.ride import Ride

class RideController:
    def __init__(self, view):
        self.view = view
        self.rides = []

    def request_ride(self, passenger, origin, destination):
        ride = Ride(passenger, origin, destination)
        self.rides.append(ride)
        self.view.show_message(f"{passenger.name} quiere viajar desde {origin} hasta {destination}")
        return ride

    def assign_driver(self, ride, driver):
        if driver.available:
            ride.driver = driver
            ride.status = "En camino"
            driver.available = True
            self.view.show_message(f"{driver.name} acepto tu viaje.")
        else:
            self.view.show_message(f"{driver.name} no hay choferess.")

    def complete_ride(self, ride):
        ride.status = "CompletadO"
        ride.driver.available = True
        self.view.show_message(f"El viaje con {ride.passenger.name} se completo")