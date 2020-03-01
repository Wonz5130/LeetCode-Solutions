> LeetCode 1365. How Many Numbers Are Smaller Than the Current Number有多少小于当前数字的数字【Easy】【Python】【暴力】

### Problem

[LeetCode](https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/)

Given the array `nums`, for each `nums[i]` find out how many numbers in the array are smaller than it. That is, for each `nums[i]` you have to count the number of valid `j's` such that `j != i` **and** `nums[j] < nums[i]`.

Return the answer in an array.

**Example 1:**

```
Input: nums = [8,1,2,2,3]
Output: [4,0,1,1,3]
Explanation: 
For nums[0]=8 there exist four smaller numbers than it (1, 2, 2 and 3). 
For nums[1]=1 does not exist any smaller number than it.
For nums[2]=2 there exist one smaller number than it (1). 
For nums[3]=2 there exist one smaller number than it (1). 
For nums[4]=3 there exist three smaller numbers than it (1, 2 and 2).
```

**Example 2:**

```
Input: nums = [6,5,4,8]
Output: [2,1,0,3]
```

**Example 3:**

```
Input: nums = [7,7,7,7]
Output: [0,0,0,0] 
```

**Constraints:**

- `2 <= nums.length <= 500`
- `0 <= nums[i] <= 100`

### 问题

[力扣](https://leetcode-cn.com/problems/how-many-numbers-are-smaller-than-the-current-number/)

给你一个数组 `nums`，对于其中每个元素 `nums[i]`，请你统计数组中比它小的所有数字的数目。

换而言之，对于每个 `nums[i]` 你必须计算出有效的 `j` 的数量，其中 `j` 满足 `j != i` 且 `nums[j] < nums[i]` 。

以数组形式返回答案。

**示例 1：**

```
输入：nums = [8,1,2,2,3]
输出：[4,0,1,1,3]
解释： 
对于 nums[0]=8 存在四个比它小的数字：（1，2，2 和 3）。 
对于 nums[1]=1 不存在比它小的数字。
对于 nums[2]=2 存在一个比它小的数字：（1）。 
对于 nums[3]=2 存在一个比它小的数字：（1）。 
对于 nums[4]=3 存在三个比它小的数字：（1，2 和 2）。
```

**示例 2：**

```
输入：nums = [6,5,4,8]
输出：[2,1,0,3]
```

**示例 3：**

```
输入：nums = [7,7,7,7]
输出：[0,0,0,0]
```

**提示：**

- `2 <= nums.length <= 500`
- `0 <= nums[i] <= 100`

### 思路

**暴力**

```
两行 for 循环暴力一下就过了。
```

**时间复杂度:** O(n^2)
**空间复杂度:** O(n)

##### Python3代码

```python
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = []
        for i in range(n):
            cnt = 0
            for j in range(n):
                if nums[j] < nums[i]:
                    cnt += 1
            ans.append(cnt)
        return ans
```

### 代码地址

[GitHub链接](https://github.com/Wonz5130/LeetCode-Solutions/blob/master/solutions/1365-How-Many-Numbers-Are-Smaller-Than-the-Current-Number/1365.py)