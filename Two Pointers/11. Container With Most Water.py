from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        res = 0
        left = 0
        right = len(height) - 1
        # 透過快慢指針，比對 height[left] 和 height[right] 的最大面積
        # 每次都更新最大面積
        # 每當 height[left] 小於 height[right]，則 left 往前移動，否則只有 right 往前移動
        
        while left < right:
            res = max(res, (right-left) * min(height[left], height[right]))

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return res