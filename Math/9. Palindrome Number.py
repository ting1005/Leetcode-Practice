class Solution:
    def isPalindrome(self, x: int) -> bool:
        # 利用 str 的特性，將字串反轉後比較，若相同則為回文
        if str(x) == str(x)[::-1]:
            return True
        return False