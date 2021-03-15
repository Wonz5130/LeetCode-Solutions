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