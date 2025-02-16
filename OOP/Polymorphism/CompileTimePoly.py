class MathOperations:
    def add(self, a, b, c=0):
        return a + b + c

math = MathOperations()
print(math.add(2, 3))
print(math.add(2, 3, 4))


class MathOperations:
    def add(self, *arguments):  # Accepts multiple arguments
        return sum(arguments)

math = MathOperations()
print(math.add(1, 2))
print(math.add(1, 2, 3, 4))
