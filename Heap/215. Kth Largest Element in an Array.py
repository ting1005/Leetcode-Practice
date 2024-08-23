from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # 將 nums 進行反向排序，並返回第 k-1 個元素
        nums.sort(reverse=True)

        return nums[k-1]