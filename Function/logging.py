import time

def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Executing: {func.__name__} with arguments: {args}, {kwargs}")
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Completed: {func.__name__} in {end_time - start_time:.4f} seconds")
        return result
    return wrapper

@logger
def addFunction(a, b):
    return a + b

print(addFunction(5, 3))
