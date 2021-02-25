# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        import collections
        res = []
        counter = collections.Counter()

        def traverse(root):
            if not root:
                return '#'
            # 后序遍历
            left = traverse(root.left)
            right = traverse(root.right)
            chain = left + ',' + right + ',' + str(root.val)
            counter[chain] += 1
            # 统计出现两次即是重复子树，加入res
            if counter[chain] == 2:
                res.append(root)
            return chain
        
        traverse(root)
        return res