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
        
if __name__ == "__main__":
    nums = [2,0,2,1,1,0]
    Solution().sortColors(nums)
    print(nums)