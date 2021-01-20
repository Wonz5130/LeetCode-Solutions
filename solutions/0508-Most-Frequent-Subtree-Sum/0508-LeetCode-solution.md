> LeetCode 0508. Most Frequent Subtree Sum出现次数最多的子树元素和【Medium】【Python】【二叉树】

## Problem

[LeetCode](https://leetcode.com/problems/most-frequent-subtree-sum/)

Given the root of a tree, you are asked to find the most frequent subtree sum. The subtree sum of a node is defined as the sum of all the node values formed by the subtree rooted at that node (including the node itself). So what is the most frequent subtree sum value? If there is a tie, return all the values with the highest frequency in any order.

**Examples 1**
Input:

```
  5
 /  \
2   -3
```

return [2, -3, 4], since all the values happen only once, return all of them in any order.

**Examples 2**
Input:

```
  5
 /  \
2   -5
```

return [2], since 2 happens twice, however -5 only occur once.

**Note:** You may assume the sum of values in any subtree is in the range of 32-bit signed integer.

## 问题

[力扣](https://leetcode-cn.com/problems/most-frequent-subtree-sum/)

给你一个二叉树的根结点，请你找出出现次数最多的子树元素和。一个结点的「子树元素和」定义为以该结点为根的二叉树上所有结点的元素之和（包括结点本身）。

你需要返回出现次数最多的子树元素和。如果有多个元素出现的次数相同，返回所有出现次数最多的子树元素和（不限顺序）。

**示例 1：**

输入:

```
  5
 /  \
2   -3
```


返回 [2, -3, 4]，所有的值均只出现一次，以任意顺序返回所有值。

**示例 2：**
输入：

```
  5
 /  \
2   -5
```


返回 [2]，只有 2 出现两次，-5 只出现 1 次。

提示： 假设任意子树元素和均可以用 32 位有符号整数表示。

## 思路

**DFS**

```
先思考每一个节点需要做的事：该节点值与左右子树的所有节点值相加。
同时，要记录次数。
再遍历子树元素和，取出次数最多的子树元素和。
```

### Python3 代码

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        import collections
        res_dic = collections.defaultdict(int)
        # 计算子树元素和
        def dfs(node):
            # 递归边界
            if not node:
                return 0
            tmp_sum = dfs(node.left) + node.val + dfs(node.right)
            res_dic[tmp_sum] += 1
            return tmp_sum
        
        if not root:
            return []
        dfs(root)
        max_cnt = 0
        for cnt in res_dic.values():
            max_cnt = max(max_cnt, cnt)
        return [key for key, cnt in res_dic.items() if cnt == max_cnt]
```

## GitHub 链接

[Python](https://github.com/Wonz5130/LeetCode-Solutions/blob/master/solutions/0508-Most-Frequent-Subtree-Sum/0508.py)