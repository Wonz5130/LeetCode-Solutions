# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        # 树为空
        if root == None:
            return None
        # 找到 key，进行删除
        if root.val == key:
            # 情况 1：两个子节点都为空
            # 情况 2：只有一个非空子节点，让这个孩子取代自己
            if root.left == None:
                return root.right
            if root.right == None:
                return root.left
            # 情况 3：有两个非空子节点，找到左子树的最大值，或者右子树的最小值，取代自己
            # Python3 需要先有一个 TreeNode 对象
            minNode = TreeNode(None)
            minNode = self.getMin(root.right)
            root.val = minNode.val
            root.right = self.deleteNode(root.right, minNode.val)
        # key 在左子树
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        # key 在右子树
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        return root
    
    def getMin(self, node: TreeNode):
        # BST 最左边的是最小值
        while node.left != None:
            node = node.left
        return node