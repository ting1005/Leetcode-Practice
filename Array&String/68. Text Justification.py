from typing import List


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        result, line, width = [], [], 0

        for word in words:
            # 如果當前行的寬度加上當前單詞的長度和當前行的長度大於最大寬度
            if width + len(word) + len(line) > maxWidth:
                # 利用迴區計算出需要填充的空格數
                for i in range(maxWidth - width):
                    # 如果當前行只有一個單詞，則將空格添加到當前行的最後
                    line[i % (len(line) - 1 or 1)] += " "
                # 將當前行的單詞組合成一個字符串，並添加到結果列表中    
                result.append(''.join(line))
                line, width = [], 0
            # 將當前單詞添加到當前行中
            line.append(word)
            width += len(word)
        # 最後一行的處理，使用ljust函數將最後一行的空格填充到最大寬度
        result.append(" ".join(line).ljust(maxWidth))
        
        return result