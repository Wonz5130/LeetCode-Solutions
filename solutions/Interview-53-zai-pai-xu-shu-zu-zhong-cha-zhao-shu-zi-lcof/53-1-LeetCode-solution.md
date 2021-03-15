> LeetCode 剑指 Offer 53 - I. 在排序数组中查找数字 I【Easy】【Python】【二分查找】

## 问题

[力扣](https://leetcode-cn.com/problems/zai-pai-xu-shu-zu-zhong-cha-zhao-shu-zi-lcof/)

统计一个数字在排序数组中出现的次数。

**示例 1:**

```
输入: nums = [5,7,7,8,8,10], target = 8
输出: 2
```

**示例 2:**

```
输入: nums = [5,7,7,8,8,10], target = 6
输出: 0
```

**限制：**

- 0 <= 数组长度 <= 50000

注意：本题与主站 34 题相同（仅返回值不同）：https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array/

## 思路

**二分查找**

```
进行两次二分查找，分别找出右边界与左边界
第二次查找左边界可以直接在[0,R]中进行查找
```

## 代码

### Python3

```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        # 求右边界
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] <= target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
        R = right
        
        # 如果R越界或者R位置的值不等于target，说明不存在target，可以直接返回0
        if R < 0 or nums[R] != target:
            return 0
        left = 0
        # 缩小区间，直接在[0,R]中寻找左边界
        right = R
        # 求左边界
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] >= target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
        L = left
        return R - L + 1
```

## 链接

[GitHub](https://github.com/Wonz5130/LeetCode-Solutions/tree/master/solutions/Interview-53-zai-pai-xu-shu-zu-zhong-cha-zhao-shu-zi-lcof)