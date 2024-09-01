from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # 合併兩個數組並排序
        nums = nums1 + nums2
        nums.sort()
        
        # 找出 nums 的長度跟中間的索引
        n = len(nums)
        m = n // 2

        # 如果 nums 的長度是偶數，則回傳中間兩個數字的平均值
        if n % 2 == 0:
            return (nums[m - 1] + nums[m]) / 2
        else:
            return nums[m]