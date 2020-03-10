# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.max = 0
        self.depth(root)
        return self.max
    
    def depth(self, root):
        if not root:
            return 0
        l = self.depth(root.left)
        r = self.depth(root.right)
        # 更新最大值
        self.max = max(self.max, l + r)
        # 返回高度
        return max(l, r) + 1