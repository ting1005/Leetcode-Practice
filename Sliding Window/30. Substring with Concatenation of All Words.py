from collections import defaultdict
from typing import List

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words: return []
        
        # 使用 defaultdict 來計算 words 中每個單字的數量
        word_count = defaultdict(int)
        for word in words:
            word_count[word] += 1
        
        substr_len = len(words) * len(words[0])
        word_len = len(words[0])
        result = []

        # 透過 Sliding Window，每次都比對 s 中的子字串是否符合 words 中的單字
        for i in range(len(s) - substr_len + 1):
            seen = defaultdict(int)
            
            for j in range(i, i + substr_len, word_len):
                # 取出 s 中的子字串
                word = s[j:j + word_len]
                # 比對 words 中的單字，如果有符合的話，則更新 seen 中的數量，並且比對是否超過 word_count 中的數量
                # 沒有符合的話，則直接 break
                if word in word_count:
                    seen[word] += 1
                    if seen[word] > word_count[word]:
                        break
                else:
                    break
            else: # 如果 for 迴圈正常結束，則表示 s 中的子字串符合 words 中的單字，則將 i 加入 result 中
                result.append(i)
        
        return result