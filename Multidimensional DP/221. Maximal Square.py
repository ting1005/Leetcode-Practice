from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]: return 0

        rows, cols = len(matrix), len(matrix[0])
        # 初始化 dp array 和 max_side
        dp = [[0] * cols for _ in range(rows)]
        max_side = 0

        for r in range(rows):
            for c in range(cols):
                # 如果 matrix[r][c] 為 '1'，則更新 dp[r][c] 的值
                # 如果 r = 0 或 c = 0，表示在邊界上，則 dp[r][c] = 1
                # 否則則辨識左、上、左上三個點的最小值再加上 1，表示能夠形成最大正方形的邊長
                if matrix[r][c] == '1':
                    if r == 0 or c == 0: 
                        dp[r][c] = 1
                    else:
                        dp[r][c] = min(dp[r - 1][c], dp[r][c - 1], dp[r - 1][c - 1]) + 1

                    # 比較 max_side 和 dp[r][c]，取最大值
                    max_side = max(max_side, dp[r][c])
        
        return max_side * max_side
