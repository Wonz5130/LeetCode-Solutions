> LeetCode 1013. Partition Array Into Three Parts With Equal Sum将数组分成和相等的三个部分【Easy】【Python】【双指针】

### Problem

[LeetCode](https://leetcode.com/problems/partition-array-into-three-parts-with-equal-sum/)

Given an array `A` of integers, return `true` if and only if we can partition the array into three **non-empty** parts with equal sums.

Formally, we can partition the array if we can find indexes `i+1 < j` with `(A[0] + A[1] + ... + A[i] == A[i+1] + A[i+2] + ... + A[j-1] == A[j] + A[j-1] + ... + A[A.length - 1])`

**Example 1:**

```
Input: A = [0,2,1,-6,6,-7,9,1,2,0,1]
Output: true
Explanation: 0 + 2 + 1 = -6 + 6 - 7 + 9 + 1 = 2 + 0 + 1
```

**Example 2:**

```
Input: A = [0,2,1,-6,6,7,9,-1,2,0,1]
Output: false
```

**Example 3:**

```
Input: A = [3,3,6,5,-2,2,5,1,-9,4]
Output: true
Explanation: 3 + 3 = 6 = 5 - 2 + 2 + 5 + 1 - 9 + 4
```

**Constraints:**

- `3 <= A.length <= 50000`
- `-10^4 <= A[i] <= 10^4`

### 问题

[力扣](https://leetcode-cn.com/problems/partition-array-into-three-parts-with-equal-sum/)

给你一个整数数组 A，只有可以将其划分为三个和相等的非空部分时才返回 true，否则返回 false。

形式上，如果可以找出索引 i+1 < j 且满足 (A[0] + A[1] + ... + A[i] == A[i+1] + A[i+2] + ... + A[j-1] == A[j] + A[j-1] + ... + A[A.length - 1]) 就可以将数组三等分。

**示例 1：**

```
输出：[0,2,1,-6,6,-7,9,1,2,0,1]
输出：true
解释：0 + 2 + 1 = -6 + 6 - 7 + 9 + 1 = 2 + 0 + 1
```

**示例 2：**

```
输入：[0,2,1,-6,6,7,9,-1,2,0,1]
输出：false
```

**示例 3：**

```
输入：[3,3,6,5,-2,2,5,1,-9,4]
输出：true
解释：3 + 3 = 6 = 5 - 2 + 2 + 5 + 1 - 9 + 4
```


提示：

1. `3 <= A.length <= 50000`
2. `-10^4 <= A[i] <= 10^4`

### 思路

**双指针**

```
先整体求和，不能被 3 整除直接返回 False。
再用双指针，分别计算两边的和是否满足等于 sum/3。
注意：题目的意思就是相邻元素相加，而不是任意相加。
```

**时间复杂度:** O(n)
**空间复杂度:** O(1)

##### Python3代码

```python
class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        sum = 0
        for x in A:
            sum += x
        # 和不能被3整除，肯定不符合
        if sum % 3:
            return False
        
        left, right = 0, len(A)-1
        leftSum, rightSum = A[left], A[right]

        # left + 1 < right: 防止将数组只分成两部分，中间部分至少要有一个元素
        while left + 1 < right:
            # 左右都等于sum/3，中间肯定等于sum/3
            if leftSum == sum/3 and rightSum == sum/3:
                return True
            if leftSum != sum/3:
                left += 1
                leftSum += A[left]
            if rightSum != sum/3:
                right -= 1
                rightSum += A[right]
        return False
```

### 代码地址

[GitHub链接](https://github.com/Wonz5130/LeetCode-Solutions/blob/master/solutions/1013-Partition-Array-Into-Three-Parts-With-Equal-Sum/1013.py)