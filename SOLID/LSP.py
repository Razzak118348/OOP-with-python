# class Vehicle:
#     def start_engine(self):
#         return "Engine started"

# class Car(Vehicle):
#     def start_engine(self):
#         return "Car engine started"

# class Bicycle(Vehicle):
#     def start_engine(self):
#         return "Bicycles don’t have engines!"  # ❌ LSP Violation


# good practice

class Vehicle:
    def move(self):
        return "I can move"

class EngineVehicle(Vehicle):  # New class for vehicles with engines
    def start_engine(self):
        return "Engine started"

class Car(EngineVehicle):
    def start_engine(self):
        return "Car engine started"

class Bicycle(Vehicle):  # No start_engine() here, since bicycles don’t have engines
    def pedal(self):
        return "Pedaling the bicycle"

cycle = Bicycle()
print(cycle.pedal())  # Output: Pedaling the

car = Car()
print(car.start_engine())  # Output: Car engine started