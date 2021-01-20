# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        # solution one: dfs遍历取节点值，再单独计算最小绝对差
        def dfs(root):
            if not root:
                return
            # 中序遍历是递增的
            if root.left:
                dfs(root.left)
            tmp_val.append(root.val)
            if root.right:
                dfs(root.right)
        tmp_val = []
        dfs(root)
        res = float("inf")
        for i in range(len(tmp_val) - 1):
            res = min(res, abs(tmp_val[i] - tmp_val[i + 1]))
        return res

        # solution two: dfs遍历直接进行绝对值比较
        pre = -1
        res = float("inf")
        def dfs(root):
            nonlocal pre, res
            if not root:
                return
            # 中序遍历是递增的
            if root.left:
                dfs(root.left)
            if pre != -1:
                res = min(res, abs(pre - root.val))
            pre = root.val
            if root.right:
                dfs(root.right)
        dfs(root)
        return res