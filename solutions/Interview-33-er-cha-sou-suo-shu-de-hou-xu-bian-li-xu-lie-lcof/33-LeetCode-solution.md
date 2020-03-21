> LeetCode 面试题33. 二叉搜索树的后序遍历序列【剑指Offer】【Medium】【Python】【递归】

### 问题

[力扣](https://leetcode-cn.com/problems/er-cha-sou-suo-shu-de-hou-xu-bian-li-xu-lie-lcof/)

输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历结果。如果是则返回 `true`，否则返回 `false`。假设输入的数组的任意两个数字都互不相同。

参考以下这颗二叉搜索树：

```
     5
    / \
   2   6
  / \
 1   3
```

**示例 1：**

```
输入: [1,6,3,2,5]
输出: false
```

**示例 2：**

```
输入: [1,3,2,6,5]
输出: true
```

**提示：**

1. `数组长度 <= 1000`

### 思路

**递归**

```
根据性质：
1. 后序遍历：左右根
2. 二叉搜索树：左子树任意节点的值 < 根节点的值，右子树任意节点的值 > 根节点的值

划分左右子树，分别判断子树是否满足二叉搜索树性质。

其他看代码注释。
```

**时间复杂度:** O(n^2)，n 为节点个数。
**空间复杂度:** O(n)，n 为节点个数。

##### Python3代码

```python
from typing import List

class Solution:
    def verifyPostorder(self, postorder: List[int]) -> bool:
        def recur(i, j):
            # 根节点小于等于1个
            if i >= j:
                return True
            l = i
            # 左子树
            while postorder[l] < postorder[j]:
                l += 1
            # 找到第一个大于根节点的节点，记为 m
            m = l
            # 右子树
            while postorder[l] > postorder[j]:
                l += 1
            # postorder[j]是根
            return l == j and recur(i, m - 1) and recur(m, j - 1)
        
        return recur(0, len(postorder) - 1)
```

### GitHub链接

[Python](https://github.com/Wonz5130/LeetCode-Solutions/blob/master/solutions/Interview-33-er-cha-sou-suo-shu-de-hou-xu-bian-li-xu-lie-lcof/33.py)