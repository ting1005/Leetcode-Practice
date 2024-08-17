from typing import List


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        

        def dfs(x: int, y: int, root: dict) -> None:
            """
            使用深度優先搜尋來尋找所有可能的單詞
            檢查是否找到單詞，如果找到則將單詞加入到 res 中
            並且將當前字母標記為已經訪問過
            透過迴圈來尋找下一個字母
            如果當前 Trie 為空，則將當前字母從 Trie 中移除
            args:
                x: int, 當前字母的 x 座標
                y: int, 當前字母的 y 座標
                root: dict, 當前的 Trie
            return:
                None
            """
            letter = board[x][y]
            current = root[letter]
            word = current.pop('#', False)
            if word:
                result.append(word)

            board[x][y] = '*'

            for dirx, diry in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                curx, cury = x + dirx, y + diry

                if 0 <= curx < m and 0 <= cury < n and board[curx][cury] in current:
                    dfs(curx, cury, current)

            board[x][y] = letter

            if not current:
                root.pop(letter)

        # 建立 Trie
        # 將 words 中的每個單詞加入到 Trie 中        
        trie = {}
        for word in words:
            current = trie
            for char in word:
                if char not in current:
                    current[char] = {}
            current['#'] = word

        # 搜尋整個 board 
        m, n = len(board), len(board[0])
        result = []
        
        for i in range(m):
            for j in range(n):
                if board[i][j] in trie:
                    dfs(i, j, trie)
        
        return result