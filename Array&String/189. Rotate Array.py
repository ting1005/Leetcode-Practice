from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 透過取餘數的方式來計算實際需要移動的步數
        # 例如 nums = [1, 2, 3, 4, 5, 6, 7]，k = 3
        # 則 nums_len = 7，k % nums_len = 3
        # temp = nums[:4] = [1, 2, 3, 4]
        # nums += temp = [1, 2, 3, 4, 5, 6, 7, 1, 2, 3, 4]
        # del nums[:4] = [5, 6, 7, 1, 2, 3, 4]
        
        nums_len = len(nums)
        k = k % nums_len
        temp = nums[:nums_len - k]
        nums += temp
        del nums[:nums_len - k]