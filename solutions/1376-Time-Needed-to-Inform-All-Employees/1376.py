from typing import List

class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        res = 0
        for i in range(len(manager)):
            # 剪枝
            if informTime[i] == 0:
                temp = 0
                index = i
                # 自底向上遍历
                while index != -1:
                    temp += informTime[index]
                    index = manager[index]
                res = max(res, temp)
        return res

if __name__ == "__main__":
    n = 6
    headID = 2
    manager = [2,2,-1,2,2,2]
    informTime = [0,0,1,0,0,0]
    print(Solution().numOfMinutes(n, headID, manager, informTime))