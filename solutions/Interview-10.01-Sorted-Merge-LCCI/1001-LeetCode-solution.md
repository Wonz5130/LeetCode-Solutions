> LeetCode 面试题 10.01. Sorted Merge LCCI【Easy】【Python】【双指针】

### 问题

[力扣](https://leetcode-cn.com/problems/sorted-merge-lcci/)

给定两个排序后的数组 A 和 B，其中 A 的末端有足够的缓冲空间容纳 B。 编写一个方法，将 B 合并入 A 并排序。

初始化 A 和 B 的元素数量分别为 *m* 和 *n*。

**示例:**

```
输入:
A = [1,2,3,0,0,0], m = 3
B = [2,5,6],       n = 3

输出: [1,2,2,3,5,6]
```

### 思路

##### 解法一

**双指针**

```
指针 i 指向 A[m-1]，指针 j 指向 B[n-1]。
A[i] 与 B[j] 相比较，取较大值插在 A 尾部，i、j 指针再分别往前移。
如果 i 指针已经移到 A 头部，判断如果 B 还有元素，就直接插在 A 前面。
```

**时间复杂度:** O(m+n)
**空间复杂度:** O(1)

##### Python3代码

```python
class Solution:
    def merge(self, A: List[int], m: int, B: List[int], n: int) -> None:
        """
        Do not return anything, modify A in-place instead.
        """
        # # solution one: sort
        # A[m:] = B
        # A.sort()

        # solution two: two point
        if n == 0: # B = []
            return
        i, j, k = m - 1, n - 1, m + n - 1
        while i > -1 and j > -1:  # > -1, if m = 0 or n = 0, then i = -1 or j = -1
            if A[i] <= B[j]:
                A[k] = B[j]
                k -= 1
                j -= 1
            else:
                A[k] = A[i]
                k -= 1
                i -= 1
        if j > -1:
            A[:j + 1] = B[:j  + 1]  # A = [], B = [1]
```

##### 解法二

**排序**

```
B 插在 A 尾部，再利用 sort 函数排下序。
```

**时间复杂度:** O((m+n)log(m+n))
**空间复杂度:** O(log(m+n))

##### Python3代码

```python
class Solution:
    def merge(self, A: List[int], m: int, B: List[int], n: int) -> None:
        """
        Do not return anything, modify A in-place instead.
        """
        # solution one: sort
        A[m:] = B
        A.sort()
```

### 代码地址

[GitHub链接](https://github.com/Wonz5130/LeetCode-Solutions/blob/master/solutions/Interview-10.01-Sorted-Merge-LCCI/1001.py)

### 相关题目

[LeetCode 0088. Merge Sorted Array合并两个有序数组](https://leetcode-cn.com/problems/merge-sorted-array/)