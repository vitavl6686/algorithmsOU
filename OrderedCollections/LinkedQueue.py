
class LinkedQueue():

    class _Node():
        def __init__(self, item: object)-> None:
            self.item = item
            self.next = None

    def __init__(self)-> None:
        self.head = None
        self.last = None
        self.size = 0
    
    def enqueue(self, item: object) -> None:
        new_node = self._Node(item)
        if self.last == None:
            self.last = new_node
            self.head = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.size += 1
    
    def dequeue(self) -> None:
        if self.head == None:
            return -1
        else:
            self.head = self.head.next
            self.size -= 1

    def length(self) -> int:
        return self.size
    
    def front(self) -> object:
        if self.head != None:
            return self.head.item
    
    def __str__(self) -> str:
        result = ""
        item = self.head
        while item != None:
            result += str(item.item)
            result += ", "
            item = item.next
        return result
    
