from StaticArray import StaticArray

class DinamicCircularQueue():
    def __init__(self) -> None:
        self.items = StaticArray(2)
        self.size = 0
        self.start = 0
        self.end = 0
    
    def _resize(self, capacity: int) -> None:
        new_array = StaticArray(capacity)
        index = self.start
        for new_index in range(0, self.size):
            new_array.set_item(new_index, self.items.get_item(index))
            index = (index + 1) % self.items.length()
        self.items = new_array
        self.start = 0
        self.end = self.size
    
    def length(self) -> int:
        return self.size

    def enqueue(self, item: object) -> None:
        self.items.set_item(self.end, item)
        self.size += 1
        self.end += 1
        if(self.end == self.items.length()):
            self._resize(self.items.length() * 2)
    
    def dequeue(self) -> None:
        self.items.set_item(self.start, None)
        self.start += 1
        self.size -= 1

        if(self.size < 0.25 * self.items.length()):
            self._resize(self.items.length // 2)
    
    def front(self) -> object:
        return self.items.get_item(self.start)

    def __str__(self) -> str:
        return str(self.items)
        