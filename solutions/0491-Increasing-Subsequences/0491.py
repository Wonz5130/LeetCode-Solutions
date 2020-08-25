class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
    	# solution one：DFS
    	res = []

    	def dfs(nums, tmp):
    		if len(tmp) > 1:
    			res.append(tmp)

    		cur_pres = set()
    		# 循环 nums 的索引值对
    		for inx, i in enumerate(nums):
    			# 当前值已经被遍历
    			if i in cur_pres:
    				continue
    			# 当前值可以加入组成递增子序列
    			if not tmp or i >= tmp[-1]:
    				cur_pres.add(i)
    				dfs(nums[inx + 1:], tmp + [i])

    	dfs(nums, [])
    	return res