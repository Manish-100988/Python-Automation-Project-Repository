from abc import ABC, abstractmethod

# ----------------------- 1. ENCAPSULATION -------------------------
# Using private variables and controlled access with methods

class Human:
    def __init__(self, name, aadhar_id, age, gender):
        self.__name = name
        self.__aadhar_id = aadhar_id
        self.__age = age
        self.__gender = gender

    def walk(self):
        print(f"{self.__name} is walking.")

    def talk(self):
        print(f"{self.__name} is talking.")

    def pay_taxes(self):
        print(f"{self.__name} has paid taxes.")

    def get_identity(self):
        return self.__name, self.__aadhar_id


# ----------------------- 2. ABSTRACTION -------------------------
# Abstract base for system actors

class TrafficEntity(ABC):
    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def stop(self):
        pass


# ----------------------- 3. INHERITANCE -------------------------
# Car inherits from TrafficEntity

class Car(TrafficEntity):
    def __init__(self, plate_number, color, speed, fuel_level):
        self.plate_number = plate_number
        self.color = color
        self.speed = speed
        self.fuel_level = fuel_level

    def move(self):
        print(f"Car {self.plate_number} is driving at {self.speed} km/h.")

    def stop(self):
        print(f"Car {self.plate_number} has stopped.")

    def honk(self):
        print("Beep beep!")


# TrafficLight is not abstracted but encapsulates state
class TrafficLight:
    def __init__(self, location, color):
        self.location = location
        self.__color = color

    def change_color(self, new_color):
        self.__color = new_color
        print(f"Traffic light at {self.location} changed to {self.__color}.")

    def blink(self):
        print(f"Traffic light at {self.location} is blinking.")


# Building class with encapsulated data
class Building:
    def __init__(self, building_id, address, floors, building_type):
        self.__building_id = building_id
        self.address = address
        self.floors = floors
        self.building_type = building_type

    def open(self):
        print(f"Building {self.address} is now open.")

    def close(self):
        print(f"Building {self.address} is now closed.")

    def turn_lights_on(self):
        print(f"Lights are ON in building {self.address}.")


# Abstract class for public servant behavior
class Authority(ABC):
    @abstractmethod
    def patrol(self):
        pass

    @abstractmethod
    def arrest(self):
        pass


# ----------------------- 3. INHERITANCE CONTINUED -------------------------
# Police inherits from Authority
class Police(Authority):
    def __init__(self, badge_id, area, status):
        self.badge_id = badge_id
        self.area = area
        self.status = status

    def patrol(self):
        print(f"Police officer {self.badge_id} is patrolling in {self.area}.")

    def arrest(self):
        print(f"Police officer {self.badge_id} made an arrest.")

    def report_crime(self):
        print(f"Crime reported by officer {self.badge_id}.")


# ----------------------- 4. POLYMORPHISM -------------------------
# Unified interface for interaction

def system_start(entity):
    if hasattr(entity, 'move'):
        entity.move()
    if hasattr(entity, 'walk'):
        entity.walk()

def system_stop(entity):
    if hasattr(entity, 'stop'):
        entity.stop()
    if hasattr(entity, 'pay_taxes'):
        entity.pay_taxes()


# ----------------------- SYSTEM SIMULATION -------------------------

# Objects
john = Human("John", "1234-5678", 30, "Male")
car1 = Car("MH12AB1234", "Red", 60, 70)
signal = TrafficLight("Main Square", "Red")
mall = Building("B101", "MG Road", 5, "Mall")
officer = Police("P007", "Sector 9", "On Duty")

# Actions
print("\n--- System Boot ---")
system_start(john)
system_start(car1)

signal.change_color("Green")
mall.open()
officer.patrol()

print("\n--- System Shutdown ---")
system_stop(car1)
system_stop(john)
mall.close()
officer.report_crime()
