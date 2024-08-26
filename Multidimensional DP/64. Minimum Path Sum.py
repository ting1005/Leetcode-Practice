from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        # 
        for i in range(m):
            for j in range(n):
                # 依照格子的位置，加上左邊或上面的最小值
                if i > 0 and j > 0:
                    grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])
                # 如果在第一列，則只能加上另一邊的值
                elif i > 0:
                    grid[i][j] += grid[i - 1][j]
                # 如果在第一行，則只能加上另一邊的值
                elif j > 0:
                    grid[i][j] += grid[i][j - 1]

        return grid[-1][-1]