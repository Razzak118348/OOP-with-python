# class student:
#     name='John'

# # s1 is instance or object of student class
# s1 = student()
# print(s1.name)

# class car:
# #    self parameter is a reference to the current instance of the class and is used to access variables that belosngs to the class
#     def __init__(self,name,model):
#         self.name=name
#         self.model=model


# c1=car('Toyota','Camry')
# print(c1.name)


# class student:
#     # default constructor is __init__ method
#     def __init__(self):
#         pass

#         # parameter constructor
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
#         print('Adding a new student in Database ....')

#     def display(self):
#         print('Name : ',self.name)
#         print('marks : ',self.marks)


# s1=student('John',90)
# s1.display()

# s2=student('Doe',80)
# s2.display()


def factorial(n):
    if n == 1:
        return 1
    else:
        return (n * factorial(n-1))

print(factorial(5))
