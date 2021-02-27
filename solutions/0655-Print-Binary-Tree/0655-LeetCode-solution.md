> LeetCode 0655. Print Binary Tree 输出二叉树【Medium】【Python】【二叉树】

## 问题

[力扣](https://leetcode-cn.com/problems/print-binary-tree/)

在一个 m*n 的二维字符串数组中输出二叉树，并遵守以下规则：

1. 行数 m 应当等于给定二叉树的高度。
2. 列数 n 应当总是奇数。
3. 根节点的值（以字符串格式给出）应当放在可放置的第一行正中间。根节点所在的行与列会将剩余空间划分为两部分（左下部分和右下部分）。你应该将左子树输出在左下部分，右子树输出在右下部分。左下和右下部分应当有相同的大小。即使一个子树为空而另一个非空，你不需要为空的子树输出任何东西，但仍需要为另一个子树留出足够的空间。然而，如果两个子树都为空则不需要为它们留出任何空间。
4. 每个未使用的空间应包含一个空的字符串""。
5. 使用相同的规则输出子树。

**示例 1:**

```
输入:
     1
    /
   2
输出:
[["", "1", ""],
 ["2", "", ""]]
```

**示例 2:**

```
输入:
     1
    / \
   2   3
    \
     4
输出:
[["", "", "", "1", "", "", ""],
 ["", "2", "", "", "", "3", ""],
 ["", "", "4", "", "", "", ""]]
```

**示例 3:**

```
输入:
      1
     / \
    2   5
   / 
  3 
 / 
4 
输出:
[["",  "",  "", "",  "", "", "", "1", "",  "",  "",  "",  "", "", ""]
 ["",  "",  "", "2", "", "", "", "",  "",  "",  "",  "5", "", "", ""]
 ["",  "3", "", "",  "", "", "", "",  "",  "",  "",  "",  "", "", ""]
 ["4", "",  "", "",  "", "", "", "",  "",  "",  "",  "",  "", "", ""]]
```

**注意:** 二叉树的高度在范围 [1, 10] 中。

## 思路

**DFS**

```
先求出二叉树的最大深度depth， 然后构建二维矩阵，列数就是 2*depth-1，行数就是depth。
再利用 DFS 存二叉树，左右子树的节点值存到对应的 (start+end)/2 的左右侧。
```

## 代码

### Python3

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def printTree(self, root: TreeNode) -> List[List[str]]:
        # 求最大深度
        def maxDepth(root):
            if not root:
                return 0
            left = maxDepth(root.left)
            right = maxDepth(root.right)
            return 1 + max(left, right)
        
        depth = maxDepth(root)
        # 二维矩阵宽度
        wid = 2**depth - 1
        res = [[''] * wid for _ in range(depth)]

        # DFS
        def dfs(root, depth, start, end):
            # 当前根节点放在(start+end)/2这个中间位置
            res[depth - 1][(start + end) // 2] = str(root.val)
            if root.left:
                dfs(root.left, depth + 1, start, (start + end) // 2)
            if root.right:
                dfs(root.right, depth + 1, (start + end) // 2, end)
        
        dfs(root, 1, 0, wid)
        return res
```

## 链接

[GitHub](https://github.com/Wonz5130/LeetCode-Solutions/tree/master/solutions/0655-Print-Binary-Tree)