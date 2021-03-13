# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.isValid(root, None, None)

    # 辅助函数
    def isValid(self, root: TreeNode, min_: TreeNode, max_: TreeNode):
        if not root:
            return True
        if min_ != None and root.val <= min_.val:
            return False
        if max_ != None and root.val >= max_.val:
            return False
        return self.isValid(root.left, min_, root) and self.isValid(root.right, root, max_)