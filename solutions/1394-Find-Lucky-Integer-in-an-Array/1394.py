from typing import List
import collections

class Solution:
    def findLucky(self, arr: List[int]) -> int:
        cnt = collections.Counter(arr)
        # 先按频次排序，再按数值大小排序
        res = sorted(cnt.items(), key=lambda x:(x[1],x[0]), reverse=True)
        for i in range(len(res)):
            # 频次等于数值大小
            if res[i][0] == res[i][1]:
                return res[i][0]
        return -1

if __name__ == "__main__":
    arr = [2,2,3]
    print(Solution().findLucky(arr))