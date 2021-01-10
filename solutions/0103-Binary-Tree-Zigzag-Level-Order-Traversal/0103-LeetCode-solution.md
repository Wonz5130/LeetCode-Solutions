> LeetCode 0103. Binary Tree Zigzag Level Order Traversal 二叉树的锯齿形层序遍历【Medium】【Python】【二叉树】【BFS】

## Problem

[LeetCode](https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/)

Given a binary tree, return the *zigzag level order* traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree `[3,9,20,null,null,15,7]`,

```
    3
   / \
  9  20
    /  \
   15   7
```

return its zigzag level order traversal as:

```
[
  [3],
  [20,9],
  [15,7]
]
```

## 问题

[力扣](https://leetcode-cn.com/problems/binary-tree-zigzag-level-order-traversal/)

给定一个二叉树，返回其节点值的锯齿形层序遍历。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。

例如：
给定二叉树 [3,9,20,null,null,15,7],

    	3
       / \
      9  20
        /  \
       15   7
返回锯齿形层序遍历如下：

```
[
  [3],
  [20,9],
  [15,7]
]
```

## 思路

**BFS**

```
当队列不为空：
	当前层打印循环：
		队首元素出队，记为 node
		根据 flag 将 node.val 添加到 temp 尾部/头部
		若左（右）子节点不为空，则将左（右）子节点加入队列
	把当前 temp 中的所有元素加入 res
```

**时间复杂度:** O(n)，n 为二叉树的节点数。
**空间复杂度:** O(n)，n 为二叉树的节点数。

### Python3 代码

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        import collections
        if not root:
            return []
        
        res, q = [], collections.deque()
        flag = False  # 做奇偶判断
        q.append(root)
        
        while q:
            temp = []
            flag = not flag
            for _ in range(len(q)):
                node = q.popleft()
                # 头插
                if flag:
                    temp.append(node.val)
                # 尾插
                else:
                    temp.insert(0, node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(temp)
        
        return res
```

## GitHub 链接

[Python](https://github.com/Wonz5130/LeetCode-Solutions/blob/master/solutions/0103-Binary-Tree-Zigzag-Level-Order-Traversal/0103.py)