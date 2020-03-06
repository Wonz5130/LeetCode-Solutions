> LeetCode 面试题 57 - Ⅱ.  和为s的连续正数序列【Easy】【Python】【滑窗】【数学】

### 问题

[力扣](https://leetcode-cn.com/problems/he-wei-sde-lian-xu-zheng-shu-xu-lie-lcof/)

输入一个正整数 target ，输出所有和为 target 的连续正整数序列（至少含有两个数）。

序列内的数字由小到大排列，不同序列按照首个数字从小到大排列。

**示例 1：**

```
输入：target = 9
输出：[[2,3,4],[4,5]]
```

**示例 2：**

```
输入：target = 15
输出：[[1,2,3,4,5],[4,5,6],[7,8]]
```

**限制：**

* `1 <= target <= 10^5`

### 思路

##### 解法一

**滑动窗口**

```
i 指针表示窗口左边界，j 指针表示窗口右边界。
当 sum < target 时，j 指针右移。
当 sum > target 时，i 指针右移。
当 sum = target 时，窗口内的数组加入 res，i 指针右移。
注意窗口的 range 是左闭右开 [ )。
```

**时间复杂度:** O(n)

##### Python3代码

```python
class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        # solution one: sliding window
        i, j = 1, 1
        sum = 0
        res = []

        while i <= target // 2:
            if sum < target:
                # j + 1
                sum += j
                j += 1
            elif sum > target:
                # i + 1
                sum -= i
                i += 1
            else:
                arr = list(range(i, j))
                res.append(arr)
                # i + 1
                sum -= i
                i += 1

        return res
```

##### 解法二

**求根公式**

```
可以看出是等差数列，于是想到求和公式:
```

$$
S_n = \frac{n}{2}(a+a_n)
$$

```
设 x 为首项，y 为末项，则 y-x+1 为项数。设和为 target:
```

$$
target=\frac{(x+y)*(y-x+1)}{2}
$$

```
将上式展开：
```

$$
x^2-x-y^2-y+2*target=0
$$

```
根据求根公式：
```

$$
x_{1,2}=\frac{-b \pm\ \sqrt{b^2-4ac}}{2a}
$$

```
去掉负数根，就能得到下式：
```

$$
x = \sqrt{y^2+y-2*target+\frac{1}{4}}-\frac{1}{2}
$$

##### Python3代码

```python
class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        # solution two: formula
        res = []
        
        for y in range(1, target // 2 + 2):  # range:[ )
            x = (1/4 + y**2 + y - 2*target) ** (1/2) + 0.5
            if type(x) != complex and x - int(x) == 0:  # x can't be complex and x must be int
                res.append(list(range(int(x), y + 1)))
        
        return res
```

##### 解法三

**间隔法**

```
根据解法二的求根公式，将 i = y - x 代入，得到：
```

$$
target=\frac{(2x+i)*(i+1)}{2}
$$

```
进一步化简，得到：
```

$$
target = x(i+1)+\frac{i(i+1)}{2}
$$

```
最终得到：
```

$$
x = \frac{target-\frac{i(i+1)}{2}}{i+1}
$$

```
于是，得到两个条件：
1. i(i+1)/2 要小于 target
2. 分子必须可以整除分母
```

##### Python3代码

```python
class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
         # solution three
        i, res = 1, []

        while i*(i+1)/2 < target:
            if not (target - i*(i+1)/2) % (i+1):
                x = int((target - i*(i+1)/2) // (i+1))
                res.append(list(range(x, x+i+1)))
            i += 1
        
        # reverse
        return res[::-1]
```

### 代码地址

[GitHub链接](https://github.com/Wonz5130/LeetCode-Solutions/blob/master/solutions/Interview-57-II/5702.py)

### 参考

[什么是滑动窗口，以及如何用滑动窗口解这道题（C++/Java/Python）](https://leetcode-cn.com/problems/he-wei-sde-lian-xu-zheng-shu-xu-lie-lcof/solution/shi-yao-shi-hua-dong-chuang-kou-yi-ji-ru-he-yong-h/)

[【详解】滑动窗口法 -> 求根法 -> 间隔法，一山还有一山高](https://leetcode-cn.com/problems/he-wei-sde-lian-xu-zheng-shu-xu-lie-lcof/solution/xiang-jie-hua-dong-chuang-kou-fa-qiu-gen-fa-jian-g/)