> LeetCode 1362. Closest Divisors最接近的因数【Medium】【Python】【数学】

### Problem

[LeetCode](https://leetcode.com/problems/closest-divisors/)

Given an integer `num`, find the closest two integers in absolute difference whose product equals `num + 1` or `num + 2`.

Return the two integers in any order.

**Example 1:**

```
Input: num = 8
Output: [3,3]
Explanation: For num + 1 = 9, the closest divisors are 3 & 3, for num + 2 = 10, the closest divisors are 2 & 5, hence 3 & 3 is chosen.
```

**Example 2:**

```
Input: num = 123
Output: [5,25]
```

**Example 3:**

```
Input: num = 999
Output: [40,25] 
```

**Constraints:**

- `1 <= num <= 10^9`

### 问题

[力扣](https://leetcode-cn.com/problems/closest-divisors/)

给你一个整数 `num`，请你找出同时满足下面全部要求的两个整数：

* 两数乘积等于  `num + 1` 或 `num + 2`
* 以绝对差进行度量，两数大小最接近

你可以按任意顺序返回这两个整数。 

**示例 1：**

```
输入：num = 8
输出：[3,3]
解释：对于 num + 1 = 9，最接近的两个因数是 3 & 3；对于 num + 2 = 10, 最接近的两个因数是 2 & 5，因此返回 3 & 3 。
```

**示例 2：**

```
输入：num = 123
输出：[5,25]
```

**示例 3：**

```
输入：num = 999
输出：[40,25]
```

**提示：**

* `1 <= num <= 10^9`

### 思路

**数学**

```
从 1 遍历到 sqrt(x)，找到最接近的两个因数。
其实从 sqrt(x) 倒过来遍历会更快。
```

**时间复杂度:** O(sqrt(n))
**空间复杂度:** O(1)

### Python3代码

```python
class Solution:
    def closestDivisors(self, num: int) -> List[int]:
        import math
        num1, num2 = num + 1, num + 2
        ans1 = self.crack(num1)
        ans2 = self.crack(num2)
        res = []
        if abs(ans1 - int(num1 / ans1)) < abs(ans2 - int(num2 / ans2)):  # int
            res.append(ans1)
            res.append(int(num1 / ans1))
            return res
        else:
            res.append(ans2)
            res.append(int(num2 / ans2))
            return res
    
    # calculate factor
    def crack(self, integer):
        factor1, factor2 = 1, integer
        for i in range(1, int(math.sqrt(integer)) + 1):  # range: [1, sqrt(x) + 1)
            if int(integer / i) == integer / i:  # i is factor
                if integer / i - i < factor2 - factor1:
                    factor1, factor2 = i, integer / i
        return factor1
```

### 代码地址

[GitHub链接](https://github.com/Wonz5130/LeetCode-Solutions/tree/master/solutions/1362-Closest-Divisors)