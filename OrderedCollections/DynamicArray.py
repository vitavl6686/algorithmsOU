from StaticArray import StaticArray

class DynamicArray(StaticArray):
    def resize(self, length: int) -> None:
        new_array = [None]*length

        for i in range(min(length, self.length())):
            new_array[i] = self.items[i]
        
        self.items = new_array


    