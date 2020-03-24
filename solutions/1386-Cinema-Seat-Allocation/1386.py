from typing import List

class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        left, right, mid = set(), set(), set()
        count = 0
        
        # 统计被预约的位置
        for r, c in reservedSeats:
            if r in left and r in right and r in mid:
                continue
            if c < 6 and c > 1:
                left.add(r)
            if c < 10 and c > 5:
                right.add(r)
            if c < 8 and c > 3:
                mid.add(r)
        for i in (left|right|mid):
            # 预约位置在两边：1 or 10
            if i not in left and i not in right:
                count += 2
            # 预约位置在左边/右边：2 or 3 or 8 or 9
            elif i not in mid:
                count += 1
            # 预约位置在中间：4 or 5 or 6 or 7
            elif i not in left or i not in right:
                count += 1
        # 反向筛选一下，没有被预约的行最多可以坐两家人
        count += 2*(n - len(left|right|mid))
        return count

        """
        # 超时/超内存
        res = 0
        for i in range(1, n +1):
            for j in range(1, 11):
                if j >= 7:
                    break
                if [i, j] in reservedSeats:
                    continue
                if j == 1 or j == 3 or j == 5:
                    continue
                if [i, j + 1] in reservedSeats or [i, j + 2] in reservedSeats  or [i, j + 3]  in reservedSeats :
                    continue
                if [i, j]  not  in reservedSeats  and [i, j + 1] not in reservedSeats and [i, j + 2]  not in reservedSeats and [i, j + 3]  not in reservedSeats :
                    reservedSeats.append([i, j+1])
                    reservedSeats.append([i, j+2])
                    reservedSeats.append([i, j+2])
                    res += 1
                    # print(i,j)
        return res
        """

if __name__ == "__main__":
    n = 3
    reservedSeats = [[1,2],[1,3],[1,8],[2,6],[3,1],[3,10]]
    print(Solution().maxNumberOfFamilies(n, reservedSeats))