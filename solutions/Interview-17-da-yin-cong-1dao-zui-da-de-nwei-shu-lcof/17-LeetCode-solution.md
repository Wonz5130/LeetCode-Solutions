> LeetCode 面试题17. 打印从1到最大的n位数【剑指Offer】【Easy】【Python】【遍历】

### 问题

[力扣](https://leetcode-cn.com/problems/da-yin-cong-1dao-zui-da-de-nwei-shu-lcof/)

输入数字 n，按顺序打印出从 1 到最大的 n 位十进制数。比如输入 3，则打印出 1、2、3 一直到最大的 3 位数 999。

**示例 1:**

```
输入: n = 1
输出: [1,2,3,4,5,6,7,8,9]
```


说明：

* 用返回一个整数列表来代替打印
* n 为正整数

### 思路

##### Python3代码

```python
class Solution:
    def printNumbers(self, n: int) -> List[int]:
        res = []
        for i in range(1, 10**n):
            res.append(i)
        return res

        # 一行代码
        return list(range(1, 10**n))
```

### GitHub链接

[Python](https://github.com/Wonz5130/LeetCode-Solutions/blob/master/solutions/Interview-17-da-yin-cong-1dao-zui-da-de-nwei-shu-lcof/17.py)