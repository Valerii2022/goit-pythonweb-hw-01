from abc import ABC, abstractmethod

# Абстрактний клас транспортного засобу
class Vehicle(ABC):
    def __init__(self, make, model, region):
        self.make = make
        self.model = model
        self.region = region
    
    @abstractmethod
    def start_engine(self):
        pass

# Класи Car і Motorcycle успадковуються від Vehicle
class Car(Vehicle):
    def start_engine(self):
        print(f"{self.make} {self.model} ({self.region} Spec): Двигун запущено")

class Motorcycle(Vehicle):
    def start_engine(self):
        print(f"{self.make} {self.model} ({self.region} Spec): Мотор заведено")

# Абстрактна фабрика транспортних засобів
class VehicleFactory(ABC):
    @abstractmethod
    def create_car(self, make, model):
        pass

    @abstractmethod
    def create_motorcycle(self, make, model):
        pass

# Фабрика для США
class USVehicleFactory(VehicleFactory):
    def create_car(self, make, model):
        return Car(make, model, "US")
    
    def create_motorcycle(self, make, model):
        return Motorcycle(make, model, "US")

# Фабрика для ЄС
class EUVehicleFactory(VehicleFactory):
    def create_car(self, make, model):
        return Car(make, model, "EU")
    
    def create_motorcycle(self, make, model):
        return Motorcycle(make, model, "EU")

# Використання фабрики
us_factory = USVehicleFactory()
eu_factory = EUVehicleFactory()

vehicle1 = us_factory.create_car("Ford", "Mustang")
vehicle1.start_engine()

vehicle2 = eu_factory.create_motorcycle("BMW", "R1250GS")
vehicle2.start_engine()
