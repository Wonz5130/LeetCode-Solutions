> LeetCode 0559. Maximum Depth of N-ary Tree N 叉树的最大深度【Easy】【Python】【二叉树】

## Problem

[LeetCode](https://leetcode.com/problems/maximum-depth-of-n-ary-tree/)

Given a n-ary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

*Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value (See examples).*

**Example 1:**

![img](https://assets.leetcode.com/uploads/2018/10/12/narytreeexample.png)

```
Input: root = [1,null,3,2,4,null,5,6]
Output: 3
```

**Example 2:**

![img](https://assets.leetcode.com/uploads/2019/11/08/sample_4_964.png)

```
Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
Output: 5
```

**Constraints:**

- The depth of the n-ary tree is less than or equal to `1000`.
- The total number of nodes is between `[0, 104]`.

## 问题

[力扣](https://leetcode-cn.com/problems/maximum-depth-of-n-ary-tree/)

给定一个 N 叉树，找到其最大深度。

最大深度是指从根节点到最远叶子节点的最长路径上的节点总数。

N 叉树输入按层序遍历序列化表示，每组子节点由空值分隔（请参见示例）。

**示例 1：**

![img](https://assets.leetcode.com/uploads/2018/10/12/narytreeexample.png)

```
输入：root = [1,null,3,2,4,null,5,6]
输出：3
```

**示例 2：**

![img](https://assets.leetcode.com/uploads/2019/11/08/sample_4_964.png)

```
输入：root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
输出：5
```

**提示：**

- 树的深度不会超过 1000 。
- 树的节点数目位于 [0, 10^4] 之间。

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
    def maxDepth(self, root: 'Node') -> int:
        # DFS
        if not root:
            return 0
        depth = 0
        for child in root.children:
            depth = max(self.maxDepth(child), depth)
        return depth + 1
```

**BFS**

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
    def maxDepth(self, root: 'Node') -> int:
        # BFS
        import collections
        # 特判，不写会报错
        if not root:
            return 0
        
        q = collections.deque()
        q.append(root)
        depth = 0
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                for child in node.children:
                    q.append(child)
            depth += 1
        return depth
```

## GitHub 链接

[Python](https://github.com/Wonz5130/LeetCode-Solutions/blob/master/solutions/0559-Maximum-Depth-of-N-ary-Tree/0559.py)