> LeetCode 1382. Balance a Binary Search Tree将二叉搜索树变平衡【Medium】【Python】【二叉树】

### Problem

[LeetCode](https://leetcode.com/problems/balance-a-binary-search-tree/)

Given a binary search tree, return a **balanced** binary search tree with the same node values.

A binary search tree is *balanced* if and only if the depth of the two subtrees of every node never differ by more than 1.

If there is more than one answer, return any of them.

**Example 1:**

![](https://cdn.jsdelivr.net/gh/Wonz5130/My-Private-ImgHost/img/1515_ex1.png)

![](https://cdn.jsdelivr.net/gh/Wonz5130/My-Private-ImgHost/img/1515_ex1_out.png)

```
Input: root = [1,null,2,null,3,null,4,null,null]
Output: [2,1,3,null,null,null,4]
Explanation: This is not the only correct answer, [3,1,4,null,2,null,null] is also correct.
```

**Constraints:**

- The number of nodes in the tree is between `1` and `10^4`.
- The tree nodes will have distinct values between `1` and `10^5`.

### 问题

[力扣](https://leetcode-cn.com/problems/balance-a-binary-search-tree/)

给你一棵二叉搜索树，请你返回一棵 **平衡后** 的二叉搜索树，新生成的树应该与原来的树有着相同的节点值。

如果一棵二叉搜索树中，每个节点的两棵子树高度差不超过 1 ，我们就称这棵二叉搜索树是 **平衡的** 。

如果有多种构造方法，请你返回任意一种。

**示例：**

![](https://cdn.jsdelivr.net/gh/Wonz5130/My-Private-ImgHost/img/1515_ex1.png)

![](https://cdn.jsdelivr.net/gh/Wonz5130/My-Private-ImgHost/img/1515_ex1_out.png)

```
输入：root = [1,null,2,null,3,null,4,null,null]
输出：[2,1,3,null,null,null,4]
解释：这不是唯一的正确答案，[3,1,4,null,2,null,null] 也是一个可行的构造方案。
```

**提示：**

- 树节点的数目在 `1` 到 `10^4` 之间。
- 树节点的值互不相同，且在 `1` 到 `10^5` 之间。

### 思路

**二分建树**

```
先把二叉搜索树转为数组，再二分建树。
```

##### Python3代码

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from typing import List

class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        if not root:
            return
        return self.build(self.dfs(root))
    
    # 二叉搜索树转数组
    def dfs(self, root):
        if not root:
            return []
        return self.dfs(root.left) + [root.val] + self.dfs(root.right)
    
    # 数组二分构建平衡二叉树
    def build(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None
        mid = len(nums) // 2
        node = TreeNode(nums[mid])

        left = nums[:mid]
        right = nums[mid+1:]

        node.left = self.build(left)
        node.right = self.build(right)
        
        return node
```

### 代码地址

[GitHub链接](https://github.com/Wonz5130/LeetCode-Solutions/blob/master/solutions/1382-Balance-a-Binary-Search-Tree/1382.py)