
class LinkedDeque():
    class _Node():
        def __init__(self, item: object)-> None:
            self.item = item
            self.next = None
            self.previous = None
    
    def __init__(self)-> None:
        self.head = None
        self.last = None
        self.size = 0

    def length(self) -> int:
        return self.size
    
    def add_front(self, item: object) -> None:
        new_node = self._Node(item)
        if self.head == None:
            self.head = new_node
            self.last = new_node
        else:
            self.head.previous = new_node
            new_node.next = self.head
            self.head = new_node
        self.size += 1

    def add_back(self, item: object) -> None:
        new_node = self._Node(item)
        if self.last == None:
            self.last = new_node
            self.head = new_node
        else:
            new_node.previous = self.last
            self.last.next = new_node
            self.last = new_node
        self.size += 1

    def remove_front(self) -> None:
        if self.head == None:
            return -1
        else:
            self.head = self.head.next
            self.head.previous = None
            self.size -= 1

    def remove_back(self) -> None:
        if self.last == None:
            return -1
        else:
            previous = self.last.previous
            previous.next = None
            self.last = previous
            self.size -= 1
    
    def front(self) -> object:
        if self.head != None:
            return self.head.item
        else:
            return None

    def back(self) -> object:
        if self.back != None:
            return self.back.item
        else:
            return None

    def __str__(self) -> str:
        result = ""
        item = self.head
        while item != None:
            result += str(item.item)
            result += ", "
            item = item.next
        return result
