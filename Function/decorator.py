
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print(*args,**kwargs) # Accepts any number of arguments
        print("Before function execution...")
        result = func(*args, **kwargs)  # Calls the original function
        print("After function execution...")
        return result
    return wrapper

@my_decorator
def add(a, b):
    return a + b

print(add(5, 10))
