from ArraySequence import ArraySequence
class ArrayStack():
    def __init__(self):
        self.items = ArraySequence()
        self.size = 0
    
    def length(self) -> int:
        return self.size
    
    def push(self, item: object) -> None:
        self.items.append(item)
        self.size += 1
    
    def pop(self) -> None:
        self.items.remove(self.size - 1)
        self.size -= 1
    
    def peek(self) -> object:
        return self.items.get_item(self.size - 1)
    
    def __str__(self) -> str:
        return str(self.items)
    