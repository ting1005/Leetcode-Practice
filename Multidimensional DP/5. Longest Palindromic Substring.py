class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1: return s

        # 紀錄最長的回文子串
        max_len = 1
        max_str = s[0]

        for i in range(len(s) - 1):
            for j in range(i + 1, len(s)):
                # 如果當前子串的長度大於最長的回文子串，且是回文子串，則更新最長的回文子串
                if j - i + 1 > max_len and s[i:j + 1] == s[i: j + 1][::-1]:
                    max_len = j - i + 1
                    max_str = s[i:j + 1]
        
        return max_str