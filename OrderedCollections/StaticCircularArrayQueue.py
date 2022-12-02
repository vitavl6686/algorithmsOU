from StaticArray import StaticArray

class StaticCircularArrayQueue:
    def __init__(self, capacity: int):
        self.items = StaticArray(capacity)
        self.size = 0
        self.start = 0
        self.end = 0
        
    
    def length(self) -> int:
        return self.size
    
    def enqueue(self, item: object) -> None:
        self.items.set_item(self.end, item)
        if self.end + 1 == self.items.length():
            self.end = 0
        else:
            self.end += 1
        
        self.size += 1
    
    def dequeue(self) -> None:
        self.items.set_item(self.start, None)
        if self.start + 1 == self.items.length():
            self.start = 0
        else:
            self.start += 1
        self.size -= 1
    
    def front(self) -> None:
        return self.items.get_item(self.start)

    def __str__(self) -> str:
        return str(self.items)
