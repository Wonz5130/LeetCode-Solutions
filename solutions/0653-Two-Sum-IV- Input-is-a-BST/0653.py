# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        # 中序遍历是递增序列
        def inorder(root):
            if not root:
                return []
            return inorder(root.left) + [root.val] + inorder(root.right)
        
        val = inorder(root)
        # 双指针
        left, right = 0, len(val) - 1
        while left < right:
            sumVal = val[left] + val[right]
            if sumVal == k:
                return True
            elif sumVal > k:
                right -= 1
            else:
                left += 1
        return False