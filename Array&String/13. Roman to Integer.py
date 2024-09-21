class Solution:
    def romanToInt(self, s: str) -> int:
        # 先將羅馬數字與整數的對應關係存入 Dictionary
        roman_dict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        result = 0
        index = len(s) - 1
        
        # 從右至左遍歷羅馬數字
        # 如果當前羅馬數字比右邊的羅馬數字小，則減去當前羅馬數字，否則加上當前羅馬數字

        for index in range(len(s)):
            if index < len(s) - 1 and roman_dict[s[index]] < roman_dict[s[index + 1]]:
                result -= roman_dict[s[index]]
            else: 
                result += roman_dict[s[index]]
        
        return result