# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        import collections
        if not root:
            return []
        
        res, q = [], collections.deque()
        # 做奇偶判断
        flag = False
        q.append(root)
        while q:
            # 输出是二维数组
            temp = []
            flag = not flag
            for x in range(len(q)):
                node = q.popleft()
                # 尾插
                if flag:
                    temp.append(node.val)
                # 头插
                else:
                    temp.insert(0, node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(temp)
        return res