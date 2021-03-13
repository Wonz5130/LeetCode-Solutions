> LeetCode 面试题 04.02. 最小高度树【Easy】【Python】【二叉树】

## 问题

[力扣](https://leetcode-cn.com/problems/minimum-height-tree-lcci/)

给定一个有序整数数组，元素各不相同且按升序排列，编写一个算法，创建一棵高度最小的二叉搜索树。

**示例:**

```
给定有序数组: [-10,-3,0,5,9],

一个可能的答案是：[0,-3,9,-10,null,5]，它可以表示下面这个高度平衡二叉搜索树：

      0 
     / \ 
   -3   9 
   /   / 
 -10  5 
```

## 思路

**递归**

```
二叉搜索树根节点一定是有序数组的中位数：长度为奇数则取唯一中位数，长度为偶数则取右中位数。
递归终止条件：有序数组为空
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
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None
        
        mid = len(nums) // 2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid + 1:])

        return root
```

## 链接

[GitHub](https://github.com/Wonz5130/LeetCode-Solutions/tree/master/solutions/Interview-04.02-Minimum-Height-Tree-LCCI)