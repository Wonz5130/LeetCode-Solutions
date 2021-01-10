# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        # 递归
        res = []
        def dfs(root):
            if not root:
                return []
            res.append(root.val)
            dfs(root.left)
            dfs(root.right)
        
        dfs(root)
        return res

        # 迭代
        res = []
        if not root:
            return res
        stack = []
        node = root
        while stack or node:
            while node:
                res.append(node.val)
                stack.append(node)
                # 前序遍历
                node = node.left
            node = stack.pop()
            node = node.right
        return res