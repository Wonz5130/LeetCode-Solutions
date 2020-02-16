class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        if not intervals or len(intervals) == 0:
            return 0
        intervals.sort(key = lambda x: x[0])  # 按左端点从小到大排序
        temp_pos = 0
        cnt = 0
        for i in range(1, len(intervals)):
            if intervals[temp_pos][1] > intervals[i][0]:  # 当当前右端点>左端点
                if intervals[i][1] < intervals[temp_pos][1]:  # 当右端点<当前右端点，表示intervals[i][1]被覆盖在intervals[temp_pos][1]中
                    temp_pos = i  # 更新temp_pos，选择覆盖范围小的intervals[i][1]
                cnt += 1
            else:
                temp_pos = i  # 当当前右端点<=左端点，表示不重叠，要更新temp_pos
        return cnt

if __name__ == "__main__":
    intervals = [[1,2],[1,2],[1,2]]
    # intervals = [[1,2],[2,3],[3,4],[1,3]]
    # intervals = [[1,2],[2,3]]
    print(Solution().eraseOverlapIntervals(intervals))