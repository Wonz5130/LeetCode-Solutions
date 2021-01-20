> LeetCode 0513. Find Bottom Left Tree Value找树左下角的值【Medium】【Python】【二叉树】

## Problem

[LeetCode](https://leetcode.com/problems/find-bottom-left-tree-value/)

Given the `root` of a binary tree, return the leftmost value in the last row of the tree.

**Example 1:**

![img](https://assets.leetcode.com/uploads/2020/12/14/tree1.jpg)

```
Input: root = [2,1,3]
Output: 1
```

**Example 2:**

![img](https://assets.leetcode.com/uploads/2020/12/14/tree2.jpg)

```
Input: root = [1,2,3,4,null,5,6,null,null,7]
Output: 7
```

**Constraints:**

- The number of nodes in the tree is in the range `[1, 104]`.
- `-231 <= Node.val <= 231 - 1`

## 问题

[力扣](https://leetcode-cn.com/problems/find-bottom-left-tree-value/)

给定一个二叉树，在树的最后一行找到最左边的值。

**示例 1:**

    输入:
    	2
       / \
      1   3
    输出:
    1
**示例 2:**



    输入:
    	1
       / \
      2   3
     /   / \
    4   5   6
       /
      7
    输出:
    7

**注意:** 您可以假设树（即给定的根节点）不为 **NULL**。

## 思路

**BFS**

```
常规 BFS 是先上后下，先左后右层次遍历。我们可以改变一下 BFS 遍历顺序，先上后下，先右后左，这样最后遍历的一个节点一定是左下角节点，最后直接返回节点值就行。
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
    def findBottomLeftValue(self, root: TreeNode) -> int:
        import collections
        q = collections.deque()
        q.append(root)
        while q:
            node = q.popleft()
            # 先右后左
            if node.right:
                q.append(node.right)
            if node.left:
                q.append(node.left)
        # 最后一个必是最左下角的节点
        return node.val
```

## GitHub 链接

[Python](https://github.com/Wonz5130/LeetCode-Solutions/blob/master/solutions/0513-Find-Bottom-Left-Tree-Value/0513.py)