# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        # solution one: 后序+剪枝
        def recur(root):
            if not root:
                return 0
            left = recur(root.left)
            if left == -1:
                return -1
            right = recur(root.right)
            if right == -1:
                return -1
            # 左右子树深度差 <= 1，符合平衡二叉树
            return max(left, right) + 1 if abs(left - right) <= 1 else -1
        
        # 若 recur(root) != -1，说明平衡
        return recur(root) != -1

        # solution two: 前序+判断深度
        # 特判：root 为空
        if not root:
            return True
        # 当前子树是否平衡
        # 当前子树的左子树是否平衡
        # 当前子树的右子树是否平衡
        return abs(self.depth(root.left) - self.depth(root.right)) <= 1 and \
            self.isBalanced(root.left) and self.isBalanced(root.right)
    
    # 计算深度
    def depth(self, root):
        if not root:
            return 0
        return max(self.depth(root.left), self.depth(root.right)) + 1
