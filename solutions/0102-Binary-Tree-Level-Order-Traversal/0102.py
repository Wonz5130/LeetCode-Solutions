# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        # solution one: 非递归
        import collections
        if not root:
            return []
        
        res, q = [], collections.deque()
        q.append(root)
        while q:
            # 输出是二维数组
            temp = []
            for x in range(len(q)):
                node = q.popleft()
                temp.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(temp)
        return res

        # solution two: 递归
        res = []
        
        def helper(root, depth):
            if not root:
                return
            if len(res) == depth:
                res.append([])
            res[depth].append(root.val)
            helper(root.left, depth + 1)
            helper(root.right, depth + 1)
        helper(root , 0)
        return res