from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        # jumps: 記錄總跳耀的次數
        # current_end: 記錄當前跳耀的最遠距離
        # farthest: 記錄所有點能跳耀的最遠距離
        jumps, current_end, farthest = 0, 0, 0


        for i in range(len(nums) - 1):
            # 更新當前位置跳耀時可以到達的最遠距離
            farthest = max(farthest, i + nums[i])

            # 如果當前位置等於當前跳耀的最遠距離，則更新當前跳耀的最遠距離為 farthest，並且跳耀次數加一
            if i == current_end:
                jumps += 1
                current_end = farthest
            
            # 如果當前跳耀的最遠距離已經大於等於最後一個點的索引，則跳出迴圈
            if current_end >= len(nums) - 1:
                break
        
        return jumps

