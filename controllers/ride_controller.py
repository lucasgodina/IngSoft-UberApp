from models.ride import Ride

class RideController:
    def __init__(self, view):
        self.view = view
        self.rides = []
        self.mileage = 0
    def request_ride(self, passenger, origin, destination):
        ride = Ride(passenger, origin, destination)
        self.rides.append(ride)
        self.view.show_message(f"{passenger.name} quiere viajar desde {origin} hasta {destination}")
        return ride

    def assign_driver(self, ride, driver):
        if not driver.esta_trabajando:  # Solo si NO está trabajando
            ride.driver = driver
            ride.status = "En camino"
            driver.definir_esta_trabajando(True)
            self.view.show_message(f"{driver.name} aceptó tu viaje.")
        else:
            self.view.show_message(f"{driver.name} no está disponible.")

    def complete_ride(self, ride):
        ride.status = "CompletadO"
        ride.driver.available = True
        self.view.show_message(f"El viaje con {ride.passenger.name} se completo")
    
    def calcular_viaje(self, mileage):
        valorMileage = 1600
        priceJourney = mileage* valorMileage
        return priceJourney
    
    