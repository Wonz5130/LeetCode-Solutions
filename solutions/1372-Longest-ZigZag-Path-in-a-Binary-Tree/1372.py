# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def longestZigZag(self, root: TreeNode) -> int:
        if root == None:
            return 0
        self.max_ = 0
        self.dfs(root, 0, 0)
        return self.max_
    
    def dfs(self, root, prev, depth):
        self.max_ = max(depth, self.max_)

        if root.left:
            # left->left
            if prev == 0:
                self.dfs(root.left, 0, 1)
            # left->right
            else:
                self.dfs(root.left, 0, depth + 1)
        if root.right:
            # right->right
            if prev == 1:
                self.dfs(root.right, 1, 1)
            # right->left
            else:
                self.dfs(root.right, 1, depth + 1)