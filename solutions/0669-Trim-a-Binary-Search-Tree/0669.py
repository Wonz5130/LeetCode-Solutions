# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: TreeNode, low: int, high: int) -> TreeNode:
        if not root:
            return
        # 只需考虑根节点需要做什么，其他的交给递归
        # 左边的全部小于low，所以都剪枝
        if root.val < low:
            root = root.right
            root = self.trimBST(root, low, high)
        # 右边的全部大于high，所以都剪枝
        elif root.val > high:
            root = root.left
            root = self.trimBST(root, low, high)
        else:
            root.left = self.trimBST(root.left, low, high)
            root.right = self.trimBST(root.right, low, high)
        return root