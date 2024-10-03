from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # 透過快慢指針，比對 numbers[i] 和 numbers[j] 的和是否等於 target
        # 每當 numbers[i] + numbers[j] 大於 target，則 j 往前移動，否則只有 i 往前移動
        
        for i in range(len(numbers)):
            t = target - numbers[i]
            if t in numbers and numbers.index(t) != i:
                res = [i+1, numbers.index(t)+1]
                res.sort()
                return res
            