# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        # 两棵树都为空
        if not p and not q:
            return True
        # 一棵树为空，另一棵不为空
        elif not p or not q:
            return False
        # 两棵树都非空，但节点值不同
        elif p.val != q.val:
            return False
        # 分别判断左子树和右子树
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)