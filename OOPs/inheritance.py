# 15 10 2026


# parent class(multilevel inheritance)

class Vehicle:
    def __init__ (self, brand, year):
        self.brand = brand
        self.year = year

    def display_info(self):
        return f"{self.year} {self.brand}"


# child class inherits from parent class
class Car(Vehicle):
    def __init__(self, steering, brand, year):
        self.steering = steering
        super().__init__(brand, year)
    def honk(self):
        print(self.steering)
        return "Beep beep!"
class Bike(Vehicle):
    def __init__(self, stand, brand, year):
        self.stand = stand
        super().__init__(brand, year)
    def perforn_stunt(self):
        return "wroom wroom!"

class SportsBike(Bike):
    def __init__(self, cruizeControll, stand, brand, year):
        self.ccontrol = cruizeControll
        super().__init__(stand, brand, year)
    def info(self):
        return "I am a sport bike"

# usage
my_car = Car(True, "Toyota", 2024)
print(my_car.display_info())
print(my_car.honk())

my_bike = Bike(True, "Bajaj", 2024)
print(my_bike.display_info())
print(my_bike.perforn_stunt())

my_sportsBike = SportsBike(True, True, "Kawasaki", 2020)
print(my_sportsBike.display_info())
print(my_sportsBike.perforn_stunt())
print(my_sportsBike.info())