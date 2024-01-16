class RandomizedSet:
    # method 1
    # Runtime 584ms Beats 10.20% of users with Python3
    # Memory 64.60MB Beats 27.57% of users with Python3
    def __init__(self):
        self.rand_set = []

    def insert(self, val: int) -> bool:
        if val not in self.rand_set:
            self.rand_set.append(val)
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        if val not in self.rand_set:
            return False
        else:
            self.rand_set.remove(val)
            return True

    def getRandom(self) -> int:
        import random
        index = random.randint(1,len(self.rand_set)) - 1
        return self.rand_set[index]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
