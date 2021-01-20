# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        import collections
        if not root:
            return []
        res = []
        q = collections.deque()
        q.append(root)
        while q:
            size = len(q)
            tmp_max = -float('inf')
            # 取每一层最大值
            for i in range(size):
                node = q.popleft()
                tmp_max = max(tmp_max, node.val)
                # 一层树遍历完，加入该层最大值
                if i == size - 1:
                    res.append(tmp_max)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return res