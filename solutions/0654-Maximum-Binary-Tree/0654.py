# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        # 特判
        if not nums:
            return None
        
        # 找到数组中的最大值和对应的索引
        maxVal = max(nums)
        maxIndex = nums.index(maxVal)
 
        root = TreeNode(nums[maxIndex])
        # 递归构造左右子树
        root.left = self.constructMaximumBinaryTree(nums[:maxIndex])
        root.right = self.constructMaximumBinaryTree(nums[maxIndex + 1:])
        
        return root