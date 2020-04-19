from typing import List

class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        n = len(nums)
        temp = [0 for x in range(n)]
        for i in range(n):
            temp[i] = sum(nums[:i+1])
        if min(temp) >= 1:
            return 1
        else:
            return (abs(min(temp)) + 1)

if __name__ == "__main__":
    nums = [-3,2,-3,4,2]
    nums = [1,-2,-3]
    nums = [1, 2]
    print(Solution().minStartValue(nums))