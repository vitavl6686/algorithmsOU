
class LinkedStack:

    class Node:
        def __init__(self, item: object):
            self.item = item
            self.next = None

    def __init__(self):
        self.head = None
        self.length = 0
    
    def size(self) -> int:
        return self.length
    
    def push(self, item: object) -> None:
        newItem = LinkedStack.Node(item)
        newItem.item = item
        newItem.next =self.head
        self.head = newItem
        self.length += 1
    
    def pop(self) -> object:
        el = self.head.item
        self.head = self.head.next
        self.length -= 1
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
    
    
def main():
    print("start")
    ls = LinkedStack()
    print(ls.size())
    ls.push(1)
    ls.push(2)
    ls.push(3)
    print(ls.size())
    print(ls)
    ls.pop()
    print(ls.size())
    print(ls)
    
    

    
if __name__ == "__main__":
    main()


    
