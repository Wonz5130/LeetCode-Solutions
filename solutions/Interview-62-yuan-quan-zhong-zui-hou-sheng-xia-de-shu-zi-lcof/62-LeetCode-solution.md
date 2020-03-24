> LeetCode 面试题62. 圆圈中最后剩下的数字【剑指Offer】【Easy】【Python】【数学】

### 问题

[力扣](https://leetcode-cn.com/problems/yuan-quan-zhong-zui-hou-sheng-xia-de-shu-zi-lcof/)

0,1,,n-1这n个数字排成一个圆圈，从数字0开始，每次从这个圆圈里删除第m个数字。求出这个圆圈里剩下的最后一个数字。

例如，0、1、2、3、4这5个数字组成一个圆圈，从数字0开始每次删除第3个数字，则删除的前4个数字依次是2、0、4、1，因此最后剩下的数字是3。

**示例 1：**

```
输入: n = 5, m = 3
输出: 3
```

**示例 2：**

```
输入: n = 10, m = 17
输出: 2
```

**限制：**

- `1 <= n <= 10^5`
- `1 <= m <= 10^6`

### 思路

**数学**

```
今天笔试正好考了类似的题目，其实就是约瑟夫环。
直接给出递推公式:
```

$$
f(n,m) = \begin{cases} 
		0,\quad n = 1 \\
		[f(n-1,m)+m]\%n,\quad n > 1 
		\end{cases}
$$

##### Python3代码

```python
class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        if n < 1 or m < 1:
            return None
            
        last = 0
        for i in range(2, n + 1):
            last = (last + m) % i
        return last
```

### GitHub链接

[Python](https://github.com/Wonz5130/LeetCode-Solutions/blob/master/solutions/Interview-62-yuan-quan-zhong-zui-hou-sheng-xia-de-shu-zi-lcof/62.py)