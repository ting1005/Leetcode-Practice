from collections import Counter, defaultdict


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t: return ""

        # 使用 Counter 計算 t 中每個字元的數量
        dict_t = Counter(t)

        # required 紀錄需要的字元數量
        required = len(dict_t)
        left, right = 0, 0
        formed = 0

        window_counts = defaultdict(int)
        ans = float("inf"), None, None

        # 透過不斷擴展 right 指針來包括更多的字元
        while right < len(s):
            character = s[right]
            window_counts[character] += 1

            if character in dict_t and window_counts[character] == dict_t[character]:
                formed += 1
            
            # 滿足條件後，開始縮小 left 指針
            while left <= right and formed == required:
                character = s[left]

                # 如果 window 的大小比目前的答案更小，則更新答案
                if right - left + 1 < ans[0]:
                    ans = (right - left + 1, left, right)
                
                window_counts[character] -= 1
                if character in dict_t and window_counts[character] < dict_t[character]:
                    formed -= 1

                left += 1
        
            right += 1

        return "" if ans[0] == float("inf") else s[ans[1]: ans[2] + 1]

            