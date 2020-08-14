"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""
class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        def dfs(cur):
            if not cur:
                return
            # 递归左子树
            dfs(cur.left)
            # 修改节点引用
            if self.pre:
                self.pre.right, cur.left = cur, self.pre
            # 记录头节点
            else:
                self.head = cur
            # 保存 cur
            self.pre = cur
            # 递归右子树
            dfs(cur.right)
        
        # 特例处理：root为空
        if not root:
            return
        # 空节点
        self.pre = None
        # 转为双向链表
        dfs(root)
        # 构建循环链表
        self.head.left, self.pre.right = self.pre, self.head
        return self.head