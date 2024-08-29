class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)

        # 初始化 dp array
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # 當 i = 0 時，word1 的前 i 個字元可以等於 word2 的前 0 個字元
        for i in range(1, m + 1):
            dp[i][0] = i
        
        # 當 j = 0 時，word1 的前 0 個字元可以等於 word2 的前 j 個字元
        for j in range(1, n + 1):
            dp[0][j] = j

        # word1 的前 i 個字元和 word2 的前 j 個字元的最小編輯距離
        # 插入 = dp[i][j - 1] + 1 >>> 表示在 word1 中插入了 word2[j - 1]
        # 刪除 = dp[i - 1][j] + 1 >>> 表示在 word1 中刪除了 word1[i - 1]
        # 替換 = dp[i - 1][j - 1] + 1 >>> 表示將 word1[i - 1] 替換成 word2[j - 1]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1
        
        return dp[-1][-1]