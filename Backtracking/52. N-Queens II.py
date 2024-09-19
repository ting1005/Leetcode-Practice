class Solution:
    def totalNQueens(self, n: int) -> int:
        def backtrack(row: int) -> int:
            # 嘗試每次在當前行的每一列放置皇后，並判斷這個位置是否合法
            # 如果合法，則繼續放下一個皇后
            if row == n:  # 成功擺放所有皇后
                return 1
            count = 0
            for col in range(n):
                if col not in cols and (row - col) not in diag1 and (row + col) not in diag2:
                    # 放置皇后
                    cols.add(col)
                    diag1.add(row - col)
                    diag2.add(row + col)
                    count += backtrack(row + 1)  # 試圖放下一個皇后
                    # 回溯
                    cols.remove(col)
                    diag1.remove(row - col)
                    diag2.remove(row + col)
            return count

        # 紀錄不能擺放皇后的列與對角線
        # 紀錄每一列是否有皇后
        cols = set()  
        # 紀錄左斜對角線 (row - col)
        diag1 = set()
        # 紀錄右斜對角線 (row + col)  
        diag2 = set()  
        
        return backtrack(0)