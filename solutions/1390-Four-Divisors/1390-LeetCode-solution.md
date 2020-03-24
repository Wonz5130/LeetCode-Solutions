> LeetCode 1390. Four Divisors四因数【Medium】【Python】【数学】

### Problem

[LeetCode](https://leetcode.com/problems/four-divisors/)

Given an integer array `nums`, return the sum of divisors of the integers in that array that have exactly four divisors.

If there is no such integer in the array, return `0`.

**Example 1:**

```
Input: nums = [21,4,7]
Output: 32
Explanation:
21 has 4 divisors: 1, 3, 7, 21
4 has 3 divisors: 1, 2, 4
7 has 2 divisors: 1, 7
The answer is the sum of divisors of 21 only.
```

**Constraints:**

- `1 <= nums.length <= 10^4`
- `1 <= nums[i] <= 10^5`

### 问题

[力扣](https://leetcode-cn.com/problems/four-divisors/)

给你一个整数数组 nums，请你返回该数组中恰有四个因数的这些整数的各因数之和。

如果数组中不存在满足题意的整数，则返回 0 。

**示例：**

```
输入：nums = [21,4,7]
输出：32
解释：
21 有 4 个因数：1, 3, 7, 21
4 有 3 个因数：1, 2, 4
7 有 2 个因数：1, 7
答案仅为 21 的所有因数的和。
```


提示：

- `1 <= nums.length <= 10^4`
- `1 <= nums[i] <= 10^5`

### 思路

**数学**

```
暴力计算每个数的因数个数。
满足四个，就因数相加。
注意：因数不能重复。
```

**时间复杂度:** O(n*max(int(sqrt(x)), 4))，n 为 nums 个数。
**空间复杂度:** O(1)

##### Python3代码

```python
from typing import List

class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        sum = 0
        for x in nums:
            if x == 1 or x == 2 or x == 3:
                continue
            num = 2
            temp = [1, x]
            # 计算因数
            while num ** 2 <= x:  # 用 num^2 <= x 比 num <= sqrt(x) 好
                if len(temp) > 4:
                    break
                if not x % num:
                    if num not in temp:
                        temp.append(num)
                    if int(x/num) not in temp:
                        temp.append(int(x/num))
                num += 1
            # print(temp)
            if len(temp) == 4:
                for _ in temp:
                    # print(_)
                    sum += _
        return int(sum)
```

### GitHub链接

[Python](https://github.com/Wonz5130/LeetCode-Solutions/blob/master/solutions/1390-Four-Divisors/1390.py)