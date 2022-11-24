from Sequence import Sequence
from StaticArray import StaticArray

class BoundedSequence(Sequence):
    def __init__(self, capacity: int):
        self.items = StaticArray(capacity)
        self.size = 0

    def capacity(self) -> float:
        return (self.items.length())

    def length(self) -> int:
        return self.size

    def get_item(self, index: int) -> object:
        return self.items.get_item(index)
    
    def set_item(self, index: int, item: object) -> None:
        self.items.set_item(index, item)

    def insert(self, index: int, item: object) -> None:
        for i in range(self.size-1, index - 1, -1):
            self.items.set_item(i + 1, self.items.get_item(i))
        self.items.set_item(index, item)
        self.size += 1

    def append(self, item: object) -> None:
        self.items.set_item(self.size, item)
        self.size += 1

    def remove(self, index: int) -> object:
        for i in range(index+1, self.size):
            self.items.set_item(i - 1, self.items.get_item(i))
        self.size -= 1

    def __str__(self) -> str:
        result = "["
        for i in range(self.size - 1):
            result += str(self.items.get_item(i))
            result += (', ')
        result += str(self.items.get_item(self.size-1))
        result += "]"
        return result


def main():
    print('start')


if __name__ == "__main__":
    main()