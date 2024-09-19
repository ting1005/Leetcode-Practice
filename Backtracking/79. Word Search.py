from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # 初始化 rows, cols, visited
        # visited 用於存取已經走過的位置
        rows, cols = len(board), len(board[0])
        visited = set()

        def dfs(r: int, c: int, idx: int) -> bool:
            # 建立一個遞迴函數，用來判斷是否有符合的 word
            # 如果 idx 等於 word 的長度，則表示找到了，返回 True
            # 如果目前超過邊界，或是已經走過，或是目前的字母不等於 word 的字母，則返回 False
            # 將目前的位置加入 visited，並在四個方向上遞迴
            # 遞迴完成後，將目前的位置從 visited 中移除
            if idx == len(word):
                return True

            if not (0 <= r < rows) or not (0 <= c < cols) or (r,c) in visited or board[r][c] != word[idx]:
                return False
            
            visited.add((r,c))
            result = dfs(r + 1, c, idx + 1) or \
                      dfs(r - 1, c, idx + 1) or \
                      dfs(r, c + 1, idx + 1) or \
                      dfs(r, c - 1, idx + 1)
            visited.remove((r,c))

            return result
        # 根據 word 的第一個字母，判斷是否需要反轉 word
        # 如果單字中第一個字母的數量大於最後一個字母的數量，則反轉
        count = {}
        for c in word:
            count[c] = 1 + count.get(c, 0)
        
        if count[word[0]] > count[word[-1]]:
            word = word[::-1]
        
        # 遍歷整個 board，並呼叫 dfs
        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0): return True
        
        return False