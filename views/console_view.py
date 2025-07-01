class ConsoleView:
    def show_message(self, message):
        print(message)

    def get_ride_data(self):
        origin = input("Origen: ")
        destination = input("Destino: ")
        return origin, destination
