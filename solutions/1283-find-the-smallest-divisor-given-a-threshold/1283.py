class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        left, right = 1, max(nums)

        def getSum(nums: List[int], mid: int) -> int:
            tmp_sum = 0
            for num in nums:
                tmp_sum += (num + mid - 1) // mid
            return tmp_sum

        while left < right:
            mid = (left + right) >> 1
            tmp_sum = getSum(nums, mid)
            if tmp_sum <= threshold:
                right = mid
            else:
                left = mid + 1
        return left