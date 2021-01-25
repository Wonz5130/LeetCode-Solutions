"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        # DFS
        res = []
        def dfs(root):
            if not root:
                return
            res.append(root.val)
            for child in root.children:
                dfs(child)
            
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
            # 逆序加入，从右到左
            for child in node.children[::-1]:
                q.append(child)
        return res