
# storing function in data structure example
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

# Storing functions in a dictionary
dictionary = {
    "add": add,
    "subtract": subtract
}

# Calling functions from the dictionary
print(dictionary["add"],dictionary["subtract"])
print(dictionary["add"](5, 3))
print(dictionary["subtract"](5, 3))