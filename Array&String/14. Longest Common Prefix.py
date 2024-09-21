from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        str_index = 1

        # 如果字串陣列為空，則回傳空字串
        # 如果字串陣列只有一個元素，則回傳該元素
        if len(strs) == 0 : return ""
        if len(strs) == 1 : return strs[0]
        
        
        while str_index >= 0:
            is_prefix = False
            # 以第一個字串為基準，比對其他字串的第 str_index 個字元是否相同
            # 如果不相同，則回傳第一個字串的前 str_index - 1 個字元
            # 如果相同，則將 is_prefix 設為 True，並繼續比對下一個字串
            for i in range(1, len(strs)):
                if len(strs[i]) < str_index:
                    return strs[0][:str_index-1]
                if (strs[i])[:str_index] == (strs[0])[:str_index]:
                    is_prefix = True
                else:
                    is_prefix = False
                    break
                
            if is_prefix == False:
                return strs[0][:str_index-1]
            else:
                str_index += 1
