from typing import List


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        # max_sum 用來記錄遍歷過程中的最大值
        # current_max 用來記錄當前的最大值
        max_sum = float('-inf')
        current_max = 0 
        # min_sum 用來記錄遍歷過程中的最小值
        # current_min 用來記錄當前的最小值
        min_sum = float('inf')
        current_min = 0 
        # total_sum 用來記錄整個數組的總和
        total_sum = sum(nums)

        # 遍歷 nums 找出 max_sum 和 min_sum
        for num in nums:
            current_max = max(current_max + num, num)
            max_sum = max(max_sum, current_max)

            current_min = min(current_min + num, num)
            min_sum = min(min_sum, current_min)
        # 如果 total_sum == min_sum 代表整個數組都是負數，則返回 max_sum
        # 如果 total_sum != min_sum 代表整個數組不全是負數，則返回 max(max_sum, total_sum - min_sum)
        return max_sum if total_sum == min_sum else max(max_sum, total_sum - min_sum)