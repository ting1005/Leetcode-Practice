class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        s_char = ""
        answer = 0

        # 透過 Sliding Window，每次都比對 s 中的子字串是否有重複的字元
        for value in s:
            # 將 value 加入 s_char 中
            s_char += value
            # 如果 s_char 和 set(s_char) 的長度不同，則表示有重複的字元，進入 while 迴圈
            while len(set(s_char)) != len(s_char):
                # 將 s_char 的第一個字元移除，並且更新 answer，取最大值，left 往前移動
                s_char = s_char[1:]
                answer = max(len(s_char), answer)
                left += 1
        # 最後再比對一次 s_char 和 answer 的長度，取最大值        
        answer = max(len(s_char), answer)
        
        return answer