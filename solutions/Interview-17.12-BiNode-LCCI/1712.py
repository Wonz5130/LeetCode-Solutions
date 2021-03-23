# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def convertBiNode(self, root: TreeNode) -> TreeNode:
        def dfs(root):
            pre = cur = root
            if root:
                if root.left:
                    pre, cur = dfs(root.left)
                    # 左子树的下一个链表节点是当前root节点
                    cur.right = root
                    # 修改当前指针
                    cur = root
                    root.left = None
                if root.right:
                    root.right, cur = dfs(root.right)
            return pre, cur
        
        return dfs(root)[0]