> LeetCode 0102. Binary Tree Level Order Traversal二叉树的层次遍历【Medium】【Python】【BFS】

### Problem

[LeetCode](https://leetcode.com/problems/binary-tree-level-order-traversal/)

Given a binary tree, return the *level order* traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree `[3,9,20,null,null,15,7]`,

```
    3
   / \
  9  20
    /  \
   15   7
```

return its level order traversal as:

```
[
  [3],
  [9,20],
  [15,7]
]
```

### 问题

[力扣](https://leetcode-cn.com/problems/binary-tree-level-order-traversal/)

给定一个二叉树，返回其按层次遍历的节点值。 （即逐层地，从左到右访问所有节点）。

例如:
给定二叉树: `[3,9,20,null,null,15,7]`,

```
    3
   / \
  9  20
    /  \
   15   7
```

返回其层次遍历结果：

```
[
  [3],
  [9,20],
  [15,7]
]
```

### 思路

**BFS**

##### 解法一：非递归

```
当队列不为空：
	当前层打印循环：
		队首元素出队，记为 node
		将 node.val 添加到 temp 尾部
		若左（右）子节点不为空，则将左（右）子节点加入队列
	把当前 temp 中的所有元素加入 res
```

**时间复杂度:** O(n)，n 为二叉树的节点数。
**空间复杂度:** O(n)，n 为二叉树的节点数。

##### Python3代码

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        # solution one: 非递归
        import collections
        if not root:
            return []
        
        res, q = [], collections.deque()
        q.append(root)
        while q:
            # 输出是二维数组
            temp = []
            for x in range(len(q)):
                node = q.popleft()
                temp.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(temp)
        return res
```

##### 解法二：递归

##### Python3代码

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        # solution two: 递归
        res = []
        
        def helper(root, depth):
            if not root:
                return
            if len(res) == depth:
                res.append([])
            res[depth].append(root.val)
            helper(root.left, depth + 1)
            helper(root.right, depth + 1)
        helper(root , 0)
        return res
```

### GitHub链接

[Python](https://github.com/Wonz5130/LeetCode-Solutions/blob/master/solutions/0102-Binary-Tree-Level-Order-Traversal/0102.py)