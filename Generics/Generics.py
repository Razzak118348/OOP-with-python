from typing import TypeVar, Generic
GenericVariable= TypeVar("anyPeramete")

class Box(Generic[GenericVariable]):
    def __init__(self, item: GenericVariable):
        self.item = item

    def get_item(self) -> GenericVariable: # ->GenericVariable denote Type hint and get_item() return  GenericVariable type value
        return self.item

box1 = Box(10)
box2 = Box("Hello")
box3 = Box([1, 2, 3])

print(box1.get_item())
print(box2.get_item())
print(box3.get_item())
