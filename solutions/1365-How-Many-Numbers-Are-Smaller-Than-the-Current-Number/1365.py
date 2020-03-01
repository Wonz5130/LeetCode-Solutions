from typing import List

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

if __name__ == "__main__":
    nums = [8,1,2,2,3]
    print(Solution().smallerNumbersThanCurrent(nums))