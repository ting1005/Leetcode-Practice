from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # 建立一個長度為 len(s) + 1 的 list 來記錄是否可以拆分
        # dp[0] = True 代表空字串可以拆分
        dp = [False] * (len(s) + 1)
        dp[0] = True

        for i in range(1, len(s) + 1):
            for j in range(i):
                # 判斷如果 dp[j] 為 True 且 s[j:i] 在 wordDict 中，則 dp[i] 為 True
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break

        return dp[-1]
