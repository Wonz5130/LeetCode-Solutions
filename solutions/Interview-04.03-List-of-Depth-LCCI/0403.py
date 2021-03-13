# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def listOfDepth(self, tree: TreeNode) -> List[ListNode]:
        import collections

        if not tree:
            return []
        
        queue = collections.deque()
        queue.append(tree)
        res = []
        # BFS
        while queue:
            n = len(queue)
            for i in range(n):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                # 当前层的第一个节点
                if i == 0:
                    # 头节点
                    head = ListNode(node.val)
                    tmp = head
                else:
                    tmp.next = ListNode(node.val)
                    tmp = tmp.next
            # 这里加入res的是head
            res.append(head)
        return res