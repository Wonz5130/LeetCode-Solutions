class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        while m > 0 and n > 0:
            if nums1[m-1] > nums2[n-1]:
                nums1[m+n-1] = nums1[m-1]
                m -= 1
            else: 
                nums1[m+n-1] = nums2[n-1]
                n -= 1
        if n > 0:  # 如果 nums2 有剩余, 全部加到 nums1 中
            nums1[:n] = nums2[:n]

if __name__ == "__main__":
    nums1 = [1,2,3,0,0,0]
    nums2 = [2,5,6]
    m, n = 3, 3
    Solution().merge(nums1, m, nums2, n)
    print(nums1)