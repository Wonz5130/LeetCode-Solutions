# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:
        if not root:
            return
        
        # 将原先整棵树作为 v 的左子树
        if d == 1:
            node = TreeNode(v)
            node.left = root
            return node
        
        if d == 2:
            # 新左节点
            L = TreeNode(v)
            # 新右节点
            R = TreeNode(v)

            L.left = root.left
            R.right = root.right

            root.left = L
            root.right = R
            return root
        
        # d > 2 不断分解
        self.addOneRow(root.left, v, d - 1)
        self.addOneRow(root.right, v, d - 1)
        return root