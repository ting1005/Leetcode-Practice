# Definition for a binary tree node.
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Preorder = [3,9,20,15,7]
        # Inorder = [9,3,15,20,7]

        if not preorder or not inorder: return None

        # 建立一個 Dict，用來保存中序遍歷中每個節點的索引
        # [9, 3, 15, 20, 7] -> {9: 0, 3: 1, 15: 2, 20: 3, 7: 4}
        inorder_map = {val: index for index, val in enumerate(inorder)}

        # 建立一個遞迴 Function 用來構建 Binary Tree
        # pre_start: Preorder index of the start node
        # pre_end: Preorder index of the end node
        # in_start: Inorder index of the start node
        # in_end: Inorder index of the end node
        def build(pre_start: int, pre_end: int, in_start: int, in_end: int) -> Optional[TreeNode]:
            # 如果 Preorder start > Preorder end 則返回 None
            if pre_start > pre_end: return None

            # 取出 Preoreder 的第一個節點作為根節點 (因為 Preorder 第一個index就是根節點)
            root_val = preorder[pre_start]

            # 建立根節點
            root = TreeNode(root_val)

            # 取得根節點在 Inorder 的 index
            in_index = inorder_map[root_val]
            
            # 計算左子樹的節點數量
            left_size = in_index - in_start

            # 遞迴構建左子樹
            # 從 Preorder 的下一個節點開始，到 Preorder 的左子樹節點數量
            # 從 Inorder 的 start index 開始，到 Inorder 的根節點的前一個節點
            root.left = build(pre_start + 1, pre_start + left_size, in_start, in_index - 1)

            # 遞迴構建右子樹
            # 從 Preorder 的左子樹節點數量 + 1 開始，到 Preorder 的最後一個節點
            # 從 Inorder 的根節點的下一個節點開始，到 Inorder 的最後一個節點
            root.right = build(pre_start + left_size + 1, pre_end, in_index + 1, in_end)

            return root
        
        return build(0, len(preorder) - 1, 0, len(inorder) - 1)