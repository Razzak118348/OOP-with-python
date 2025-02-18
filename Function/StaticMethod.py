class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

# Calling the static method without creating an instance
result = MathUtils.add(5, 10)
print(result)
