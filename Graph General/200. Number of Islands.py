from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: return 0

        # 建立一個深度優先搜尋的函數
        # i 和 j 代表當前的位置
        def dfs(i: int, j: int) -> None:
            # 如果 i 或 j 超出範圍或是當前位置不是 '1'，則返回
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != '1':
                return
            # 將當前位置標記為 '0'，代表已經訪問過
            grid[i][j] = '0'
            # 分別檢查當前位置的上下左右
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)

        islands = 0
        # 遍歷整個矩陣
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    islands += 1
                    dfs(i, j)
                    
        return islands
