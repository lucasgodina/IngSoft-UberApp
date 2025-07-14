from abc import ABC, abstractmethod #de esta forma podemos crear una clase abstracta, que no se puede instanciar, pero si heredar.
class User(ABC):
    def __init__(self, name, dni, email, number_phone):
        self._name = name
        self._dni = dni
        self._email = email
        self._number_phone = number_phone

    @property
    def name(self):
        return self._name
    
    @property
    def dni(self):
        return self._dni

    @property
    def email(self):
        return self._email

    @property
    def number_phone(self):
        return self._number_phone    
    
    @abstractmethod
    def rate(self, rating):
        pass