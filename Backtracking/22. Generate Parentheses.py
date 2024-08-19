from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def dfs(open: int, close: int, s: str) -> None:
            """
            利用深度優先搜尋來尋找所有可能的括號組合
            如果 open 和 close 都等於 n，則將 s 加入到 result 中
            如果 open 小於 n，則遞迴下去
            如果 close 小於 open，則遞迴下去
            args:
                open: int, 目前左括號的數量
                close: int, 目前右括號的數量
                s: str, 目前的括號組合
            return:
                None
            """
            if open == close and open + close == n * 2:
                result.append(s)
                return
            
            if open < n:
                dfs(open + 1, close, s + "(")
        
            if close < open:
                dfs(open, close + 1, s + ")")

        dfs(0, 0, "")

        return result
        