class Bag:
    def __init__(self) -> None:
        self.inn = dict()
        self.size = 0

    def length(self) -> int:
        return self.size

    def has(self, key: object) -> bool:
        return key in self.inn
    
    def count(self, key: object) -> bool:
        if not key in self.inn:
            return 0
        return self.inn[key]
    
    def add(self, key: object) -> None:
        if key in self.inn:
            self.inn[key] += 1
        else:
            self.inn[key] = 1
        self.size += 1

    def remove(self, key: object) -> None:
        if key in self.inn:
            if self.inn[key] > 1:
                self.inn[key] -= 1
            else:
                self.inn.pop(key)
    
    def items(self) -> list:
        return self.inn.items()
    
    def union(self, other: "Bag") -> "Bag":
        union = Bag()
        if (other.length > self.length):
            arr = other.items()
            for pair in arr:
                maximum = pair[1]
                if(self.has(pair[0])):
                    maximum = max(maximum, self.count(pair[0]))
                for i in range(maximum):
                    union.add(pair[0])
        arr = self.items()
        for pair in arr:
            for i in range(pair[1]):
                union.add(pair[0])
        return union
