class Solution(object):
    def reverseWords(self, s: str) -> str:
        # 先將字串以空白分割
        words = s.split()
        # 再將字串反轉，並以空白連接
        reversed_words = words[::-1]
        reversed_string = ' '.join(reversed_words)
        
        return reversed_string