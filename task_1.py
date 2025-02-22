import logging
from abc import ABC, abstractmethod

# Налаштування логування
logging.basicConfig(level=logging.INFO)


# Абстрактний базовий клас для транспортних засобів
class Vehicle(ABC):
    def __init__(self, make: str, model: str):
        self.make = make
        self.model = model

    @abstractmethod
    def start_engine(self):
        pass


# Клас Car
class Car(Vehicle):
    def start_engine(self):
        logging.info(f"{self.make} {self.model}: Двигун запущено")


# Клас Motorcycle
class Motorcycle(Vehicle):
    def start_engine(self):
        logging.info(f"{self.make} {self.model}: Мотор заведено")


# Абстрактна фабрика для створення транспортних засобів
class VehicleFactory(ABC):
    @abstractmethod
    def create_car(self) -> Car:
        pass

    @abstractmethod
    def create_motorcycle(self) -> Motorcycle:
        pass


# Фабрика для США
class USVehicleFactory(VehicleFactory):
    def create_car(self) -> Car:
        return Car("Ford", "Mustang (US Spec)")

    def create_motorcycle(self) -> Motorcycle:
        return Motorcycle("Harley-Davidson", "Sportster (US Spec)")


# Фабрика для ЄС
class EUVehicleFactory(VehicleFactory):
    def create_car(self) -> Car:
        return Car("Volkswagen", "Golf (EU Spec)")

    def create_motorcycle(self) -> Motorcycle:
        return Motorcycle("BMW", "R1200 (EU Spec)")


# Використання фабрик
def main():
    us_factory = USVehicleFactory()
    eu_factory = EUVehicleFactory()

    # Створення транспортних засобів для США
    us_car = us_factory.create_car()
    us_motorcycle = us_factory.create_motorcycle()
    us_car.start_engine()
    us_motorcycle.start_engine()

    # Створення транспортних засобів для ЄС
    eu_car = eu_factory.create_car()
    eu_motorcycle = eu_factory.create_motorcycle()
    eu_car.start_engine()
    eu_motorcycle.start_engine()


if __name__ == "__main__":
    main()
