import random


class RandomizedSet:

    def __init__(self):
        self.numMap = {}
        self.numList = []
    
    def insert(self, val: int) -> bool:
        res = val not in self.numMap
        if res:
            self.numMap[val] = len(self.numList)
            self.numList.append(val)
        return res

    def remove(self, val: int) -> bool:
        res = val in self.numMap
        if res:
            idx = self.numMap[val]
            lastVal = self.numList[-1]            
            self.numList[idx] = lastVal            
            self.numList.pop()            
            self.numMap[lastVal] = idx            
            del self.numMap[val]
        return res
    
    def getRandom(self) -> int:
        return random.choice(self.numList)


randomizedSet = RandomizedSet()

# Prueba de inserción
print(randomizedSet.insert(1))  # True
print(randomizedSet.insert(3))  # True
print(randomizedSet.insert(5))  # True
# print(randomizedSet.insert(1))  # False

# # Prueba de eliminación
print(randomizedSet.remove(3))  # True
# print(randomizedSet.remove(3))  # True
# print(randomizedSet.remove(3))  # False

# # Prueba de getRandom
# print(randomizedSet.getRandom())  # Puede ser 2 (único elemento restante)