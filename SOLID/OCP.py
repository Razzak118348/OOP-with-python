
# Base class
class Employee:
    def __init__(self, name):
        self.name = name
    def calculate_salary(self): #just a demo method
        pass

# New roles extend Employee class
class Developer(Employee):
    def calculate_salary(self):
        return 50000

class Manager(Employee):
    def calculate_salary(self):
        return 70000

class Designer(Employee):
    def calculate_salary(self):
        return 60000

# Usage
dev = Developer("Alice")
print("salary for developers",dev.calculate_salary())  # 50000

manager = Manager("Bob")
print("salary for manager",manager.calculate_salary())  # 70000

designer = Designer("Charlie")
print("salary for designer",designer.calculate_salary())  # 60000

# bad practice :using if else
"""

class Employee:
    def __init__(self, name, role):
        self.name = name
        self.role = role

    def calculate_salary(self):
        if self.role == "Developer":
            return 50000
        elif self.role == "Manager":
            return 70000
        else:
            return 40000

# Usage
dev = Employee("Alice", "Developer")
print(dev.calculate_salary())  # 50000

manager = Employee("Bob", "Manager")
print(manager.calculate_salary())  # 70000



"""