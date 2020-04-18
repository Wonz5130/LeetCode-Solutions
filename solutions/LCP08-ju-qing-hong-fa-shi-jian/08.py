from typing import List

class Solution:
    def getTriggerTime(self, increase: List[List[int]], requirements: List[List[int]]) -> List[int]:
        n = len(requirements)
        res = [-1 for x in range(n)]

        # 累加 increase
        increase = [[0, 0, 0]] + increase
        for i in range(len(increase) - 1):
            for j in range(3):
                increase[i + 1][j] += increase[i][j]
        
        # 二分
        for i in range(len(requirements)):
            left, right = 0, len(increase) - 1
            while left <= right:  # 注意条件：<=
                mid = (left + right) // 2
                if increase[mid][0] >= requirements[i][0] and increase[mid][1] >= requirements[i][1] and increase[mid][2] >= requirements[i][2]:
                    res[i] = mid
                    right = mid - 1
                else:
                    left = mid + 1

        return res

if __name__ == "__main__":
    increase = [[2,8,4],[2,5,0],[10,9,8]]
    # increase = [[1,1,1]]
    requirements = [[2,11,3],[15,10,7],[9,17,12],[8,1,14]]
    # requirements = [[0,0,0]]
    print(Solution().getTriggerTime(increase, requirements))