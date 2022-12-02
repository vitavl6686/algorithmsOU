
class LinkedStack:

    class Node:
        def __init__(self, item: object):
            self.item = item
            self.next = None

    def __init__(self):
        self.head = None
        self.size = 0
    
    def length(self) -> int:
        return self.size
    
    def push(self, item: object) -> None:
        newItem = LinkedStack.Node(item)
        newItem.item = item
        newItem.next =self.head
        self.head = newItem
        self.size += 1
    
    def pop(self) -> object:
        el = self.head.item
        self.head = self.head.next
        self.size -= 1
        return el
    
    def peek(self) -> object:
        return self.head.item
    
    
    def __str__(self) -> str:
        result = "["
        current = self.head
        while(current != None):
            result += str(current.item)
            current = current.next
            if(current == None):
                result += "]"
            else:
                result += ", "
        return result



    
