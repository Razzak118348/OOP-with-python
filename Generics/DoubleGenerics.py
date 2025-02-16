from typing import TypeVar, Generic

T = TypeVar('T')
U = TypeVar('U')

class Pair(Generic[T, U]):
    def __init__(self, first: T, second: U):
        self.first = first
        self.second = second

    def get_pair(self):
        return (self.first, self.second)

pair1 = Pair(1, "Hello")
pair2 = Pair(3.14, [1, 2, 3])

print(pair1.get_pair())
print(pair2.get_pair())
