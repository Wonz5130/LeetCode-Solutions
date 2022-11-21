class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # # 法一：分类
        # red, white, blue = 0, 0, 0
        # for i in nums:
        #     if i == 0:
        #         red += 1
        #     elif i == 1:
        #         white += 1
        # for i in range(red):
        #     nums[i] = 0
        # for i in range(red, red+white):
        #     nums[i] = 1
        # for i in range(red+white, len(nums)):
        #     nums[i] = 2
        
        # 法二：荷兰旗问题 三指针
        left, mid, right = 0, 0, len(nums)-1
        while mid <= right:
            if nums[mid] == 0:
                nums[left], nums[mid] = nums[mid], nums[left]
                left += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[mid], nums[right] = nums[right], nums[mid]
                right -= 1  # 只需要right往左移一位就行，mid不需要动
        
        # solution 3: 快排
        def quick_sort(left: int, right: int):
            if left >= right:
                return
                
            pivot = left
            i, j = left, right
            while i < j:
                while i < j and nums[j] > nums[pivot]:
                    j -= 1
                while i < j and nums[i] <= nums[pivot]:
                    i += 1
                nums[i], nums[j] = nums[j], nums[i]
            nums[pivot], nums[j] = nums[j], nums[pivot]
            quick_sort(left, j - 1)
            quick_sort(j + 1, right)
        
        quick_sort(0, len(nums) - 1)

        # solution 4: 赋值
        n0, n1 = 0, 0
        # for num in nums: # num 不是原地更新，会不通过
        for i in range(len(nums)):
            tmp, nums[i] = nums[i], 2
            if tmp < 2:
                nums[n1] = 1
                n1 += 1
            if tmp < 1:
                nums[n0] = 0
                n0 += 1

if __name__ == "__main__":
    nums = [2,0,2,1,1,0]
    Solution().sortColors(nums)
    print(nums)