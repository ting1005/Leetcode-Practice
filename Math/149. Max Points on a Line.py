from collections import defaultdict
from math import gcd
from typing import List


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        def get_slope(p1, p2) -> tuple:
            """
            取得兩點之間的斜率
            args:
                p1: tuple
                p2: tuple
            return:
                tuple: (dy, dx)
            """
            dx = p2[0] - p1[0]
            dy = p2[1] - p1[1]
            
            if dx == 0: return (float('inf'), 0) # 垂直線，斜率為無限大
            if dy == 0: return (0, 0) # 水平線，斜率為 0
            
            # 簡化斜率
            d = gcd(dx, dy)
            dx //= d
            dy //= d
            
            # 保持一致性，確保 dx 為正數
            if dx < 0:
                dx = -dx
                dy = -dy
                
            return (dy, dx)
                
        n = len(points)
        if n <= 2: return n
        
        max_points = 1
        # 遍歷所有點，計算每個點與其他點之間的斜率
        # 利用 defaultdict 來記錄每個斜率的出現次數
        for i in range(n):
            slopes = defaultdict(int)
            duplicate = 0
            current_max = 0
            for j in range(i + 1, n):
                if points[i] == points[j]:
                    duplicate += 1
                    continue
                slope = get_slope(points[i], points[j])
                slopes[slope] += 1
                current_max = max(current_max, slopes[slope])
            # 更新最大點數
            max_points = max(max_points, current_max + duplicate + 1)
        
        return max_points