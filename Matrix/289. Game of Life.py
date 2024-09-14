from typing import List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        # 取得 board 的 row 和 col 的長度
        rows, cols = len(board), len(board[0])

        # 定義8個方向
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]

        # 0 -> 0: 0
        # 0 -> 1: 2
        # 1 -> 0: -1
        # 1 -> 1: 1

        for r in range(rows):
            for c in range(cols):
                live_neighbors = 0
                # 計算目前位置的鄰居有幾個是活著的
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and abs(board[nr][nc]) == 1:
                        live_neighbors += 1
                # 根據題目的規則，更新 board
                if board[r][c] == 1 and (live_neighbors < 2 or live_neighbors > 3):
                    board[r][c] = -1
                
                if board[r][c] == 0 and live_neighbors == 3:
                    board[r][c] = 2
        # 更新 board 的狀態
        for r in range(rows):
            for c in range(cols):
                if board[r][c] > 0:
                    board[r][c] = 1
                else:
                    board[r][c] = 0
