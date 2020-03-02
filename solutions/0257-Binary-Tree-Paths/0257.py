# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []
        ans = []
        self.dfs(root, ans, '' + str(root.val))
        return ans

    def dfs(self, root, ans, path):
        if root.left == None and root.right == None:
            ans.append(path)
        if root.left != None:
            self.dfs(root.left, ans, path + '->' + str(root.left.val))
        if root.right != None:
            self.dfs(root.right, ans, path + '->' + str(root.right.val))