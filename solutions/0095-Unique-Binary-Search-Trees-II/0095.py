# from typing import List

# # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        if n == 0:
            return []
        else:
            return self.generateTreesDFS(1, n)
    
    # DFS
    def generateTreesDFS(self, left, right):
        if left > right:
            return [None]
        ans = []
        for i in range(left, right + 1):
            left_nodes = self.generateTreesDFS(left, i -  1)  # all possible left subtrees if i is choosen to be a root
            right_nodes = self.generateTreesDFS(i + 1, right)  # all possible right subtrees if i is choosen to be a root
            for left_node in left_nodes:
                for right_node in right_nodes:
                    root = TreeNode(i)
                    root.left = left_node
                    root.right = right_node
                    ans.append(root)
        return ans