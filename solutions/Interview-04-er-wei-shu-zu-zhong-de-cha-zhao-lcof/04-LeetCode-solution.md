> LeetCode 面试题04. 二维数组中的查找【剑指Offer】【Easy】【Python】【数组】

### 问题

[力扣](https://leetcode-cn.com/problems/er-wei-shu-zu-zhong-de-cha-zhao-lcof/)

在一个 n * m 的二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。 

**示例:**

现有矩阵 matrix 如下：

```
[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
```


给定 target = 5，返回 true。

给定 target = 20，返回 false。

**限制：**

`0 <= n <= 1000`

`0 <= m <= 1000`

**注意：** 本题与主站 240 题相同：https://leetcode-cn.com/problems/search-a-2d-matrix-ii/

### 思路

##### 解法一

**暴力**

```
直接暴力遍历，遇到相同就返回 True，遍历完所有还没有遇到就返回 False。
```

**时间复杂度:** O(n*m)，n 为 matrix 矩阵的行数，m 为 matrix 矩阵的列数。
**空间复杂度:** O(1)

##### Python3代码

```python
from typing import List

class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        # solution one: 暴力
        # 特判
        if matrix == []:
            return False
        
        n, m = len(matrix), len(matrix[0])
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == target:
                    return True
                elif matrix[i][j] > target:
                    break
        return False
```

##### 解法二

**左下角标志数法**

```
从左下角开始判断
如果相等，就返回；
如果大于 target，就表示该行最小值都要大于 target，所以往上移一行；
如果小于 target，就表示该列最大值都要小于 target，所以往右移一列。
```

**时间复杂度:** O(n + m)，n 为 matrix 矩阵的行数，m 为 matrix 矩阵的列数。
**空间复杂度:** O(1)

##### Python3代码

```python
from typing import List

class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        # solution two: 左下角标志数法
        i, j = len(matrix) - 1, 0
        while i >= 0 and j < len(matrix[0]):
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                i -= 1
            else:
                j += 1
        return False
```

### 代码地址

[GitHub链接](https://github.com/Wonz5130/LeetCode-Solutions/blob/master/solutions/Interview-04-er-wei-shu-zu-zhong-de-cha-zhao-lcof/04.py)