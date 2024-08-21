from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        temp = nums[0]
        
        # 這裡的 nums[1:] 是從第二個元素開始遍歷
        # 透過 temp 來記錄當前的最大值，res 來記錄遍歷過程中的最大值
        for num in nums[1:]:
            temp = max(num, temp + num)
            res = max(res, temp)
        
        return res