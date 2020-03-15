# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from typing import List

class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        if not root:
            return
        return self.build(self.dfs(root))
    
    # 二叉搜索树转数组
    def dfs(self, root):
        if not root:
            return []
        return self.dfs(root.left) + [root.val] + self.dfs(root.right)
    
    # 数组二分构建平衡二叉树
    def build(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None
        mid = len(nums) // 2
        node = TreeNode(nums[mid])

        left = nums[:mid]
        right = nums[mid+1:]

        node.left = self.build(left)
        node.right = self.build(right)
        
        return node