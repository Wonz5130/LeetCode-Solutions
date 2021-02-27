# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0
        # 分别是坐标和节点
        queue = [(0, root)]
        res = 1
        # BFS
        while queue:
            # 首末元素的坐标差就是最大宽度
            res = max(res, queue[-1][0] - queue[0][0] + 1)
            tmp = []
            for i, q in queue:
                if q.left:
                    tmp.append((i * 2, q.left))
                if q.right:
                    tmp.append((i * 2 + 1, q.right))
            queue = tmp
        return res