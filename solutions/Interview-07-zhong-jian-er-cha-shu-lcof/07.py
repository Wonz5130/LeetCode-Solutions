# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder:
            return None
        root = TreeNode(preorder[0])

        # 根在中序遍历中的索引
        i = inorder.index(root.val)
        # left: preorder[1] ~ preorder[i], inorder[0] ~ inorder[i-1]
        root.left = self.buildTree(preorder[1:i+1], inorder[:i])
        # right: preorder[i+1] ~ preorder[-1], inorder[i+1] ~ inorder[-1]
        root.right = self.buildTree(preorder[i+1:], inorder[i+1:])

        return root