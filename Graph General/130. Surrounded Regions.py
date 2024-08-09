from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # 檢查 board 是否為空，如果是則不做任何動作
        if not board or not board[0]: return

        m = len(board)
        n = len(board[0])

        def dfs(i: int, j: int) -> None:
            """
              定義DFS函數進行深度優先搜尋，標記所有與邊界相連的 "O" 為 "T"，防止 "O" 被覆蓋
              args:
                i: int : 當前的行
                j: int : 當前的列
              returns:
                None
            """

            # 如果 i 或 j 超出範圍或是當前位置不是 'O'，則返回
            if 0 <= i < m and 0 <= j < n and board[i][j] == "O":
                board[i][j] = "T"
                dfs(i + 1, j)
                dfs(i - 1, j)
                dfs(i, j + 1)
                dfs(i, j - 1)
        
        # 檢查四個邊界，將與邊界相連的 "O" 標記為 "T"
        for i in range(m):
            dfs(i, 0)
            dfs(i, n - 1)
        
        for j in range(1, n - 1):
            dfs(0, j)
            dfs(m - 1, j)
            
        # 將所有 "O" 標記為 "X"，將所有 "T" 標記為 "O"
        for i in range(m):
            for j in range(n):
                if board[i][j] == "O": board[i][j] = "X"
                elif board[i][j] == "T": board[i][j] = "O"