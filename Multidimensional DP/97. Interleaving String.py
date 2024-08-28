class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m, n = len(s1), len(s2)

        if m + n != len(s3): return False

        # 初始化 dp array
        # s1 的前 i 個字元和 s2 的前 j 個字元能否交錯組成 s3 的前 i + j 個字元
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True

        # 當 j = 0 時，s1 的前 i 個字元可以等於 s3 的前 i 個字元
        for i in range(1, m + 1):
            dp[i][0] = dp[i - 1][0] and s1[i - 1] == s3[i - 1]
        
        # 當 i = 0 時，s2 的前 j 個字元可以等於 s3 的前 j 個字元
        for j in range(1, n + 1):
            dp[0][j] = dp[0][j - 1] and s2[j - 1] == s3[j - 1]

        # s1 的前 i 個字元和 s2 的前 j 個字元能否交錯組成 s3 的前 i + j 個字元
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                dp[i][j] = (dp[i - 1][j] and s1[i - 1] == s3[i + j - 1]) or (dp[i][j - 1] and s2[j -  1] == s3[i + j - 1]) 
        
        return dp[-1][-1]