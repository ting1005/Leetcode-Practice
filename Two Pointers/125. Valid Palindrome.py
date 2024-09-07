class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 1: return True

        new_s = ""
        
        for i in range(len(s)):
          # 使用 str.isalnum() 判斷是否為字母或數字，是的話就加入 new_s
          if str.isalnum(s[i]) :
            new_s += s[i]
        # 取得 new_s 的長度的一半    
        new_s_len = len(new_s) // 2
        
        # 如果 new_s 是空的，代表是空字串，回傳 True
        if len(new_s) == 0: return True

        # 如果 new_s 的前半部分等於 new_s 的後半部分，回傳 True
        if (new_s[:new_s_len]).lower() == (new_s[::-1][:new_s_len]).lower():
            return True
        
        return False