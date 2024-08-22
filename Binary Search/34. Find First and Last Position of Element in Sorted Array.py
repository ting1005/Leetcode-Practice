from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # 如果 target 不在 nums 中，則返回 [-1, -1]
        if target not in nums: return [-1, -1]
        
        # 將 nums 進行反向排序，用於找出最後一個 target 的 index
        sorted_nums = sorted(nums, reverse=True)

        first_idx = nums.index(target)
        last_idx = len(nums) - sorted_nums.index(target) -1

        return [first_idx, last_idx]
