from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # 若 digits 為空，則直接回傳
        if len(digits) == 0: return digits

        # 將 digits 反轉，由最後一位開始加 1
        re_digits = digits[::-1]
        re_digits[0] += 1

        # 從頭開始檢查是否有進位，有則將進位加到下一位
        # 再判斷目前 index 是否超過 digits 長度，若超過則在最後面加上 1
        # 最後再將 digits 反轉回來回傳結果
        for i in range(len(re_digits)):
            if re_digits[i] > 9:
                re_digits[i] %= 10
                if i + 1 >= len(re_digits):
                    re_digits.append(1)
                    break
                else:
                    re_digits[i + 1] += 1
        return re_digits[::-1]