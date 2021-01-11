# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ancestor = root
        while True:
            # p q 在左边
            if p.val < ancestor.val and q.val < ancestor.val:
                ancestor = ancestor.left
            # p q 在右边
            elif p.val > ancestor.val and q.val > ancestor.val:
                ancestor = ancestor.right
            # p q 分别在左右，当前节点就是最近公共祖先
            else:
                break
        return ancestor