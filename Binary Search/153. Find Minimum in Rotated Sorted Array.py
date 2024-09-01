from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        # 設定一個變數來存放最小值
        # 透過迴圈來比較每個數字，找出最小值
        min_nums = float('inf')

        for num in nums:
            min_nums = min(min_nums, num)

        return min_nums