class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # 如果只有一列或是字串長度小於列數，則直接回傳字串
        if numRows == 1 or numRows >= len(s):
            return s

        # 初始化
        # idx 追蹤當前字元應該放在哪一行
        # d 代表方向，1 代表往下，-1 代表往上
        # rows 用來存放每一列的字元
        idx, d = 0, 1
        rows = [[] for _ in range(numRows)]

        # 遍歷字串，將字元放入對應的列
        # 如果 idx 為 0，則方向為向下 (d = 1)
        # 如果 idx 為 numRows - 1，則方向為向上 (d = -1)
        # 根據 d 的方向，更新 idx
        for char in s:
            rows[idx].append(char)
            if idx == 0:
                d = 1
            elif idx == numRows - 1:
                d = -1
            idx += d

        # 合併結果
        # 將每一行的字元合併成一個字串
        # 再將所有行的字串合併成一個字串
        for i in range(numRows):
            rows[i] = ''.join(rows[i])

        return ''.join(rows)   