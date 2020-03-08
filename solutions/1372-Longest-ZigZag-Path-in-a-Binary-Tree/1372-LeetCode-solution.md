> LeetCode 1372. Longest ZigZag Path in a Binary Tree二叉树中的最长交错路径【Medium】【Python】【DFS】

### Problem

[LeetCode](https://leetcode.com/problems/longest-zigzag-path-in-a-binary-tree/)

Given a binary tree `root`, a ZigZag path for a binary tree is defined as follow:

- Choose **any** node in the binary tree and a direction (right or left).
- If the current direction is right then move to the right child of the current node otherwise move to the left child.
- Change the direction from right to left or right to left.
- Repeat the second and third step until you can't move in the tree.

Zigzag length is defined as the number of nodes visited - 1. (A single node has a length of 0).

Return the longest **ZigZag** path contained in that tree.

**Example 1:**

![](https://cdn.jsdelivr.net/gh/Wonz5130/My-Private-ImgHost/img/sample_1_1702.png)

```
Input: root = [1,null,1,1,1,null,null,1,1,null,1,null,null,null,1,null,1]
Output: 3
Explanation: Longest ZigZag path in blue nodes (right -> left -> right).
```

**Example 2:**

![](https://cdn.jsdelivr.net/gh/Wonz5130/My-Private-ImgHost/img/sample_2_1702.png)

```
Input: root = [1,1,1,null,1,null,null,1,1,null,1]
Output: 4
Explanation: Longest ZigZag path in blue nodes (left -> right -> left -> right).
```

**Example 3:**

```
Input: root = [1]
Output: 0
```

**Constraints:**

- Each tree has at most `50000` nodes..
- Each node's value is between `[1, 100]`.

### 问题

[力扣](https://leetcode-cn.com/problems/longest-zigzag-path-in-a-binary-tree/)

给你一棵以 `root` 为根的二叉树，二叉树中的交错路径定义如下：

* 选择二叉树中 **任意** 节点和一个方向（左或者右）。
* 如果前进方向为右，那么移动到当前节点的的右子节点，否则移动到它的左子节点。
* 改变前进方向：左变右或者右变左。
* 重复第二步和第三步，直到你在树中无法继续移动。

交错路径的长度定义为：**访问过的节点数目 - 1**（单个节点的路径长度为 0 ）。

请你返回给定树中最长 **交错路径** 的长度。

**示例 1：**

![](https://cdn.jsdelivr.net/gh/Wonz5130/My-Private-ImgHost/img/sample_1_1702.png)

```
输入：root = [1,null,1,1,1,null,null,1,1,null,1,null,null,null,1,null,1]
输出：3
解释：蓝色节点为树中最长交错路径（右 -> 左 -> 右）。
```

**示例 2：**

![](https://cdn.jsdelivr.net/gh/Wonz5130/My-Private-ImgHost/img/sample_2_1702.png)

```
输入：root = [1,1,1,null,1,null,null,1,1,null,1]
输出：4
解释：蓝色节点为树中最长交错路径（左 -> 右 -> 左 -> 右）。
```

**示例 3：**

```
输入：root = [1]
输出：0
```

**提示：**

* 每棵树最多有 `50000` 个节点。
* 每个节点的值在 `[1, 100]` 之间。

### 思路

**DFS**

```
递归时记录前面的节点是左节点还是右节点，以及深度。
```

##### Python3代码

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def longestZigZag(self, root: TreeNode) -> int:
        if root == None:
            return 0
        self.max_ = 0
        self.dfs(root, 0, 0)
        return self.max_
    
    def dfs(self, root, prev, depth):
        self.max_ = max(depth, self.max_)

        if root.left:
            # left->left
            if prev == 0:
                self.dfs(root.left, 0, 1)
            # left->right
            else:
                self.dfs(root.left, 0, depth + 1)
        if root.right:
            # right->right
            if prev == 1:
                self.dfs(root.right, 1, 1)
            # right->left
            else:
                self.dfs(root.right, 1, depth + 1)
```

### 代码地址

[GitHub链接](https://github.com/Wonz5130/LeetCode-Solutions/blob/master/solutions/1372-Longest-ZigZag-Path-in-a-Binary-Tree/1372.py)