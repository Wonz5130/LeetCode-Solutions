> LeetCode 0222. Count Complete Tree Nodes完全二叉树的节点个数【Medium】【Python】【二叉树】

## Problem

[LeetCode](https://leetcode.com/problems/count-complete-tree-nodes/)

Given a **complete** binary tree, count the number of nodes.

**Note:**

**Definition of a complete binary tree from [Wikipedia](http://en.wikipedia.org/wiki/Binary_tree#Types_of_binary_trees):**
In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2^h nodes inclusive at the last level h.

**Example:**

```
Input: 
    1
   / \
  2   3
 / \  /
4  5 6

Output: 6
```

## 问题

[力扣](https://leetcode-cn.com/problems/count-complete-tree-nodes/)

给出一个**完全二叉树**，求出该树的节点个数。

**说明：**

完全二叉树的定义如下：在完全二叉树中，除了最底层节点可能没填满外，其余每层节点数都达到最大值，并且最下面一层的节点都集中在该层最左边的若干位置。若最底层为第 h 层，则该层包含 1~ 2^h 个节点。

示例:

```
输入: 
    1
   / \
  2   3
 / \  /
4  5 6

输出: 6
```

## 思路

**中序遍历**

```
普通二叉树：遍历一遍左右子树
满二叉树：节点总数与高度呈指数关系
完全二叉树：结合普通二叉树与满二叉树
```

**时间复杂度**

时间复杂度是 O(logN*logN)

因为一棵完全二叉树中，必存在一棵子树是满二叉树。因此，肯定会触发 heightleft == heightright 条件，所以递归深度就是树的高度，时间复杂度是 O(logN)。每次递归就是 while 循环，时间复杂度也是 O(logN)，总体时间复杂度就是 O(logN*logN)。

### Python3 代码

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        l = TreeNode(None)
        l = root
        r = TreeNode(None)
        r = root
        heightleft, heightright = 0, 0  # 记录左右子树的高度
        while l != None:
            l = l.left
            heightleft += 1
        while r != None:
            r = r.right
            heightright += 1
        
        # 如果左右子树高度相同，则是一棵满二叉树
        if heightleft == heightright:
            return 2**heightleft - 1
        
        # 如果左右子树高度不相同，则是按普通二叉树计算
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
```

## GitHub 链接

[Python](https://github.com/Wonz5130/LeetCode-Solutions/blob/master/solutions/0222-Count-Complete-Tree-Nodes/0222.py)