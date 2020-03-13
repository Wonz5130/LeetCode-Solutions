from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # solution one: 哈希表
        import collections
        counts = collections.Counter(nums)
        return max(counts.keys(), key=counts.get)

        # solution two: 排序
        nums.sort()
        return nums[len(nums)//2]

        # solution three: Boyer-Moore 投票算法
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            # 众数和非众数相互抵消，最后剩下的肯定是众数
            count += (1 if num == candidate else -1)
        
        return candidate

if __name__ == "__main__":
    nums = [3,2,3]
    print(Solution().majorityElement(nums))