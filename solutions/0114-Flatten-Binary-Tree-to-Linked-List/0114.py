# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        
        # 递归调用
        self.flatten(root.left)
        self.flatten(root.right)

        # 后序遍历：左-右-根
        # 左右子树拉平成链表
        left = TreeNode()
        left = root.left
        right = TreeNode()
        right = root.right

        # 左子树作为右子树
        root.left = None
        root.right = left

        # 原先右子树接到当前右子树末端
        p = TreeNode()
        p = root
        # 找到当前右子树末端
        while p.right != None:
            p = p.right
        p.right = right