from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1 

        # 設定兩個指針，分別指向最左邊和最右邊
        left_max = height[left]
        right_max = height[right]

        water = 0
        # 判斷當前左右兩側的最大高度來決定能積多少水
        # 如果左側的最大高度小於右側的最大高度，則左側的指針往右移動
        # 如果左側的最大高度大於右側的最大高度，則右側的指針往左移動
        while left < right:
            if left_max < right_max:
                left += 1
                left_max = max(left_max, height[left])
                water += left_max - height[left]
            else:
                right -= 1
                right_max = max(right_max, height[right])
                water += right_max - height[right]
            
        
        return water