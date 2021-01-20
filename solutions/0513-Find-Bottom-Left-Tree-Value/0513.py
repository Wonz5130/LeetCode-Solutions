# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        import collections
        q = collections.deque()
        q.append(root)
        while q:
            node = q.popleft()
            # 先右后左
            if node.right:
                q.append(node.right)
            if node.left:
                q.append(node.left)
        # 最后一个必是最左下角的节点
        return node.val