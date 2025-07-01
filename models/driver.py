from models.user import User

class Driver(User):
    def __init__(self, name):
        super().__init__(name)
        self.available = True #Por ahora esta dispo
