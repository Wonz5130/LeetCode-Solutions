class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        low, high = 0, len(nums) - 1
        while low < high:  # < not <=, or <= will TLE
            mid = int((low + high) / 2)
            if nums[mid] <= nums[high]:  # <=
                high = mid  # h = m not m - 1
            else:
                low = mid + 1
        return nums[low]

if __name__ == "__main__":
    nums = [4,5,6,7,0,1,2]
    print(Solution().findMin(nums))