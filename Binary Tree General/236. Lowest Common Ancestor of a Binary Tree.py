class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # 如果 root 為空或是 root 等於 p 或 q 表示找到其中一個節點，可以直接回傳root
        if not root or root == p or root == q: return root

        # 分別從左右子樹找 p 或 q，找最近的共同祖先
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        # 如果左右子樹都找到 p 或 q，表示 root 是最近的共同祖先
        if left and right: return root

        # 如果只有左子樹找到 p 或 q，回傳左子樹的結果，反之亦然
        return left or right