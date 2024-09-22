class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        stack_len = len(haystack)
        need_len = len(needle)

        # 遍歷 haystack，比對是否有相同的字串
        # 透過將 haystack 分割成與 needle 相同長度的字串，比對是否相同
        # 如果有則回傳索引值，沒有則回傳 -1
        for i in range(stack_len - need_len + 1):
            
            if (haystack[i:i + need_len] == needle):
                return i
        return -1
