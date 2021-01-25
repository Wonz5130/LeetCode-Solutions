> LeetCode 0589. N-ary Tree Preorder Traversal N叉树的前序遍历【Easy】【Python】【二叉树】

## Problem

[LeetCode](https://leetcode.com/problems/n-ary-tree-preorder-traversal/)

Given an n-ary tree, return the *preorder* traversal of its nodes' values.

*Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value (See examples).*

**Follow up:**

Recursive solution is trivial, could you do it iteratively?

**Example 1:**

![img](https://assets.leetcode.com/uploads/2018/10/12/narytreeexample.png)

```
Input: root = [1,null,3,2,4,null,5,6]
Output: [1,3,5,6,2,4]
```

**Example 2:**

![img](https://assets.leetcode.com/uploads/2019/11/08/sample_4_964.png)

```
Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
Output: [1,2,3,6,7,11,14,4,8,12,5,9,13,10]
```

**Constraints:**

- The height of the n-ary tree is less than or equal to `1000`
- The total number of nodes is between `[0, 10^4]`

## 问题

[力扣](https://leetcode-cn.com/problems/n-ary-tree-preorder-traversal/)

给定一个 N 叉树，返回其节点值的前序遍历。

例如，给定一个 3叉树 :

 ![img](https://assets.leetcode.com/uploads/2018/10/12/narytreeexample.png)

返回其前序遍历: [1,3,5,6,2,4]。

**说明:** 递归法很简单，你可以使用迭代法完成此题吗?

## 思路

**DFS**

### Python3 代码

```python
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        # DFS
        res = []
        def dfs(root):
            if not root:
                return
            res.append(root.val)
            for child in root.children:
                dfs(child)
            
        dfs(root)
        return res
```

**BFS**

```
遍历子树的时候选择的是逆序加入，因为是弹出尾部元素。
```

### Python3 代码

```python
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        # BFS
        if not root:
            return []

        q = [root]
        res = []
        while q:
            # 弹出列表尾部的一个元素
            node = q.pop()
            res.append(node.val)
            # 逆序加入，从右到左
            for child in node.children[::-1]:
                q.append(child)
        return res
```

## GitHub 链接

[Python](https://github.com/Wonz5130/LeetCode-Solutions/blob/master/solutions/0589-N-ary-Tree-Preorder-Traversal/0589.py)