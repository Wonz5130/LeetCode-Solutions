> LeetCode 0515. Find Largest Value in Each Tree Row在每个树行中找最大值【Medium】【Python】【二叉树】

## Problem

[LeetCode](https://leetcode.com/problems/find-largest-value-in-each-tree-row/)

Given the `root` of a binary tree, return *an array of the largest value in each row* of the tree **(0-indexed)**.

**Example 1:**

![img](https://assets.leetcode.com/uploads/2020/08/21/largest_e1.jpg)

```
Input: root = [1,3,2,5,3,null,9]
Output: [1,3,9]
```

**Example 2:**

```
Input: root = [1,2,3]
Output: [1,3]
```

**Example 3:**

```
Input: root = [1]
Output: [1]
```

**Example 4:**

```
Input: root = [1,null,2]
Output: [1,2]
```

**Example 5:**

```
Input: root = []
Output: []
```

**Constraints:**

- The number of nodes in the tree will be in the range `[0, 104]`.
- `-231 <= Node.val <= 231 - 1`

## 问题

[力扣](https://leetcode-cn.com/problems/find-largest-value-in-each-tree-row/)

您需要在二叉树的每一行中找到最大的值。

**示例：**

    输入: 
    	  1
         / \
        3   2
       / \   \  
      5   3   9 
    输出: [1, 3, 9]

## 思路

**BFS**

```
使用 BFS 遍历完每一层，将该层最大值加入 res 中。
```

### Python3 代码

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        import collections
        if not root:
            return []
        res = []
        q = collections.deque()
        q.append(root)
        while q:
            size = len(q)
            tmp_max = -float('inf')
            # 取每一层最大值
            for i in range(size):
                node = q.popleft()
                tmp_max = max(tmp_max, node.val)
                # 一层树遍历完，加入该层最大值
                if i == size - 1:
                    res.append(tmp_max)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return res
```

## GitHub 链接

[Python](https://github.com/Wonz5130/LeetCode-Solutions/blob/master/solutions/0515-Find-Largest-Value-in-Each-Tree-Row/0515.py)