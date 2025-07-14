class Ride:
    def __init__(self, passenger, origin, destination, mileage=0):
        self.passenger = passenger
        self.origin = origin
        self.destination = destination
        self.mileage = mileage
        self.driver = None
        self.status = "Pendiente"
