# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not postorder:
            return None
        root = TreeNode(postorder[-1])

        # 根在中序遍历中的索引
        i = inorder.index(root.val)
        # left: inorder[0] ~ inorder[i-1], postorder[0] ~ postorder[i-1]
        root.left = self.buildTree(inorder[:i], postorder[:i])
        # right: inorder[i+1] ~ inorder[-1], postorder[i] ~ postorder[-2]
        root.right = self.buildTree(inorder[i+1:], postorder[i:-1])

        return root