from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        # 初始化 dp Array，並設定dp[0][0]的值
        dp = [[0 for _ in range(n)] for _ in range(m)]
        dp[0][0] = 1 - obstacleGrid[0][0]

        
        for i in range(m):
            for j in range(n):
                # 如果往下走不超出範圍且下一格沒有障礙物，則下一格的值加上當前格的值
                if i + 1 < m and obstacleGrid[i + 1][j] == 0: dp[i + 1][j] += dp[i][j]
                # 如果往右走不超出範圍且下一格沒有障礙物，則下一格的值加上當前格的值
                if j + 1 < n and obstacleGrid[i][j + 1] == 0: dp[i][j + 1] += dp[i][j]

        # 返回最終到達右下角的路徑數量
        return dp[-1][-1]