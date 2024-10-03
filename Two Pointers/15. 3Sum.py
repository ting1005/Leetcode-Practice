from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        # 透過快慢指針，比對 nums[i]、nums[j] 和 nums[k] 的和是否等於 0
        # 每當 nums[i] + nums[j] + nums[k] 大於 0，則 k 往前移動，否則只有 j 往前移動
        # 每次都要避免重複的組合
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            j = i + 1
            k = len(nums) - 1
            

            while j < k:
                total = nums[i] + nums[j] + nums[k]

                if total > 0:
                    k -= 1
                elif total < 0:
                    j += 1
                else:
                    result.append([nums[i], nums[j], nums[k]])
                    j += 1

                    while nums[j] == nums[j - 1] and j < k:
                        j += 1
                
        return result