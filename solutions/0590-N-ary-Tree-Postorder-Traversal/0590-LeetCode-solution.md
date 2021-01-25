> LeetCode 0590. N-ary Tree Postorder Traversal N叉树的后序遍历【Easy】【Python】【二叉树】

## Problem

[LeetCode](https://leetcode.com/problems/n-ary-tree-postorder-traversal/)

Given an n-ary tree, return the *postorder* traversal of its nodes' values.

*Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value (See examples).*

**Follow up:**

Recursive solution is trivial, could you do it iteratively?

**Example 1:**

![img](https://assets.leetcode.com/uploads/2018/10/12/narytreeexample.png)

```
Input: root = [1,null,3,2,4,null,5,6]
Output: [5,6,3,2,4,1]
```

**Example 2:**

![img](https://assets.leetcode.com/uploads/2019/11/08/sample_4_964.png)

```
Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
Output: [2,6,14,11,7,3,12,8,4,13,9,10,5,1]
```

**Constraints:**

- The height of the n-ary tree is less than or equal to `1000`
- The total number of nodes is between `[0, 10^4]`

## 问题

[力扣](https://leetcode-cn.com/problems/n-ary-tree-postorder-traversal/)

给定一个 N 叉树，返回其节点值的后序遍历。

例如，给定一个 3叉树 :

 ![img](https://assets.leetcode.com/uploads/2018/10/12/narytreeexample.png)

返回其后序遍历: [5,6,3,2,4,1].

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
    def postorder(self, root: 'Node') -> List[int]:
        # DFS
        res = []
        def dfs(root):
            if not root:
                return
            for child in root.children:
                dfs(child)
            res.append(root.val)
            
        dfs(root)
        return res
```

**BFS**

```
遍历子树的时候加入顺序是类似根右左，因此最后要做一下逆序。
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
    def postorder(self, root: 'Node') -> List[int]:
        # BFS
        if not root:
            return []

        q = [root]
        res = []
        while q:
            # 弹出列表尾部的一个元素
            node = q.pop()
            res.append(node.val)
            # 顺序加入
            for child in node.children:
                q.append(child)
        return res[::-1]
```

## GitHub 链接

[Python](https://github.com/Wonz5130/LeetCode-Solutions/blob/master/solutions/0590-N-ary-Tree-Postorder-Traversal/0590.py)