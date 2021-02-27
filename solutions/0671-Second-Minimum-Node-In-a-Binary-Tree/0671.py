# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        if not root:
            return -1
        
        def dfs(root, val):
            if not root:
                return -1
            # 根据题意，最小元素一定是根节点，所以只要找到比根节点大的节点就行
            if root.val > val:
                return root.val
            left = dfs(root.left, val)
            right = dfs(root.right, val)
            if left == -1:
                return right
            if right == -1:
                return left
            return min(left, right)
        
        return dfs(root, root.val)