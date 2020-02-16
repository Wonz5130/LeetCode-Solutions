class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        if not points or len(points) == 0:
            return 0
        points.sort(key = lambda x: x[1])  # 按右端点从小到大排序
        temp_pos = points[0][1]
        cnt = 1
        for i in range(len(points)):
            if temp_pos >= points[i][0]:  # 当右端点<左端点时，要再加一支箭
                continue
            temp_pos = points[i][1]
            cnt += 1
        return cnt
        

if __name__ == "__main__":
    points = [[10,16], [2,8], [1,6], [7,12]]
    print(Solution().findMinArrowShots(points))