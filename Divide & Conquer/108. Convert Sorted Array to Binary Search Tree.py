from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def helper(start: int, end: int) -> Optional[TreeNode]:
            """
            建立一個遞迴函數來將排序過的數組轉換成二元搜尋樹
            如果 start 大於 end，則返回 None
            選擇中間的數字做為 TreeNode 的值，可以確保左右子樹的高度差不超過 1
            遞迴建立左右子樹
            """
            if start > end: return None
            mid = (start + end) // 2
            root = TreeNode(nums[mid])
            root.left = helper(start, mid - 1)
            root.right = helper(mid + 1, end)
            return root
        
        return helper(0, len(nums)-1)