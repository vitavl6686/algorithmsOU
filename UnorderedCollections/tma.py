class LWPriorityQueue:
    """A dynamic array implementation of a max-priority queue.
    Items with the same priority are retrieved in FIFO order.
    Items are stored as dictionaries.
    """

    def __init__(self):
        """Create a new empty queue."""
        self.items = [] # in ascending order

    def length(self) -> int:
        """Return the number of items in the queue."""
        return len(self.items)

    def find_max(self) -> int:
        """Return index of the oldest item with the highest priority."""
        if self.length() == 0:
            return -1
        max_priority = 0
        oldest_item = 0
        for index in range(self.length()):
            if self.items[index]['priority'] >= max_priority:
                max_priority = self.items[index]['priority']
                oldest_item = index
        return oldest_item

    def remove_max(self) -> None:
        """Remove the oldest item with the highest priority."""
        if self.length() > 0:
            item_to_remove = self.find_max()
            self.items.pop(item_to_remove)

    def get_max(self) -> dict:
        """Returns the dictionary of the oldest item with the highest priority,
        or an empty dictionary."""
        index = self.find_max()
        if index == -1:
            return {}
        else:
            return self.items[index]

    def bump(self, customer: str) -> None:
        """Increases by one the priority of all items
        attributed to the specified customer."""
        for index in range(self.length()):
            if self.items[index]['customer'] == customer:
                self.items[index]['priority'] += 1

    def insert(self, priority: int, task: str, customer: str, complete_time: int) -> None:
        """Add item with the given priority to the queue."""
        item = {
            'priority': priority,
            'task': task,
            'customer': customer,
            'complete_time': complete_time
        }
        self.items.insert(0, item)
    
    def print_queue(self) -> None:
        """ Prints the current state of the priority queue """
        print('[')
        for item in self.items:
            print('   ', item)
        print(']')

    ### ADD YOUR CODE HERE ###

    def compact(self) -> None:
        old_priorities = dict()
        for item in self.items:
            priority = item['priority']
            old_priorities[priority] = True
        
        list_of_priorities = list(old_priorities.keys())
        list_of_priorities.sort()

        for index in range(len(list_of_priorities)):
            old_priority = list_of_priorities[index]
            old_priorities[old_priority] = index

        for item in self.items:
            old_priority = item['priority']
            new_priority = old_priorities[old_priority]
            item['priority'] = new_priority       

def main():
    print("hi everyone")
    leather_list = LWPriorityQueue()
    leather_list.insert(34, 'belt', 'Steff', 45)
    leather_list.insert(256, 'wallet', 'stock', 60)
    leather_list.insert(12, 'wallet', 'Mo', 60)
    leather_list.insert(12, 'wallet', 'stock', 60)
    leather_list.insert(11, 'custom belt', 'Erich', 90)
    
    print(leather_list.print_queue())

    leather_list.compact()
    print(leather_list.print_queue())
if __name__ == "__main__":
    main()

