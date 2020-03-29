> LeetCode 1395. Count Number of Teams统计作战单位数【Medium】【Python】【暴力】

### Problem

[LeetCode](https://leetcode.com/problems/count-number-of-teams/)

There are `n` soldiers standing in a line. Each soldier is assigned a **unique** `rating` value.

You have to form a team of 3 soldiers amongst them under the following rules:

- Choose 3 soldiers with index (`i`, `j`, `k`) with rating (`rating[i]`, `rating[j]`, `rating[k]`).
- A team is valid if: (`rating[i] < rating[j] < rating[k]`) or (`rating[i] > rating[j] > rating[k]`) where (`0 <= i < j < k < n`).

Return the number of teams you can form given the conditions. (soldiers can be part of multiple teams).

**Example 1:**

```
Input: rating = [2,5,3,4,1]
Output: 3
Explanation: We can form three teams given the conditions. (2,3,4), (5,4,1), (5,3,1). 
```

**Example 2:**

```
Input: rating = [2,1,3]
Output: 0
Explanation: We can't form any team given the conditions.
```

**Example 3:**

```
Input: rating = [1,2,3,4]
Output: 4
```

**Constraints:**

- `n == rating.length`
- `1 <= n <= 200`
- `1 <= rating[i] <= 10^5`

### 问题

[力扣](https://leetcode-cn.com/problems/count-number-of-teams/)

n 名士兵站成一排。每个士兵都有一个 独一无二 的评分 rating 。

每 3 个士兵可以组成一个作战单位，分组规则如下：

* 从队伍中选出下标分别为 i、j、k 的 3 名士兵，他们的评分分别为 rating[i]、rating[j]、rating[k]
* 作战单位需满足： rating[i] < rating[j] < rating[k] 或者 rating[i] > rating[j] > rating[k] ，其中  0 <= i < j < k < n

请你返回按上述条件可以组建的作战单位数量。每个士兵都可以是多个作战单位的一部分。 

**示例 1：**

```
输入：rating = [2,5,3,4,1]
输出：3
解释：我们可以组建三个作战单位 (2,3,4)、(5,4,1)、(5,3,1) 。
```

**示例 2：**

```
输入：rating = [2,1,3]
输出：0
解释：根据题目条件，我们无法组建作战单位。
```

**示例 3：**

```
输入：rating = [1,2,3,4]
输出：4
```

**提示：**

* `n == rating.length`
* `1 <= n <= 200`
* `1 <= rating[i] <= 10^5`

### 思路

**暴力**

```
三层循环，暴力求解。
因为数据 n 是 [1, 200]，所以不会 LTE。
```

**时间复杂度:** O(n^3)
**空间复杂度:** O(1)

##### Python3代码

```python
from typing import List

class Solution:
    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)
        count = 0
        for i in range(n-2):
            for j in range(i+1, n-1):
                for k in range(j+1, n):
                    if rating[i] < rating[j]:
                        if rating[j] < rating[k]:
                            count += 1
                    elif rating[i] > rating[j]:
                        if rating[j] > rating[k]:
                            count += 1
        return count
```

### GitHub链接

[Python](https://github.com/Wonz5130/LeetCode-Solutions/blob/master/solutions/1395-Count-Number-of-Teams/1395.py)