# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        # 递归
        res = []
        def dfs(root):
            if not root:
                return []
            dfs(root.left)
            dfs(root.right)
            res.append(root.val)
        
        dfs(root)
        return res

        # 迭代
        res = []
        if not root:
            return res
        stack = []
        node = root
        while stack or node:
            while node:
                # 根节点入栈
                stack.append(node)
                # 左子树存在
                if node.left:
                    node = node.left
                # 左子树不存在，转右子树
                else:
                    node = node.right
            # 取出栈顶元素
            node = stack.pop()
            res.append(node.val)
            # 栈不为空且当前节点是栈顶元素的左节点
            # stack[-1]就是取出的栈顶元素：node
            if stack and node == stack[-1].left:
                node = stack[-1].right
            # 没有左子树或右子树，退栈
            else:
                node = None
        return res