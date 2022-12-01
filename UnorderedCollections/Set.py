from HashMap import HashMap
class Set():
    def __init__(self) -> None:
        self.hm = HashMap
        self.size = 0
    
    def length(self) -> int:
        return self.size
    
    def has(self, key: object) -> bool:
        if self.hm.has(key) == False or self.hm.find(key) == False:
            return False
        return True
    
    
    def add(self, key: object) -> None:
        self.hm.associate(key, False)
        size += 1
    
    def union(self, aSet: "Set") -> "Set":
        union = HashMap()
        for el in self.hm:
            if(self.hm[el] == True):
                union.associate(el, True)
        
        for el in aSet:
            if(self.hm[el] == True):
                union.associate(el, True)
        return union
