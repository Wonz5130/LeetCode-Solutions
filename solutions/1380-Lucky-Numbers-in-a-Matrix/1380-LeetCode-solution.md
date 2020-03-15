> LeetCode 1380. Lucky Numbers in a Matrix矩阵中的幸运数【Easy】【Python】【暴力】

### Problem

[LeetCode](https://leetcode.com/problems/lucky-numbers-in-a-matrix/)

Given a `m * n` matrix of **distinct** numbers, return all lucky numbers in the matrix in **any** order.

A lucky number is an element of the matrix such that it is the minimum element in its row and maximum in its column.

**Example 1:**

```
Input: matrix = [[3,7,8],[9,11,13],[15,16,17]]
Output: [15]
Explanation: 15 is the only lucky number since it is the minimum in its row and the maximum in its column
```

**Example 2:**

```
Input: matrix = [[1,10,4,2],[9,3,8,7],[15,16,17,12]]
Output: [12]
Explanation: 12 is the only lucky number since it is the minimum in its row and the maximum in its column.
```

**Example 3:**

```
Input: matrix = [[7,8],[1,2]]
Output: [7]
```

**Constraints:**

- `m == mat.length`
- `n == mat[i].length`
- `1 <= n, m <= 50`
- `1 <= matrix[i][j] <= 10^5`.
- All elements in the matrix are distinct.

### 问题

[力扣](https://leetcode-cn.com/problems/lucky-numbers-in-a-matrix/)

给你一个 m * n 的矩阵，矩阵中的数字 **各不相同** 。请你按 **任意** 顺序返回矩阵中的所有幸运数。

幸运数是指矩阵中满足同时下列两个条件的元素：

* 在同一行的所有元素中最小
* 在同一列的所有元素中最大

**示例 1：**

```
输入：matrix = [[3,7,8],[9,11,13],[15,16,17]]
输出：[15]
解释：15 是唯一的幸运数，因为它是其所在行中的最小值，也是所在列中的最大值。
```

**示例 2：**

```
输入：matrix = [[1,10,4,2],[9,3,8,7],[15,16,17,12]]
输出：[12]
解释：12 是唯一的幸运数，因为它是其所在行中的最小值，也是所在列中的最大值。
```

**示例 3：**

```
输入：matrix = [[7,8],[1,2]]
输出：[7]
```


**提示：**

- `m == mat.length`
- `n == mat[i].length`
- `1 <= n, m <= 50`
- `1 <= matrix[i][j] <= 10^5`
- 矩阵中的所有元素都是不同的

### 思路

**暴力**

##### 解法一

```
找出每一行的最小值，再判断是否是当前列的最大值。
```

**时间复杂度:** O(m*n)，m 是 matrix 的行数，n 是 matrix 的列数。

##### Python3代码

```python
from typing import List

class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        # solution one
        m, n = len(matrix), len(matrix[0])
        flag = 0
        res = []
        for i in range(m):
            min_ = max_ = matrix[i][0]
            for j in range(n):
                if matrix[i][j] < min_:
                    flag = j
                    min_ = matrix[i][j]
            max_ = min_
            for x in range(m):
                if matrix[x][flag] > max_:
                    break
                elif x == m - 1:
                    res.append(max_)
        return res
```

##### 解法二

```
分别找出每一行的最小值和每一列的最大值，再判断是否相等。
```

**时间复杂度:** O(max(m, n))，m 是 matrix 的行数，n 是 matrix 的列数。

##### Python3代码

```python
from typing import List

class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        # solution two
        min_ = {min(rows) for rows in matrix}
        max_ = {max(columns) for columns in zip(*matrix)}  # zip(*) 对矩阵进行转置，即找出每一列中的最大值
        return list(min_ & max_)
```

### 代码地址

[GitHub链接](https://github.com/Wonz5130/LeetCode-Solutions/blob/master/solutions/1380-Lucky-Numbers-in-a-Matrix/1380.py)