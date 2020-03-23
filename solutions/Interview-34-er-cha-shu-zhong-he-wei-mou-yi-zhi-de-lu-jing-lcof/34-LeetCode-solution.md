> LeetCode 面试题34. 二叉树中和为某一值的路径【剑指Offer】【Medium】【Python】【回溯】

### 问题

[力扣](https://leetcode-cn.com/problems/er-cha-shu-zhong-he-wei-mou-yi-zhi-de-lu-jing-lcof/)

输入一棵二叉树和一个整数，打印出二叉树中节点值的和为输入整数的所有路径。从树的根节点开始往下一直到叶节点所经过的节点形成一条路径。

**示例:**
给定如下二叉树，以及目标和 sum = 22，

              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
**返回:**

```
[
   [5,4,11,2],
   [5,8,4,5]
]
```

**提示：**

1. `节点总数 <= 10000`

注意：本题与主站 [113 题](https://leetcode-cn.com/problems/path-sum-ii/) 相同。

### 思路

**回溯**

```
先序遍历二叉树，记录路径。
符合条件的加入 res 中。
回溯记得要删除当前节点。
```

**时间复杂度:** O(n)，n 为二叉树节点个数。
**空间复杂度:** O(n)，最坏情况，二叉树退化成单链表。

##### Python3代码

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        res, path = [], []

        # 先序遍历：根左右
        def recur(root, target):
            if not root:
                return
            
            path.append(root.val)
            target -= root.val
            # 找到路径
            if target == 0 and not root.left and not root.right:
                res.append(list(path))  # 复制了一个 path 加入到 res 中，这样修改 path 不影响 res
            recur(root.left, target)
            recur(root.right, target)
            # 向上回溯，需要删除当前节点
            path.pop()
        
        recur(root, sum)
        return res
```

### GitHub链接

[Python](https://github.com/Wonz5130/LeetCode-Solutions/blob/master/solutions/Interview-34-er-cha-shu-zhong-he-wei-mou-yi-zhi-de-lu-jing-lcof/34.py)