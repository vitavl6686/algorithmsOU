from ArraySequence import ArraySequence
class ArrayQueue:
    def __init__(self) -> None:
        self.items = ArraySequence()
        self.size = 0
        self.start = 0
    
    def length(self) -> int:
        return self.size
    
    def enqueue(self, item: object) -> None:
        self.items.append(item)
        self.size += 1
    
    def dequeue(self) -> None:
        self.items.set_item(self.start, None)
        self.start += 1
        self.size -= 1
    
    def front(self) -> None:
        return self.items.get_item(self.start)

    def __str__(self) -> str:
        return str(self.items)
