> LeetCode 剑指 Offer 11. 旋转数组的最小数字【Easy】【Python】【二分查找】

## 问题

[力扣](https://leetcode-cn.com/problems/xuan-zhuan-shu-zu-de-zui-xiao-shu-zi-lcof/)

把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。输入一个递增排序的数组的一个旋转，输出旋转数组的最小元素。例如，数组 [3,4,5,1,2] 为 [1,2,3,4,5] 的一个旋转，该数组的最小值为1。  

**示例 1：**

```
输入：[3,4,5,1,2]
输出：1
```

**示例 2：**

```
输入：[2,2,2,0,1]
输出：0
```


注意：本题与主站 154 题相同：https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array-ii/

## 思路

**二分查找**

## 代码

### Python3

```python
class Solution:
    def minArray(self, numbers: List[int]) -> int:
        left = 0
        right = len(numbers) - 1
        # 注意这里和labuladong模板有区别，循环是left<right，而不是left<=right
        while left < right:
            mid = left + (right - left) // 2
            # 注意这里比较的是mid和right，而不是mid和left
            # 右边有序，最小值一定在左边
            if numbers[mid] < numbers[right]:
                right = mid
            # 右边无序，最小值一定在右边
            elif numbers[mid] > numbers[right]:
                left = mid + 1
            # 因为包含重复，所以缩小右边界
            # 这里不能和上面合并，而要单独判断，举个例子：[3,3,1,3]，不能判断出在左边还是右边
            else:
                right -= 1
        return numbers[left]
```

## 链接

[GitHub](https://github.com/Wonz5130/LeetCode-Solutions/tree/master/solutions/Interview-11-xuan-zhuan-shu-zu-de-zui-xiao-shu-zi-lcof)