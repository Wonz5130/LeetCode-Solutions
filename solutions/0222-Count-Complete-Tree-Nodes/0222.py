# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        l = TreeNode(None)
        l = root
        r = TreeNode(None)
        r = root
        heightleft, heightright = 0, 0  # 记录左右子树的高度
        while l != None:
            l = l.left
            heightleft += 1
        while r != None:
            r = r.right
            heightright += 1
        
        # 如果左右子树高度相同，则是一棵满二叉树
        if heightleft == heightright:
            return 2**heightleft - 1
        
        # 如果左右子树高度不相同，则是按普通二叉树计算
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)