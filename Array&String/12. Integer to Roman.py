class Solution:
    def intToRoman(self, num: int) -> str:
        # 建立一個 dict 來存放羅馬數字
        roman_dict = {
            1: "I",
            5: "V",
            4: "IV",
            10: "X",
            9: "IX",
            50: "L",
            40: "XL",
            100: "C",
            90: "XC",
            500: "D",
            400: "CD",
            1000: "M",
            900: "CM"
        }

        result = ""
        # 進行羅馬數字的轉換
        for n in [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]:
            # 當 num 大於等於 n 時，將 n 加入到 out 中，並將 num 減去 n
            while num >= n:
                result += roman_dict[n]
                num -= n
        return result