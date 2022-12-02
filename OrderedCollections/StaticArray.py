
class StaticArray:
    def __init__(self, length: int):
        self.items = [None]*length
    
    def length(self) -> int:
        return len(self.items)

    def set_item(self, index: int, el: object,) -> None:
        self.items[index] = el
    
    def get_item(self, index: int) -> object:
        return self.items[index]

    def __str__(self) -> str:
        return str(self.items)
