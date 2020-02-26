> LeetCode 0095. Unique Binary Search Trees II不同的二叉搜索树 II【Medium】【Python】【分治】【DFS】

### Problem

[LeetCode](https://leetcode.com/problems/unique-binary-search-trees-ii/)

Given an integer *n*, generate all structurally unique **BST's** (binary search trees) that store values 1 ... *n*.

**Example:**

```
Input: 3
Output:
[
  [1,null,3,2],
  [3,2,null,1],
  [3,1,null,null,2],
  [2,1,3],
  [1,null,2,null,3]
]
Explanation:
The above output corresponds to the 5 unique BST's shown below:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
```

### 问题

[力扣](https://leetcode-cn.com/problems/unique-binary-search-trees-ii/)

给定一个整数 n，生成所有由 1 ... n 为节点所组成的**二叉搜索树**。

**示例:**

```
输入: 3
输出:
[
  [1,null,3,2],
  [3,2,null,1],
  [3,1,null,null,2],
  [2,1,3],
  [1,null,2,null,3]
]
解释:
以上的输出对应以下 5 种不同结构的二叉搜索树：

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
```

### 思路

**分治**  **递归**  **DFS**

```
递归构造
从 1-n 中任选一个 i 作为根节点，i 左边的所有节点构成左子树，i 右边的所有节点构成右子树。
```

**时间复杂度:** 
$$
O(\frac{4^n}{n^{1/2}})
$$
**空间复杂度:**
$$
O(\frac{4^n}{n^{1/2}})
$$

### Python3代码

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        if n == 0:
            return []
        else:
            return self.generateTreesDFS(1, n)
    
    # DFS
    def generateTreesDFS(self, left, right):
        if left > right:
            return [None]
        ans = []
        for i in range(left, right + 1):
            left_nodes = self.generateTreesDFS(left, i -  1)  # all possible left subtrees if i is choosen to be a root
            right_nodes = self.generateTreesDFS(i + 1, right)  # all possible right subtrees if i is choosen to be a root
            for left_node in left_nodes:
                for right_node in right_nodes:
                    root = TreeNode(i)
                    root.left = left_node
                    root.right = right_node
                    ans.append(root)
        return ans
```

### 代码地址

[GitHub链接](https://github.com/Wonz5130/LeetCode-Solutions/blob/master/solutions/0095-Unique-Binary-Search-Trees-II/0095.py)