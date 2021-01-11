"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        import collections
        res = []
        if not root:
            return res
        
        q = collections.deque()
        q.append(root)
        # BFS
        while q:
            tmp = []
            for _ in range(len(q)):
                node = q.popleft()
                tmp.append(node.val)
                # 使用extend在列表末尾一次追加多个值
                q.extend(node.children)
            res.append(tmp)
        return res