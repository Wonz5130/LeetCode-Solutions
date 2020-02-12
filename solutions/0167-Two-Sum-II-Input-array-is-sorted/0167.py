class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        left = 0  # 从头指向尾
        right = len(numbers) - 1  # 从尾指向头
        while left < right:
            if numbers[left] + numbers[right] == target:
                return [left + 1, right + 1]
            elif numbers[left] + numbers[right] > target:
                right -= 1 
            else:
                left += 1 
        return []

if __name__ == "__main__":
    array = [2, 7, 11, 15]
    target = 9
    print(Solution().twoSum(array, target))