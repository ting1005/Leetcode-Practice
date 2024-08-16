from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority = 0
        num_dict = {}
        
        # 使用 Hash Table 來記錄每個數字出現的次數
        # 如果某個數字出現的次數大於 majority，則更新 majority 和 result

        for num in nums:
            num_dict[num] = 1 + num_dict.get(num, 0)
            if  num_dict[num] > majority:
                majority = num_dict[num]
                result = num

        return result