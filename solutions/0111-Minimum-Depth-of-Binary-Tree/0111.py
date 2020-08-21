# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        # solution one: DFS
        # 根为空
        if not root:
            return 0
        
        # 左右子树都为空
        if not root.left and not root.right:
            return 1
        
        min_depth = 10**9
        if root.left:
            min_depth = min(self.minDepth(root.left), min_depth)
        if root.right:
            min_depth = min(self.minDepth(root.right), min_depth)
        
        return min_depth + 1

        # solution two: BFS
        import collections
        # 根为空
        if not root:
            return 0
        
        que = collections.deque([(root, 1)])
        while que:
            node, depth = que.popleft()
            # 到达叶子节点
            if not node.left and not node.right:
                return depth
            if node.left:
                que.append((node.left, depth + 1))
            if node.right:
                que.append((node.right, depth + 1))
        
        return 0