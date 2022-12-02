import math
from DynamicArray import DynamicArray
from Sequence import Sequence


class ArraySequence():
    def __init__(self):
        self.items = DynamicArray(1)
        self.size = 0
    
    def capacity(self) -> float:
        return math.inf

    def length(self) -> int:
        return self.size

    def get_item(self, index: int) -> object:
        return self.items.get_item(index)

    def set_item(self, index: int, item: object) -> None:
        self.items.set_item(index, item)


    def insert(self, index: int, item: object) -> None:
        if(self.items.length() == self.size):
            self.items.resize(2 * self.size)
        for i in range(self.size-1, index - 1, -1):
            self.items.set_item(i + 1, self.items.get_item(i))
        self.items.set_item(index, item)
        self.size += 1

    def append(self, item: object) -> None:
        if(self.items.length() == self.size):
            self.items.resize(2 * self.size)
        self.items.set_item(self.size, item)
        self.size += 1

    def remove(self, index: int) -> object:
        for position in range(index, self.size - 1):
            self.items.set_item(position, self.items.get_item(position+1))
        self.size = self.size - 1
        if(self.size < 0.25 * self.items.length()):
            self.items.resize(self.items.length()//2)

    def __str__(self) -> str:
        result = "["
        for i in range(self.size - 1):
            result += str(self.items.get_item(i))
            result += (', ')
        result += str(self.items.get_item(self.size-1))
        result += "]"
        return result
