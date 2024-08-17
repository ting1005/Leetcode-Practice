from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []
        # 建立數字與字母的對應關係
        mapping = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        def backtrack(combination: str, next_digits: str) -> None:
            """
            將數字轉換成字母
            判斷 next_digits 是否為空，如果是則將 combination 加入到 result 中
            否則透過迴圈來將 next_digits 的第一個數字轉換成字母，並且呼叫自己
            例如 digits = "23"
            第一次呼叫 backtrack("", "23")
            combination = ""，next_digits = "23"
            第二次呼叫 backtrack("a", "3")
            combination = "a"，next_digits = "3"
            第三次呼叫 backtrack("ad", "")
            combination = "ad"，next_digits = ""
            因此 result = ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]

            args: 
                combination: str, 目前的字母組合
                next_digits: str, 下一個數字
            return:
                None
            """
            if len(next_digits) == 0:
                result.append(combination)
            else:
                for letter in mapping[next_digits[0]]:
                    backtrack(combination + letter, next_digits[1:])

        result = []
        backtrack("", digits)
        return result