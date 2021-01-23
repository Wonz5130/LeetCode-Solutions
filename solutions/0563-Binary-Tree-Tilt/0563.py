# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: TreeNode) -> int:
        # 后序遍历
        def dfs(root):
            nonlocal res
            if not root:
                return 0
            # if root.left:
            left = dfs(root.left)
            # if root.right:
            right = dfs(root.right)
            res += abs(left - right)
            return root.val + left + right
        
        res = 0
        dfs(root)
        return res