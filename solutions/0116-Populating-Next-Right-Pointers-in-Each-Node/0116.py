"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        
        # 将每两个相邻节点连接起来
        def connectTwoNode(node1: 'Node', node2: 'Node'):
            if not node1 or not node2:
                return
            
            node1.next = node2
            
            # 链接相同父节点的两个子节点
            connectTwoNode(node1.left, node1.right)
            connectTwoNode(node2.left, node2.right)
            # 链接不同父节点的两个子节点
            connectTwoNode(node1.right, node2.left)

        connectTwoNode(root.left, root.right)
        return root