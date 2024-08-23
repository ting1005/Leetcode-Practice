class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # s 存放結果
        # carry 用來記錄進位
        # i 和 j 分別用來遍歷 a 和 b
        s = []
        carry = 0
        i = len(a) - 1
        j = len(b) - 1

        
        while i >= 0 or j >= 0 or carry:
            # 分別判斷 i 和 j 是否大於等於 0
            # 如果是則將 a[i] 和 b[j] 轉換為整數，並加入 carry 中，i 和 j 各減 1
            # 將 carry % 2 加入 s 中，carry 除以 2
            if i >= 0:
                carry += int(a[i])
                i -= 1
            if j >= 0:
                carry += int(b[j])
                j -= 1

            s.append(str(carry % 2))
            carry //= 2

        return ''.join(reversed(s))
