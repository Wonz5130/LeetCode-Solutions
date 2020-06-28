> LeetCode 0701. Insert into a Binary Search Tree 二叉搜索树中的插入操作【Medium】【Python】【二叉树】

### Problem

[LeetCode](https://leetcode.com/problems/insert-into-a-binary-search-tree/)

Given the root node of a binary search tree (BST) and a value to be inserted into the tree, insert the value into the BST. Return the root node of the BST after the insertion. It is guaranteed that the new value does not exist in the original BST.

Note that there may exist multiple valid ways for the insertion, as long as the tree remains a BST after insertion. You can return any of them.

For example, 

```
Given the tree:
        4
       / \
      2   7
     / \
    1   3
And the value to insert: 5
```

You can return this binary search tree:

```
         4
       /   \
      2     7
     / \   /
    1   3 5
```

This tree is also valid:

```
         5
       /   \
      2     7
     / \   
    1   3
         \
          4
```

**Constraints:**

- The number of nodes in the given tree will be between `0` and `10^4`.
- Each node will have a unique integer value from `0` to -`10^8`, inclusive.
- `-10^8 <= val <= 10^8`
- It's guaranteed that `val` does not exist in the original BST.

### 问题

[力扣](https://leetcode-cn.com/problems/insert-into-a-binary-search-tree/)

给定二叉搜索树（BST）的根节点和要插入树中的值，将值插入二叉搜索树。 返回插入后二叉搜索树的根节点。 保证原始二叉搜索树中不存在新值。

注意，可能存在多种有效的插入方式，只要树在插入后仍保持为二叉搜索树即可。 你可以返回任意有效的结果。

例如, 

给定二叉搜索树:

        4
       / \
      2   7
     / \
    1   3

和 插入的值: 5
你可以返回这个二叉搜索树:

         4
       /   \
      2     7
     / \   /
    1   3 5
或者这个树也是有效的:

         5
       /   \
      2     7
     / \   
    1   3
         \
          4

### 思路

**二叉树**

##### Python3代码

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        # 找到空位置
        if not root:
            return TreeNode(val)
        if root.val < val:
            root.right = self.insertIntoBST(root.right, val)
        if root.val > val:
            root.left = self.insertIntoBST(root.left, val)
        return root
```

### GitHub链接

[Python](https://github.com/Wonz5130/LeetCode-Solutions/blob/master/solutions/0701-Insert-into-a-Binary-Search-Tree/0701.py)