# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def tree2str(self, t: TreeNode) -> str:
        def dfs(root):
            if not root:
                return ''
            # 左子树为空右子树不为空，要加一个()
            if not root.left and root.right:
                return str(root.val) + '()' + '(' + dfs(root.right) + ')'
            # 左子树不为空右子树为空
            elif root.left and not root.right:
                return str(root.val) + '(' + dfs(root.left) + ')'
            # 左右子树都为空
            elif not root.left and not root.right:
                return str(root.val)
            return str(root.val) + '(' + dfs(root.left) + ')' + '(' + dfs(root.right) + ')'
        
        return dfs(t)