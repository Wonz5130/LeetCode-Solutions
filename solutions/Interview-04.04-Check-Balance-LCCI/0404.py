# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        
        # 计算树的高度
        def height(root):
            if not root:
                return 0
            return max(height(root.left), height(root.right)) + 1
        
        # 不止根节点左右高度差小于等于1，左右子树也要满足平衡
        return abs(height(root.left) - height(root.right)) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)