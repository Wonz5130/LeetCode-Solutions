# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        def dfs(root):
            nonlocal sumval
            if root:
                dfs(root.right)
                sumval += root.val
                root.val = sumval  # 将BST转化成累加树
                dfs(root.left)
        
        sumval = 0
        dfs(root)
        return root