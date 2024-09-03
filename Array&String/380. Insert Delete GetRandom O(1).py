import random


class RandomizedSet:

    def __init__(self):
        # 建立一個空的 list 來存放 random_array
        self.random_array = []

    def insert(self, val: int) -> bool:
        # 判斷 val 是否在 random_array 中，如果不在，則將 val 加入 random
        if val not in self.random_array:
            self.random_array.append(val)
            return True
        return False

    def remove(self, val: int) -> bool:
        # 判斷 val 是否在 random_array 中，如果在，則將 val 移除 random_array
        if val in self.random_array:
            self.random_array.remove(val)
            return True
        return False

    def getRandom(self) -> int:
        # 隨機回傳 random_array 中的值
        return random.choice(self.random_array)
