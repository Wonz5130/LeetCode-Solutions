"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        # DFS
        res = []
        def dfs(root):
            if not root:
                return
            for child in root.children:
                dfs(child)
            res.append(root.val)
            
        dfs(root)
        return res

        # BFS
        if not root:
            return []

        q = [root]
        res = []
        while q:
            # 弹出列表尾部的一个元素
            node = q.pop()
            res.append(node.val)
            # 顺序加入
            for child in node.children:
                q.append(child)
        return res[::-1]