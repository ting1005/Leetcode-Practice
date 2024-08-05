from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
          初始 count 為 1，從第二個元素開始檢查
          如果當前元素和前一個元素不相等，則將當前元素放到 count 的位置並將 count 加 1
        """
        count = 1
        
        for index in range(1, len(nums)):
            if nums[index] != nums[index-1]:
                nums[count] = nums[index]
                count += 1
        return count