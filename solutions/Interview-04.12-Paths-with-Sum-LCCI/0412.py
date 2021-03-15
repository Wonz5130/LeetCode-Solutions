# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        if not root:
            return 0
        return self.dfs(root, sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)
        
    def dfs(self, root, sum):
        # 要特判为空，否则下面 sum == root.val 会报错
        if not root:
            return 0

        res = 0
        if sum == root.val:
            res += 1
        res += self.dfs(root.left, sum - root.val)
        res += self.dfs(root.right, sum - root.val)
        return res