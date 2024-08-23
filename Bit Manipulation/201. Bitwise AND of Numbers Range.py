class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        shift = 0
        # 找到 left 和 right 的公共前綴
        while left < right:
            left >>= 1
            right >>= 1
            shift += 1
            
        # 將公共前綴左移回去
        return left << shift