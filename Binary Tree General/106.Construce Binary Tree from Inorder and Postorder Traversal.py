from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        # Inorder = [9, 3, 15, 20, 7]
        # Postorder = [9, 15, 7, 20, 3]
        if not inorder or not postorder: return None

        # 建立一個 Dict，用來保存中序遍歷中每個節點的索引
        # [9, 3, 15, 20, 7] -> {9: 0, 3: 1, 15: 2, 20: 3, 7: 4}
        inorder_map = {val: index for index, val in enumerate(inorder)}

        def build(in_start: int, in_end: int, post_start: int, post_end: int) -> Optional[TreeNode]:
            """
              建立一個遞迴 Function 用來構建 Binary Tree

              Args:
                in_start: Inorder index of the start node
                in_end: Inorder index of the end node
                post_start: Postorder index of the start node
                post_end: Postorder index of the end node

              Returns:
                Optional[TreeNode]: 回傳構建好的 Binary Tree
            """
            if in_start > in_end: return None

            # 取得 Postorder 的最後一個節點作為根節點
            root_val = postorder[post_end]

            # 建立根節點
            root = TreeNode(root_val)

            # 取得根節點在 Inorder 的 index
            in_index = inorder_map[root_val]

            # 計算左子樹的節點數量
            # Inorder 特性：根節點左邊的節點都是左子樹的節點
            left_size = in_index - in_start

            # 遞迴構建左子樹
            # 從 Inorder 的 start index 開始，到 Inorder 的根節點的前一個節點
            # 從 Postorder 的 start index 開始，到 Postorder 的左子樹節點數量
            root.left = build(in_start, in_index - 1, post_start,  post_start + left_size - 1)

            # 遞迴構建右子樹
            # 從 Inorder 的根節點的下一個節點開始，到 Inorder 的最後一個節點
            # 從 Postorder 的左子樹節點數量 + 1 開始，到 Postorder 的最後一個節點的前一個節點
            root.right = build(in_index + 1, in_end, post_start + left_size, post_end - 1)

            return root
        
        return build(0, len(inorder) - 1, 0, len(postorder) - 1)