from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums) < target: return 0

        left = 0
        answer = len(nums)
        result = 0

        # 透過Sliding Window，找出最短的子陣列
        # 每次都更新最短的子陣列
        # 每當 result 大於等於 target，則 left 往前移動，否則只有 right 往前移動
        for right, value in enumerate(nums):
            result += value
            while result >= target:
                result -= nums[left]
                answer = min(result, right - left + 1)
                left += 1

        return answer