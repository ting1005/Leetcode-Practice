from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # 設定目標位置為最後一個位置
        target = len(nums) - 1

        # 透過反向迭代，更新目標位置
        # 如果目標位置可以到達，則更新目標位置
        
        for i in range(len(nums) - 2, -1, -1):
            if target <= i + nums[i]:
                target = i

        # 如果最後目標位置為 0，則代表可以到達最後一個位置
        return target == 0
            
            