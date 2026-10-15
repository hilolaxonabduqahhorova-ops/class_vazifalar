
from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, brand, model, speed):
        self.__brand = brand
        self.__model = model
        self.__speed = speed

    @property
    def brand(self):
        return self.__brand

    @property
    def model(self):
        return self.__model

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, value):
        if value < 0:
            raise ValueError("Tezlik manfiy bo'lishi mumkin emas!")
        self.__speed = value

    @abstractmethod
    def vehicle_type(self):
        pass

    def accelerate(self, amount):
        if amount <= 0:
            raise ValueError("Tezlik oshishi musbat bo'lishi kerak!")
        self.speed += amount

    def brake(self, amount):
        if amount <= 0:
            raise ValueError("Tezlik kamayishi musbat bo'lishi kerak!")
        self.speed = max(0, self.speed - amount)

    def __str__(self):
        return (
            f"{self.__brand} {self.__model}, "
            f"tezlik: {self.__speed} km/soat"
        )

    def __repr__(self):
        return (
            f"{self.__class__.__name__}"
            f"({self.__brand!r}, {self.__model!r}, "
            f"{self.__speed!r})"
        )

    def __bool__(self):
        return self.__speed > 0

    def __eq__(self, other):
        if not isinstance(other, Vehicle):
            return NotImplemented
        return self.speed == other.speed

    def __lt__(self, other):
        if not isinstance(other, Vehicle):
            return NotImplemented
        return self.speed < other.speed

    def __gt__(self, other):
        if not isinstance(other, Vehicle):
            return NotImplemented
        return self.speed > other.speed


class Car(Vehicle):
    def __init__(self, brand, model, speed, doors):
        super().__init__(brand, model, speed)
        self.doors = doors

    def vehicle_type(self):
        return "Yengil avtomobil"


class Motorcycle(Vehicle):
    def __init__(self, brand, model, speed, has_sidecar=False):
        super().__init__(brand, model, speed)
        self.has_sidecar = has_sidecar

    def vehicle_type(self):
        return "Mototsikl"


class Bus(Vehicle):
    def __init__(self, brand, model, speed, capacity):
        super().__init__(brand, model, speed)
        self.capacity = capacity

    def vehicle_type(self):
        return "Avtobus"


# Sinab ko'rish
car = Car("Chevrolet", "Cobalt", 120, 4)
motorcycle = Motorcycle("Yamaha", "R1", 180)
bus = Bus("Mercedes", "Sprinter", 90, 20)

transportlar = [car, motorcycle, bus]

for transport in transportlar:
    print(transport)
    print("Turi:", transport.vehicle_type())
    print("Harakatdami?", bool(transport))
    print()

car.accelerate(20)
bus.brake(15)

print("Mashina yangi tezligi:", car.speed)
print("Avtobus yangi tezligi:", bus.speed)

print("Mototsikl mashinadan tezmi?", motorcycle > car)
print("Mashina avtobusdan tezmi?", car > bus)

print(repr(car))
