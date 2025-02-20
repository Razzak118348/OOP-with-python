from abc import ABC, abstractmethod

# Abstract Class (High-Level Module)=> denotes as interface
# interface is a bluePrint of class
class Food(ABC):
    @abstractmethod
    def prepare(self):
        pass

# Low-Level Modules (Different Food Items)
class ChickenBiryani(Food):
    def prepare(self):
        return "Chicken Biryani is ready!"

class FishCurry(Food):
    def prepare(self):
        return "Fish Curry is ready!"

class Pasta(Food):
    def prepare(self):
        return "Pasta is ready!"

# High-Level Module (Waiter serves any Food, not just ChickenBiryani)
class Waiter:
    def __init__(self, food: Food):
        self.food = food  # ✅ Depends on  Interface

    def serve(self):
        return self.food.prepare()

# Now Waiter can serve any food
waiter1 = Waiter(ChickenBiryani())
waiter2 = Waiter(FishCurry())
waiter3 = Waiter(Pasta())

print(waiter1.serve())  # ✅ "Chicken Biryani is ready!"
print(waiter2.serve())  # ✅ "Fish Curry is ready!"
print(waiter3.serve())  # ✅ "Pasta is ready!"
