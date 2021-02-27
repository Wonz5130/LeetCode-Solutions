# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def printTree(self, root: TreeNode) -> List[List[str]]:
        # 求最大深度
        def maxDepth(root):
            if not root:
                return 0
            left = maxDepth(root.left)
            right = maxDepth(root.right)
            return 1 + max(left, right)
        
        depth = maxDepth(root)
        # 二维矩阵宽度
        wid = 2**depth - 1
        res = [[''] * wid for _ in range(depth)]

        # DFS
        def dfs(root, depth, start, end):
            # 当前根节点放在(start+end)/2这个中间位置
            res[depth - 1][(start + end) // 2] = str(root.val)
            if root.left:
                dfs(root.left, depth + 1, start, (start + end) // 2)
            if root.right:
                dfs(root.right, depth + 1, (start + end) // 2, end)
        
        dfs(root, 1, 0, wid)
        return res