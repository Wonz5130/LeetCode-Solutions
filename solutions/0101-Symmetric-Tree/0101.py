# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def recur(L, R):
            # 左右子树都为空
            if not L and not R:
                return True
            # 有一个不为空
            if not L or not R or L.val != R.val:
                return False
            # L的左子树和R的右子树，L的右子树和R的左子树
            return recur(L.left, R.right) and recur(L.right, R.left)
        
        # 特判：root为空
        if not root:
            return True
        return recur(root.left, root.right)