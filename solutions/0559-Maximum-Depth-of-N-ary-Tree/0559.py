"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        # DFS
        if not root:
            return 0
        depth = 0
        for child in root.children:
            depth = max(self.maxDepth(child), depth)
        return depth + 1

        # BFS
        import collections
        # 特判，不写会报错
        if not root:
            return 0
        
        q = collections.deque()
        q.append(root)
        depth = 0
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                for child in node.children:
                    q.append(child)
            depth += 1
        return depth