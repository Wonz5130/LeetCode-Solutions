from typing import List

class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        target = []
        for i in range(len(index)):
            target.insert(index[i], nums[i])  # insert(位置, 值)
        return target

if __name__ == "__main__":
    nums = [0,1,2,3,4]
    index = [0,1,2,2,1]
    print(Solution().createTargetArray(nums, index))