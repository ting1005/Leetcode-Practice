class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # 先將字串去除左右空白
        s = s.strip()
        # 如果字串為空，則回傳 0
        if not s: return 0
        
        # 以空白分割字串，取最後一個單字的長度
        last_word = s.split(' ')[-1]

        # 回傳最後一個單字的長度
        return len(last_word)