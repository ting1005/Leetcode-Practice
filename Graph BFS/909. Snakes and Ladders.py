from typing import List


class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        target = n * n
        mapping = dict()
        
        # 將 board 轉換成一維陣列
        # 利用 mapping 來記錄每個位置的值
        for i in range(n):
            for j in range(n):
                if board[i][j] != -1:
                    num = j + 1 if (n - 1 - i) % 2 == 0 else n - j
                    num += (n - 1 - i) * n
                    mapping[num] = board[i][j]
        
        # 設定 visited 來記錄每個位置是否被訪問過
        # visited[1] = [1] 代表 1 這個位置已經被訪問過
        # current 用來記錄當前的位置
        # steps 用來記錄走了幾步
        visited = [0 for _ in range(target + 1)]
        visited[1] = [1]
        current = [1]
        steps = 0
        
        # 透過廣度優先搜尋，尋找最短的步數
        while current:
            # 每當 current 不為空，則 steps + 1，並且建立一個新的集合 new
            steps += 1
            new = set()
            # 透過 current 來找出下一步可以走的位置
            for i in current:
                # 如果下一步可以走的位置小於等於 6，則回傳 steps
                if target - i <= 6:
                    return steps

                # 使用迴圈模擬 User 擲骰子所可能移動的所有步數
                for j in range(i + 1, i + 7):
                    # 判斷 j 是否在 mapping 中，如果在則檢查是否已經被訪問過
                    if j in mapping and (not visited[mapping[j]]):
                        # 如果 User 移動到 target 位置，則回傳 steps
                        if mapping[j] == target:
                            return steps
                        # 如果 j 移動到的位置不是終點，則將這個位置加入到 new 中，並且標記為已經訪問過
                        new.add(mapping[j])
                        visited[mapping[j]] = 1
                    # 如果 j 不在 mapping 中，表示這是一個普通位置，不會被移動，則將這個位置加入到 new 中，並且標記為已經訪問過
                    elif j not in mapping and (not visited[j]):
                        new.add(j)
                        visited[j] = 1
            
            current = new
        
        return -1