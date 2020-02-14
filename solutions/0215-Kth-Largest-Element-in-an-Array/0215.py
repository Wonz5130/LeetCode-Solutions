class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        low, high = 0, len(nums)-1
        while low <= high:
            pivot = self.partition(nums, low, high)
            if pivot == k - 1:  # 第 k 大, 即从大到小排序第 k-1 位置(从 0 开始计算)
                return nums[pivot]
            if pivot < k - 1:
                low = pivot + 1
            else:
                high = pivot - 1
    
    # 划分函数
    def partition(self, nums, low, high):
        pivot_value = nums[high]  # 因为是从大到小排序, 所以选 nums[high] 为基值
        index = low
        for i in range(low, high):
            if nums[i] >= pivot_value:
                nums[i], nums[index] = nums[index], nums[i]
                index += 1
        nums[index], nums[high] = nums[high], nums[index]
        return index  # 返回的 index 即分界点

        """
        # 直接调用 Python 的 heapq 模块
        import heapq
        list_k = heapq.nlargest(k, nums)
        return list_k.pop()
        """

        # return sorted(nums)[-k]  # 用 Python 自带的排序算法一行代码就能 AC

if __name__ == "__main__":
    nums = [3,2,1,5,6,4]
    k = 2
    print(Solution().findKthLargest(nums, k))