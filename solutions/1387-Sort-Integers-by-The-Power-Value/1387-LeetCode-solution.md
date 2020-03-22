> LeetCode 1387. Sort Integers by The Power Value将整数按权重排序【Medium】【Python】【排序】

### Problem

[LeetCode](https://leetcode.com/problems/sort-integers-by-the-power-value/)

The power of an integer `x` is defined as the number of steps needed to transform `x` into `1` using the following steps:

- if `x` is even then `x = x / 2`
- if `x` is odd then `x = 3 * x + 1`

For example, the power of x = 3 is 7 because 3 needs 7 steps to become 1 (3 --> 10 --> 5 --> 16 --> 8 --> 4 --> 2 --> 1).

Given three integers `lo`, `hi` and `k`. The task is to sort all integers in the interval `[lo, hi]` by the power value in **ascending order**, if two or more integers have **the same** power value sort them by **ascending order**.

Return the `k-th` integer in the range `[lo, hi]` sorted by the power value.

Notice that for any integer `x` `(lo <= x <= hi)` it is **guaranteed** that `x` will transform into `1` using these steps and that the power of `x` is will **fit** in 32 bit signed integer.

**Example 1:**

```
Input: lo = 12, hi = 15, k = 2
Output: 13
Explanation: The power of 12 is 9 (12 --> 6 --> 3 --> 10 --> 5 --> 16 --> 8 --> 4 --> 2 --> 1)
The power of 13 is 9
The power of 14 is 17
The power of 15 is 17
The interval sorted by the power value [12,13,14,15]. For k = 2 answer is the second element which is 13.
Notice that 12 and 13 have the same power value and we sorted them in ascending order. Same for 14 and 15.
```

**Example 2:**

```
Input: lo = 1, hi = 1, k = 1
Output: 1
```

**Example 3:**

```
Input: lo = 7, hi = 11, k = 4
Output: 7
Explanation: The power array corresponding to the interval [7, 8, 9, 10, 11] is [16, 3, 19, 6, 14].
The interval sorted by power is [8, 10, 11, 7, 9].
The fourth number in the sorted array is 7.
```

**Example 4:**

```
Input: lo = 10, hi = 20, k = 5
Output: 13
```

**Example 5:**

```
Input: lo = 1, hi = 1000, k = 777
Output: 570
```

**Constraints:**

- `1 <= lo <= hi <= 1000`
- `1 <= k <= hi - lo + 1`

### 问题

[力扣](https://leetcode-cn.com/problems/sort-integers-by-the-power-value/)

我们将整数 x 的 权重 定义为按照下述规则将 x 变成 1 所需要的步数：

* 如果 x 是偶数，那么 x = x / 2
* 如果 x 是奇数，那么 x = 3 * x + 1

比方说，x=3 的权重为 7 。因为 3 需要 7 步变成 1 （3 --> 10 --> 5 --> 16 --> 8 --> 4 --> 2 --> 1）。

给你三个整数 lo， hi 和 k 。你的任务是将区间 [lo, hi] 之间的整数按照它们的权重 升序排序 ，如果大于等于 2 个整数有 相同 的权重，那么按照数字自身的数值 升序排序 。

请你返回区间 [lo, hi] 之间的整数按权重排序后的第 k 个数。

注意，题目保证对于任意整数 x （lo <= x <= hi） ，它变成 1 所需要的步数是一个 32 位有符号整数。 

**示例 1：**

```
输入：lo = 12, hi = 15, k = 2
输出：13
解释：12 的权重为 9（12 --> 6 --> 3 --> 10 --> 5 --> 16 --> 8 --> 4 --> 2 --> 1）
13 的权重为 9
14 的权重为 17
15 的权重为 17
区间内的数按权重排序以后的结果为 [12,13,14,15] 。对于 k = 2 ，答案是第二个整数也就是 13 。
注意，12 和 13 有相同的权重，所以我们按照它们本身升序排序。14 和 15 同理。
```

**示例 2：**

```
输入：lo = 1, hi = 1, k = 1
输出：1
```

**示例 3：**

```
输入：lo = 7, hi = 11, k = 4
输出：7
解释：区间内整数 [7, 8, 9, 10, 11] 对应的权重为 [16, 3, 19, 6, 14] 。
按权重排序后得到的结果为 [8, 10, 11, 7, 9] 。
排序后数组中第 4 个数字为 7 。
```

**示例 4：**

```
输入：lo = 10, hi = 20, k = 5
输出：13
```

**示例 5：**

```
输入：lo = 1, hi = 1000, k = 777
输出：570
```

**提示：**

- `1 <= lo <= hi <= 1000`
- `1 <= k <= hi - lo + 1`

### 思路

**排序**

```
将数值、权重构造成字典，然后按照先 value 再 key 排序。
```

##### Python3代码

```python
class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        nums, weight = [], []
        for x in range(lo, hi + 1):
            nums.append(x)
            weight.append(self.step(x))
        # 将两个列表合并成字典
        dic = dict(zip(nums, weight))
        
        # 先根据权重排序，再根据数值排序
        res = sorted(dic.items(), key=lambda x: (x[1],x[0]))
        return res[k-1][0]
    
    def step(self, x):
        cnt = 0
        if x == 1:
            return cnt
        while x != 1:
            if x % 2:
                x = 3 * x + 1
            else:
                x = x / 2
            cnt += 1
        return cnt
```

### GitHub链接

[Python](https://github.com/Wonz5130/LeetCode-Solutions/blob/master/solutions/1387-Sort-Integers-by-The-Power-Value/1387.py)