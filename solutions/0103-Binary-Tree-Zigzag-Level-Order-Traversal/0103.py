# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        import collections
        if not root:
            return []
        
        res, q = [], collections.deque()
        flag = False  # 做奇偶判断
        q.append(root)
        
        while q:
            temp = []
            flag = not flag
            for _ in range(len(q)):
                node = q.popleft()
                # 头插
                if flag:
                    temp.append(node.val)
                # 尾插
                else:
                    temp.insert(0, node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(temp)
        
        return res