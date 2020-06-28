> LeetCode 0450. Delete Node in a BST 删除二叉搜索树中的节点【Medium】【Python】【二叉树】

### Problem

[LeetCode](https://leetcode.com/problems/delete-node-in-a-bst/)

Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.

Basically, the deletion can be divided into two stages:

1. Search for a node to remove.
2. If the node is found, delete the node.

**Note:** Time complexity should be O(height of tree).

**Example:**

```
root = [5,3,6,2,4,null,7]
key = 3

    5
   / \
  3   6
 / \   \
2   4   7

Given key to delete is 3. So we find the node with value 3 and delete it.

One valid answer is [5,4,6,2,null,null,7], shown in the following BST.

    5
   / \
  4   6
 /     \
2       7

Another valid answer is [5,2,6,null,4,null,7].

    5
   / \
  2   6
   \   \
    4   7
```

### 问题

[力扣](https://leetcode-cn.com/problems/delete-node-in-a-bst/)

给定一个二叉搜索树的根节点 root 和一个值 key，删除二叉搜索树中的 key 对应的节点，并保证二叉搜索树的性质不变。返回二叉搜索树（有可能被更新）的根节点的引用。

一般来说，删除节点可分为两个步骤：

1. 首先找到需要删除的节点；
2. 如果找到了，删除它。

**说明：** 要求算法时间复杂度为 O(h)，h 为树的高度。

**示例:**

```
root = [5,3,6,2,4,null,7]
key = 3
    5
   / \
  3   6
 / \   \
2   4   7

给定需要删除的节点值是 3，所以我们首先找到 3 这个节点，然后删除它。

一个正确的答案是 [5,4,6,2,null,null,7], 如下图所示。

    5
   / \
  4   6
 /     \
2       7

另一个正确答案是 [5,2,6,null,4,null,7]。
   5
  / \
  2   6
   \   \
    4   7
```

### 思路

**二叉树**

##### Python3代码

```python
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
```

### GitHub链接

[Python](https://github.com/Wonz5130/LeetCode-Solutions/blob/master/solutions/0450-Delete-Node-in-a-BST/0450.py)