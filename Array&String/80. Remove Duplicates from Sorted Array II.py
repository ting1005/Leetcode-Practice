from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = 1
        temp_count = 1

        # 透過雙指針法，將重複的元素移除
        # 設定 temp_count 變數用來計算重複元素的數量
        # 如果重複元素的數量小於等於 2，則將其保留
        # 如果重複元素的數量大於 2，則將其移除

        for index in range(1, len(nums)):
            if nums[index] == nums[index-1]:
                if temp_count < 2:
                    nums[count] = nums[index]
                    count += 1
                temp_count += 1

            if nums[index] != nums[index-1]:
                temp_count = 1
                nums[count] = nums[index]
                count += 1

        return count
