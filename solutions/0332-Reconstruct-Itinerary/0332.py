class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
    	from collections import defaultdict
    	ticket_dict = defaultdict(list)
    	for item in tickets:
    		ticket_dict[item[0]].append(item[1])

    	path = ['JFK']

    	def dfs(cur_from):
    		# 结束条件：path的长度为 tickets 长度 + 1
    		if len(path) == len(tickets) + 1:
    			return True
    		# 按字典序排序
    		ticket_dict[cur_from].sort()

    		for _ in ticket_dict[cur_from]:
    			# 去掉不合适
    			cur_to = ticket_dict[cur_from].pop(0)
    			path.append(cur_to)
    			# 下一层
    			if dfs(cur_to):
    				return True
    			# 取消选择
    			path.pop()
    			# 恢复当前节点
    			ticket_dict[cur_from].append(cur_to)
    		return False

    	dfs('JFK')
    	return path