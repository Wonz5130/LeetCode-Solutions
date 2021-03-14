# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> TreeNode:
        if not root:
            return None
        
        # p >= root，后继节点在右子树
        if root.val <= p.val:
            return self.inorderSuccessor(root.right, p)
        else:
            # 左子树不为空
            if self.inorderSuccessor(root.left, p):
                return self.inorderSuccessor(root.left, p)
            # 左子树为空，当前节点就是后继节点
            else:
                return root