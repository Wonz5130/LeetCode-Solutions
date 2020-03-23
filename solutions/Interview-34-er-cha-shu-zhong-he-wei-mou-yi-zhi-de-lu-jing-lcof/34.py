# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        res, path = [], []

        # 先序遍历：根左右
        def recur(root, target):
            if not root:
                return
            
            path.append(root.val)
            target -= root.val
            # 找到路径
            if target == 0 and not root.left and not root.right:
                res.append(list(path))  # 复制了一个 path 加入到 res 中，这样修改 path 不影响 res
            recur(root.left, target)
            recur(root.right, target)
            # 向上回溯，需要删除当前节点
            path.pop()
        
        recur(root, sum)
        return res