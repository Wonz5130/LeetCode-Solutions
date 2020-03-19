# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        # solution one: 递归
        if not root:
            return None
        # 叶子节点，直接返回自己
        if not root.left and not root.right:
            return root
        
        # 交换非叶子节点的左右两棵子树
        root.left, root.right = root.right, root.left
        if root.left:
            self.invertTree(root.left)
        if root.right:
            self.invertTree(root.right)
        return root

        # solution two: 栈
        if not root:
            return None
        # 叶子节点，直接返回自己
        if not root.left and not root.right:
            return root
        
        # 栈模拟二叉树
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                node.left, node.right = node.right, node.left
                stack.append(node.right)
                stack.append(node.left)
        return root