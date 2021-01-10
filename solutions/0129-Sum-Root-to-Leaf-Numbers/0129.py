# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        def dfs(root: TreeNode, sumNumber: int) -> int:
            if not root:
                return 0
            tmpsum = sumNumber * 10 + root.val
            # 叶子节点
            if not root.left and not root.right:
                return tmpsum
            else:
                return dfs(root.left, tmpsum) + dfs(root.right, tmpsum)
        
        return dfs(root, 0)