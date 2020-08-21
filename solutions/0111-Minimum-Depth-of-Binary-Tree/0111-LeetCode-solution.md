> LeetCode 0111. Minimum Depth of Binary Tree二叉树的最小深度【Easy】【Python】【二叉树】

### Problem

[LeetCode](https://leetcode.com/problems/minimum-depth-of-binary-tree/)

Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

**Note:** A leaf is a node with no children.

**Example:**

Given binary tree `[3,9,20,null,null,15,7]`,

```
    3
   / \
  9  20
    /  \
   15   7
```

return its minimum depth = 2.

### 问题

[力扣](https://leetcode-cn.com/problems/minimum-depth-of-binary-tree/)

给定一个二叉树，找出其最小深度。

最小深度是从根节点到最近叶子节点的最短路径上的节点数量。

说明: 叶子节点是指没有子节点的节点。

示例:

给定二叉树 [3,9,20,null,null,15,7],

        3
       / \
      9  20
        /  \
       15   7

返回它的最小深度  2.

### 思路

##### 解法一：DFS

```
对于每一个非叶子节点，分别计算其左右子树的最小叶子节点深度。
```

**时间复杂度:** O(n)，n 是二叉树的节点数。
**空间复杂度:** O(h)，h 是二叉树的高度。

##### Python3代码

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        # solution one: DFS
        # 根为空
        if not root:
            return 0
        
        # 左右子树都为空
        if not root.left and not root.right:
            return 1
        
        min_depth = 10**9
        if root.left:
            min_depth = min(self.minDepth(root.left), min_depth)
        if root.right:
            min_depth = min(self.minDepth(root.right), min_depth)
        
        return min_depth + 1
```

##### 解法二：BFS

```
找到一个叶子节点时，直接返回这个叶子节点的深度。
```

**时间复杂度:** O(n)，n 是二叉树的节点数。
**空间复杂度:** O(h)，h 是二叉树的高度。

##### Python3代码

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        # solution two: BFS
        import collections
        # 根为空
        if not root:
            return 0
        
        que = collections.deque([(root, 1)])
        while que:
            node, depth = que.popleft()
            # 到达叶子节点
            if not node.left and not node.right:
                return depth
            if node.left:
                que.append((node.left, depth + 1))
            if node.right:
                que.append((node.right, depth + 1))
        
        return 0
```

### GitHub链接

[Python](https://github.com/Wonz5130/LeetCode-Solutions/blob/master/solutions/0111-Minimum-Depth-of-Binary-Tree/0111.py)

